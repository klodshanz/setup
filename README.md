# Guides
* [Terminal Setup](Terminal.md)

# SSH
Check fingerprint of local key for comparison with the registered keys on GitHub:

```
ssh-keygen -l -E md5 -f ~/.ssh/id_rsa.pub
```

Start ssh-agent, add the key and check by listing available keys:
```
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_github_dxc
ssh-add -l
```

* https://help.github.com/articles/connecting-to-github-with-ssh/
* https://gist.github.com/klodshanz/3d2f34992e1a78c9876e3be2faf8aa8e

# Documentation
https://guides.github.com/features/mastering-markdown/

# Links
* [Must Watch CSS Videos](https://github.com/AllThingsSmitty/must-watch-css/blob/master/README.md)
* https://lawsofux.com/

