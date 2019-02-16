import webbrowser, sys, pyperclip, pyautogui, time

if len(sys.argv) > 1:
    # Get address from command line.
    # sys arguments will come in an array with each token/word separately
    text = ' '.join(sys.argv[1:])
    pyperclip.copy(text)
else:
    # Get text from clipboard.
    text = pyperclip.paste()

koUrl = 'https://translate.google.com/#view=home&op=translate&sl=auto&tl=ko'
print(koUrl)
webbrowser.open(koUrl)

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

time.sleep(3)

pyautogui.hotkey('command', 'v')
