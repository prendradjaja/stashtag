def fail_if(condition, message):
    if condition:
        print('Error: ' + message)
        exit(1)

def unlines(*lines):
    return ''.join(line + '\n' for line in lines)
