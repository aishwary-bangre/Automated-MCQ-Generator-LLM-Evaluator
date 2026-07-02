import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

def clean_pdf_to_markdown(pdf_path: str, output_md_path: str):
    """
    Uses Gemini Vision to read a Math PDF and output perfectly formatted 
    Markdown with LaTeX for all equations.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)
    
    print(f"Uploading {pdf_path} to Gemini...")
    # Upload the PDF file to the Gemini API
    uploaded_file = client.files.upload(file=pdf_path)
    
    # Wait for processing if necessary (Gemini sometimes needs a moment for large PDFs)
    while uploaded_file.state.name == "PROCESSING":
        print("Waiting for file processing...")
        time.sleep(2)
        uploaded_file = client.files.get(name=uploaded_file.name)
        
    if uploaded_file.state.name == "FAILED":
        raise Exception("File processing failed on Google's servers.")

    print("File uploaded. Generating Markdown...")
    
    prompt = """
    You are an expert at extracting text and mathematics from textbooks.
    Please read this uploaded PDF document and convert the entire content into Markdown format.
    CRITICAL INSTRUCTIONS:
    1. Maintain the exact logical flow, headings, and paragraphs of the text.
    2. Any mathematical formulas, equations, variables, or expressions MUST be formatted using standard LaTeX wrapped in $ or $$. 
    3. Do not scramble fractions, exponents, or subscripts.
    4. Do not include any conversational filler (e.g. "Here is the markdown..."). Just output the raw Markdown.
    """
    
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=[uploaded_file, prompt]
    )
    
    # Clean up the file from Google's servers after we're done
    client.files.delete(name=uploaded_file.name)
    
    markdown_content = response.text
    
    # Save the result
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    print(f"Successfully converted and saved to {output_md_path}")
    return markdown_content

if __name__ == "__main__":
    # Example usage for testing
    sample_pdf = "data/raw/sample_chapter.pdf"
    output_md = "data/processed/sample_chapter.md"
    
    if os.path.exists(sample_pdf):
        clean_pdf_to_markdown(sample_pdf, output_md)
    else:
        print(f"Please place a sample PDF at {sample_pdf} to test.")
