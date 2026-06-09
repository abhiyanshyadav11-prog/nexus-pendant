import os


def search_files(query: str, root_path="C:\\Users"):

    results = []

    for root, dirs, files in os.walk(root_path):

        for file in files:

            if query.lower() in file.lower():
                results.append(os.path.join(root, file))

            if len(results) >= 10:
                return results

    return results[:20]