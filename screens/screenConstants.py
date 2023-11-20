from poplib import CR


WELCOME_SCREEN = "welcome"
START_SCREEN = "start"
CREATE_AVATAR_SCREEN = "createAvatar"
GAME_SCREEN = "game"
PAUSE_SCREEN = "pause"
LOAD_SCREEN = "load"
ORACLE_QUESTION_SCREEN = "oracleQuestion"
ORACLE_ANSWER_SCREEN = "oracleAnswer"

def nextScreen(currentScreen: str) -> str:
    ''' nextScreen: str -> str
    Returns the next screen given the current screen.
    '''
    return {
        WELCOME_SCREEN: START_SCREEN,
        START_SCREEN: CREATE_AVATAR_SCREEN,
        CREATE_AVATAR_SCREEN: GAME_SCREEN,
        GAME_SCREEN: PAUSE_SCREEN,
        PAUSE_SCREEN: GAME_SCREEN,
        LOAD_SCREEN: GAME_SCREEN,
        ORACLE_QUESTION_SCREEN: ORACLE_ANSWER_SCREEN,
        ORACLE_ANSWER_SCREEN: GAME_SCREEN,
    }[currentScreen]

def previousScreen(currentScreen: str) -> str:
    ''' previousScreen: str -> str
    Returns the previous screen given the current screen.
    '''
    return {
        WELCOME_SCREEN: WELCOME_SCREEN,
        START_SCREEN: WELCOME_SCREEN,
        CREATE_AVATAR_SCREEN: START_SCREEN,
        PAUSE_SCREEN: GAME_SCREEN,
        LOAD_SCREEN: START_SCREEN,
        GAME_SCREEN: START_SCREEN,
        ORACLE_QUESTION_SCREEN: GAME_SCREEN,
        ORACLE_ANSWER_SCREEN: ORACLE_QUESTION_SCREEN,
    }[currentScreen]