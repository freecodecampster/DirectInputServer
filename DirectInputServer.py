# DirectInputServer v2
# 14/07/2020
# Freecodecampster
# https://github.com/freecodecampster/DirectInputServer
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
# Keys are received as a space delimited string
# This string is split and items placed in an array
# Finally the scancodes dictionary is used to translate key strings to scancode
# scancode = scancodes.get(keyToPressAndRelease, "error")
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
    # Provide the ipAddress of the host - ipconfig in command prompt Windows
    ipAddress = "192.168.0.16"
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
    # Note a numeric code is sent
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
                    listOfKeysToPress = tcpString.split()
                    # How many commands were sent?
                    numberOfKeys = len(listOfKeysToPress)

                    # Single key command
                    if numberOfKeys == 1:
                        # Check first item is list isn't empty
                        if len(listOfKeysToPress[0]) > 0:
                            # Get string for equality tests
                            typeOfKey = listOfKeysToPress[0]
                            # Stop the application
                            if typeOfKey[0:6] == "<STOP>":
                                print("You have stopped the application")
                                _LOOP = False
                            # Press but don't release the key
                            elif typeOfKey[0:10] == "<TOGGLEON>":
                                keyToPress = typeOfKey[10:len(typeOfKey)]
                                print("Key to press: " + keyToPress)
                                # Convert key string to int from scancodes dictionary
                                scancode = scancodes.get(keyToPress, "error")
                                if scancode != "error":
                                    pressKey(scancode)
                            # Release a previously pressed key, state of button managed by Swift Playground
                            elif typeOfKey[0:11] == "<TOGGLEOFF>":
                                keyToRelease = typeOfKey[11:len(typeOfKey)]
                                print("Key to release: " + keyToRelease)
                                # Convert key string to int from scancodes dictionary
                                scancode = scancodes.get(keyToRelease, "error")
                                if scancode != "error":
                                    releaseKey(scancode)
                            # A normal key press and release action
                            else:
                                keyToPressAndRelease = typeOfKey
                                print("Press and release: " + keyToPressAndRelease)
                                # Convert key string to int from scancodes dictionary
                                scancode = scancodes.get(keyToPressAndRelease, "error")
                                if scancode != "error":
                                    pressKey(scancode)
                                    releaseKey(scancode)
                        else:
                            print("Wrong key")

                    # Combination of two key commands
                    elif numberOfKeys == 2:
                        print("2 keys: " + listOfKeysToPress[0] + " " + listOfKeysToPress[1])
                        # Find first key command
                        if len(listOfKeysToPress[0]) > 0:
                            firstScancode = scancodes.get(listOfKeysToPress[0], "error")
                        # Find second key command
                        if len(listOfKeysToPress[1]) > 0:
                            secondScancode = scancodes.get(listOfKeysToPress[1], "error")
                        #if no error send the keycombo
                        if firstScancode != "error" and secondScancode != "error":
                            pressKey(firstScancode)
                            pressKey(secondScancode)
                            releaseKey(secondScancode)
                            releaseKey(firstScancode)
                        else:
                            print('wrong key')

                    # Combination of three key commands
                    elif numberOfKeys == 3:
                        print("3 key commands: " + listOfKeysToPress[0] + " " + listOfKeysToPress[1] + " " + listOfKeysToPress[2])
                        # Find first key command
                        if len(listOfKeysToPress[0]) > 0:
                            firstScancode = scancodes.get(listOfKeysToPress[0], "error")
                        # Find second key command
                        if len(listOfKeysToPress[1]) > 0:
                            secondScancode = scancodes.get(listOfKeysToPress[1], "error")
                        # Find third key command
                        if len(listOfKeysToPress[2]) > 0:
                            thirdScancode = scancodes.get(listOfKeysToPress[2], "error")
                        #if no error send the keycombo
                        if firstScancode != "error" and secondScancode != "error" and thirdScancode != "error":
                            pressKey(firstScancode)
                            pressKey(secondScancode)
                            pressKey(thirdScancode)
                            releaseKey(thirdScancode)
                            releaseKey(secondScancode)
                            releaseKey(firstScancode)
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