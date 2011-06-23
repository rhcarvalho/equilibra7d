#!/usr/bin/env ppython
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import ClockObject, WindowProperties
from panda3d.core import NodePath

from objects import Character, Enemy, Landscape, Scenario, Sea
from managers import (AIManager, CollisionManager, HUDManager, KeyboardManager,
                      LightManager, PhysicsManager)
from gamestate import GameState


class World(ShowBase):
    """Class that holds the Panda3D Scene Graph."""
    
    def __init__(self):
        ShowBase.__init__(self)
        
        # Create parent for all objects
        self.objectsNode = NodePath("objects")
        self.objectsNode.reparentTo(self.render)
        
        self.configWorld()
        self.createManagers()
        
        # Set up state engine
        self.gameState = GameState()
        
        # Start new game
        self.reset()
    
    def createObjects(self):
        """Instantiate objects.
        
        Can be run multiple times to recreate all objects."""
        self.objectsNode.removeChildren()
        self.scenario = Scenario(self.objectsNode, "arena2")
        self.character = Character(self.objectsNode, "character")
        self.enemy = Enemy(self.objectsNode, "enemy")
        self.landscape = Landscape(self.objectsNode, "landscape")
        self.sea = Sea(self.objectsNode, "sea")
    
    def createManagers(self):
        """Instantiate managers.
        
        Probably run only once."""
        self.keyboardManager = KeyboardManager()
        self.physicsManager = PhysicsManager()
        self.collisionManager = CollisionManager()
        self.lightManager = LightManager()
        self.hudManager = HUDManager()
        self.aiManager = AIManager()
    
    def configWorld(self):
        """Set general settings.
        
        Probably run only once."""
        # Set window title
        props = WindowProperties()
        props.setTitle("Equilibra7D")
        self.win.requestProperties(props)
        
        # Set up the camera
        self.camera.setY(-40)
        self.camera.setZ(15)
        self.camera.lookAt(0, 0, 0)
        self.disableMouse()
        
        # Enable per-pixel lighting
        self.render.setShaderAuto()
        
        # Enable FPS meter
        self.setFrameRateMeter(True)
        
        # Fix frame rate
        FPS = 60
        globalClock = ClockObject.getGlobalClock()
        globalClock.setMode(ClockObject.MLimited)
        globalClock.setFrameRate(FPS)
    
    def reset(self):
        self.gameState.reset()


if __name__ == "__main__":
    world = World()
    world.run()

