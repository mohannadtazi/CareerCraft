from langchain.tools import tool
from PyPDF2 import PdfReader
from crewai_tools import BaseTool

class FileReadTool(BaseTool):
    name: str = "PDF Reader"
    description: str = "Reads the content of a PDF file and returns the text."

    def _run(self,url: str) -> str:
        with open(url, 'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text

