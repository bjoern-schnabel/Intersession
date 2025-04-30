from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QInputDialog
import random

smod = 2
sstd = 40

def InputWindow (par_name, default):
    parameter, ok = QInputDialog.getInt(None, "Input Required", f"Enter a value for {par_name}:")
    if not ok:
        parameter = default
    return parameter

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

class Potion(Item):
    dur = 0
    name = "Unknown Potion"
    used = False
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
        if(self.active):
            if(self.used):
                err_box = QMessageBox()
                err_box.setWindowTitle("Not yet used")
                err_box.setText(f"You have to use the potion before finalizing it.")
                err_box.exec()
                return False
            self.remove()
            self.t.update()
            True
    def use(self):
        if(self.used):
            err_box = QMessageBox()
            err_box.setWindowTitle("Allready used")
            err_box.setText(f"You allready used this potion.")
            err_box.exec()
            return False
        return True
        super().use()
    def labelcont(self):
        return f"{self.name}: Duration: {self.dur} rnd"

class Status:
    name = "Unknown Status"
    rounds = 1
    def __init__(self,tracker):
        self.active = True
        self.t=tracker
        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.buttons = QHBoxLayout()
        remove_button = QPushButton("REMOVE")
        remove_button.clicked.connect(self.remove)
        self.buttons.addWidget(remove_button)
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
    def tick(self):
        self.rounds -= 1
        if(self.rounds <= 0):
            self.remove()
            return False
        if(not self.active):
            return False
        self.update()
        return True
    def labelcont(self):
        return f"{self.name}: Duration: {self.rounds} rds"

class CustomStatus(Status):
    name = "New Status"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.name, ok = QInputDialog.getText(None, "Creating Status", f"Enter a name for the new status:")
        if not ok and self.name!="":
            self.remove()
            return
        self.update()
        self.rounds = InputWindow("Duration", 1)
        self.t.s.scedule_during(0,self.rounds,self.tick)
        self.update()
        self.t.update()
    
class CustomItem:
    name = "New Item"
    desc = ""
    def __init__(self,tracker):
        self.active = True
        self.t=tracker
        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.buttons = QHBoxLayout()
        remove_button = QPushButton("REMOVE")
        remove_button.clicked.connect(self.remove)
        self.buttons.addWidget(remove_button)
        self.layout.addLayout(self.buttons)
        self.t.inventory.addLayout(self.layout)

        if self.name=="New Item":
            self.name, ok = QInputDialog.getText(None, "Creating Item", f"Enter a name for the new item:")
            if not ok and self.name!="":
                self.remove()
                return
            self.update()
            d, ok = QInputDialog.getText(None, "Creating Item", f"Enter a description for the new item:")
            if ok and d!="":
                self.desc = "\n"+d
            with open("./custom.py", "r") as f:
                index = int(f.readlines()[-1][1:])
            with open("./custom.py", "a") as f:
                f.write(f'''
class CustomItem{index}(CustomItem):
    name = "{self.name}"
    desc = {repr(self.desc)}
\n#{index+1}''')
        self.update()
        
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
    def labelcont(self):
        return f"{self.name}{self.desc}"


try:
    with open("./custom.py", "r") as f:
        index = int(f.readlines()[-1][1:])
except:
    with open("./custom.py", "w") as f:
        f.write("from items import CustomItem, Status\n#0")