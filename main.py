from __future__ import annotations

import argparse
from pathlib import Path

from src.finance_agent.agent import FinanceAgent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Finance agent for mutual fund category PDFs.")
    parser.add_argument("--pdf", type=Path, required=True, help="Path to the PDF to analyze.")
    parser.add_argument(
        "--query",
        type=str,
        default="Summarize the main categories and investment themes in this document.",
        help="Question to answer from the PDF content.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    agent = FinanceAgent(args.pdf)
    print(agent.answer(args.query))
