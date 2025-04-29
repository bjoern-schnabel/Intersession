from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox
import random

smod = 2
sstd = 40


class Item:
    name = "Unknown Item"
    def __init__(self,tracker):
        self.active = True
        self.superd = False
        self.mod=0
        self.t=tracker
        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.buttons = QHBoxLayout()
        remove_button = QPushButton("REMOVE")
        remove_button.clicked.connect(self.remove)
        self.buttons.addWidget(remove_button)
        use_button = QPushButton("USE")
        use_button.clicked.connect(self.use)
        self.buttons.addWidget(use_button)
        self.layout.addLayout(self.buttons)
        self.t.inventory.addLayout(self.layout)
    def update(self):
        self.label.setText(self.labelcont())
    def remove(self):
        for i in reversed(range(self.buttons.count())): 
            try:
                self.buttons.itemAt(i).widget().setParent(None)
            except:
                pass
        for i in reversed(range(self.layout.count())): 
            try:
                self.layout.itemAt(i).widget().setParent(None)
            except:
                pass
        self.active = False
    def use(self):
        self.update()
    def labelcont(self):
        return f"Unknown Item"
    
class Weapon(Item):
    name = "Unknown Weapon"
    uses = "???"
    base_dmg = 0
    base_range = 0
    bonus = 0
    special = ""
    def __init__(self, tracker):
        super().__init__(tracker)
        super_button = QPushButton("SUPERCHARGE")
        super_button.clicked.connect(self.superc)
        self.buttons.addWidget(super_button)
    def use(self):
        if(self.mod<=0):
            err_box = QMessageBox()
            err_box.setWindowTitle("Modifyer too small")
            err_box.setText(f"You can't use that weapon right now. Your skills are too low")
            err_box.exec()
            return
        attack = random.randint(0,self.mod)+random.randint(0,self.mod)+2*self.bonus
        if(self.superd):
            attack += random.randint(0,self.mod)+random.randint(0,self.mod)+2*self.bonus
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Attack Result")
        msg_box.setText(f"Attack Value: {attack}\nDoes that hit?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)

        result = msg_box.exec()

        if result == QMessageBox.StandardButton.Yes:
            damage = self.base_dmg*(1+smod*self.superd)*(self.mod/sstd) + random.randint(int(-self.base_dmg*(self.mod/sstd)/2), int(self.base_dmg*(self.mod/sstd)/2)) + self.t.dmgbuff
            dmg_box = QMessageBox()
            dmg_box.setWindowTitle("Damage Result")
            dmg_box.setText(f"Damage Dealt: {damage:.2f}{self.special}")
            dmg_box.exec()
        self.superd = False
        self.update()
    def labelcont(self):
        return f"{self.name}: Damage: {self.base_dmg*(1+smod*self.superd)*(self.mod/sstd):.2f}\nBonus: {self.bonus}, Range: {self.base_range*(1+0.5*self.superd)}, uses: {self.uses}"

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

    
class Shield(Item):
    name = "Unknown Shield"
    uses = "???"
    base_dmg = 0
    base_range = 0
    bonus = 0
    special = ""
    str_dex = 1
    def __init__(self, tracker):
        super().__init__(tracker)
        super_button = QPushButton("SUPERCHARGE")
        super_button.clicked.connect(self.superc)
        self.buttons.addWidget(super_button)
        use_button = QPushButton("SET USEAGE")
        use_button.clicked.connect(self.set_useage)
        self.buttons.addWidget(use_button)
    def use(self):
        if(self.mod<=0):
            err_box = QMessageBox()
            err_box.setWindowTitle("Modifyer too small")
            err_box.setText(f"You can't use that shield right now. Your skills are too low")
            err_box.exec()
            return
        attack = random.randint(0,self.mod)+self.bonus
        attack*=2+(2*self.superd)
        attack+=self.t.sldbuff
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Block Result")
        msg_box.setText(f"Block Value: {attack}{self.special}")
        msg_box.exec()

        self.superd = False
        self.update()
    def set_useage(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Attack Result")
        msg_box.setText(f"Select which stat you will use")
        msg_box.addButton('STR', QMessageBox.ButtonRole.NoRole)
        msg_box.addButton('DEX', QMessageBox.ButtonRole.YesRole)
        self.str_dex = msg_box.exec()

    def labelcont(self):
        return f"{self.name}: Average: {(self.mod/2+self.bonus)*(2+(2*self.superd)):.2f}, uses: {self.uses}"

class sim_shield(Shield):
    bonus = 1
    uses = "2*STR / 2*DEX"
    name = "Simple Shield"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        if(self.str_dex):
            self.t.str -= 4
        else:
            self.t.str -= 2
            self.t.dex -= 2
        self.t.update()
    def set_useage(self):
        super().set_useage()
        self.superd=False
        self.update()
    def update(self):
        if(self.str_dex):
            self.mod = int(self.t.str)
            self.uses = "2*STR"
        else:
            self.mod = int(self.t.dex)
            self.uses = "2*DEX"
        super().update() 

class mid_shield_big(Shield):
    bonus = 3
    uses = "4*STR / (2*DEX, 2*STR)"
    name = "Shieldwall"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        if(self.str_dex):
            self.t.str -= 4
        else:
            self.t.str -= 2
            self.t.dex -= 2
        self.t.update()
    def set_useage(self):
        super().set_useage()
        self.superd=False
        self.update()
    def update(self):
        if(self.str_dex):
            self.mod = int(2*self.t.str)
            self.uses = "4*STR"
        else:
            self.mod = int(self.t.str+self.t.dex)
            self.uses = "2*DEX, 2*STR"
        super().update() 

class mid_shield_small(Shield):
    bonus = 3
    uses = "(2*DEX, 2*STR) / 4*DEX"
    name = "Onehanded Shield"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        if(self.str_dex):
            self.t.str -= 2
            self.t.dex -= 2
        else:
            self.t.dex -= 4
        self.t.update()
    def set_useage(self):
        super().set_useage()
        self.superd=False
        self.update()
    def update(self):
        if(self.str_dex):
            self.mod = int(self.t.str+self.t.dex)
            self.uses = "2*DEX, 2*STR"
        else:
            self.mod = int(2*self.t.dex)
            self.uses = "4*DEX"
        super().update() 

class spe_roots(Shield):
    bonus = 6
    uses = "(4*STR, 4*MAN) / (4*DEX, 4*MAN)"
    name = "Roots"
    special = "\nThe opponent is grappeled until the end of his next turn. He cannot move but may attack."
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        if(self.str_dex):
            self.t.str -= 4
            self.t.man -= 4
        else:
            self.t.dex -= 4
            self.t.man -= 4
        self.t.update()
    def set_useage(self):
        super().set_useage()
        self.superd=False
        self.update()
    def update(self):
        if(self.str_dex):
            self.mod = int(self.t.str+self.t.man)*2
            self.uses = "4*STR, 4*MAN"
        else:
            self.mod = int(self.t.dex+self.t.man)*2
            self.uses = "4*DEX, 4*MAN"
        super().update() 

class spe_frost(Shield):
    bonus = 6
    uses = "(4*STR, 4*MAN) / (4*DEX, 4*MAN)"
    name = "Frost"
    special = "\nA wall of ice forms around the opponent. It disappears after the opponents next turn. It has a Defence of 70. All attacks against the target get attack buff 20."
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        if(self.str_dex):
            self.t.str -= 4
            self.t.man -= 4
        else:
            self.t.dex -= 4
            self.t.man -= 4
        self.t.update()
    def set_useage(self):
        super().set_useage()
        self.superd=False
        self.update()
    def update(self):
        if(self.str_dex):
            self.mod = int(self.t.str+self.t.man)*2
            self.uses = "4*STR, 4*MAN"
        else:
            self.mod = int(self.t.dex+self.t.man)*2
            self.uses = "4*DEX, 4*MAN"
        super().update() 

class spe_gust(Shield):
    bonus = 6
    uses = "(4*STR, 4*MAN) / (4*DEX, 4*MAN)"
    name = "Gust"
    special = "\nThe opponent is pushed backwards 15 feet and is knocked prone (has to spend their action to get up). All attacks against the target get attack buff 20."
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        if(self.str_dex):
            self.t.str -= 4
            self.t.man -= 4
        else:
            self.t.dex -= 4
            self.t.man -= 4
        self.t.update()
    def set_useage(self):
        super().set_useage()
        self.superd=False
        self.update()
    def update(self):
        if(self.str_dex):
            self.mod = int(self.t.str+self.t.man)*2
            self.uses = "4*STR, 4*MAN"
        else:
            self.mod = int(self.t.dex+self.t.man)*2
            self.uses = "4*DEX, 4*MAN"
        super().update() 

class spe_artefact(Shield):
    bonus = 6
    uses = "(4*STR, 4*MAN) / (4*DEX, 4*MAN)"
    name = "Artefact"
    special = "\nA dimensional rift forms halfway between you and the opponent and persists until the end of the opponents next turn. \nAll creatures within 15 feet are pulled 5 feet towards the rift at the end of their turn. \nIf a creature exept you ends their turn clser than 5 feet to the rift, they take 1/4th of the damage your opponent would have dealt you."
    def __init__(self, tracker):
        super().__init__(tracker)
        self.update()
    def superc(self):
        self.superd = True
        if(self.str_dex):
            self.t.str -= 4
            self.t.man -= 4
        else:
            self.t.dex -= 4
            self.t.man -= 4
        self.t.update()
    def set_useage(self):
        super().set_useage()
        self.superd=False
        self.update()
    def update(self):
        if(self.str_dex):
            self.mod = int(self.t.str+self.t.man)*2
            self.uses = "4*STR, 4*MAN"
        else:
            self.mod = int(self.t.dex+self.t.man)*2
            self.uses = "4*DEX, 4*MAN"
        super().update() 

class Potion(Item):
    dur = 0
    name = "Unknown Potion"
    def __init__(self, tracker):
        super().__init__(tracker)
        fin_button = QPushButton("FINALIZE")
        fin_button.clicked.connect(self.finalize)
        self.buttons.addWidget(fin_button)
        self.update()
    def use(self):
        self.name += " (used)"
        self.t.update()
    def finalize(self):
        self.remove()
        self.t.update()
    def labelcont(self):
        return f"{self.name}: Duration: {self.dur}"
    
class s_health_potion(Potion):
    name = "Small Health Potion"
    dur = "3 rnd"
    def use(self):
        self.t.hp+=5
        super().use()
    def finalize(self):
        self.t.hp-=5
        super().finalize()

class m_health_potion(Potion):
    name = "Medium Health Potion"
    dur = "6 rnd"
    def use(self):
        self.t.hp+=15
        self.t.spd-=2.5
        super().use()
    def finalize(self):
        self.t.hp-=15
        self.t.spd+=2.5
        super().finalize()

class l_health_potion(Potion):
    name = "Large Health Potion"
    dur = "9 rnd"
    def use(self):
        self.t.hp+=30
        self.t.spd-=5
        self.t.man-=4
        super().use()
    def finalize(self):
        self.t.hp-=30
        self.t.spd+=5
        super().finalize()

class s_speed_potion(Potion):
    name = "Small Speed Potion"
    dur = "3 rnd"
    def use(self):
        self.t.spd+=1
        super().use()
    def finalize(self):
        self.t.spd-=1
        super().finalize()

class m_speed_potion(Potion):
    name = "Medium Speed Potion"
    dur = "6 rnd"
    def use(self):
        self.t.hp-=15
        self.t.spd+=2.5
        super().use()
    def finalize(self):
        self.t.hp+=10
        self.t.spd-=2.5
        super().finalize()

class l_speed_potion(Potion):
    name = "Large Speed Potion"
    dur = "9 rnd"
    def use(self):
        self.t.hp-=30
        self.t.spd+=5
        self.t.man-=4
        super().use()
    def finalize(self):
        self.t.hp+=30
        self.t.spd-=5
        super().finalize()

class s_str_potion(Potion):
    name = "Small Strength Potion"
    dur = "3 rnd"
    def use(self):
        self.t.str+=5
        super().use()
    def finalize(self):
        self.t.str-=5
        super().finalize()

class l_str_potion(Potion):
    name = "Large Strength Potion"
    dur = "9 rnd"
    def use(self):
        self.t.hp-=10
        self.t.str+=15
        self.t.man-=4
        super().use()
    def finalize(self):
        self.t.hp+=10
        self.t.str-=15
        super().finalize()

class s_dex_potion(Potion):
    name = "Small Dexterity Potion"
    dur = "3 rnd"
    def use(self):
        self.t.dex+=5
        super().use()
    def finalize(self):
        self.t.dex-=5
        super().finalize()

class l_dex_potion(Potion):
    name = "Large Dexterity Potion"
    dur = "9 rnd"
    def use(self):
        self.t.hp-=10
        self.t.dex+=15
        self.t.man-=4
        super().use()
    def finalize(self):
        self.t.hp+=10
        self.t.dex-=15
        super().finalize()

class s_man_potion(Potion):
    name = "Small Mana Potion"
    sets = {"MAN": 5}
    dur = "3 rnd"
    def use(self):
        self.t.man+=5
        super().use()
    def finalize(self):
        self.t.man-=5
        super().finalize()

class l_man_potion(Potion):
    name = "Large Mana Potion"
    dur = "9 rnd"
    def use(self):
        self.t.hp-=10
        self.t.str-=4
        self.t.dex-=4
        self.t.man+=15
        super().use()
    def finalize(self):
        self.t.hp+=10
        super().finalize()

class s_soc_potion(Potion):
    name = "Small Social Potion"
    dur = "3 rnd"
    def use(self):
        self.t.soc+=5
        super().use()
    def finalize(self):
        self.t.soc-=5
        super().finalize()

class l_soc_potion(Potion):
    name = "Large Social Potion"
    dur = "9 rnd"
    def use(self):
        self.t.hp-=10
        self.t.soc+=15
        self.t.man-=4
        super().use()
    def finalize(self):
        self.t.hp+=10
        self.t.soc-=15
        super().finalize()

class dmgbuff_potion(Potion):
    name = "Damage Buff Potion"
    dur = "2 rnd"
    def use(self):
        self.t.hp-=10
        self.t.dmgbuff+=25
        self.t.man-=4
        super().use()
    def finalize(self):
        self.t.hp+=5
        self.t.dmgbuff-=25
        super().finalize()

class sldbuff_potion(Potion):
    name = "Defense Buff Potion"
    dur = "2 rnd"
    def use(self):
        self.t.hp-=10
        self.t.sldbuff+=25
        self.t.man-=4
        super().use()
    def finalize(self):
        self.t.hp+=5
        self.t.sldbuff-=25
        super().finalize()

def get_classes_dict():
    classes_dict = {}
    for cls in globals().values():
        if isinstance(cls, type) and hasattr(cls, 'name'):
            classes_dict[cls.name] = cls
    return classes_dict
