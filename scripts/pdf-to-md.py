"""
Convert all PDF files in 0-profile/ to Markdown files.
Usage: python scripts/pdf-to-md.py

Requirements: pip install pymupdf
"""

import sys
import pathlib

try:
    import fitz  # pymupdf
except ImportError:
    print("pymupdf is not installed. Run: pip install pymupdf")
    sys.exit(1)

PROFILE_DIR = pathlib.Path(__file__).resolve().parent.parent / "0-profile"


def pdf_to_markdown(pdf_path: pathlib.Path) -> str:
    doc = fitz.open(pdf_path)
    pages = []
    for page in doc:
        pages.append(page.get_text())
    doc.close()
    return "\n\n---\n\n".join(pages)


def main():
    pdf_files = list(PROFILE_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in 0-profile/")
        return

    for pdf_path in pdf_files:
        md_path = pdf_path.with_suffix(".md")
        print(f"Converting: {pdf_path.name} -> {md_path.name}")
        content = pdf_to_markdown(pdf_path)
        md_path.write_text(content, encoding="utf-8")
        print(f"  Done: {md_path.name}")

    print(f"\nConverted {len(pdf_files)} file(s).")


if __name__ == "__main__":
    main()
