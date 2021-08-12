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
python3 main.py
# Command's name (python3) may vary depending on your platform and how you installed python
# Use "python" with Termux if you installed python through pkg install python
```
## Android apps
### With QPython
Download the repo on your phone, then just [download the QPython app](https://play.google.com/store/apps/details?id=org.qpython.qpy3), go to editor, press on the folder icon on the top-right, navigate to the folder where you saved the repo and click on main.py. Then tap on the triangle at the bottom
### With other apps
Other apps are probably compatible, but I haven't tried
## Windows
### Compiled .exe file
You can find a "main.exe" file under dist/main. There is a zip file of that folder in the [releases](https://github.com/IlmastroStefanuzzo/py_cli_snake/releases/)
### Python interpreter
Clone the repo to your system with GitHub Desktop or downloading the zip file from here or whatever  
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
