# Fonts

* **Fonts Desktop**
  * https://fonts.google.com/specimen/Roboto+Condensed (used in Outlook for compact inbox)
  * https://fonts.google.com/specimen/Open+Sans (General DXC Typeface)
  * https://fonts.google.com/specimen/Roboto (Robust Sans Serif)
* **Fonts Coding**
  * https://www.jetbrains.com/lp/mono (For PyCharm and IntelliJ - skal installeres eksplicit for access uden for JetBrains)
  * https://fonts.google.com/specimen/Roboto+Mono (Sublime Text)
  * https://github.com/tonsky/FiraCode (Releases > Fira_Code_v6.2.zip)
  * https://fonts.google.com/specimen/IBM+Plex+Mono
  * https://typeof.net/Iosevka
    * Download Fonts `>` Releases `>` Show All XXX Assets `>` ttc-iosevka-22.0.2.zip

# Software

Efter installation af DXC Image - vent noget tid for at software komponenter automatisk installeres (Conradsen siger ½ time). Herefter kan der installeres nogle komponenter fra DXC Company Portal.

* **Install from Company Portal**
  * 7zip
  * Windows Terminal
  * Adobe Acrobat Reader DC
  * Ivanti Secure Access Client
* **Chrome** (https://www.google.com/chrome/)
* **AutoHotKey** (https://www.autohotkey.com)
* **Sublime Text** (https://www.sublimetext.com)  
  * Configuration: ```C:\Users\cljunggren\AppData\Roaming\Sublime Text 3\```
  * Transfer unsaved buffers by copying the file ```Session.sublime_session``` from ```Local``` in the configuration folder.
  * Install "Package Control"
    * https://packagecontrol.io/packages/FileIcons
    * https://packagecontrol.io/packages/1337%20Color%20Scheme
  * Add Sublime Text to PATH variable to make subl command work! (see Configuration)
* **Sublime Merge** (https://www.sublimemerge.com)
* **JetBrains Toolbox** (https://www.jetbrains.com/toolbox-app)
* **Launchy** (http://www.launchy.net)
  * Configuration: ```C:\Users\cljunggren\AppData\Roaming\Launchy\```
  * Skin location: ```C:\Program Files (x86)\Launchy\skins\```
* **Spotify** (https://www.spotify.com)
  * Configure local files to point to Dropbox://Music/Spotify
* **paint.net** (https://www.getpaint.net)
* **VLC** (https://www.videolan.org/vlc/)
* **GitHub for Windows** (https://desktop.github.com)
* **Git for Windows** (* https://git-scm.com/downloads/win)
* **KeyStore Explorer**
  * Download Zip File and extract to ```P:\utils```

## ```C:\opt```

Visse applikationer ligger under ```C:\opt``` der mappes til p-drevet. Disse vil bare virke når stien er etableret på den nye maskine og kopieret fra backup. Disse applikationer er følgende:

* **Java SE Development Kit** (https://openjdk.java.net/)
  * Download and unzip Windows version and place in e.g. P:\jdk-24.0.2
  * Update Environment Variables (WIN+R > ```rundll32.exe sysdm.cpl,EditEnvironmentVariables```)
    * ```JAVA_HOME=C:\opt\jdk-24.0.2```
    * ```CLASSPATH=C:\ope\jdk-24.0.2\bin```
* **MuCommander** (https://www.mucommander.com)
  * Download Portable Version and extract to ```P:\mu```
  * Configuration in ```P:\mu\.mucommander``` copy from ```X:\.backup```
  * Grap https://search.maven.org/artifact/com.formdev/flatlaf/3.2.1/jar and place it in ```P:\mu\bundle```
* **KeePass** (https://keepass.info)
  * Download Zip File and extract to ```P:\utils```
* **Cmder** (http://cmder.net)  
  * Choose Large install as it includes git For windows
  * Import ConEmu.xml in Settings
  * Prompt definition : ```/opt/cmder/vendor/git-for-windows/etc/profile.d/git-prompt-lua```

## Gear Software

* **Camera** (https://www.logitech.com/da-dk/software/capture.html)  
  Version ```Capture_2.06.12.exe``` er p.t. den eneste version der virker i Teams.
* **Keyboard** + **Mus** (https://www.logitechg.com/en-us/innovation/g-hub.html)
* **Elgato Control Center** (https://www.elgato.com/us/en/s/downloads)

## Alternative

* **Audacity** (https://www.audacityteam.org/download/windows)
* **Telegram** (https://telegram.org)
* **DbVisualizer** (https://www.dbvis.com)

# Setup

* **Google Chrome**  
  * **Bookmarks**  
    Bookmarks er sync'et, så når der logges ind i google kommer alle bookmarks - nedenstående er mere som backup
    * Export fra Chrome (CTRL+SHIFT+O) > Kebab-menu > Export Bookmarks
    * Import til Chrome (CTRL+SHIFT+O) > Kebab-menu > Import Bookmarks
  * **Extensions**
    * NewTab
    * Pinboard
    * Jenkins
* **Windows 11**  
  * **Startup**  
    Startup Folder Windows 11 : WIN+R > ```shell:startup``` her placeres ```C:\opt\bin\startup.cmd```  
  * **Power, sleep and battery settings**  
    Under **Screen, sleep and hibernate timeouts** findes **Plugged in** og her skal vælges:
      * Make my device sleep after **Never**
      * Make my device hibernate after **Never**

## Tweaks

* Alt+Tab Switcher back to traditional
  * WIN+R => regedit
  * Navigate to HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer
  * Right Click: New DWORD value ```AltTabSettings``` and set to ```1```
