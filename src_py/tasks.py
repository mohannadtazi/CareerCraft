from crewai import Task
from src_py.agents import Profile_analyzer_Agent, Job_search_Agent#, Cv_customizer_Agent, Email_crafter_Agent, Application_tracker_Agent
from src_py.tools import file_read_tool, search_tool, rag_search_tool, codding_tool# , file_writer_tool


profile_analysis_task = Task(
    description=(
        "Analyze the provided CV at this path {pdf_url} by passing this path to the tool file_read_tool"
        "and extract all relevant information use the file_read_tool, "
        "including skills, experiences, education, and contact details. "
        "This information should be structured and ready for use in subsequent tasks."
    ),
    expected_output="A detailed report in markdown summarizing strengths and weaknesses points with all key information extracted from the CV.",
    agent=Profile_analyzer_Agent,
    tools=[file_read_tool],
    output_file="profile_analysis.md"
)



job_search_task = Task(
    description=(
        "Search for job offers related to the position {position} across platforms like LinkedIn and Indeed." 
        "But it should be in the same location as the user. If the location is not specified, the search should be abt Morocco."
        "Use the extracted information from the CV such as the localisation and level to filter and match relevant job offers."
        "The search should focus on matching the key skills and experiences extracted from the CV."
    ),
    expected_output="Markdown list of relevant job offers informations. and a link to apply",
    agent=Job_search_Agent,
    tools=[search_tool, rag_search_tool,codding_tool],
    allow_code_execution=True,
    context=[profile_analysis_task]
)



#cv_customization_task = Task(
 #   description=(
  #      "Customize the CV based on the job offers found by the Job_search_Agent. "
   #     "Highlight the most relevant skills and experiences for each specific job offer for {position}."
    #    "The final CV should be saved as a PDF file."
    #),
##   agent=Cv_customizer_Agent,
  #   tools=[file_writer_tool],
   # output_file="custom_cv.pdf",
    #context=[profile_analysis_task, job_search_task]
#)


#email_crafting_task = Task(
 #   description=(
  #      "Craft a draft email for the job application using the customized CV. "
   #     "The email should be tailored to the company and the specific job offer, highlighting why the candidate is a good fit."
       # "The email should be ready to send via Gmail."
    #),
#    expected_output="A customized email (email.txt) that aligns with the job offers found.",
 #   agent=Email_crafter_Agent,
  #  output_file="email.txt",
   # context=[profile_analysis_task, job_search_task]
#)


#application_tracking_task = Task(
 #   description=(
  #      "Update the application tracking file with the new job offers found. "
   #     "Ensure that there are no duplicate entries and that all relevant details are captured."
    #),
 #   expected_output="An updated Excel file (application_tracking.xlsx) with the latest job applications tracked.",
 #   agent=Application_tracker_Agent,
  #   tools=[file_writer_tool],
   # output_file="application_tracking.xlsx"
#)
