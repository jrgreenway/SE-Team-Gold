'''
All button callbacks return the state of the running variable from the Game class
after their action has been performed. Also, they should return the next screen of
the game.
'''
from ast import Tuple
from screens.screenConstants import LOAD_SCREEN, START_SCREEN


def startButtonCB() -> tuple[bool, str]:
    return True, START_SCREEN

def loadButtonCB() -> tuple[bool, str]:
    return True, LOAD_SCREEN

def exitButtonCB() -> tuple[bool, str]:
    return False, ''