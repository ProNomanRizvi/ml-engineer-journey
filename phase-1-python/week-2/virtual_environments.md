# Virtual Environments
**Phase:** 1 — Python Complete Mastery
**Week:** 2

## 01 - What a virtual environment is and why it matters?
A virtual environment is like a separate workspace for your Python projects. It allows you to keep all the libraries and dependencies for a specific project isolated from other projects. This is important because different projects might require different versions of the same library, and using a virtual environment helps prevent conflicts between them. It also makes it easier to manage and share your projects without worrying about breaking other projects on your system.

## 02 - How to create one (python3 -m venv venv)?
To create a virtual environment, you can use the command `python3 -m venv venv`. Here's what it does:
- `python3` tells your system to use Python 3.
- `-m venv` is a flag that tells Python to run the `venv` module, which is responsible for creating virtual environments.
- `venv` is the name of the directory where the virtual environment will be created. You can choose any name you like, but "venv" is a common convention.

## 03 - How to activate and deactivate it (Kali Linux / Zsh)?

### Activate
To activate the virtual environment in Kali Linux using Zsh, you can use the following command:
```bash
source venv/bin/activate
```
This will change your command prompt to indicate that you are now working within the virtual environment. You can install packages and run your Python code without affecting your global Python installation.

### Deactivate
To deactivate the virtual environment and return to your global Python environment, use:
```bash
deactivate
```  

## 04 - How to install packages and save them (pip install, pip freeze > requirements.txt)?
To install packages in your virtual environment, you can use the `pip install` command followed by the name of the package you want to install. For example:
```bash
pip install numpy
```
This will install the NumPy library in your virtual environment.
To save the list of installed packages and their versions, you can use the `pip freeze` command and redirect the output to a file called `requirements.txt`:
```bash
pip freeze > requirements.txt
```
This will create a `requirements.txt` file that contains all the packages and their versions currently installed in your virtual environment. This file can be used later to recreate the same environment by running:
```bash
pip install -r requirements.txt
```
## 05 - How to recreate an environment from requirements.txt (pip install -r)?
To recreate an environment from a `requirements.txt` file, you can use the following command:
```bash
pip install -r requirements.txt
```
This command tells pip to read the `requirements.txt` file and install all the packages listed in it.