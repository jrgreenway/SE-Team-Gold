import json
import os
from turtle import st

from game import Game
from scenes.sceneDrawer import scene_loader_data


def get_saved_games() -> list[str]:
    ''' get_saved_games: None -> list[str]
    Returns a list of the names of the saved games
    '''
    saves_dir = "saved_games"
    return [f"{filename}"[:-5] for filename in os.listdir(saves_dir) if filename.endswith(".json")]

def load_game(currentInstace: Game, gameName: str) -> None:
    ''' load_game: Game, str -> None
    Loads the game with the given name and updates the current instance with the loaded data
    '''
    saves_dir = "saved_games"

    
    selected_file = f"{saves_dir}/{gameName}" + ".json"

    with open(selected_file) as f:
        game_data = json.load(f)
    
    scene = scene_loader_data(game_data['currentScene'])
    currentInstace.setCurrentScreen(game_data['currentScreen'])
    currentInstace.setCurrentScene(scene)