import json
import math
import pickle
from typing import Any
import pygame

from gameObject import GameObject
from scene import Scene

directionCoordMap = {
    'E': (128, 0),
    'S': (0, 128),
    'W': (-128, 0),
    'N': (0, -128)
}

def load_attribute(attribute: str, object: dict, default=None) -> Any:
    ''' loadAttribute: str, dict, Any -> Any
    Loads the given attribute from the given object and returns it. If the attribute is not found, returns the default value
    '''
    try:
        return object[attribute]
    except KeyError:
        return default

def scene_loader_data(sceneData: dict) -> Scene:
    ''' sceneLoaderData: dict -> Scene
    Loads the scene with the given data and returns it
    '''
    objects = sceneData['objects']
    gameObjects = []

    for object in objects:

        try:
            gameSprite = pygame.transform.scale(pygame.image.load(object['texture']), (128, 128))
        except pygame.error:
            # it means it was saved as pickle
            with open(object['texture'], "rb") as f:
                surf_array = pickle.load(f)
            gameSprite = pygame.surfarray.make_surface(surf_array)
            gameSprite = pygame.transform.scale(gameSprite, (128, 128))
        
        isInteractive = load_attribute('interactive', object, False)
        happiness_effect = load_attribute('happiness-effect', object, 0)
        time_effect = load_attribute('time-effect', object, 0)
        health_effect = load_attribute('health-effect', object, 0)
        isCollidable = load_attribute('collidable', object, True)
        navigateTo = load_attribute('navigateTo', object, None)
        nextDay = load_attribute('next-day', object, False)

        gameObject = GameObject(object['id'],
            happiness_effect=happiness_effect,
            time_effect=time_effect,
            health_effect=health_effect,
            interactive=isInteractive,
            sprite=gameSprite,
            isCollidable=isCollidable,
            navigateTo=navigateTo,
            next_day=nextDay
        )
        try:
            pos = object['position-absolute']
            gameObject.setPosition(pygame.Vector2(pos['x'], pos['y']))
        except KeyError:
            pos = object['position-relative']
            relativeTo = [obj for obj in gameObjects if obj.getID() == pos['relativeTo']][0]
            direction = pos['direction']
            offset = directionCoordMap[direction]
            gameObject.setPosition(relativeTo.getPosition() + pygame.Vector2(offset[0], offset[1]))
        
        gameObjects.append(gameObject)
    
    try:
        texture = pygame.transform.scale(pygame.image.load(sceneData['texture']),  (128, 128))
    except pygame.error:
        # it means it was saved as pickle
        with open(sceneData['texture'], "rb") as f:
            surf_array = pickle.load(f)
        texture = pygame.surfarray.make_surface(surf_array)
        texture = pygame.transform.scale(texture, (128, 128))

    texture_width, texture_height = texture.get_size()
    scene_width, scene_height = (1280, 720)
    num_repeats_x = math.ceil(scene_width / texture_width)
    num_repeats_y = math.ceil(scene_height / texture_height)
    new_texture = pygame.Surface((num_repeats_x * texture_width, num_repeats_y * texture_height))
    for i in range(num_repeats_x):
        for j in range(num_repeats_y):
            new_texture.blit(texture, (i * texture_width, j * texture_height))
    
    return Scene(sceneData['id'], sceneData['name'], new_texture, gameObjects)

def scene_loader(sceneNumber: int) -> Scene:
    ''' sceneLoader: int -> Scene
    Loads the scene with the given number from the scenes.json file and returns it
    '''
    with open('scenes/scenes.json') as f:
        scenes = json.load(f)
        
    scene = [scene for scene in scenes if scene['id'] == sceneNumber][0]
    return scene_loader_data(scene)

def scene_drawer(screen: pygame.Surface, scene: Scene) -> None:
    ''' sceneDrawer: pygame.Surface, Scene -> None
    Draws the given scene to the screen
    '''
    screen.blit(scene.getBackground(), (0, 0))
    for obj in scene.getObjects():
        screen.blit(obj.getSprite(), obj.getPosition())

    
            
