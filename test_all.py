import pytest
import unittest.mock as mock

import stashtag

def test_print(capsys):
    print(3)
    out, err = capsys.readouterr()
    assert out == "3\n"

@mock.patch('git.get_branch')
def test_branch(mock_get_branch):
    mock_get_branch.return_value = 'foo'
    assert stashtag.branch() == 'foo'

stash0 = 'stash@{0}: WIP on feature/fizz: Do the thing #fizz'
stash1 = 'stash@{1}: WIP on feature/fizz: Buzz #fizz'
stash2 = 'stash@{2}: On asdf: Verbose logging #debug'
stash3 = 'stash@{3}: On feature/fizz: Quiet logging #debug #fizz'
all_stashes = [stash0, stash1, stash2, stash3]

def make_expected_output(*lines):
    return '\n'.join(lines) + '\n'

@pytest.mark.parametrize('branch,stashes,config_text,argv,expected', [
    ('master', all_stashes, '', [], make_expected_output(*all_stashes))
])
@mock.patch('config.read_config_file')
@mock.patch('git.get_stashes')
@mock.patch('git.get_branch')
def test_e2e(mock_branch, mock_stashes, mock_config, capsys, branch, stashes, config_text, argv, expected):
    mock_branch.return_value = branch
    mock_stashes.return_value = stashes
    mock_config.return_value = config_text

    stashtag.main([])
    out, err = capsys.readouterr()
    assert out == expected
