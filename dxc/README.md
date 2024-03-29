# Fonts

* **Fonts Desktop**
  * https://fonts.google.com/specimen/Roboto+Condensed (used in Outlook for compact inbox)
  * https://fonts.google.com/specimen/Open+Sans (General DXC Typeface)
  * https://fonts.google.com/specimen/Roboto (Robust Sans Serif)
* **Fonts Coding**
  * https://www.jetbrains.com/lp/mono (For PyCharm and IntelliJ)
  * https://fonts.google.com/specimen/Roboto+Mono (Sublime Text)
  * https://github.com/tonsky/FiraCode (Releases > Fira_Code_v6.2.zip)
  * https://fonts.google.com/specimen/IBM+Plex+Mono
  * https://typeof.net/Iosevka
    * Download Fonts `>` Releases `>` Show All XXX Assets `>` ttc-iosevka-22.0.2.zip

# Software

* **Chrome** (https://www.google.com/chrome/)
* **Dropbox** (https://www.dropbox.com)
  * Setup to keep all files locally
* **Sublime Text** (https://www.sublimetext.com)  
  * Configuration: ```C:\Users\cljunggren\AppData\Roaming\Sublime Text 3\```
  * Transfer unsaved buffers by copying the file ```Session.sublime_session``` from ```Local``` in the configuration folder.
  * Install "Package Control"
    * https://packagecontrol.io/packages/FileIcons
    * https://packagecontrol.io/packages/1337%20Color%20Scheme
  * Add Sublime Text to PATH variable to make subl command work! (see Configuration)
* **Sublime Merge** (https://www.sublimemerge.com)
* **Java SE Development Kit** (https://openjdk.java.net/)
  * Download and unzip Windows version and place in e.g. P:\jdk-15
  * Update Environment Variables (WIN+R > ```rundll32.exe sysdm.cpl,EditEnvironmentVariables```)
    * ```JAVA_HOME=P:\jdk-15```
    * ```CLASSPATH=P:\jdk-15\bin```
* **JetBrains Toolbox** (https://www.jetbrains.com/toolbox-app)
* **MuCommander** (https://www.mucommander.com)
  * Download Portable Version and extract to ```P:\mu```
  * Configuration in ```P:\mu\.mucommander``` copy from ```X:\.backup```
  * Grap https://search.maven.org/artifact/com.formdev/flatlaf/3.2.1/jar and place it in ```P:\mu\bundle```
* **Launchy** (http://www.launchy.net)
  * Configuration: ```C:\Users\cljunggren\AppData\Roaming\Launchy\```
  * Skin location: ```C:\Program Files (x86)\Launchy\skins\```
* **AutoHotKey** (https://www.autohotkey.com)
* **Cmder** (http://cmder.net)  
  * Choose Large install as it includes git For windows
  * Import ConEmu.xml in Settings
  * Prompt definition : ```/opt/cmder/vendor/git-for-windows/etc/profile.d/git-prompt-lua```
* **Slack** (https://slack.com/downloads/windows)
* **Spotify** (https://www.spotify.com)
  * Configure local files to point to Dropbox://Music/Spotify
* **paint.net** (https://www.getpaint.net)
* **Adobe Acrobat Reader** (https://get.adobe.com/reader/)
* **VLC** (https://www.videolan.org/vlc/)
* **GitHub for Windows** (https://desktop.github.com)
* **Install from Microsoft Store**
  * 7zip
  * Windows Terminal
* **KeePass** (https://keepass.info)
  * Download Zip File and extract to ```P:\utils```
* **KeyStore Explorer**
  * Download Zip File and extract to ```P:\utils```
## Gear Software

* **Camera** (https://www.logitech.com/da-dk/software/capture.html)
* **Keyboard** (https://www.logitechg.com/en-us/innovation/g-hub.html)
* **Elgato Control Center** (https://www.elgato.com/us/en/s/downloads)

## Alternative

* **Audacity** (https://www.audacityteam.org/download/windows)
* **Telegram** (https://telegram.org)
* **DbVisualizer** (https://www.dbvis.com)

# Setup

* Chrome Bookmarks
  * Export fra Chrome (CTRL+SHIFT+O) > Kebab-menu > Export Bookmarks
  * Import til Chrome (CTRL+SHIFT+O) > Kebab-menu > Import Bookmarks
* Chrome Extensions
  * NewTab
  * Pinboard
  * Jenkins
* Power and Sleep Settings
  * Never sleep when on Power

## Tweaks

* Startup Folder Windows 10 : Win+R > ```shell:startup```
* Alt+Tab Switcher back to traditional
  * WIN+R => regedit
  * Navigate to HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer
  * Right Click: New DWORD value ```AltTabSettings``` and set to ```1```
* Map OneDrive to drive X: ```subst x: C:\Claus\OneDrive\Folder\Example``` Remove again with ```subst x: /D```
* ```opt/bin``` folder contains important executables that you use a lot

## Medarbejdercertifikat

Export from DanID Application (to html) file and just load in Firefox on the new PC.
