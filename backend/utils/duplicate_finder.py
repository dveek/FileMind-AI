# utils/duplicate_finder.py

import hashlib
import os


def get_hash(filepath):

    hasher = hashlib.md5()

    try:

        with open(filepath, "rb") as f:

            while chunk := f.read(4096):

                hasher.update(chunk)

        return hasher.hexdigest()

    except:

        return None


def find_duplicates(folder):

    hashes = {}

    duplicates = []

    for root, dirs, files in os.walk(folder):

        for file in files:

            path = os.path.join(root, file)

            file_hash = get_hash(path)

            if not file_hash:
                continue

            if file_hash in hashes:

                duplicates.append(
                    (hashes[file_hash], path)
                )

            else:

                hashes[file_hash] = path

    return duplicates