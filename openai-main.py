import pdfplumber
import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def parse_invoice_with_openai(invoice_text):
    prompt = (
        "Extract the following fields from this invoice text: "
        "Invoice Number, Invoice Date, Vendor Name, Total Amount, and Due Date. "
        "Return the result as a JSON object.\n\n"
        f"Invoice Text:\n{invoice_text}"
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    pdf_path = "invoice_sample.pdf"
    invoice_text = extract_text_from_pdf(pdf_path)
    parsed_data = parse_invoice_with_openai(invoice_text)
    print(parsed_data)
