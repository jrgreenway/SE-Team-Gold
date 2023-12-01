import os
import pickle
import pygame

from gameObject import GameObject


class Scene:
    '''
    Scene class - Has a background and contains a list of all objects in the scene
    
    Attributes:
    name: str
    background: pygame.image / bmp? - TODO need to research
    objects: list - list of all objects in the scene
    npcs?: list - list of all NPCs in the scene - TODO discuss whether this is necessary

    Methods:
    constructor: __init__(self, name, background, objects) - TODO decide
        on optional parameters
    getters and setters for all attributes
    '''

    def __init__(self,
                 id: int, 
                 name: str, 
                 background: pygame.Surface, 
                 objects: list[GameObject] = [], 
                 ) -> None:
        self.id = id
        self.name = name
        self.background = background
        self.loadObjects(objects)


    def getID(self) -> int:
        return self.id
    
    def getName(self) -> str:
        return self.name
    
    def getBackground(self) -> pygame.Surface:
        return self.background
    
    def getObjects(self) -> list[GameObject]:
        return self.interactable_objects + self.noninteractable_objects
    
    def getInteractableObjects(self) -> list[GameObject]:
        return self.interactable_objects
    
    def getNonInteractableObjects(self) -> list[GameObject]:
        return self.noninteractable_objects
    
    def loadObjects(self, objects) -> None:
        self.noninteractable_objects = []
        self.interactable_objects = []
        for object in objects:
            if object.getInteractive():
                self.interactable_objects.append(object)
            else:
                self.noninteractable_objects.append(object)


    def toJson(self) -> dict:
        
        # crop the rectangle from 0,0 to 128, 128 from baground
        cropped_background = self.background.subsurface(pygame.Rect(0, 0, 128, 128))
        texture = pygame.transform.scale(cropped_background, (32, 32))

        serialized_texture = pygame.surfarray.array3d(texture)

        dir = "assets/scenes/"

        bkg = pickle.dumps(serialized_texture)
        fileName = dir + f"{self.id}.pickle"

        if not os.path.exists(dir):
            os.makedirs(dir)
        
        with open(fileName, "wb") as f:
            f.write(bkg)

        return {
            'id': self.id,
            'name': self.name,
            'texture': fileName,
            'objects': [obj.toJson() for obj in self.getObjects()]
        }
