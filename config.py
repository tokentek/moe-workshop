import os
from dotenv import load_dotenv

from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

load_dotenv()

API_KEY = os.getenv("API_KEY_OAI")
ENDPOINT = os.getenv("ENDPOINT_GPT4O")


def get_model_client_4o() -> AzureOpenAIChatCompletionClient:

    return AzureOpenAIChatCompletionClient(
    api_version="2025-01-01-preview",
    model="gpt-4o-2024-11-20",
    model_capabilities={
    "function_calling": True,
    "json_output": True,
    "vision": True,
    },
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    )
