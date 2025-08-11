import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
API_BASE = "https://api.invofox.com"
API_KEY = os.getenv("INVOFOX_API_KEY")
PDF_PATH = "invoice_sample.pdf"

headers = {"accept": "application/json", "x-api-key": API_KEY}

with open(PDF_PATH, "rb") as f:
    files = {"files": f}
    info = {"type": "6840c4511cbcc77119347248", "data": {"companyActsLike": "issuer"}}
    print(info)
    data = {"info": json.dumps(info)}
    resp_upload = requests.post(
        f"{API_BASE}/v1/ingest/uploads", headers=headers, files=files, data=data
    )

upload_result = resp_upload.json()
print(upload_result)

document_id = upload_result["files"][0]["id"]
print(document_id)

resp_get = requests.get(f"{API_BASE}/documents/{document_id}", headers=headers)
parsed_doc = resp_get.json()
print("Parsed Document Data:", parsed_doc)
