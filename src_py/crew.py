from crewai import Crew
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from src_py.tasks import profile_analysis_task,job_search_task#,cv_customization_task,email_crafting_task,application_tracking_task
from src_py.agents import Profile_analyzer_Agent,Job_search_Agent#,Cv_customizer_Agent,Email_crafter_Agent,Application_tracker_Agent

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",verbose=True, 
temperature=0.2,google_api_key=os.getenv("GOOGLE_API_KEY"))


crew= Crew(agents=[Profile_analyzer_Agent, Job_search_Agent],#, Cv_customizer_Agent, Email_crafter_Agent, Application_tracker_Agent],
tasks=[profile_analysis_task, job_search_task],#, cv_customization_task, email_crafting_task, application_tracking_task],
)

