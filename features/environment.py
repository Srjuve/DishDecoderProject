from splinter.browser import Browser
from selenium import webdriver

def before_all(context):
    context.browser = Browser('chrome', headless=True)
    

def after_all(context):
    context.browser.quit()
    context.browser = None