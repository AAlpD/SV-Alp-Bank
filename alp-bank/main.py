import pyautogui as k
from time import sleep as s
import pyperclip
import webbrowser
import requests
from bs4 import BeautifulSoup


def get_html():
    url = 'https://sites.google.com/view/alpbanksv/html-kodu'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='h.4ddea1f7b9e74f0e_23').get_text()
    return title


webbrowser.open(url='https://stardewvalleywiki.com/Stardew_Valley_Wiki')
s(1)
k.press('f12')
s(2)
k.press('f2')
s(0.1)
k.press('esc')
for i in range(2):
    s(0.1)
    k.press('up')
s(0.1)
k.press('f2')
s(0.1)
k.hotkey('ctrl', 'a')
s(0.1)
pyperclip.copy(get_html())
s(0.1)
k.hotkey('ctrl', 'v')
s(0.1)
k.press('f2')
s(0.1)
k.press('f12')
