#!/usr/bin/env python3
import sys
import subprocess
import os

def main():
    argv = sys.argv
    if '-l' in argv or '--list-defaults' in argv:
        assert len(argv) == 2
        show_branch_defaults()
    elif '-n' in argv or '--no-defaults' in argv:
        assert argv[1] in ('-n', '--no-defaults')
        list_stashes(argv[2:], False)
    else:
        list_stashes(argv[1:], True)

def show_branch_defaults():
    defaults = get_defaults()
    if defaults:
        print(' '.join(defaults))

def list_stashes(hashtags_no_hash, use_defaults):
    # TODO ignore defaults
    hashtags = ['#' + tag for tag in hashtags_no_hash]
    if use_defaults:
        hashtags.extend(get_defaults())
    for line in get_stashes():
        if all(tag in line for tag in hashtags):
            print(line)

def get_stashes():
    output = (subprocess.check_output(['git', 'stash', 'list'])
        .decode('utf-8')
        .split('\n'))
    output = [line for line in output if line != '']
    return output

def get_defaults():
    """ with # """
    branch = (subprocess.check_output('git rev-parse --abbrev-ref HEAD'.split())
            .decode('utf-8')
            .strip())
    config_text = read_config_file()
    defaults = {}
    if config_text:
        defaults = parse_defaults(config_text)
    if branch in defaults:
        return defaults[branch]
    else:
        return []

def parse_defaults(config_text):
    nonempty = [line for line in config_text if line != '\n']
    defaults = {}
    for line in nonempty:
        branch, tags_with_spaces = line.split(':')
        tags = tags_with_spaces.split()
        tags_with_hashes = ['#' + tag for tag in tags]
        defaults[branch] = tags_with_hashes
    return defaults

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

if __name__ == '__main__':
    main()
