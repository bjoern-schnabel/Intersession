from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from items import Potion

class s_health_potion(Potion):
    name = "Small Health Potion"
    dur = 2
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp+=5
    def finalize(self):
        if super().finalize():
            pass

class m_health_potion(Potion):
    name = "Medium Health Potion"
    dur = 6
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp+=15
            self.t.spd-=2.5
    def finalize(self):
        if super().finalize():
            self.t.spd+=1.5

class l_health_potion(Potion):
    name = "Large Health Potion"
    dur = 9
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp+=30
            self.t.spd-=5
            self.t.man-=4
    def finalize(self):
        if super().finalize():
            self.t.hp-=10
            self.t.spd+=5

class s_speed_potion(Potion):
    name = "Small Speed Potion"
    dur = 3
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.spd+=1
    def finalize(self):
        if super().finalize():
            self.t.spd-=1

class m_speed_potion(Potion):
    name = "Medium Speed Potion"
    dur = 6
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp-=15
            self.t.spd+=2.5
    def finalize(self):
        if super().finalize():
            self.t.hp+=10
            self.t.spd-=2.5

class l_speed_potion(Potion):
    name = "Large Speed Potion"
    dur = 9
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp-=30
            self.t.spd+=5
            self.t.man-=4
    def finalize(self):
        if super().finalize():
            self.t.hp+=30
            self.t.spd-=5

class s_str_potion(Potion):
    name = "Small Strength Potion"
    dur = 3
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.str+=5
    def finalize(self):
        if super().finalize():
            self.t.str-=5

class l_str_potion(Potion):
    name = "Large Strength Potion"
    dur = 9
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp-=10
            self.t.str+=15
            self.t.man-=4
    def finalize(self):
        if super().finalize():
            self.t.hp+=10
            self.t.str-=15

class s_dex_potion(Potion):
    name = "Small Dexterity Potion"
    dur = 3
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.dex+=5
    def finalize(self):
        if super().finalize():
            self.t.dex-=5

class l_dex_potion(Potion):
    name = "Large Dexterity Potion"
    dur = 9
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp-=10
            self.t.dex+=15
            self.t.man-=4
    def finalize(self):
        if super().finalize():
            self.t.hp+=10
            self.t.dex-=15

class s_man_potion(Potion):
    name = "Small Mana Potion"
    sets = {"MAN": 5}
    dur = 3
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.man+=5
    def finalize(self):
        if super().finalize():
            self.t.man-=5

class l_man_potion(Potion):
    name = "Large Mana Potion"
    dur = 9
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp-=10
            self.t.str-=4
            self.t.dex-=4
            self.t.man+=15
    def finalize(self):
        if super().finalize():
            self.t.hp+=10

class s_soc_potion(Potion):
    name = "Small Social Potion"
    dur = 3
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.soc+=5
    def finalize(self):
        if super().finalize():
            self.t.soc-=5

class l_soc_potion(Potion):
    name = "Large Social Potion"
    dur = 9
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp-=10
            self.t.soc+=15
            self.t.man-=4
    def finalize(self):
        if super().finalize():
            self.t.hp+=10
            self.t.soc-=15

class dmgbuff_potion(Potion):
    name = "Attack Buff Potion"
    dur = 2
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp-=10
            self.t.dmgbuff+=25
            self.t.man-=4
    def finalize(self):
        if super().finalize():
            self.t.hp+=5
            self.t.dmgbuff-=25

class sldbuff_potion(Potion):
    name = "Defense Buff Potion"
    dur = 2
    def use(self):
        if super().use():
            self.used=True
            self.t.s.scedule(self.dur, self.finalize)
            self.t.hp-=10
            self.t.sldbuff+=25
            self.t.man-=4
    def finalize(self):
        if super().finalize():
            self.t.hp+=5
            self.t.sldbuff-=25
