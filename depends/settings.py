import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ARTIFACT_TOKEN = os.getenv("ARTIFACT_TOKEN")