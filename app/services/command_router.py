from app.services.app_launcher import launch_app
from app.services.website_launcher import open_website
from app.services.system_control import lock_pc

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

    command = command.lower().strip()

    if command in COMMANDS:
        COMMANDS[command]()
        return f"Executed: {command}"

    return f"Unknown command: {command}"