
from items import Weapon
import random

class sim_crossbow(Weapon):
    base_dmg = 7
    base_range = 20
    bonus = 0
    uses = "2*DEX"
    name = "Simple Crossbow"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= 2
        self.t.update()
    def update(self):
        self.mod = int(self.t.dex)
        super().update()
        
class sim_axe(Weapon):
    base_dmg = 14
    base_range = 5
    bonus = 2
    uses = "2*STR"
    name = "Simple Axe"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.str -= 2
        self.t.update()
    def update(self):
        self.mod = int(self.t.str)
        super().update() 

class sim_sword(Weapon):
    base_dmg = 12
    base_range = 5
    bonus = 3
    uses = "1.5*STR, 0.5*DEX"
    name = "Simple Sword"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.str -= 1.5
        self.t.dex -= 0.5
        self.t.update()
    def update(self):
        self.mod = int((self.t.str*2 + self.t.dex)/3)
        super().update()

class sim_bow(Weapon):
    base_dmg = 8
    base_range = 25
    bonus = -1
    uses = "1.5*DEX, 0.5*STR"
    name = "Simple Bow"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= 1.5
        self.t.str -= 0.5
        self.t.update()
    def update(self):
        self.mod = int((self.t.dex*2 + self.t.str)/3)
        super().update()

class mid_dagger(Weapon):
    base_dmg = 15
    base_range = 4
    bonus = 3
    uses = "2*DEX, 1*STR"
    name = "Dagger"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(1,7)+random.randint(1,7))/4
        self.t.str -= 1
        self.t.update()
    def update(self):
        self.mod = int(self.t.dex + 0.5+self.t.str)
        super().update()

class mid_katana(Weapon):
    base_dmg = 18
    base_range = 5
    bonus = 4
    uses = "2*DEX, 2*STR"
    name = "Katana"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(1,7)+random.randint(1,7))/4
        self.t.str -= (random.randint(1,7)+random.randint(1,7))/4
        self.t.update()
    def update(self):
        self.mod = int(self.t.dex + self.t.str)
        super().update()

class mid_rapier(Weapon):
    base_dmg = 16
    base_range = 7
    bonus = 5
    uses = "3*DEX, 1*STR"
    name = "Rapier"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(3,9)+random.randint(3,9))/4
        self.t.str -= (random.randint(1,3)+random.randint(1,3))/4
        self.t.update()
    def update(self):
        self.mod = int((3*self.t.dex + self.t.str)/2)
        super().update()

class mid_saber(Weapon):
    base_dmg = 22
    base_range = 5
    bonus = 4
    uses = "1*DEX, 3*STR"
    name = "Saber"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(1,3)+random.randint(1,3))/4
        self.t.str -= (random.randint(3,9)+random.randint(3,9))/4
        self.t.update()
    def update(self):
        self.mod = int((self.t.dex + 3*self.t.str)/2)
        super().update()

class mid_sword(Weapon):
    base_dmg = 20
    base_range = 5
    bonus = 3.5
    uses = "4*STR"
    name = "Greatsword"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.str -= (random.randint(3,13)+random.randint(3,13))/4
        self.t.update()
    def update(self):
        self.mod = int(2*self.t.str) 
        super().update()

class mid_bow(Weapon):
    base_dmg = 16
    base_range = 35
    bonus = 2
    uses = "3*DEX, 1*STR"
    name = "Recurve Bow"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(3,9)+random.randint(3,9))/4
        self.t.str -= (random.randint(1,3)+random.randint(1,3))/4
        self.t.update()
    def update(self):
        self.mod = int((3*self.t.dex + self.t.str)/2)
        super().update()

class mid_crossbow(Weapon):
    base_dmg = 18
    base_range = 30
    bonus = 2
    uses = "4*DEX"
    name = "Compound Crossbow"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(3,13)+random.randint(3,13))/4
        self.t.update()
    def update(self):
        self.mod = int(2*self.t.dex)
        super().update()

class mid_axe(Weapon):
    base_dmg = 25
    base_range = 5
    bonus = 2
    uses = "1*DEX, 4*STR"
    name = "Greataxe"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(1,3)+random.randint(1,3))/4
        self.t.str -= (random.randint(5,11)+random.randint(5,11))/4
        self.t.update()
    def update(self):
        self.mod = int((self.t.dex + 4*self.t.str)/2)
        super().update()


class mid_hammer(Weapon):
    base_dmg = 27
    base_range = 3
    bonus = 1.5
    uses = "5*STR"
    name = "HAMMAR!"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.str -= (random.randint(5,15)+random.randint(5,15))/4
        self.t.update()
    def update(self):
        self.mod = int(2.5*self.t.str)
        super().update()

class mid_musket(Weapon):
    base_dmg = 13
    base_range = 50
    bonus = 1
    uses = "6*DEX"
    name = "Musket"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(7,17))/2
        self.t.update()
    def update(self):
        self.mod = int(3*self.t.dex)
        super().update()

class mid_pistol(Weapon):
    base_dmg = 20
    base_range = 20
    bonus = 2
    uses = "5*DEX"
    name = "Pistol"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(5,15))/2
        self.t.update()
    def update(self):
        self.mod = int(2.5*self.t.dex)
        super().update()

class spe_bow(Weapon):
    base_dmg = 40
    base_range = 50
    bonus = 6
    uses = "4*DEX, 4*MAN"
    name = "Green Dart"
    special = "\nFor the next 2 rounds, the opponent takes 1.5 times of all damage dealt"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(4,12))/2
        self.t.man -= (random.randint(6,10))/2
        self.t.update()
    def update(self):
        self.mod = int((2*self.t.dex + 2*self.t.man)*1.5)
        super().update()

class spe_hammer(Weapon):
    base_dmg = 60
    base_range = 7
    bonus = 6
    uses = "4*STR, 4*MAN"
    name = "Mjölnir"
    special = "\nThe opponent is stunned for the next round"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.str -= (random.randint(4,12))/2
        self.t.man -= (random.randint(6,10))/2
        self.t.update()
    def update(self):
        self.mod = int((2*self.t.str + 2*self.t.man)*1.5)
        super().update()

class spe_sword(Weapon):
    base_dmg = 57
    base_range = 9
    bonus = 6
    uses = "2*STR, 2*DEX, 4*MAN"
    name = "Burning Blade"
    special = "\nFor the next two rounds, the opponent takes 1/4th of this damage"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.str -= (random.randint(2,6))/2
        self.t.dex -= (random.randint(2,6))/2
        self.t.man -= (random.randint(6,10))/2
        self.t.update()
    def update(self):
        self.mod = int((self.t.str + self.t.dex + 2*self.t.man)*1.5)
        super().update()

class spe_katana(Weapon):
    base_dmg = 55
    base_range = 10
    bonus = 6
    uses = "3*DEX, 1*STR, 4*MAN"
    name = "Vamos"
    special = "\nYou may regain 1/4th of this damage in HP"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        self.t.dex -= (random.randint(2,10))/2
        self.t.str -= (random.randint(0,4))/2
        self.t.man -= (random.randint(6,10))/2
        self.t.update()
    def update(self):
        self.mod = int((0.5*self.t.str + 1.5*self.t.dex + 2*self.t.man)*1.5)
        super().update()
