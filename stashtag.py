#!/usr/bin/env python3
import sys

import git
import config
from util import fail_if, maybe_remove

def main(argv):
    if '-l' in argv or '--list-defaults' in argv:
        fail_if(len(argv) != 2,
                '-l (or --list-defaults) cannot be used with other arguments.')
        show_branch_defaults()
    elif '-n' in argv or '--no-defaults' in argv:
        argv = list(argv)
        maybe_remove(argv, '-n')
        maybe_remove(argv, '--no-defaults')
        list_stashes(argv[1:], False)
    else:
        list_stashes(argv[1:], True)

def show_branch_defaults():
    defaults = get_defaults()
    if defaults:
        print(' '.join(defaults))

def list_stashes(hashtags, use_defaults):
    if use_defaults:
        hashtags.extend(get_defaults())
    hashtags = add_hash_symbol(hashtags)
    for line in git.get_stashes():
        if all(tag in line for tag in hashtags):
            print(line)

def get_defaults():
    branch = git.get_branch()
    config_text = config.read_config_file()
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
        defaults[branch] = tags
    return defaults

def add_hash_symbol(lst):
    return ['#' + tag for tag in lst]

if __name__ == '__main__':
    main(sys.argv)
