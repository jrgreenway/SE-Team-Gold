import json
import math

import pygame

from gameObject import GameObject

directionCoordMap = {
    'E': (128, 0),
    'S': (0, 128),
    'W': (-128, 0),
    'N': (0, -128)
}

def scene_drawer(screen: pygame.Surface, sceneNumber: int) -> None:
    ''' sceneDrawer: pygame.Surface, int -> None
    Draws the scene with the given number to the screen
    '''
    with open('scenes/scenes.json') as f:
        scenes = json.load(f)
        
    scene = scenes[str(sceneNumber)]

    objects = scene['objects']
    gameObjects = []

    for object in objects:
        gameObject = GameObject(object['id'], sprite=pygame.transform.scale(pygame.image.load(object['texture']), (128, 128)))
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
    
    texture = pygame.image.load(scene['texture'])
    texture_width, texture_height = texture.get_size()
    scene_width, scene_height = screen.get_size()
    num_repeats_x = math.ceil(scene_width / texture_width)
    num_repeats_y = math.ceil(scene_height / texture_height)
    new_texture = pygame.Surface((num_repeats_x * texture_width, num_repeats_y * texture_height))
    for i in range(num_repeats_x):
        for j in range(num_repeats_y):
            new_texture.blit(texture, (i * texture_width, j * texture_height))
    screen.blit(new_texture, (0, 0))

    for gameObject in gameObjects:
        screen.blit(gameObject.getSprite(), gameObject.getPosition())

    
            
