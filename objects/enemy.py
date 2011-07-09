from physicalnode import PhysicalNode
from handlers.collision import CollisionEventHandler


class Enemy(PhysicalNode, CollisionEventHandler):
    ANIM_WALK = "anim1"
    JUMP_SOUND = ["water_jumping", 7]
    
    def __init__(self, parent, model, name="enemy"):
        PhysicalNode.__init__(self, parent, model, name, [self.ANIM_WALK])
        
        self.mass = 20.0
        
        self.addCollisionSphere(1.25)
        self._impact = 2
        
        self.model.loop(self.ANIM_WALK)
    
    def handleCollisionEvent(self, entry, type):
        normal = entry.getSurfaceNormal(self)
        normal.z = 0
        normal.normalize()
        
        character = base.gameState.currentState.objects['character']
        otherVelocity = character.velocity
        otherMass = character.mass
        self.collide(-normal, otherVelocity, otherMass, 0.75)
        
