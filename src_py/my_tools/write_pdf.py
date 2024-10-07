import fitz 
from crewai_tools import BaseTool


class FileWriteTool(BaseTool):
    name: str = "PDF Writer"
    description: str = "Write the content passed to it in a PDF file and returns it."

    def _run(self,content: str) -> str:
    # Create a canvas object
      pdf_document = fitz.open()
      page = pdf_document.new_page()
      page.insert_text((72, 72), content, fontsize=12)

      pdf_document.save("custom_cv.pdf")
      pdf_document.close()