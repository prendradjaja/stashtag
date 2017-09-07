import os

def find_vcs_root(test=os.getcwd(), dirs=(".git",), default=None):
    """
    Adapted from ideasman42 on StackOverflow:
    https://stackoverflow.com/a/43786287
    """
    prev, test = None, os.path.abspath(test)
    while prev != test:
        if any(os.path.isdir(os.path.join(test, d)) for d in dirs):
            return test
        prev, test = test, os.path.abspath(os.path.join(test, os.pardir))
    return default

def read_config_file():
    """
    Return contents of config file or None
    """
    git_root = find_vcs_root()
    filepath = str(git_root) + '/.stashtag'
    # the str() call is a bit of a hack: if git_root is None, filepath will be
    # nonsense, but the condition below will evaluate to False anyway.
    if git_root and os.path.isfile(filepath):
        return open(filepath, 'r').readlines()
    else:
        return None

