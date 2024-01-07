from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://www.tensor.trade/"
browser = webdriver.Firefox()

browser.get(URL)
assert 'tensor' in browser.title
