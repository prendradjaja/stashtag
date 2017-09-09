import pytest
import unittest.mock as mock
import collections

import stashtag
from util import unlines

stash0 = 'stash@{0}: WIP on feature/fizz: Do the thing #fizz'
stash1 = 'stash@{1}: WIP on feature/fizz: Buzz #fizz'
stash2 = 'stash@{2}: On asdf: Verbose logging #debug'
stash3 = 'stash@{3}: On feature/fizz: Quiet logging #debug #fizz'
all_stashes = [stash0, stash1, stash2, stash3]

P = collections.namedtuple('P', 'name,branch,args,expected')

params = [
    # Examples from the README
    P(
        name='README 10',
        branch='master',
        args=['debug'],
        expected=unlines(stash2, stash3)
    ),
    P(
        name='README 20',
        branch='master',
        args=['fizz'],
        expected=unlines(stash0, stash1, stash3)
    ),
    P(
        name='README 30',
        branch='master',
        args=['fizz', 'debug'],
        expected=unlines(stash3)
    ),
    P(
        name='README 40',
        branch='master',
        args=['-l'],
        expected=unlines()
    ),
    P(
        name='README 50',
        branch='feature/fizz',
        args=['-l'],
        expected=unlines('fizz')
    ),
    P(
        name='README 60',
        branch='feature/fizz',
        args=[],
        expected=unlines(stash0, stash1, stash3)
    ),
    P(
        name='README 70',
        branch='feature/fizz',
        args=['debug'],
        expected=unlines(stash3)
    ),
    P(
        name='README 80',
        branch='feature/fizz',
        args=['-n'],
        expected=unlines(*all_stashes)
    ),
    P(
        name='README 90',
        branch='feature/fizz',
        args=['-n', 'debug'],
        expected=unlines(stash2, stash3)
    ),

    # Other
    P(
        name='Running without arguments shows all stashes',
        branch='master',
        args=[],
        expected=unlines(*all_stashes)
    ),
]
@pytest.mark.parametrize('name,branch,args,expected', params)
@mock.patch('config.read_config_file')
@mock.patch('git.get_stashes')
@mock.patch('git.get_branch')
def test_e2e(mock_branch, mock_stashes, mock_config, capsys, name, branch, args, expected):
    mock_branch.return_value = branch
    mock_stashes.return_value = all_stashes
    mock_config.return_value = ['feature/fizz: fizz']

    stashtag.main(['UNUSED'] + args)  # argv = first_arg + args
    out, err = capsys.readouterr()
    assert out == expected, name
