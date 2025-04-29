import os
from dotenv import load_dotenv

from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from mistralai import Mistral

load_dotenv()

API_KEY = os.getenv("API_KEY_OAI")
ENDPOINT = os.getenv("ENDPOINT_GPT4O")

API_KEY_41 = os.getenv("API_KEY_OAI")
ENDPOINT_41 = os.getenv("ENDPOINT_GPT4O")


api_key_mistral = os.getenv("API_KEY_MISTRAL")


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

def get_model_client_41() -> AzureOpenAIChatCompletionClient:

    return AzureOpenAIChatCompletionClient(
    api_version="2025-01-01-preview",
    model="gpt-4o",
    model_capabilities={
    "function_calling": True,
    "json_output": True,
    "vision": True,
    },
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    )


def get_mistral_ocr_client():
    return Mistral(api_key=api_key_mistral)

