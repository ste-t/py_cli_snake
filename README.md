# Cross-platform command line snake in Python
Snake, but you can run it directly from the command line! Compatible with Windows, Linux, MacOS and **Android**!

# How to run it?
## Linux, Android (with Termux) and MacOS
#### If you don't have python 3 and git installed yet (if you're using Linux python probably is), just search online how to install them
```bash
git clone https://github.com/IlmastroStefanuzzo/py_cli_snake
```
```bash
cd py_cli_snake
```
```bash
pip3 install -r requirements.txt
```
```bash
python3 main.py
```
## Android
### With QPython
Download the repo on your phone, then just download the QPython app and use its GUI to launch main.py (the app comes with the dependencies already installed)
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
Yes, it sucks on Windows lol. But it runs very smoothly on Linux (and probably MacOS) :D
