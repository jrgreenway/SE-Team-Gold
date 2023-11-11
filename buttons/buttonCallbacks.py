'''
All button callbacks return the state of the running variable from the Game class
after their action has been performed. Also, they should return the next screen of
the game.
'''
from ast import Tuple
from screens.screenConstants import CREATE_AVATAR_SCREEN, GAME_SCREEN, LOAD_SCREEN, START_SCREEN, previousScreen


def startButtonCB(*_) -> tuple[bool, str]:
    return True, CREATE_AVATAR_SCREEN

def loadButtonCB(*_) -> tuple[bool, str]:
    return True, LOAD_SCREEN

def exitButtonCB(*_) -> tuple[bool, str]:
    return False, ''

def backButtonCB(**kwargs) -> tuple[bool, str]:
    currentScreen = kwargs['currentScreen']
    return True, previousScreen(currentScreen)

def startGameButtonCB(*_) -> tuple[bool, str]:
    return True, GAME_SCREEN