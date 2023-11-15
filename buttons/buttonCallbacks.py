'''
All button callbacks return the state of the running variable from the Game class
after their action has been performed. Also, they should return the next screen of
the game.
'''
from ast import Tuple
from json import load
from typing import Callable
from urllib.request import CacheFTPHandler
from screens.screenConstants import CREATE_AVATAR_SCREEN, GAME_SCREEN, LOAD_SCREEN, PAUSE_SCREEN, START_SCREEN, previousScreen
from utils.gameLoader import load_game
from utils.gameSaver import save_game


def startButtonCB(**_) -> tuple[bool, str]:
    return True, CREATE_AVATAR_SCREEN

def loadButtonCB(**_) -> tuple[bool, str]:
    return True, LOAD_SCREEN

def loadGameButtonCB(**kwargs) -> tuple[bool, str]:
    load_game(kwargs['game'], kwargs['gameName'])
    return True, GAME_SCREEN

def exitButtonCB(**_) -> tuple[bool, str]:
    return False, START_SCREEN

def backButtonCB(**kwargs) -> tuple[bool, str]:
    currentScreen = kwargs['currentScreen']
    return True, previousScreen(currentScreen)

def startGameButtonCB(**kwargs) -> tuple[bool, str]:
    kwargs['player'].reset()
    return True, GAME_SCREEN

def saveButtonCB(**kwargs) -> tuple[bool, str]:
    save_game(kwargs['game'])
    return True, GAME_SCREEN

def backToMainMenuButtonCB(**_) -> tuple[bool, str]:
    return True, START_SCREEN

def createButtonCBDict() -> dict[str, Callable]:
    ''' createButtonCBDict: None -> dict[str, Callable]
    Creates a dictionary of button callbacks
    '''
    return {
        'start': startButtonCB,
        'load': loadButtonCB,
        'loadGame': loadGameButtonCB,
        'exit': exitButtonCB,
        'back': backButtonCB,
        'startGame': startGameButtonCB,
        'save': saveButtonCB,
        'backToMainMenu': backToMainMenuButtonCB
    }