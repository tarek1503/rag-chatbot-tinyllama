from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_pdf(file_path):
    text = ""  # Initialize an empty string to store all text from the PDF
    with open(file_path, "rb") as f: # Open the PDF file in binary read mode
        reader = PdfReader(f)  # Create a PdfReader object to read the PDF
        for page in reader.pages:  # Loop through each page in the PDF
            text += page.extract_text()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    return text_splitter.split_text(text) # Split the full extracted text into smaller chunks and return the list of chunks