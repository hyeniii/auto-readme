from github import Github

def get_all_files(repo, path=""):
    files = {}
    contents = repo.get_contents(path)
    for content in contents:
        if content.type == "dir":
            files[content.path] = get_all_files(repo, content.path)
        else:
            files[content.path] = content.content # base64
    return files