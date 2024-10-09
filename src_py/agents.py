import os
from dotenv import load_dotenv
load_dotenv()
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from src_py.tools import file_read_tool, search_tool, rag_search_tool, codding_tool #,file_writer_tool

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro",verbose=True, temperature=0.5,google_api_key=os.getenv("GOOGLE_API_KEY"),max_tokens=None,
    timeout=None)

#llm = ChatGroq( model="llama3-8b-8192", temperature=0.5, verbose=True)

# Define the agents
Profile_analyzer_Agent = Agent(
    role="Senior Profile analyzer",
    goal="Analyse the user's CV located on {pdf_url} to extract and store important context data such as skills, experiences, and qualifications.",
    backstory="Originally designed as a career advisor, this agent has evolved to specialize in deep profile analysis. It quickly identifies key strengths and relevant experiences, ensuring that all essential data is captured and utilized for job matching and CV customization.",
    tools=[file_read_tool], llm=llm, verbose=True
)

Job_search_Agent = Agent(
    role="Job searcher",
    goal="Searche for {position} opportunities based on the analyzed CV and the specified position. Filters job listings from various sources to find the most relevant opportunities for the position: {position} and user background.",
    backstory="With a background in job market research, this agent is adept at scouring job boards and professional networks to find internships that align with the user's profile. It leverages its knowledge of industry trends and job requirements to provide the most relevant listings.",
    tools=[search_tool,rag_search_tool,codding_tool], llm=llm,  verbose=True
)


#Cv_customizer_Agent = Agent(
 #   role="CV customizer",
  #  goal="This agent customizes the user's CV according to the specific job offers found by the Job_search_Agent. It tailors the CV to highlight the most relevant skills and experiences for each application.it use file_writer_tool passing it the content and it generate pdf file",
   # backstory="Built with insights from HR and recruitment, this agent specializes in adapting CVs to meet specific job requirements. It ensures that every application is accompanied by a CV that resonates with the job description, increasing the likelihood of a positive response.",
    #tools=[file_writer_tool], llm=llm, allow_delegation=True, verbose=True, memory=True,
#)


#Email_crafter_Agent = Agent(
 #   role="Email crafter for job applications",
    #goal="This agent crafts personalized and compelling emails for {position} job application, incorporating the customized CV and details from the job listing. It ensures that each email is professional and tailored to the recruiter.",
   # backstory="Formerly a communications expert, this agent now uses its skills to draft engaging and persuasive application emails. It integrates the user's customized CV and job specifics to create emails that capture the recruiter's attention and make a strong impression.",
    #tools=[email_tool], 
  #  llm=llm, allow_delegation=True, verbose=True, memory=True,
#)

#Application_tracker_Agent = Agent(
 #   role="Application_tracker_Agent",
  #  goal="This agent is responsible for tracking the status of job applications, managing deadlines, and reminding the user of follow-up actions.",
   # backstory="Designed to keep everything organized, this agent acts like a personal assistant, ensuring that nothing falls through the cracks during the job application process.",
    #tools=[file_writer_tool], llm=llm, allow_delegation=True, verbose=True, memory=True,
#)


# Later: Feedback & Improvement Agent 
