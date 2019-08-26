import os
from dotenv import load_dotenv
import slack

dotenv_path = os.path.join(os.path.dirname(__file__), '../../../../.env')
load_dotenv(dotenv_path)


client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

