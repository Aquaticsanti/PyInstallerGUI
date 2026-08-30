import PyInstaller.__main__
import sys

PyInstaller.__main__.run([sys.argv[1:]])

"""
All this file (and executable) does is wrap PyInstaller.
sys.argv[1:] takes all the arguments except this script.
This file is for the users who either don't have python or don't have pyinstaller.
"""