# Money Finance Agent

This project sets up a lightweight finance agent for working with the mutual fund category PDF in this repository.

## What it does

- Reads a PDF file from disk
- Extracts text from the document
- Identifies likely fund categories and major themes
- Produces an answer to a user question about the content

## Quick start

1. Create a virtual environment if desired.
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Run the agent:
   ```bash
   python main.py --pdf indianmutualfundcategories.pdf --query "Summarize the main mutual fund categories in this document."
   ```

## Project layout

- `main.py` – command-line entry point
- `src/finance_agent/agent.py` – logic for loading and analyzing the PDF
