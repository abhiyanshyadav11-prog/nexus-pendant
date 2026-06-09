import os


def open_file(file_path: str):

    if os.path.exists(file_path):

        os.startfile(file_path)

        return f"Opened: {file_path}"

    return "File not found"