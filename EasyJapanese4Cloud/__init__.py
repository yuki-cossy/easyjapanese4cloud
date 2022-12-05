__version__ = '0.0.1'
__author__       = 'Yuki Cossy'
__author_email__ = 'domokomod5@gmail.com'
__url__          = 'http://github.com/account/repository'



import os
from pathlib import Path

from changepath import change
from easyjapanese import EasyJapanese


def runthrough():
    change_objs = [Path(os.getcwd()+'/chromedriver'), Path(os.getcwd()+'/headless-chromium')]
    for obj in change_objs:
        change.add_execute_permission(obj, target='a')

    change.settingDriver()

    EasyJapanese()

