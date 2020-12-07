# Software

* **Fonts**
  * Desktop Fonts
    * https://fonts.google.com/specimen/Roboto+Condensed (used in Outlook for compact inbox)
    * https://fonts.google.com/specimen/Open+Sans
    * https://fonts.google.com/specimen/Roboto
  * Coding Fonts (https://github.com/ryanoasis/nerd-fonts/releases)
    * Download individual font zips and extract to a single folder
    * Select all in Explorer and choose **install**
* **Chrome** (https://www.google.com/chrome/)
* **Java SE Development Kit** (https://openjdk.java.net/)
  * Download and unzip Windows version and place in e.g. P:\jdk-15
  * Update JAVA_HOME=P:\jdk-15
  * Update CLASSPATH=P:\jdk-15\bin
* **Sublime Text** (https://www.sublimetext.com)  
  * Configuration: ```C:\Users\cljunggren\AppData\Roaming\Sublime Text 3\```
  * Transfer unsaved buffers by copying the file ```Session.sublime_session``` from ```Local``` in the configuration folder.
  * Install "Package Control"
    * https://packagecontrol.io/packages/FileIcons
    * https://packagecontrol.io/packages/1337%20Color%20Scheme
  * Add Sublime Text to PATH variable to make subl command work! (see Configuration)
* **MuCommander** (https://www.mucommander.com)
  * Configuration: ```~/.mucommander```
* **Dropbox** (https://www.dropbox.com)
* **KeePass** (https://keepass.info)
* **Launchy** (http://www.launchy.net)
  * Configuration: ```C:\Users\cljunggren\AppData\Roaming\Launchy\```
  * Skin location: ```C:\Program Files (x86)\Launchy\skins\```
* **Cmder** (http://cmder.net)  
  * Large install with Git For windows included
  * Import ConEmu.xml in Settings
  * Prompt definition : ```/opt/cmder/vendor/git-for-windows/etc/profile.d/git-prompt-lua```
* **VirtualBox** (https://www.virtualbox.org)
* **Telegram** (https://telegram.org)
* **Spotify** (https://www.spotify.com)
* **DbVisualizer** (https://www.dbvis.com)
* **paint.net** (https://www.getpaint.net)
* **GitHub for Windows** (https://desktop.github.com)
* **KeyExplorer (https://keystore-explorer.org/downloads.html)

-----

* **Docker For Windows** (https://www.docker.com/docker-windows)
* FlashBack Express Recorder (https://www.flashbackrecorder.com)
* IntelliJ IDEA
* Tray

# Configuration

## Additions to PATH variable

* ```%GRAILS_HOME%```  
* ```%MVN_HOME%```  
  Should also be defined (location in /opt/java)
* ```/opt/bin```
* ```C:\Program Files\Sublime Text 3\```

## Tweaks

* Startup Folder Windows 10 : Win+R and type ```shell:startup```
* Alt+Tab Switcher back to traditional
  * WIN+R => regedit
  * Navigate to HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer
  * Right Click: New DWORD value ```AltTabSettings``` and set to ```1```
* Map OneDrive to drive X: ```subst x: C:\Claus\OneDrive\Folder\Example``` Remove again with ```subst x: /D```
* ```opt/bin``` folder contains important executables that you use a lot

## Medarbejdercertifikat

Export from DanID Application (to html) file and just load in Firefox on the new PC.
