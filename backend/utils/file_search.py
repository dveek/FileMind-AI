# utils/file_search.py

import os


def search_files(root_directory, keyword):

    matches = []

    keyword = keyword.lower()

    for root, dirs, files in os.walk(root_directory):

        for file in files:

            if keyword in file.lower():

                matches.append(
                    os.path.join(root, file)
                )

    return matches