import webbrowser, sys, pyperclip, pyautogui, time

if len(sys.argv) > 1:
    # Get address from command line.
    # sys arguments will come in an array with each token/word separately
    s = '%20' #for spacing between words
    text = s.join(sys.argv[1:])
else:
    # Get text from clipboard.
    text = pyperclip.paste()

webbrowser.open('https://translate.google.com/#view=home&op=translate&sl=auto&tl=ko&text=')

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

time.sleep(1)

pyautogui.hotkey('command', 'v')
