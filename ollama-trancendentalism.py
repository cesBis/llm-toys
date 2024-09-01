from ollama import Client

client = Client(
    host='http://llama:11434',
    timeout=8000,
)

text_output = open('trancendentalism.md', 'a')
for number in range(1, 13, 1):
    prompt = f'Explain the transcendentalist school of thought at a grade {number} reading level'
    text_output.write(f'\n\n## {prompt}\n\n')
    response = client.chat(
        model = "smollm:135m",
        # https://platform.openai.com/docs/guides/chat-completions/message-roles
        messages = [
            {"role" : "user", "content" : prompt}
        ],
    )
    text_output.write(response['message']['content'])
text_output.close()
