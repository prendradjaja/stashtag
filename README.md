# stashtag

`stashtag` filters your `git` stashes by hashtags.

Not in any sort of stable state. Use at your own peril.

```sh
$ git status
On branch master

$ git stash list
stash@{0}: WIP on feature/fizz: Do the thing #fizz
stash@{1}: WIP on feature/fizz: Buzz #fizz
stash@{2}: On asdf: Verbose logging #debug
stash@{3}: On feature/fizz: Quiet logging #debug #fizz

$ stashtag debug
stash@{2}: On asdf: Verbose logging #debug
stash@{3}: On feature/fizz: Quiet logging #debug #fizz

$ stashtag fizz
stash@{0}: WIP on feature/fizz: Do the thing #fizz
stash@{1}: WIP on feature/fizz: Buzz #fizz
stash@{3}: On feature/fizz: Quiet logging #debug #fizz
```

**Multiple tags:**
```sh
$ stashtag fizz debug
stash@{3}: On feature/fizz: Quiet logging #debug #fizz
```

**Branch-specific default tags:**
```sh
$ stashtag -l  # or --list-defaults. My master branch has no defaults.

$ git checkout feature/fizz

$ stashtag -l  # My feature/fizz branch has one default tag: #fizz.
#fizz

$ stashtag
stash@{0}: WIP on feature/fizz: Do the thing #fizz
stash@{1}: WIP on feature/fizz: Buzz #fizz
stash@{3}: On feature/fizz: Quiet logging #debug #fizz

$ stashtag debug
stash@{3}: On feature/fizz: Quiet logging #debug #fizz

$ cat .stashtag  # This file must be at your git repo's root directory.
feature/fizz: fizz
```

**Ignoring defaults:**
```sh
$ stashtag -n  # or --no-defaults.
stash@{0}: WIP on feature/fizz: Do the thing #fizz
stash@{1}: WIP on feature/fizz: Buzz #fizz
stash@{2}: On asdf: Verbose logging #debug
stash@{3}: On feature/fizz: Quiet logging #debug #fizz

$ stashtag -n debug
stash@{2}: On asdf: Verbose logging #debug
stash@{3}: On feature/fizz: Quiet logging #debug #fizz
```

## Installation

**Clone this repo**
```
cd SOME_DIRECTORY
git clone https://github.com/prendradjaja/stashtag
```

**Add an alias to your bashrc**
```
alias stashtag="SOME_DIRECTORY/stashtag/stashtag.py"
```

Requires Python 3.
