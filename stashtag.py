#!/usr/bin/env python3
import sys
import subprocess

# TODO not hardcoded lol
DEFAULTS = '''
hardcoded-defaults: fizz

something: else abc
'''

def main():
    argv = sys.argv
    if '-s' in argv or '--show-defaults' in argv:
        assert len(argv) == 2
        show_branch_defaults()
    else:
        list_stashes(argv[1:])

def show_branch_defaults():
    raise Exception('Not implemented')

def list_stashes(hashtags_no_hash):
    # TODO ignore defaults
    hashtags = ['#' + tag for tag in hashtags_no_hash]
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
    # return [
    #     'stash #fizz #debug',
    #     'stash #debug',
    #     'stash #fizz',
    #     'stash',
    #     ]

def get_defaults():
    """ with # """
    branch = (subprocess.check_output('git rev-parse --abbrev-ref HEAD'.split())
            .decode('utf-8')
            .strip())
    defaults = parse_defaults(DEFAULTS)
    if branch in defaults:
        return defaults[branch]
    else:
        return []

def parse_defaults(config_text):
    nonempty = [line for line in config_text.split('\n') if line != '']
    defaults = {}
    for line in nonempty:
        branch, tags_with_spaces = line.split(':')
        tags = tags_with_spaces.split()
        tags_with_hashes = ['#' + tag for tag in tags]
        defaults[branch] = tags_with_hashes
    return defaults

if __name__ == '__main__':
    main()
