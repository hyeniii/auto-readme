from github import Github
from collections.abc import MutableMapping
import base64
import logging 
import re

logger = logging.getLogger(__name__)

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
            logger.debug("Getting file %s", content.path)
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
    # TODO: Convert this into a parameter and let user specify when parsing is added.
    ext_to_ignore = [".DS_Store", ".pdf", ".ipynb", ".csv", ".zip", ".pptx", ".jpg", ".jpeg",".png"]
    decoded_files = {}
    ignored_files = []
    for path, content in files.items():
        
        if isinstance(content, dict):
            # Recursively decode nested dictionaries
            decoded_files[path], ignored_files = decode_files(content)
        else:
            logger.debug("Path to decode: %s", path)
            # Check if the extension should be ignored.
            extension = re.findall("\.[^.]+$", path)
            try:
                extension = extension[0]
            except:
                extension = ""
            logger.debug("File extension: %s", extension)

            if extension in ext_to_ignore:
                ignored_files.append(path)
                logger.debug("Ignoring file %s", path)
                continue
            else:
                # Decode the base64-encoded content
                decoded_files[path] = base64.b64decode(content.encode('utf-8')).decode('utf-8')
                logger.info("Decoding file %s", path)

    return decoded_files, ignored_files

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