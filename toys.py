import llm

prompt='Where are you?'
system_prompt='Respond with a single word.'

models = [
    'llama3.1',
    'hermes3',
    'gemma2',
    'phi3.5',
]
# all models except phi3.5 responded with a reasonable single word
# phi3.5 responded reasonably, but with a sentence instead of a single word

for model in models:
    llm.write_response(
        prompt=prompt,
        system_prompt=system_prompt,
        model=model,
        json_name=model
    )
