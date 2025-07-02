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
    # print(text)
    return text

def parse_invoice_with_openai(invoice_text):
    prompt = (
        "Extract the following fields from this invoice text and return as a JSON object:\n"
        "- Invoice Number\n"
        "- Invoice Date\n"
        "- Due Date\n"
        "- Invoice Status (e.g. unpaid/paid)\n"
        "- Sender Name and Email\n"
        "- Recipient Name and Email\n"
        "- Items (description, quantity, rate)\n"
        "- Total Amount\n"
        "- Memo\n\n"
        "Invoice Text:\n"
        f"{invoice_text}"
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
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
