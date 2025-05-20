"""Example PDF generation using the itext library."""

# NOTE: The itext package must be installed separately.
# For example: pip install itextpdf

from itextpdf import Document


def create_pdf(text: str, output_file: str) -> None:
    """Create a simple PDF containing the provided text."""
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_file)


if __name__ == "__main__":
    create_pdf("Hello from itext", "output.pdf")
