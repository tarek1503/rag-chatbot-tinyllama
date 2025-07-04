from pypdf import PdfReader
from docx import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
import os

def load_file(file_path):
    """Load PDF or DOCX file content"""
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".pdf":
        return load_pdf(file_path)
    elif ext == ".docx":
        return load_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def load_pdf(file_path):
    """Load text from PDF with layout preservation"""
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text(extraction_mode="layout") + "\n\n"
    return clean_text(text)

def load_docx(file_path):
    """Load text from DOCX files"""
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return clean_text(text)

def clean_text(text):
    """Normalize whitespace and fix common issues"""
    text = re.sub(r'\s+', ' ', text)  # Standardize whitespace
    text = re.sub(r'-\n', '', text)    # Fix hyphenated words
    text = re.sub(r'\x00', '', text)   # Remove null bytes
    return text.strip()

def split_text(text):
    """Split text into chunks with improved separators"""
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", "! ", "? ", "; ", " ", ""],
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(text)