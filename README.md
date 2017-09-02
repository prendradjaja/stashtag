`stashtag` filters your stashes by hashtags.
```sh
$ git status
On branch master

$ git stash list
stash@{0}: ... WIP on feature/fizz: Do the thing #fizz
stash@{1}: ... WIP on feature/fizz: Buzz #fizz
stash@{2}: ... On asdf: Verbose logging #debug
stash@{3}: ... On feature/fizz: Quiet logging #debug #fizz

$ stashtag debug
stash@{2}: ... On asdf: Verbose logging #debug
stash@{3}: ... On feature/fizz: Quiet logging #debug #fizz

$ stashtag fizz
stash@{1}: ... WIP on feature/fizz: Buzz #fizz
stash@{3}: ... On feature/fizz: Quiet logging #debug #fizz
```

Multiple hashtags:
```sh
$ stashtag fizz debug
stash@{3}: ... On feature/fizz: Quiet logging #debug #fizz
```

```sh
$ stashtag -b  # or --branch-defaults

$ git checkout feature/fizz

$ stashtag -b
fizz

$ stashtag debug
stash@{3}: ... On feature/fizz: Quiet logging #debug #fizz

$ cat .stashtag
feature/fizz: fizz
```
