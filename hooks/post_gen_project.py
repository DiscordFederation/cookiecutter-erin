from typing import List

ignore_lines = """
# Erin Configuration Files
{{cookiecutter.config_file}}
"""


def append_contents(filename, items: List[str]):
    with open(filename, "a") as fh:
        for item in items:
            fh.write(f"\n{item}")


if __name__ == "__main__":
    append_contents(".ignore", ignore_lines.strip("\n").split("\n"))
