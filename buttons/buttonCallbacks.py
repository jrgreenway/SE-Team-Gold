'''
All button callbacks return the state of the running variable from the Game class
after their action has been performed. Also, they should return the next screen of
the game.
'''
from typing import Callable
from game import Game
from oracle import Oracle
from player import Player
from scenes.sceneDrawer import scene_loader, scene_loader_data
from screens.screenConstants import *
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
    return True, INTRODUCTION_SCREEN

def saveButtonCB(**kwargs) -> tuple[bool, str]:
    save_game(kwargs['game'])
    return True, GAME_SCREEN

def backToMainMenuButtonCB(**_) -> tuple[bool, str]:
    return True, START_SCREEN

def clickOracleCB(**_) -> tuple[bool, str]:
    return True, ORACLE_QUESTION_SCREEN

def clickOracleQuestionCB(**kwargs) -> tuple[bool, str]:
    kwargs['oracle'].setQuestion(kwargs['question'])
    return True, ORACLE_ANSWER_SCREEN

def clickMapLocation(**kwargs) -> tuple[bool, str]:
    game: Game = kwargs['game']
    sceneIndex: int = kwargs['sceneIndex']
    print(sceneIndex)
    game.setCurrentScene(scene_loader(sceneIndex))
    return True, GAME_SCREEN

def nextButtonCB(**kwargs) -> tuple[bool, str]:
    currentScreen = kwargs['currentScreen']
    return True, nextScreen(currentScreen)

def oracleCancelIncomingCall(**kwargs) -> tuple[bool, str]:
    kwargs['oracle'].cancelIncomingCall()
    return True, GAME_SCREEN

def toTitleCB(**_) -> tuple[bool, str]:
    return True, START_SCREEN

def nextDayCB(**kwargs) -> tuple[bool, str]:
    player: Player = kwargs['player']
    oracle: Oracle = kwargs['oracle']
    game: Game = kwargs['game']
    game.nextDay()
    player.resetNextDay()
    oracle.resetNextDay()
    save_game(game)
    return True, GAME_SCREEN

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
        'backToMainMenu': backToMainMenuButtonCB,
        'clickOracle': clickOracleCB,
        'clickOracleQuestion': clickOracleQuestionCB,
        'closeOracle': oracleCancelIncomingCall,
        'next': nextButtonCB,
        'nextDay': nextDayCB,
        'toTitle': toTitleCB,
        'clickMapLocation': clickMapLocation
    }