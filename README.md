# Document Parsing

A collection of example scripts for extracting structured invoice data from PDFs using various APIs and services.

## What’s Inside

- Extract text from invoice PDFs with [pdfplumber](https://github.com/jsvine/pdfplumber)
- Parse invoice contents using:
  - OpenAI GPT-4 (`openai-main.py`)
  - Anthropic Claude (`anthropic-main.py`)
  - Invofox API (`invofox-main.py`)
- Includes sample invoice files (`invoice_sample.pdf`, `invoice_sample.jpg`)

## Prerequisites

- Python 3.8 or higher
- A virtual environment (Recommended)
- API keys for:
  - OpenAI (`OPENAI_API_KEY`)
  - Anthropic (`ANTHROPIC_API_KEY`)
  - Invofox (`INVOFOX_API_KEY`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Anmol-Baranwal/doc-parsing.git
   cd doc-parsing
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate    # macOS/Linux
   env\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API keys:

   ```env
   OPENAI_API_KEY=your-openai-api-key
   ANTHROPIC_API_KEY=your-anthropic-api-key
   INVOFOX_API_KEY=your-invofox-api-key
   ```

## Usage

- **OpenAI GPT-4**:

  ```bash
  python openai-main.py
  ```

- **Anthropic Claude**:

  ```bash
  python anthropic-main.py
  ```

- **Invofox API**:
  ```bash
  python invofox-main.py
  ```

Thanks for visiting!
