from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox
import itemizer as items
import random

class sceduler:
    tasks = []

    def __init__(self):
        pass

    def scedule(self, dt, func):
        self.tasks.append([dt,func])

    def scedule_during(self, ts, te, func):
        for dt in range(ts, te):
            self.scedule(dt,func)

    def execute(self):
        done = []
        for i in range(len(self.tasks)):
            self.tasks[i][0] -= 1
            if(self.tasks[i][0]<0):
                self.tasks[i][1]()
                done.append(i)
        for i in done:
            self.tasks.pop(i)

class tracker:
    hp=100
    spd=10
    str=25
    dex=25
    man=25
    soc=25
    inventory = QVBoxLayout()
    itemlist = []
    dmgbuff=0
    sldbuff=0

    def __init__(self, labels):
        self.l = labels
        self.s = sceduler()
        self.update()

    def update(self):
        for item in self.itemlist:
            if(item.active):
                item.update()
        self.l[0].setText(f"{self.hp:.2f}")
        self.l[1].setText(f"{self.spd:.2f}")
        self.l[2].setText(f"{self.str:.2f}")
        self.l[3].setText(f"{self.dex:.2f}")
        self.l[4].setText(f"{self.man:.2f}")
        self.l[5].setText(f"{self.soc:.2f}")
        self.l[6].setText(f"{self.dmgbuff:.2f}")
        self.l[7].setText(f"{self.sldbuff:.2f}")

    def reupdate(self):
        self.hp=float(self.l[0].text())
        self.spd=float(self.l[1].text())
        self.str=float(self.l[2].text())
        self.dex=float(self.l[3].text())
        self.man=float(self.l[4].text())
        self.soc=float(self.l[5].text())
        self.dmgbuff=float(self.l[6].text())
        self.sldbuff=float(self.l[7].text())
        self.update()

class CharacterSheetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Character Sheet")
        #self.setGeometry(100, 100, 400, 300)

        overlayer = QVBoxLayout()
        layout = QHBoxLayout()

        stats_lab = QVBoxLayout()
        stats_lab.addWidget(QLabel("Health"))
        stats_lab.addWidget(QLabel("Speed"))
        stats_lab.addWidget(QLabel("Strength"))
        stats_lab.addWidget(QLabel("Dexterity"))
        stats_lab.addWidget(QLabel("Mana"))
        stats_lab.addWidget(QLabel("Social"))
        stats_lab.addWidget(QLabel("Attack buff"))
        stats_lab.addWidget(QLabel("Defense buff"))
        layout.addLayout(stats_lab)
        
        stats = QVBoxLayout()
        hp_label = QLineEdit()
        spd_label = QLineEdit()
        str_label = QLineEdit()
        dex_label = QLineEdit()
        man_label = QLineEdit()
        soc_label = QLineEdit()
        dmgbuff_label = QLineEdit()
        sldbuff_label = QLineEdit()

        labels = (hp_label,spd_label,str_label,dex_label,man_label,soc_label,dmgbuff_label,sldbuff_label)

        self.t = tracker(labels)

        for label in labels:
            stats.addWidget(label)
            label.returnPressed.connect(self.t.reupdate)
            
        layout.addLayout(stats)
        layout.addLayout(self.t.inventory)
        overlayer.addLayout(layout)

        add_layout = QHBoxLayout()
        self.add_item_text = QLineEdit()
        add_layout.addWidget(self.add_item_text)
        self.add_item_text.returnPressed.connect(self.add_item)
        add_item_button = QPushButton("Add")
        add_item_button.clicked.connect(self.add_item)
        add_layout.addWidget(add_item_button)
        overlayer.addLayout(add_layout)

        button_layout = QHBoxLayout()
        turn_button = QPushButton("End of Turn")
        turn_button.clicked.connect(self.t.s.execute)
        button_layout.addWidget(turn_button)
        roll_button = QPushButton("Roll")
        roll_button.clicked.connect(self.roll)
        button_layout.addWidget(roll_button)
        damage_button = QPushButton("Get Damage")
        damage_button.clicked.connect(self.get_damage)
        button_layout.addWidget(damage_button)
        save_button = QPushButton("Save stats")
        save_button.clicked.connect(self.save)
        button_layout.addWidget(save_button)
        load_button = QPushButton("Load stats")
        load_button.clicked.connect(self.load)
        button_layout.addWidget(load_button)
        overlayer.addLayout(button_layout)

        container = QWidget()
        container.setLayout(overlayer)
        self.setCentralWidget(container)
    
    def save(self):
        try:
            with open("stats.txt", "w") as file:
                file.write(f"{self.t.hp}\n")
                file.write(f"{self.t.spd}\n")
                file.write(f"{self.t.str}\n")
                file.write(f"{self.t.dex}\n")
                file.write(f"{self.t.man}\n")
                file.write(f"{self.t.soc}\n")
                file.write(f"{self.t.dmgbuff}\n")
                file.write(f"{self.t.sldbuff}\n")
            with open("items.txt", "w") as file:
                for item in self.t.itemlist:
                    if item.active:
                        file.write(f"{item.name}\n")
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Save Successful")
            msg_box.setText("Character stats have been saved successfully.")
            msg_box.exec()
        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Save Failed")
            msg_box.setText(f"An error occurred while saving: {e}")
            msg_box.exec()

    def load(self):
        try:
            with open("stats.txt", "r") as file:
                stats = file.readlines()
                self.t.hp = float(stats[0].strip())
                self.t.spd = float(stats[1].strip())
                self.t.str = float(stats[2].strip())
                self.t.dex = float(stats[3].strip())
                self.t.man = float(stats[4].strip())
                self.t.soc = float(stats[5].strip())
                self.t.dmgbuff = float(stats[6].strip())
                self.t.sldbuff = float(stats[7].strip())
                self.t.update()
            with open("items.txt", "r") as file:
                for item in self.t.itemlist:
                    item.remove()
                self.t.itemlist = []
                for line in file:
                    item_name = line.strip()
                    try:
                        self.t.itemlist.append(items.get_classes_dict()[item_name](self.t))
                    except KeyError:
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Item Load Error")
                        msg_box.setText(f"Error: '{item_name}' is not a valid item.")
                        msg_box.exec()
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Load Successful")
            msg_box.setText("Character stats have been loaded successfully.")
            msg_box.exec()
        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Load Failed")
            msg_box.setText(f"An error occurred while loading: {e}")
            msg_box.exec()

    def add_item(self):
        try:
            self.t.itemlist.append(items.get_classes_dict()[self.add_item_text.text()](self.t))
        except KeyError:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Item not found.")
            msg_box.setText(f"Error: '{self.add_item_text.text()}' is not a valid item.")
            msg_box.exec()

    def roll(self):
        self.roll_window = QMainWindow()
        self.roll_window.setWindowTitle("Roll")

        layout = QVBoxLayout()

        def roll_stat(stat_name):
            stat = getattr(self.t, stat_name.lower())
            result = (random.randint(0, stat)+random.randint(0, stat))
            msg_box = QMessageBox()
            msg_box.setWindowTitle(f"{stat_name} Roll")
            msg_box.setText(f"Roll result for {stat_name}: {result}")
            msg_box.exec()

        str_button = QPushButton("Roll STR")
        str_button.clicked.connect(lambda: roll_stat("STR"))
        layout.addWidget(str_button)

        dex_button = QPushButton("Roll DEX")
        dex_button.clicked.connect(lambda: roll_stat("DEX"))
        layout.addWidget(dex_button)

        man_button = QPushButton("Roll MAN")
        man_button.clicked.connect(lambda: roll_stat("MAN"))
        layout.addWidget(man_button)

        soc_button = QPushButton("Roll SOC")
        soc_button.clicked.connect(lambda: roll_stat("SOC"))
        layout.addWidget(soc_button)

        container = QWidget()
        container.setLayout(layout)
        self.roll_window.setCentralWidget(container)
        self.roll_window.show()

    def get_damage(self):
        damage_window = QMainWindow()
        damage_window.setWindowTitle("Get Damage")

        input_field = QLineEdit()
        submit_button = QPushButton("Submit")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter damage value:"))
        layout.addWidget(input_field)
        layout.addWidget(submit_button)

        container = QWidget()
        container.setLayout(layout)
        damage_window.setCentralWidget(container)

        def apply_damage():
            try:
                damage = float(input_field.text())
                self.t.hp -= damage
                self.t.update()
                damage_window.close()
            except ValueError:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Invalid Input")
                msg_box.setText("Please enter a valid number.")
                msg_box.exec()

        submit_button.clicked.connect(apply_damage)
        input_field.returnPressed.connect(apply_damage)
        damage_window.show()
if __name__ == "__main__":
    app = QApplication([])
    window = CharacterSheetWindow()
    window.show()
    app.exec()