`stashtag` filters your `git` stashes by hashtags.
```
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
stash@{1}: WIP on feature/fizz: Buzz #fizz
stash@{3}: On feature/fizz: Quiet logging #debug #fizz
```

Multiple hashtags:
```
$ stashtag fizz debug
stash@{3}: On feature/fizz: Quiet logging #debug #fizz
```

Branch-specific default hashtags:
```
$ stashtag -s  # or --show-defaults

$ git checkout feature/fizz

$ stashtag -s
fizz

$ stashtag
stash@{1}: WIP on feature/fizz: Buzz #fizz
stash@{3}: On feature/fizz: Quiet logging #debug #fizz

$ stashtag debug
stash@{3}: On feature/fizz: Quiet logging #debug #fizz

$ cat .stashtag
feature/fizz: fizz
```

Ignoring defaults:
```
$ stashtag -n  # or --no-defaults
stash@{0}: WIP on feature/fizz: Do the thing #fizz
stash@{1}: WIP on feature/fizz: Buzz #fizz
stash@{2}: On asdf: Verbose logging #debug
stash@{3}: On feature/fizz: Quiet logging #debug #fizz

$ stashtag -n debug
stash@{2}: On asdf: Verbose logging #debug
stash@{3}: On feature/fizz: Quiet logging #debug #fizz
```
