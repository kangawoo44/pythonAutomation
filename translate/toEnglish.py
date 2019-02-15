#! python3
# toEnglish.py - Launches a google translate in the browser
# using text from command line or clipboard.

import webbrowser, sys, pyperclip, requests, bs4

if len(sys.argv) > 1:
    # Get address from command line.
    # sys arguments will come in an array with each token/word separately
    address = ' '.join(sys.argv[1:])
else:
    # Get text from clipboard.
    # example text to translate to english: 안녕하세요
    text = pyperclip.paste()

#webbrowser.open('https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text=' + text)
res = requests.get('https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text=' + text)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

soup = bs4.BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())
#spanElem = soup.select('body > div.frame > div.page.tlid-homepage.homepage.translate-text > div.homepage-content-wrap > div.tlid-source-target.main-header > div.source-target-row > div.tlid-results-container.results-container > div.tlid-result.result-dict-wrapper > div.result.tlid-copy-target > div.text-wrap.tlid-copy-target > div > span.tlid-translation.translation > span')
