import subprocess

def get_stashes():
    output = (subprocess.check_output(['git', 'stash', 'list'])
        .decode('utf-8')
        .split('\n'))
    output = [line for line in output if line != '']
    return output

def get_branch():
    return (subprocess.check_output('git rev-parse --abbrev-ref HEAD'.split())
            .decode('utf-8')
            .strip())

