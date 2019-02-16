#! python3
# toEnglish.py - Launches a google translate in the browser
# using text from command line or clipboard.

import webbrowser, sys, pyperclip, pyautogui, time #, requests, bs4

if len(sys.argv) > 1:
    # Get address from command line.
    # sys arguments will come in an array with each token/word separately
    s = '%20' #for spacing between words
    text = s.join(sys.argv[1:])
else:
    # Get text from clipboard.
    # example text to translate to english: 안녕하세요
    text = pyperclip.paste()

# testText = 'https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text=' + '안녕하세요'
# print(testText)
webbrowser.open('https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text=')

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

time.sleep(1)

pyautogui.hotkey('command', 'v')

# print(text)
# textList = list(text)
# textList.append('enter')
# print(textList)
# pyautogui.typewrite(textList)

#webbrowser.open('https://translate.google.com/%23view=home&op=translate&sl=auto&tl=en&text=what%20is%20the%20token')

# res = requests.get('https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text=' + text)
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
