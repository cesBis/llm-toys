import json
from openai import AzureOpenAI

azure_paramater = json.load(open('.secrets/openai.json'))

client = AzureOpenAI(
    api_version = "2023-05-15",
    azure_endpoint = azure_paramater['api_url'],
    api_key = azure_paramater['api_key'],
    azure_deployment = azure_paramater['chat_model_id']
)

text_output = open('trancendentalism.md', 'a')
for number in range(1, 13, 1):
    prompt = f'Explain the transcendentalist school of thought at a grade {number} reading level'
    text_output.write(f'\n\n## {prompt}\n\n')
    response = client.chat.completions.create(
        model = azure_paramater['cheap_chat_model_name'],
        # https://platform.openai.com/docs/guides/chat-completions/message-roles
        messages = [
            {"role" : "user", "content" : prompt}
        ],
    )
    text_output.write(response.choices[0].message.content)
text_output.close()
