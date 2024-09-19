import ollama
import json


def write_response(
    prompt,
    system_prompt,
    model,
    options={},
    json_name="response",
    client=ollama.Client(
        host="http://llama.moo:11434",
        timeout=8000,
    ),
):
    response = client.generate(
        prompt=prompt,
        system=system_prompt,
        model=model,
        options=options,
    )

    json.dump(response, open(json_name + ".json", "w"))
