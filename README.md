# DirectInputServer
 Send keystrokes from an iPad Playground to Windows DirectX Games. Requires https://github.com/freecodecampster/DirectInputClient a Swift Playground running on iPadOS 13+
 
 
 ![How it works](https://github.com/freecodecampster/DirectInputServer/blob/master/images/DI.jpeg)

http://www.youtube.com/watch?v=7ppZ2OEdLFg
[![Screencast of DirectInputClient and DirectInputServer working together](https://img.youtube.com/vi/7ppZ2OEdLFg/0.jpg)](http://www.youtube.com/watch?v=7ppZ2OEdLFg)

 Install Visual Studio Code and a Python 3 Environment.
 https://code.visualstudio.com
 https://www.python.org
 
 Visual Studio Code

Verfiy the Python installation

Windows: open a command prompt and run the following command:
`py -3 --version`

Start VS Code in a project (workspace) folder#
Using a command prompt or terminal, create an empty folder called "hello", navigate into it, and open VS Code (code) in that folder (.) by entering the following commands:
```
mkdir hello
cd hello
code .
```


Use the Command Palette `Ctrl-Shift-P` to run Terminal: Create New Integrated Terminal `Ctrl-Shift-`\`

A best practice among Python developers is to avoid installing packages into a global interpreter environment. You instead use a project-specific virtual environment that contains a copy of a global interpreter. Once you activate that environment, any packages you then install are isolated from other environments. Such isolation reduces many complications that can arise from conflicting package versions. To create a virtual environment and install the required packages, enter the following commands as appropriate for your operating system:

Create and activate the virtual environment

Note: When you create a new virtual environment, you should be prompted by VS Code to set it as the default for your workspace folder. If selected, the environment will automatically be activated when you open a new terminal.

`py -3 -m venv .venv`




Select your new environment by using the Python: Select Interpreter command from the Command Palette.



To close a terminal window type `exit`

Once you are finished, type `deactivate` in the terminal window to deactivate the virtual environment.

From <https://code.visualstudio.com/docs/python/python-tutorial> 

 Install the Python extension for Visual Studio Code.

 Run DirectInputServer.py

 On your Mac or Ipad open Swift Playgrounds and copy in the playground code from https://github.com/freecodecampster/DirectInputClient


https://guides.github.com/features/mastering-markdown/
