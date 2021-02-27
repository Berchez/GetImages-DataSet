# :camera: Get Images For a DataSet
If you want to make artificial intelligence that differentiates classes, but you don't have an appropriate image dataset, then this repository was made for you.

---
## :gear: How To Config ?
1. Download or Clone this repository

2. To use this repository you must have Python3 installed on your machine, click [here](https://phoenixnap.com/kb/how-to-install-python-3-windows) if you don't have it. After obtaining Python, download the [PIP](https://phoenixnap.com/kb/install-pip-windows).

3. After that, we will need to install selenium, run this command in the terminal:

> pip install selenium

4. When you finish downloading, also download the latest version of [ChromeDriver](https://chromedriver.chromium.org/downloads) and save it in the folder "C:\Program Files (x86)".

5. Once this is done, we will have to [create a profile](https://support.google.com/chrome/answer/2364824?co=GENIE.Platform%3DDesktop&hl=en) in Chrome (if you don't already have at least one). Then, access the directory 
> "C:/Users/**_YOUR-PC-USERNAME_**/AppData/Local/Google/Chrome"


and create a folder called "AutoBot" (without the quotes). Once this is done, copy all the files from the "UserData" folder and paste in the "AutoBot" folder.

6. Change the path that is in line 20 of the 'index.py' file, putting the username of your PC:

![code](https://user-images.githubusercontent.com/50505615/109402564-9c73e280-7935-11eb-9e26-61c7e25bd439.png)

## :rocket: How to use
[Open the terminal in the downloaded folder](https://www.groovypost.com/howto/open-command-window-terminal-window-specific-folder-windows-mac-linux/) And type:
> ```python index.py```

## License
The project license is MIT License - see the file LICENSE.md for more details.

