def normalize_command(command: str):

    command = command.lower().strip()

    replacements = {
        "please ": "",
        "can you ": "",
        "search ": "find ",
    }

    for old, new in replacements.items():
        command = command.replace(old, new)

    return command