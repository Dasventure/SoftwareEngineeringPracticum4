from pathlib import Path

import json


def read_file(file_name: Path):
    """
        Read the file.
    """
    with open(file_name, 'r') as in_file:
        return in_file.read()


def write_file(fileName: Path, contents):
    """
        Write the file.
    """
    with open(fileName, 'w') as out_file:
        out_file.write(contents)


def write_json_file(filename: str, data: list):
    write_file(json.dumps(obj=data), data)

def read_file_json(filename: str):
    return json.loads(s=read_file(filename))
