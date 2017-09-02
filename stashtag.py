#!/usr/bin/env python3
import sys
import subprocess

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
    # TODO branch defaults (then ignore defaults too)
    hashtags = ['#' + tag for tag in hashtags_no_hash]
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

if __name__ == '__main__':
    main()
