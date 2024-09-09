import llm

prompt='Describe the style of Emily Dickinson'
system_prompt="""
You are a concise, curt, poetry critic. You will be asked about a poet.
Respond with a brief summary, and an example of the poet's work.
"""

models = [
    'llama3.1', # good, coherent response; but misquoted a poem
    'hermes3', # best reponse, adhered to the system_prompt the best, was fastest, and used the most natural language
    'gemma2', # good response, but seemed robotic and overstructured
    'phi3.5', # lost coherency through its response
]

for model in models:
    llm.write_response(
        prompt=prompt,
        system_prompt=system_prompt,
        model=model,
        json_name=model
    )
