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

