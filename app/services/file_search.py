import os
from app.services.search_memory import LAST_RESULTS


def search_files(query: str, root_path="C:\\Users"):

    results = []

    for root, dirs, files in os.walk(root_path):

        for file in files:

            if query.lower() in file.lower():
                results.append(os.path.join(root, file))

            if len(results) >= 10:
                break

    LAST_RESULTS.clear()
    LAST_RESULTS.extend(results)

    return results[:20]