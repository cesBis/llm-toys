import llm

prompt='Where are you?',
system_prompt='Respond with a single word.',

models = [
    'llama3.1', # provides a reasonable one word anser
    'tinyllama', # does not follow one word instruction. asks for more information. knows it's a computer
    'smollm:135m', # does not follow one word instruction. adopts a human persona. says its at work or busy.
]

# on first pass
# tinyllama was the fastest by an order of magnitude
# and responded 2nd best to llama
# it's been hard to get a good answer out of it though
# it doesn't appear as responsive to the system prompt

# on another pass
# llama was the fastest and best response
# perhaps most time is in reading the model from disk to ram
# thus, subsequent calls are much faster?
# perhaps instead of total_duration, should measure load_duration or eval_duration?
# indeed, when measuring eval_duration llama is much faster
# but load_duration (the time it takes to get from disk to memory), is much slower

# on other passes
# set temperature to 0, no discernible effect
# add repeat_penalty at 10, no discernible effect
# replace repeat_penalty with mirostat_tau at 0.1, no discernible effect
# https://github.com/ollama/ollama/blob/main/docs/api.md#request-7

for model in models:
    llm.write_response(
        prompt=prompt,
        system_prompt=system_prompt,
        model=model,
        json_name = model
    )
