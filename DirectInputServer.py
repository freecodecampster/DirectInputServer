# Python 3.7
# https://docs.python.org/3/library/index.html
# Developed on Visual Studio 2019 Community Edition with Python Workload installed.
# https://docs.microsoft.com/en-gb/visualstudio/python/overview-of-python-tools-for-visual-studio?view=vs-2019
# Python Server examples used
# https://jeffreydavidsz.github.io/VICREO-Listener/
# https://github.com/sevren/DirectInput-Game-Controller-Python
# Use pyinstaller to create a Windows executable that runs as a console application
# http://www.pyinstaller.org/
# If installing pyinstaller in a virtual environment you can find the exe at DirectInputServer\env\Scripts\pyinstaller.exe

# TCP handling
import socket
import sys

# Keyboard handling
import time,ctypes

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]
    
class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# DirectX scancodes are input into the game as integers
# Direct X scancode definitions https://wiki.nexusmods.com/index.php/DirectX_Scancodes_And_How_To_Use_Them

scancodes = {
    "Escape":1,
    "Keyboard1":2,
    "Keyboard2":3,
    "Keyboard3":4,
    "Keyboard4":5,
    "Keyboard5":6,
    "Keyboard6":7,
    "Keyboard7":8,
    "Keyboard8":9,
    "Keyboard9":10,
    "Keyboard0":11,
    "Minus":12,
    "Equals":13,
    "Backspace":14,
    "Tab":15,
    "Q":16,
    "W":17,
    "E":18,
    "R":19,
    "T":20,
    "Y":21,
    "U":22,
    "I":23,
    "O":24,
    "P":25,
    "LeftBracket":26,
    "RightBracket":27,
    "Enter":28,
    "LeftControl":29,
    "A":30,
    "S":31,
    "D":32,
    "F":33,
    "G":34,
    "H":35,
    "J":36,
    "K":37,
    "L":38,
    "Semicolon":39,
    "Apostrophe":40,
    "Tilde":41,
    "LeftShift":42,
    "BackSlash":43,
    "Z":44,
    "X":45,
    "C":46,
    "V":47,
    "B":48,
    "N":49,
    "M":50,
    "Comma":51,
    "Period":52,
    "ForwardSlash":53,
    "RightShift":54,
    "NumpadMultiply":55,
    "LeftAlt":56,
    "Spacebar":57,
    "CapsLock":58,
    "F1":59,
    "F2":60,
    "F3":61,
    "F4":62,
    "F5":63,
    "F6":64,
    "F7":65,
    "F8":66,
    "F9":67,
    "F10":68,
    "NumLock":69,
    "ScrollLock":70,
    "Numpad7":71,
    "Numpad8":72,
    "Numpad9":73,
    "NumpadMinus":74,
    "Numpad4":75,
    "Numpad5":76,
    "Numpad6":77,
    "NumpadPlus":78,
    "Numpad1":79,
    "Numpad2":80,
    "Numpad3":81,
    "Numpad0":82,
    "NumpadPeriod":83,
    "F11":87,
    "F12":88,
    "NumpadEnter":156,
    "RightControl":157,
    "NumpadDivide":181,
    "RightAlt":184,
    "Home":199,
    "UpArrow":200,
    "PageUp":201,
    "LeftArrow":203,
    "RightArrow":205,
    "End":207,
    "DownArrow":208,
    "PageDown":209,
    "Insert":210,
    "Delete":211,
    "LeftMouseButton":256,
    "RightMouseButton":257,
    "MiddleMouseWheel":258,
    "MouseButton3":259,
    "MouseButton4":260,
    "MouseButton5":261,
    "MouseButton6":262,
    "MouseButton7":263,
    "MouseWheelUp":264,
    "MouseWheelDown":265
}

# Functions for pressing and releasing the keys
# time.sleep(0.1) necessary otherwise key presses happen too fast to register
def pressKey(scancode):
    time.sleep(0.1)
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, scancode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def releaseKey(scancode):
    time.sleep(0.1)
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, scancode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def start_server():
    # Control server loop
    _LOOP = True
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    ipAddress = socket.gethostbyname(socket.getfqdn())
    port = 10001
    server_address = (ipAddress, port)
    print("Starting up on ip address %s port %s" % server_address)
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)

    print ("Now run the Directx game and make sure the game is in the foreground")

    # Test sending p to game
    #time.sleep(5)
    #print("Pressing P")
    #pressAndRelease(25)
    
    # Wait for a connection
    while _LOOP:
        print("Waiting for a connection")
        # sock.accept() returns socket object and address info
        connection, client_address = sock.accept()

        # Receive the data and retransmit it
        try:
            print("Connection from", client_address)
            while _LOOP:
                data = connection.recv(160)
                if data:
                    tcpString = data.decode()
                    print("Receiving: ", tcpString)
                    # Sent string commands should be seperated by single space delimiters
                    # "command1 command2 command3"
                    list = tcpString.split()
                    # How many commands were sent?
                    numberOfScancodes = len(list)

                    # Single key command
                    if numberOfScancodes == 1:
                        # Stop the application
                        if tcpString[0:6] == "<STOP>":
                            print("You have stopped the application")
                            _LOOP = False
                        else:
                            print("1 command: " + list[0])
                            # Find first command
                            # Check for empty string
                            if len(list[0]) > 0:
                                command1 = scancodes.get(list[0], "error")
                            if command1 != "error":
                                pressKey(command1)
                                releaseKey(command1)
                            else:
                                print("Wrong key")

                    # Combination of two commands
                    elif numberOfScancodes == 2:
                        print("2 commands: " + list[0] + " " + list[1])
                        # Find first command
                        if len(list[0]) > 0:
                            command1 = scancodes.get(list[0], "error")
                        # Find second command
                        if len(list[0]) > 0:
                            command2 = scancodes.get(list[1], "error")
                        #if no error send the keycombo
                        if command1 != "error" and command2 != "error":
                            pressKey(command1)
                            pressKey(command2)
                            releaseKey(command2)
                            releaseKey(command1)
                        else:
                            print('wrong key')

                    # Combination of three commands
                    elif numberOfScancodes == 3:
                        print("3 commands: " + list[0] + " " + list[1] + " " + list[2])
                        # Find first command
                        if len(list[0]) > 0:
                            command1 = scancodes.get(list[0], "error")
                        # Find second command
                        if len(list[0]) > 0:
                            command2 = scancodes.get(list[1], "error")
                        # Find third command
                        if len(list[0]) > 0:
                            command3 = scancodes.get(list[2], "error")
                        #if no error send the keycombo
                        if command1 != "error" and command2 != "error" and command3 != "error":
                            pressKey(command1)
                            pressKey(command2)
                            pressKey(command3)
                            releaseKey(command3)
                            releaseKey(command2)
                            releaseKey(command1)
                        else:
                            print('wrong key')

                    # Something wrong with the sent string
                    else:
                        print("Cannot process the string message sent")
                    

                else:
                    print("No more data from", client_address)
                    break
        
        # Clean up the connection    
        finally:
            print("Finalize this transmission")
            connection.close()

# Environment Module
if __name__=="__main__":
    start_server()