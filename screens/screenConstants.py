WELCOME_SCREEN = "welcome"
START_SCREEN = "start"
GAME_SCREEN = "game"
PAUSE_SCREEN = "pause"
LOAD_SCREEN = "load"

def nextScreen(currentScreen: str) -> str:
    ''' nextScreen: str -> str
    Returns the next screen given the current screen.
    '''
    return {
        WELCOME_SCREEN: START_SCREEN,
        START_SCREEN: GAME_SCREEN,
        GAME_SCREEN: PAUSE_SCREEN,
        PAUSE_SCREEN: GAME_SCREEN,
        LOAD_SCREEN: GAME_SCREEN
    }[currentScreen]