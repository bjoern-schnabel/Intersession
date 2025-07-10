from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from items import Potion

class s_health_potion(Potion):
    name = "Small Health Potion"
    dur = 2
    def use(self):
        if super().use():
            self.t.hp+=50
        self.t.update()
    def finalize(self):
        if super().finalize():
            pass
        self.t.update()

class m_health_potion(Potion):
    name = "Medium Health Potion"
    dur = 6
    def use(self):
        if super().use():
            self.t.hp+=150
            self.t.spd-=2.5
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.spd+=1.5
        self.t.update()

class l_health_potion(Potion):
    name = "Large Health Potion"
    dur = 9
    def use(self):
        if super().use():
            self.t.hp+=300
            self.t.spd-=5
            self.t.man-=4
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.hp-=100
            self.t.spd+=5
        self.t.update()

class s_speed_potion(Potion):
    name = "Small Speed Potion"
    dur = 3
    def use(self):
        if super().use():
            self.t.spd+=1
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.spd-=1
        self.t.update()

class m_speed_potion(Potion):
    name = "Medium Speed Potion"
    dur = 6
    def use(self):
        if super().use():
            self.t.hp-=150
            self.t.spd+=2.5
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.hp+=100
            self.t.spd-=2.5
        self.t.update()

class l_speed_potion(Potion):
    name = "Large Speed Potion"
    dur = 9
    def use(self):
        if super().use():
            self.t.hp-=300
            self.t.spd+=5
            self.t.man-=4
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.hp+=300
            self.t.spd-=5
        self.t.update()

class s_str_potion(Potion):
    name = "Small Strength Potion"
    dur = 3
    def use(self):
        if super().use():
            self.t.str+=5
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.str-=5
        self.t.update()

class l_str_potion(Potion):
    name = "Large Strength Potion"
    dur = 9
    def use(self):
        if super().use():
            self.t.hp-=100
            self.t.str+=15
            self.t.man-=4
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.hp+=100
            self.t.str-=15
        self.t.update()

class s_dex_potion(Potion):
    name = "Small Dexterity Potion"
    dur = 3
    def use(self):
        if super().use():
            self.t.dex+=5
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.dex-=5
        self.t.update()

class l_dex_potion(Potion):
    name = "Large Dexterity Potion"
    dur = 9
    def use(self):
        if super().use():
            self.t.hp-=100
            self.t.dex+=15
            self.t.man-=4
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.hp+=100
            self.t.dex-=15
        self.t.update()

class s_man_potion(Potion):
    name = "Small Mana Potion"
    sets = {"MAN": 5}
    dur = 3
    def use(self):
        if super().use():
            self.t.man+=5
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.man-=5
        self.t.update()

class l_man_potion(Potion):
    name = "Large Mana Potion"
    dur = 9
    def use(self):
        if super().use():
            self.t.hp-=100
            self.t.str-=4
            self.t.dex-=4
            self.t.man+=15
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.hp+=100
        self.t.update()

class s_soc_potion(Potion):
    name = "Small Social Potion"
    dur = 3
    def use(self):
        if super().use():
            self.t.soc+=5
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.soc-=5
        self.t.update()

class l_soc_potion(Potion):
    name = "Large Social Potion"
    dur = 9
    def use(self):
        if super().use():
            self.t.hp-=100
            self.t.soc+=15
            self.t.man-=4
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.hp+=100
            self.t.soc-=15
        self.t.update()

class dmgbuff_potion(Potion):
    name = "Attack Buff Potion"
    dur = 2
    def use(self):
        if super().use():
            self.t.hp-=100
            self.t.dmgbuff+=25
            self.t.man-=4
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.hp+=50
            self.t.dmgbuff-=25
        self.t.update()

class sldbuff_potion(Potion):
    name = "Defense Buff Potion"
    dur = 2
    def use(self):
        if super().use():
            self.t.hp-=100
            self.t.sldbuff+=25
            self.t.man-=4
        self.t.update()
    def finalize(self):
        if super().finalize():
            self.t.hp+=50
            self.t.sldbuff-=25
        self.t.update()
