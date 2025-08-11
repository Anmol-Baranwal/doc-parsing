import requests
import os
import json
from dotenv import load_dotenv
import time

load_dotenv()

API_BASE = "https://api.invofox.com"
API_KEY = os.getenv("INVOFOX_API_KEY")
PDF_PATH = "invoice_sample.pdf"

headers = {"accept": "application/json", "x-api-key": API_KEY}

with open(PDF_PATH, "rb") as f:
    files = {"files": f}
    info = {"type": "6840c4511cbcc77119347248", "data": {"companyActsLike": "issuer"}}
    data = {"info": json.dumps(info)}
    resp_upload = requests.post(
        f"{API_BASE}/v1/ingest/uploads", headers=headers, files=files, data=data
    )

upload_result = resp_upload.json()
print("Upload response:", upload_result)

import_id = upload_result.get("importId")
if not import_id:
    raise ValueError("Import ID not found in upload response.")

# wait a moment for processing
time.sleep(2)

resp_import = requests.get(f"{API_BASE}/v1/ingest/imports/{import_id}", headers=headers)
import_info = resp_import.json()
print("Import info:", import_info)

files_info = import_info.get("files", [])
if not files_info or not files_info[0].get("documentIds"):
    raise ValueError("Document IDs not found in import info.")

document_id = files_info[0]["documentIds"][0]
print("Document ID:", document_id)

time.sleep(20)

resp_get = requests.get(f"{API_BASE}/documents/{document_id}", headers=headers)
parsed_doc = resp_get.json()
print("Parsed Document Data:")
print(json.dumps(parsed_doc, indent=2))
