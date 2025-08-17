import pdfplumber
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

print("API Key loaded:", api_key[:12], "...")


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def parse_invoice_with_claude(invoice_text):

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

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=500,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.content[0].text


if __name__ == "__main__":
    pdf_path = "samples/invoice_sample.pdf"
    invoice_text = extract_text_from_pdf(pdf_path)
    parsed_data = parse_invoice_with_claude(invoice_text)
    print(parsed_data)
