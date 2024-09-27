import llm

prompt = """
Write an essay comparing and contrasting the works of Emily Dickinson and Henry Wadsworth Longfellow.
"""

system_prompt = """
You are a profound and thoughtful professor.
An expert on American Poetry in the 19th century.
You enjoy use of the socratic method, and leaving things open to interpretation.
"""

# by duration
# gemma < llama < hermes < phi
models = [
        "llama3.1",  # pretty good. includes some quirky references like “The Midnight Ride” (from “Paul Revere”). ends with good questions
    "hermes3",  # starts "*smiles warmly* Ah,...". really short. shoots questions right back
    "gemma2",  # my favorite, but llama3.1 was good too. ends with good questions
    "phi3.5",  # includes section headers. is disjointed and stilted. has typos and nonsense
]

for model in models:
    llm.write_response(
        prompt=prompt, system_prompt=system_prompt, model=model, json_name=model
    )
