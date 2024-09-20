import llm

prompt = """
Draft a bullet point list of 3 discussion prompts on the topic of Health Equity in the United States.
Preface this list with a short introductory paragraph.
"""

system_prompt = """
You are a profound and thoughtful professor.
An expert on Healthcare in the United States.
You enjoy use of the socratic method, and leaving things open to interpretation.
"""

# by duration
# hermes3 < llama3.1 < phi3.5 < gemma2
models = [
    "llama3.1",  # the best, but nonetheless, still bland discussion points
    "hermes3",  # pretty good. paroted "profound" but wasn't that profound
    "gemma2",  # what a try hard for the "profound professor" thing
    "phi3.5",  # a bit disjointed
]

for model in models:
    llm.write_response(
        prompt=prompt, system_prompt=system_prompt, model=model, json_name=model
    )
