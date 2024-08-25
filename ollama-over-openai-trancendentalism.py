from openai import OpenAI

client = OpenAI(
    base_url='http://llama:11434/v1/',
    timeout=8000,
    max_retries=3,
    api_key='ollama', # required but ignored
)

text_output = open('trancendentalism.md', 'a')
for number in [5]:
    prompt = f'Explain the transcendentalist school of thought at a grade {number} reading level'
    text_output.write(f'\n\n## {prompt}\n\n')
    response = client.chat.completions.create(
        model = "llama3.1",
        # https://platform.openai.com/docs/guides/chat-completions/message-roles
        messages = [
            {"role" : "user", "content" : prompt}
        ],
    )
    text_output.write(response.choices[0].message.content)
text_output.close()
