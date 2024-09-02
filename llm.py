import ollama
import json

def write_response(prompt,
                   model,
                   client = ollama.Client(
                                host='http://llama.moo:11434',
                                timeout=8000,
                            )
                   ):

    response = client.generate(
        model = model,
        prompt = prompt
    )

    with open(model + ".json", "w") as outfile: 
        json.dump(response, outfile)

models = [
    'tinyllama:latest',
    'smollm:135m',
    'llama3.1:latest',
    'codegemma:2b',
]

prompt = """
Respond with a single word.
Where are you?
"""

for model in models:
    write_response(prompt, model)
