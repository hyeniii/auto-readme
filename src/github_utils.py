from github import Github
from collections.abc import MutableMapping
import base64

def get_all_files(repo, path=""):
    """
    Recursively retrieves all files and directories from a GitHub repository.

    Parameters:
    - repo (github.Repository.Repository): An instance of a GitHub repository.
    - path (str): The directory path within the repository from which to start 
      retrieving files. Defaults to the root of the repository.

    Returns:
    dict: A nested dictionary where each key is a file or directory path, and 
    each value is either the base64-encoded content of a file or another dictionary 
    representing a directory's contents.
    """
    files = {}
    contents = repo.get_contents(path)
    for content in contents:
        if content.type == "dir":
            files[content.path] = get_all_files(repo, content.path)
        else:
            files[content.path] = content.content # base64
    return files

def decode_files(files):
    """
    Decodes the base64-encoded content of files.

    Parameters:
    - files (dict): A dictionary of files where each key is a file path and each 
      value is a base64-encoded string or a nested dictionary for directories.

    Returns:
    dict: A dictionary similar to the input but with all file contents decoded 
    from base64 to UTF-8 strings.
    """
    decoded_files = {}
    for path, content in files.items():
        if isinstance(content, dict):
            # Recursively decode nested dictionaries
            decoded_files[path] = decode_files(content)
        else:
            # Decode the base64-encoded content
            decoded_files[path] = base64.b64decode(content.encode('utf-8')).decode('utf-8')
    return decoded_files

def flatten(dictionary, parent_key='', separator='_'):
    """
    Flattens a nested dictionary into a single-level dictionary with composite keys.

    Parameters:
    - dictionary (dict): The nested dictionary to flatten.
    - parent_key (str): Used to build composite keys to represent nested structure. 
      Defaults to an empty string.
    - separator (str): The string used to separate components of the composite keys.
      Defaults to an underscore.

    Returns:
    dict: A single-level dictionary with composite keys, where each key represents 
    the path to a value in the original nested structure.
    """
    items = []
    for key, value in dictionary.items():
        if isinstance(value, MutableMapping):
            items.extend(flatten(value, key, separator=separator).items())
        else:
            items.append((key, value))
    return dict(items)