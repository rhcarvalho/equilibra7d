from direct.showbase.ShowBase import ShowBase

from scenario import Scenario
from character import Character
from enemy import Enemy
from inputmanager import InputManager
from physicsmanager import PhysicsManager
from collisionmanager import CollisionManager
from lightingmanager import LightingManager

class World(ShowBase):
    """Class that holds the Panda3D Scene Graph."""
    
    def __init__(self):
        ShowBase.__init__(self)
        
        # Placing the scenario in the world.
        self.scenario = Scenario(self.render, "arena1")
        
        # Placing the character in the world.
        self.character = Character(self.render, "ball")
        self.character.setZ(5)
        self.character.setScale(1.5)

        # Placing an enemy in the world.
        self.enemy = Enemy(self.render, "enemy")
        self.enemy.setPos(4, 4, 5)

        # Setting up the Input Manager
        self.inputManager = InputManager(self)
        self.inputManager.addKeyboardEventHandler(self.character)
        
        # Setting up the Physics Manager
        self.physicsManager = PhysicsManager(self)
        self.physicsManager.addLinearForce(0, 0, -1)
        self.physicsManager.addActor(self.character)
        self.physicsManager.addActor(self.enemy)

        # Setting up the Collision Manager        
        self.collisionManager = CollisionManager(self)
        self.collisionManager.addCollider(self.character)
        self.collisionManager.addCollider(self.enemy)
        
        # Setting up the Lighting Manager
        self.lightingManager = LightingManager(self)
        self.lightingManager.setAmbientLight(0.3, 0.3, 0.3)
        self.lightingManager.setPointLight(1, 1, 1, 0, -8, 5)
        
        # Setting up the camera
        self.camera.setY(-20)
        self.camera.setZ(4)
        self.camera.lookAt(0, 0, 0)
        self.disableMouse()

world = World()
world.run()
