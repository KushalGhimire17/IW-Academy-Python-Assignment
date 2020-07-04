"""Super mario
"""
class Mario():
    def __init__(self, x, y, level, screen, dashboard, sound, gravity=0.75):
        super(Mario, self).__init__(x, y, gravity)
        self.spriteCollection = Sprites().spriteCollection
        self.camera = Camera(self.rect, self)
        self.sound = sound
        self.input = Input(self)
        self.inAir = False
        self.inJump = False

    def update(self):
        self.updateTraits()
        self.moveMario()
        self.camera.move()
        self.applyGravity()
        self.checkEntityCollision()
        self.input.checkForInput()

    def moveMario(self):
        self.rect.y += self.vel.y
        self.collision.checkY()
        self.rect.x += self.vel.x
        self.collision.checkX()

    def checkEntityCollision(self):
        pass

    def _onCollisionWithItem(self, item):
        pass

    def _onCollisionWithBlock(self, block):
        pass

    def _onCollisionWithMob(self, mob, collisionState):
        pass

    def bounce(self):
        self.traits["bounceTrait"].jump = True

    def killEntity(self, ent):
        pass

    def gameOver(self):
        pass

    def getPos(self):
        return self.camera.x + self.rect.x, self.rect.y

    def setPos(self,x,y):
        self.rect.x = x
        self.rect.y = y