def fail_if(condition, message):
    if condition:
        print('Error: ' + message)
        exit(1)

def unlines(*lines):
    return ''.join(line + '\n' for line in lines)

def maybe_remove(lst, item):
    if item in lst:
        lst.remove(item)
