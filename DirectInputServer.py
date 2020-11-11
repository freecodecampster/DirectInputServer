# DirectInputServer
# 11 Nov 2020
# Freecodecampster
# https://github.com/freecodecampster/DirectInputServer

# Developed on Visual Studio Code with Python 3
# https://channel9.msdn.com/Series/Intro-to-Python-Development
# https://code.visualstudio.com/docs/python/python-tutorial
# https://docs.microsoft.com/en-gb/visualstudio/python/overview-of-python-tools-for-visual-studio?view=vs-2019
# https://www.youtube.com/watch?v=jFCNu1-Xdsw

# List of Virtual-Key Codes
# https://docs.microsoft.com/en-gb/windows/win32/inputdev/virtual-key-codes

################################################################################
# Thanks to Aniruddha Tapas
# https://gist.github.com/Aniruddha-Tapas/1627257344780e5429b10bc92eb2f52a

# Keyboard handling
import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# List of all codes for keys:
# # msdn.microsoft.com/en-us/library/dd375731
scancodes = {
    "VK_LBUTTON":0x01, # Left mouse button
    "VK_RBUTTON":0x02, # Right mouse button
    "VK_CANCEL":0x03, # Control-break processing
    "VK_MBUTTON":0x04, # Middle mouse button (three-button mouse)
    "VK_XBUTTON1":0x05, # X1 mouse button
    "VK_XBUTTON2":0x06, # X2 mouse button
    "VK_BACK":0x08, # BACKSPACE key
    "VK_TAB":0x09, # TAB key
    "VK_CLEAR":0x0C, # CLEAR key
    "VK_RETURN":0x0D, # ENTER key
    "VK_SHIFT":0x10, # SHIFT key
    "VK_CONTROL":0x11, # CTRL key
    "VK_MENU":0x12, # ALT key
    "VK_PAUSE":0x13, # PAUSE key
    "VK_CAPITAL":0x14, # CAPS LOCK key
    "VK_KANA":0x15, # IME Kana mode
    "VK_HANGUEL":0x15, # IME Hanguel mode (maintained for compatibility; use VK_HANGUL)
    "VK_HANGUL":0x15, # IME Hangul mode
    "VK_IME_ON":0x16, # IME On
    "VK_JUNJA":0x17, # IME Junja mode
    "VK_FINAL":0x18, # IME final mode
    "VK_HANJA":0x19, # IME Hanja mode
    "VK_KANJI":0x19, # IME Kanji mode
    "VK_IME_OFF":0x1A, # IME Off
    "VK_ESCAPE":0x1B, # ESC key
    "VK_CONVERT":0x1C, # IME convert
    "VK_NONCONVERT":0x1D, # IME nonconvert
    "VK_ACCEPT":0x1E, # IME accept
    "VK_MODECHANGE":0x1F, # IME mode change request
    "VK_SPACE":0x20, # SPACEBAR
    "VK_PRIOR":0x21, # PAGE UP key
    "VK_NEXT":0x22, # PAGE DOWN key
    "VK_END":0x23, # END key
    "VK_HOME":0x24, # HOME key
    "VK_LEFT":0x25, # LEFT ARROW key
    "VK_UP":0x26, # UP ARROW key
    "VK_RIGHT":0x27, # RIGHT ARROW key
    "VK_DOWN":0x28, # DOWN ARROW key
    "VK_SELECT":0x29, # SELECT key
    "VK_PRINT":0x2A, # PRINT key
    "VK_EXECUTE":0x2B, # EXECUTE key
    "VK_SNAPSHOT":0x2C, # PRINT SCREEN key
    "VK_INSERT":0x2D, # INS key
    "VK_DELETE":0x2E, # DEL key
    "VK_HELP":0x2F, # HELP key
    "VK_0":0x30, # 0 key
    "VK_1":0x31, # 1 key
    "VK_2":0x32, # 2 key
    "VK_3":0x33, # 3 key
    "VK_4":0x34, # 4 key
    "VK_5":0x35, # 5 key
    "VK_6":0x36, # 6 key
    "VK_7":0x37, # 7 key
    "VK_8":0x38, # 8 key
    "VK_9":0x39, # 9 key
    "VK_A":0x41, # A key
    "VK_B":0x42, # B key
    "VK_C":0x43, # C key
    "VK_D":0x44, # D key
    "VK_E":0x45, # E key
    "VK_F":0x46, # F key
    "VK_G":0x47, # G key
    "VK_H":0x48, # H key
    "VK_I":0x49, # I key
    "VK_J":0x4A, # J key
    "VK_K":0x4B, # K key
    "VK_L":0x4C, # L key
    "VK_M":0x4D, # M key
    "VK_N":0x4E, # N key
    "VK_O":0x4F, # O key
    "VK_P":0x50, # P key
    "VK_Q":0x51, # Q key
    "VK_R":0x52, # R key
    "VK_S":0x53, # S key
    "VK_T":0x54, # T key
    "VK_U":0x55, # U key
    "VK_V":0x56, # V key
    "VK_W":0x57, # W key
    "VK_X":0x58, # X key
    "VK_Y":0x59, # Y key
    "VK_Z":0x5A, # Z key
    "VK_LWIN":0x5B, # Left Windows key (Natural keyboard)
    "VK_RWIN":0x5C, # Right Windows key (Natural keyboard)
    "VK_APPS":0x5D, # Applications key (Natural keyboard)
    "VK_SLEEP":0x5F, # Computer Sleep key
    "VK_NUMPAD0":0x60, # Numeric keypad 0 key
    "VK_NUMPAD1":0x61, # Numeric keypad 1 key
    "VK_NUMPAD2":0x62, # Numeric keypad 2 key
    "VK_NUMPAD3":0x63, # Numeric keypad 3 key
    "VK_NUMPAD4":0x64, # Numeric keypad 4 key
    "VK_NUMPAD5":0x65, # Numeric keypad 5 key
    "VK_NUMPAD6":0x66, # Numeric keypad 6 key
    "VK_NUMPAD7":0x67, # Numeric keypad 7 key
    "VK_NUMPAD8":0x68, # Numeric keypad 8 key
    "VK_NUMPAD9":0x69, # Numeric keypad 9 key
    "VK_MULTIPLY":0x6A, # Multiply key
    "VK_ADD":0x6B, # Add key
    "VK_SEPARATOR":0x6C, # Separator key
    "VK_SUBTRACT":0x6D, # Subtract key
    "VK_DECIMAL":0x6E, # Decimal key
    "VK_DIVIDE":0x6F, # Divide key
    "VK_F1":0x70, # F1 key
    "VK_F2":0x71, # F2 key
    "VK_F3":0x72, # F3 key
    "VK_F4":0x73, # F4 key
    "VK_F5":0x74, # F5 key
    "VK_F6":0x75, # F6 key
    "VK_F7":0x76, # F7 key
    "VK_F8":0x77, # F8 key
    "VK_F9":0x78, # F9 key
    "VK_F10":0x79, # F10 key
    "VK_F11":0x7A, # F11 key
    "VK_F12":0x7B, # F12 key
    "VK_F13":0x7C, # F13 key
    "VK_F14":0x7D, # F14 key
    "VK_F15":0x7E, # F15 key
    "VK_F16":0x7F, # F16 key
    "VK_F17":0x80, # F17 key
    "VK_F18":0x81, # F18 key
    "VK_F19":0x82, # F19 key
    "VK_F20":0x83, # F20 key
    "VK_F21":0x84, # F21 key
    "VK_F22":0x85, # F22 key
    "VK_F23":0x86, # F23 key
    "VK_F24":0x87, # F24 key
    "VK_NUMLOCK":0x90, # NUM LOCK key
    "VK_SCROLL":0x91, # SCROLL LOCK key
    "VK_LSHIFT":0xA0, # Left SHIFT key
    "VK_RSHIFT":0xA1, # Right SHIFT key
    "VK_LCONTROL":0xA2, # Left CONTROL key
    "VK_RCONTROL":0xA3, # Right CONTROL key
    "VK_LMENU":0xA4, # Left MENU key
    "VK_RMENU":0xA5, # Right MENU key
    "VK_BROWSER_BACK":0xA6, # Browser Back key
    "VK_BROWSER_FORWARD":0xA7, # Browser Forward key
    "VK_BROWSER_REFRESH":0xA8, # Browser Refresh key
    "VK_BROWSER_STOP":0xA9, # Browser Stop key
    "VK_BROWSER_SEARCH":0xAA, # Browser Search key
    "VK_BROWSER_FAVORITES":0xAB, # Browser Favorites key
    "VK_BROWSER_HOME":0xAC, # Browser Start and Home key
    "VK_VOLUME_MUTE":0xAD, # Volume Mute key
    "VK_VOLUME_DOWN":0xAE, # Volume Down key
    "VK_VOLUME_UP":0xAF, # Volume Up key
    "VK_MEDIA_NEXT_TRACK":0xB0, # Next Track key
    "VK_MEDIA_PREV_TRACK":0xB1, # Previous Track key
    "VK_MEDIA_STOP":0xB2, # Stop Media key
    "VK_MEDIA_PLAY_PAUSE":0xB3, # Play/Pause Media key
    "VK_LAUNCH_MAIL":0xB4, # Start Mail key
    "VK_LAUNCH_MEDIA_SELECT":0xB5, # Select Media key
    "VK_LAUNCH_APP1":0xB6, # Start Application 1 key
    "VK_LAUNCH_APP2":0xB7, # Start Application 2 key
    "VK_OEM_1":0xBA, # Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the ';:' key
    "VK_OEM_PLUS":0xBB, # For any country/region, the '+' key
    "VK_OEM_COMMA":0xBC, # For any country/region, the ',' key
    "VK_OEM_MINUS":0xBD, # For any country/region, the '-' key
    "VK_OEM_PERIOD":0xBE, # For any country/region, the '.' key
    "VK_OEM_2":0xBF, # Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '/?' key
    "VK_OEM_3":0xC0, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '`~' key
    "VK_OEM_4":0xDB, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '[{' key
    "VK_OEM_5":0xDC, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '\|' key
    "VK_OEM_6":0xDD, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the ']}' key
    "VK_OEM_7":0xDE, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the 'single-quote/double-quote' key
    "VK_OEM_8":0xDF, # Used for miscellaneous characters; it can vary by keyboard.
    "VK_OEM_102":0xE2, # Either the angle bracket key or the backslash key on the RT 102-key keyboard
    "VK_PROCESSKEY":0xE5, # IME PROCESS key
    "VK_PACKET":0xE7, # Used to pass Unicode characters as if they were keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP
    "VK_ATTN":0xF6, # Attn key
    "VK_CRSEL":0xF7, # CrSel key
    "VK_EXSEL":0xF8, # ExSel key
    "VK_EREOF":0xF9, # Erase EOF key
    "VK_PLAY":0xFA, # Play key
    "VK_ZOOM":0xFB, # Zoom key
    "VK_NONAME":0xFC, # Reserved
    "VK_PA1":0xFD, # PA1 key
    "VK_OEM_CLEAR":0xFE, # Clear key
}

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def pressKey(hexKeyCode):
    time.sleep(0.1)
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def releaseKey(hexKeyCode):
    time.sleep(0.1)
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


################################################################################
# Python Server examples used
# https://jeffreydavidsz.github.io/VICREO-Listener/
# https://github.com/sevren/DirectInput-Game-Controller-Python

# TCP handling
import socket
import sys

def start_server():
    # Control server loop
    _LOOP = True
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Provide the ipAddress of the host - ipconfig in command prompt Windows
    #ipAddress = "192.168.0.7"
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