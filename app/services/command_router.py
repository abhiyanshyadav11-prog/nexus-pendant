from app.services.app_launcher import launch_app
from app.services.website_launcher import open_website
from app.services.system_control import lock_pc
from app.services.file_search import search_files
from app.services.file_opener import open_file
from app.services.command_parser import normalize_command

COMMANDS = {
    "open chrome": lambda: launch_app("chrome"),
    "open vscode": lambda: launch_app("vscode"),
    "open calculator": lambda: launch_app("calculator"),
    "open notepad": lambda: launch_app("notepad"),

    "open youtube": lambda: open_website("https://youtube.com"),
    "open github": lambda: open_website("https://github.com"),
    "lock pc": lambda: lock_pc(),
}


def execute_command(command: str):

    command = normalize_command(command)


    if command.startswith("find "):

        query = command.replace("find ", "")

        results = search_files(query)

        return results

    if command.startswith("open file "):

        file_path = command.replace("open file ", "")

        return open_file(file_path)

    if command in COMMANDS:

        COMMANDS[command]()

        return f"Executed: {command}"

    return "Unknown command"