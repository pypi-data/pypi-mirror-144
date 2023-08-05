# PyInput

Python library to send inputs to an executable, useful for scenarios such as having a neural network send decisions to a game. Essentially a wrapper around the win32api. Please leave an issue for a feature request. Made with games in mind, but might work with other applications.

## Installation
You can install via pip

    pip install pyinput


## Usage
Simply pass in the window name to get the handle, then you can use press_key to send inputs for a specific timeframe and whether or not to force the window to come into the foreground.

    import  pyinputkeycodes
    import  pyinput
    
	window_name  =  "Game Window Name Here"
    hwnd  =  pyinput.get_handle(window_name) # Gets the handle
    pyinput.press_key(hwnd, pyinputkeycodes.VK_RETURN) # Sends Return key (default for 0.1 seconds)
    pyinput.press_key(hwnd, pyinputkeycodes.VK_KEY_W, 2) # Sends W key for 2 seconds
    pyinput.press_key(hwnd, pyinputkeycodes.VK_KEY_W, 2, false) # Sends W key for 2 seconds, but doesnt force foreground

## Keycodes
A list of keycodes can be found here http://www.kbdedit.com/manual/low_level_vk_list.html
If the keycode you need is not supported, you may pass it in instead.

    pyinput.press_key(hwnd, 0x33)
