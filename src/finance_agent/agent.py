from __future__ import annotations

import re
from pathlib import Path
from typing import List

from pypdf import PdfReader


class FinanceAgent:
    """Simple finance PDF analysis agent."""

    def __init__(self, pdf_path: str | Path):
        self.pdf_path = Path(pdf_path)

    def _extract_text(self) -> str:
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")

        reader = PdfReader(str(self.pdf_path))
        pages = []
        for page in reader.pages:
            text = page.extract_text() or ""
            pages.append(text)
        return "\n".join(pages)

    def _summarize_categories(self, text: str) -> List[str]:
        cleaned = re.sub(r"\s+", " ", text)
        lines = [line.strip() for line in cleaned.split(".") if line.strip()]

        candidate_categories = []
        for line in lines:
            if len(line) < 5:
                continue
            if any(keyword in line.lower() for keyword in [
                "equity",
                "debt",
                "hybrid",
                "solution",
                "fund",
                "category",
                "large cap",
                "mid cap",
                "small cap",
                "index",
                "gold",
                "banking",
                "infrastructure",
                "technology",
                "sector",
                "thematic",
                "liquid",
                "short duration",
                "dynamic bond",
                "gilt",
                "international",
                "fof",
            ]):
                candidate_categories.append(line)

        deduped = []
        seen = set()
        for item in candidate_categories:
            key = item.lower()
            if key not in seen:
                seen.add(key)
                deduped.append(item)

        return deduped[:12]

    def answer(self, query: str) -> str:
        text = self._extract_text()
        if not text.strip():
            return "No readable text was found in the PDF."

        categories = self._summarize_categories(text)

        answer = [
            "I reviewed the document and extracted a few likely mutual fund category themes.",
            "",
        ]

        if categories:
            answer.append("Likely categories or themes mentioned:")
            for idx, category in enumerate(categories, start=1):
                answer.append(f"{idx}. {category}")
        else:
            answer.append("No clear category names were detected from the extracted text.")

        answer.extend([
            "",
            "The document appears to be a fund-category reference, so the main value is in identifying broad segments such as equity, debt, hybrid, sector/thematic, and solution-oriented funds.",
        ])

        return "\n".join(answer)
