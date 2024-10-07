from langchain_google_community import GmailToolkit
from langchain_google_community.gmail.utils import build_resource_service, get_gmail_credentials

credentials = get_gmail_credentials(
    scopes=["https://mail.google.com/"],
    client_secrets_file="src_py\config\credentials.json",
)

###api_resource = build_resource_service(credentials=credentials)
###toolkit = GmailToolkit(api_resource=api_resource)

###email_tool= toolkit.get_tools()
