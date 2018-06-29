"""
Utilities for analyzing files within the git repo
"""

TEXT_EXTENSIONS = [
    "rs", "py", "txt", "md", "toml", "yml"
]

def is_source_file(filename):
    """
    Whether the filename is source code
    """
    for ext in TEXT_EXTENSIONS:
        if filename.endswith(ext):
            return True

    return False
