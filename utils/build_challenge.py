#!/usr/bin/env python
"""
Script meant to be run in the directory of the challenge type.
Ex: `Data_Structures_and_Algorithms/Arrays/Easy/`

export/source the filepath for this script in the appropriate config:
Ex: .zshrc, .bashrc, ~/.venv/<VIRTUALENV>/bin/activate
"""
import sys
import os
import shutil


BUILD_CHALLENGE_BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CHALLENGE_DIR_TEMPLATE = (
    f"{BUILD_CHALLENGE_BASE_PATH}/templates/PYTHON_CHALLENGE_DIR_TEMPLATE"
)
README_MD_PATH = f"{BUILD_CHALLENGE_BASE_PATH}/../README.md"
PYTHON_LOGO_PATH = "utils/images/logos/python.png"


def get_challenge_name():
    """
    Gets the challenge name from the cmd line args
    """
    if len(sys.argv) < 2:
        raise ValueError("You must provide a challenge name")
    if os.getcwd().split('/')[-1] not in ["Easy", "Medium", "Hard"]:
        raise RuntimeError(
            "Your working directory must be a valid challenge category in "
            "one of these subdirectories: (Easy, Medium, Hard)"
        )
    return sys.argv[1]


def build_challenge_dir(challenge_name: str,
                        challenge_base_path: str = os.getcwd()) -> None:
    """
    Builds the challenge directory at the provided path with the following
    structure:

        challenge_name/
        ├── description.md
        ├── solutions.py
        └── tests.json
    """
    challenge_dir_path = f"{challenge_base_path}/{challenge_name}"
    try:
        shutil.copytree(
            CHALLENGE_DIR_TEMPLATE, challenge_dir_path
        )
    except FileExistsError:
        raise FileExistsError(
            "You must provide a unique challenge name"
        )
    return challenge_dir_path


def titalize_str(string: str) -> str:
    """
    Makes the given string titlecase and replaces underscores with spaces
    """
    string = string.title()
    string = string.replace('_', " ")
    return string


def create_table_row(challenge_dir_path: str,
                     logo_path: str = PYTHON_LOGO_PATH) -> str:
    """
    Creates the new challenge row for the md table on README.md
    """
    challenge_type, difficulty, name = (challenge_dir_path).split("/")[-3:]
    titalized_type = titalize_str(challenge_type)
    titalized_name = titalize_str(name)
    capitalized_name = name.title()
    capitalized_name = capitalized_name.replace('_', " ")
    return (
        f"{titalized_type} | {difficulty}"
        f" | [{titalized_name}]({challenge_dir_path}/description.md)"
        f" | [<img src={logo_path} alt='python' width='24'/>]"
        f"({challenge_type}/{difficulty}/{name}/solutions.py)\n"
    )


def sort_table_rows(table_rows: list) -> list:
    """
    Sorts the table rows by type, difficulty, and name
    """
    rows_lst = [row.split(" | ") for row in table_rows]
    rows_lst.sort(key=lambda r: (r[0], r[1], r[2]))
    return [" | ".join(row) for row in rows_lst]


def add_challenge_to_readme(challenge_dir_path: str) -> None:
    """
    Adds the new challenge and links to the md table in README.md
    """
    new_challenge_row = create_table_row(challenge_dir_path)

    with open(README_MD_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
        alignment_row_idx = lines.index(":-|:-:|:-|:-:|\n")
        header = lines[:alignment_row_idx+1]
        challenge_rows = lines[alignment_row_idx+1:]
        challenge_rows.append(new_challenge_row)
        challenge_rows = sort_table_rows(challenge_rows)
        processed_lines = header + challenge_rows

    with open(README_MD_PATH, "w", encoding="utf-8") as f:
        f.writelines(processed_lines)


def main():
    """
    Main driver function
    """
    try:
        challenge_name = get_challenge_name()
        challenge_dir_path = build_challenge_dir(challenge_name)
        add_challenge_to_readme(challenge_dir_path)
    except (ValueError, RuntimeError, FileExistsError) as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
