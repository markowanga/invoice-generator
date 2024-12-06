from abc import ABC, abstractmethod


class PdfGenerator(ABC):
    @abstractmethod
    def generate_pdf_from_string(self, input_html: str, output_pdf_path: str) -> None:
        pass
