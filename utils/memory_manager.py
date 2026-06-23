import json
import os


MEMORY_FILE = "memory/research_memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_memory(memory):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )


def get_topic(topic):

    memory = load_memory()

    return memory.get(topic)


def save_topic(
    topic,
    report,
    summary,
    sources
):

    memory = load_memory()

    memory[topic] = {
        "report": report,
        "summary": summary,
        "sources": sources
    }
    save_memory(memory)