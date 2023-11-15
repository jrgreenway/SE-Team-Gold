import json
import os
from datetime import datetime

from requests import get

from game import Game
from utils.gameLoader import get_saved_games

def save_game(game_instance: Game):
    ''' save_game: Game -> None
    Saves the game instance to a file
    '''
    
    # Create a directory to store saved games if it doesn't exist
    if not os.path.exists('saved_games'):
        os.makedirs('saved_games')

    # Serialize the game instance to JSON
    game_json = json.dumps(game_instance.toJson())

    # Save the game to a file with the current date as the filename
    date_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"saved_games/game_{date_string}.json"
    with open(filename, 'w') as f:
        f.write(game_json)

    game_instance.setSavedGames(get_saved_games())
