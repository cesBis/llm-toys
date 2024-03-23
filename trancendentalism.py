import json
from openai import AzureOpenAI

azure_paramater = json.load(open('.secrets/openai.json'))

client = AzureOpenAI(
    api_version = "2023-05-15",
    azure_endpoint = azure_paramater['api_url'],
    api_key = azure_paramater['api_key'],
    azure_deployment = azure_paramater['chat_model_id']
)

prompt = "Explain the transcendentalist school of thought at a third grade reading level"

response = client.chat.completions.create(
    model = azure_paramater['cheap_chat_model_name'],
    messages = [{"role" : "assistant", "content" : prompt}],
)

print(response.choices[0].message.content)
