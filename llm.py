from ollama import Client

client = Client(
    host='http://llama:11434',
    timeout=8000,
)

system_prompt = """
Respond concisely and correctly.
"""

assistant_prompt = """

"""

user_prompt = """
about how big do pigs need to be to produce jowl bacon?
"""

response = client.chat(
    model = "tinyllama",
    messages = [
        {"role" : "system", "content" : system_prompt},
        {"role" : "user", "content" : user_prompt},
    ],
)
