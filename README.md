# Awesome

* SVG: [UnDraw](https://undraw.co/), [Waves](https://getwaves.io/) and [Blobs](https://www.blobmaker.app/) and [Editing](https://www.figma.com/)
* [Awesome](https://project-awesome.org/troxler/awesome-css-frameworks)
* [Shields.IO](https://shields.io/category/build)
* [Carrd](https://carrd.co/build)
* Emoji [List](https://unicode.org/Public/emoji/1.0/emoji-data.txt), [Copy](https://www.emojicopy.com/) and [Favicons](https://favicon.io/emoji-favicons/)

# Design

* [Must Watch CSS Videos](https://github.com/AllThingsSmitty/must-watch-css/blob/master/README.md)
* [Laws Of UX](https://lawsofux.com/)
* [Unsplash](https://unsplash.com/)
* [HTML5UP](https://html5up.net/)
* [Simple Icons](https://simpleicons.org/)
* [Fontello](http://fontello.com/)
* [GetWaves (SVG)](https://getwaves.io/)

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

# Create bootable USB with Ubuntu (on Mac)
* Erase the USB with mac DiskUtil (GUI) and select MS DOS (FAT)
* download ubuntu ISO image and convert it to DMG with  
  ``` hdiutil convert -format UDRW -o ~/Downloads/ubuntu-18.04.1-desktop-amd64 ~/Downloads/ubuntu-18.04.1-desktop-amd64.iso```
* Identify the USB drive with ```diskutil list```
* Run ```diskutil unmountDisk /dev/disk2```
* Run ```sudo dd if=/Users/claus/Downloads/ubuntu-18.04.1-desktop-amd64.dmg of=/dev/rdisk1 bs=1m```
