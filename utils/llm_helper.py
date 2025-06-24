from transformers import AutoTokenizer, pipeline
import torch
from langchain.prompts import PromptTemplate

def setup_llm():
    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # 1.1B parameters
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    pipe = pipeline(
        "text-generation",
        model=model_name,
        device_map="auto",
        tokenizer=tokenizer,
        max_new_tokens=256,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        do_sample=True,
        temperature=0.7,
        top_p=0.95
    )
    
    return pipe

def format_prompt(query, context):
    template = """
    <|system|>
    Use the context below to answer the question. If unsure, say "I don't know".
    
    Context: {context}
    </s>
    <|user|>
    {question}</s>
    <|assistant|>
    """
    return template.format(context=context, question=query)

def get_response(llm_pipeline, prompt):
    response = llm_pipeline(
        prompt,
        pad_token_id=llm_pipeline.tokenizer.eos_token_id
    )
    return response[0]['generated_text']