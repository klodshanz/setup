# Git Recipes

## Make current branch to master

Source from [stackoverflow](http://stackoverflow.com/a/2763118)

```Shell
$ git checkout better_branch
$ git merge --strategy=ours master           # keep the content of this branch, but record a merge
$ git checkout master
$ git merge better_branch                    # fast-forward master up to the merge
```

And to document better 

```Shell
git merge --strategy=ours --no-commit master
git commit                                   # add information to the template merge message
```
