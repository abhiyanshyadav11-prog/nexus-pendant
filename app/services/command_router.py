from app.services.app_launcher import launch_app
from app.services.website_launcher import open_website


def execute_command(command: str):

    command = command.lower().strip()

    if "youtube" in command:
        open_website("https://youtube.com")
        return "Opened YouTube"

    if "chrome" in command:
        launch_app("chrome")
        return "Opened Chrome"

    return "Unknown command"