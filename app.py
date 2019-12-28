#!/usr/bin/env python

##########################
# MAIN EXE FOR SCRAPEAPP
# AUTHOR: Alp Akpinar
# 
# This app is a result of Web Scraping/Tkinter 
# exercise in Python. This application scrapes
# the data in Wikipedia for the given artist and 
# extracts the discography, and presents it in a 
# user friendly format.
# 
# Execute this file to launch the start window/main page
# of the application. From this page, one can have access
# to the application page where artists can be searched to 
# get albums.
##########################

from lib.gui import StartWindow

def main():
    
    start_window = StartWindow()
    start_window.launch_start_window()

if __name__ == '__main__':
    main()
