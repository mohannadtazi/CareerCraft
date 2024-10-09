from dotenv import load_dotenv
load_dotenv()
from src_py.my_tools.read_pdf import FileReadTool
#from my_tools.send_draft import email_tool
#from src_py.my_tools.write_pdf  import FileWriteTool
import os
from crewai_tools import SerperDevTool, SeleniumScrapingTool, CodeInterpreterTool

os.environ["SERPER_API_KEY"]= os.getenv("SERPER_API_KEY")

search_tool= SerperDevTool()
rag_search_tool= SeleniumScrapingTool()

#email_tool= email_tool

#file_read_tool = FileReadTool(file_path='src_py\Data\PFA-mohannad_tazi--DataScience__BigData.pdf')
file_read_tool = FileReadTool()
codding_tool = CodeInterpreterTool()
#file_writer_tool = FileWriteTool()



