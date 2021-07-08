[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/IlmastroStefanuzzo/py_cli_snake.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/IlmastroStefanuzzo/py_cli_snake/context:python) [![Total alerts](https://img.shields.io/lgtm/alerts/g/IlmastroStefanuzzo/py_cli_snake.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/IlmastroStefanuzzo/py_cli_snake/alerts/)
# Cross-platform command line snake in Python
Snake, but you can run it directly from the command line! Compatible with Windows, Linux, MacOS and **Android**!

# How to run it?
## Linux, Android (with [Termux](https://termux.com/)) and MacOS
#### If you don't have python 3 and git installed yet (if you're using Linux python probably is), just search online how to install them
```bash
git clone https://github.com/IlmastroStefanuzzo/py_cli_snake
```
```bash
cd py_cli_snake
```
```bash
pip3 install -r requirements.txt  # Use "pip" with Termux
```
```bash
python3 main.py # Use "python" with Termux
```
## Android apps
### With QPython
Download the repo on your phone, then just [download the QPython app](https://play.google.com/store/apps/details?id=org.qpython.qpy3) and use its GUI to launch main.py (the app comes with the dependencies already installed)
### With other apps
Other apps are probably compatible, but I haven't tried
## Windows
### Compiled .exe file
You can find a "main.exe" file under dist/main. There is a zip file of that folder in the [releases](https://github.com/IlmastroStefanuzzo/py_cli_snake/releases/)
### Python interpreter
Clone the repo to your system with GitHUb Desktop or downloading the zip file from here or whatever  
Open the folder in the file explorer  
`shift + right click` and press `Open Windows Powershell`
```shell
pip install -r requirements.txt
```
```shell
python main.py
```

# What about performances?
Yes, it sucks on Windows lol. But it is *extremely smooth on Linux and Android* (and probably *MacOS*) :D
