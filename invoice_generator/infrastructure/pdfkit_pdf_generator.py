import pdfkit

from invoice_generator.application.pdf_generator import PdfGenerator


class PdfkitPdfGenerator(PdfGenerator):

    def generate_pdf_from_string(self, input_html: str, output_pdf_path: str):
        pdfkit.from_string(input_html, output_pdf_path)
