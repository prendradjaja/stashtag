import pytest
import unittest.mock as mock
import collections

import stashtag

# TODO move to testdata/fixtures/something
# TODO stashes,config_text don't vary
stash0 = 'stash@{0}: WIP on feature/fizz: Do the thing #fizz'
stash1 = 'stash@{1}: WIP on feature/fizz: Buzz #fizz'
stash2 = 'stash@{2}: On asdf: Verbose logging #debug'
stash3 = 'stash@{3}: On feature/fizz: Quiet logging #debug #fizz'
all_stashes = [stash0, stash1, stash2, stash3]
myconfig = ['feature/fizz: fizz']

def unlines(*lines):
    return ''.join(line + '\n' for line in lines)

P = collections.namedtuple('P', 'branch,stashes,config_text,args,expected')

# TODO maybe don't use parametrize -- makes it hard to see which test failed
# for something like this
@pytest.mark.parametrize('branch,stashes,config_text,args,expected', [
    P(
        branch='master',
        stashes=all_stashes,
        config_text=myconfig,
        args=[],
        expected=unlines(*all_stashes)
    ),
    P(
        branch='master',
        stashes=all_stashes,
        config_text=myconfig,
        args=['debug'],
        expected=unlines(stash2, stash3)
    ),
    P(
        branch='master',
        stashes=all_stashes,
        config_text=myconfig,
        args=['fizz'],
        expected=unlines(stash0, stash1, stash3)
    ),
    P(
        branch='master',
        stashes=all_stashes,
        config_text=myconfig,
        args=['fizz', 'debug'],
        expected=unlines(stash3)
    ),
    P(
        branch='master',
        stashes=all_stashes,
        config_text=myconfig,
        args=['-l'],
        expected=unlines()
    ),
    P(
        branch='feature/fizz',
        stashes=all_stashes,
        config_text=myconfig,
        args=['-l'],
        expected=unlines('fizz')
    ),
    P(
        branch='feature/fizz',
        stashes=all_stashes,
        config_text=myconfig,
        args=[],
        expected=unlines(stash0, stash1, stash3)
    ),
    P(
        branch='feature/fizz',
        stashes=all_stashes,
        config_text=myconfig,
        args=['debug'],
        expected=unlines(stash3)
    ),
    P(
        branch='feature/fizz',
        stashes=all_stashes,
        config_text=myconfig,
        args=['-n'],
        expected=unlines(*all_stashes)
    ),
    P(
        branch='feature/fizz',
        stashes=all_stashes,
        config_text=myconfig,
        args=['-n', 'debug'],
        expected=unlines(stash2, stash3)
    ),
])
@mock.patch('config.read_config_file')
@mock.patch('git.get_stashes')
@mock.patch('git.get_branch')
def test_e2e(mock_branch, mock_stashes, mock_config, capsys, branch, stashes, config_text, args, expected):
    mock_branch.return_value = branch
    mock_stashes.return_value = stashes
    mock_config.return_value = config_text

    stashtag.main(['UNUSED'] + args)  # argv = first_arg + args
    out, err = capsys.readouterr()
    assert out == expected
