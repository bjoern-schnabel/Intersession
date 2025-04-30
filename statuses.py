from items import Status, InputWindow

class stuck(Status):
    name = "Stuck"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.rounds = InputWindow("Duration", 1)
        self.t.s.scedule(self.rounds,self.undo)
        self.t.s.scedule_during(0,self.rounds,self.tick)
        self.val = InputWindow("Slowdown Factor", 1)
        self.t.spd /= self.val
        self.update()
        self.t.update()
    def undo(self):
        self.t.spd *= self.val
        self.t.update()
    def labelcont(self):
        return f"{self.name}: Duration: {self.rounds} rds, Slowdown Factor: {self.val}"
    
class total_stuck(Status):
    name = "Totally Stuck"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.rounds = InputWindow("Duration", 1)
        self.t.s.scedule(self.rounds,self.undo)
        self.t.s.scedule_during(0,self.rounds,self.tick)
        self.val = self.t.spd
        self.t.spd = 0
        self.update()
        self.t.update()
    def undo(self):
        self.t.spd = self.val
        self.t.update()
    def labelcont(self):
        return f"{self.name}: Duration: {self.rounds} rds, Slowdown Factor: {self.val}"
    
class weak(Status):
    name = "Weak"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.rounds = InputWindow("Duration", 1)
        self.t.s.scedule(self.rounds,self.undo)
        self.t.s.scedule_during(0,self.rounds,self.tick)
        self.val = InputWindow("Weakness Factor", 1)
        self.t.str /= self.val
        self.t.dex /= self.val
        self.update()
        self.t.update()
    def undo(self):
        self.t.str *= self.val
        self.t.dex *= self.val
        self.t.update()
    def labelcont(self):
        return f"{self.name}: Duration: {self.rounds} rds, Weakness Factor: {self.val}"
    
class mana_drain(Status):
    name = "Mana-drain"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.rounds = InputWindow("Duration", 1)
        self.t.s.scedule(self.rounds,self.undo)
        self.t.s.scedule_during(0,self.rounds,self.tick)
        self.val = InputWindow("Weakness Factor", 1)
        self.t.man /= self.val
        self.update()
        self.t.update()
    def undo(self):
        self.t.man *= self.val
        self.t.update()
    def labelcont(self):
        return f"{self.name}: Duration: {self.rounds} rds, Drain Factor: {self.val}"
    
class bleeding(Status):
    name = "Bleeding"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.rounds = InputWindow("Duration", 1)
        self.t.s.scedule(self.rounds,self.undo)
        self.t.s.scedule_during(0,self.rounds,self.tick)
        self.val = InputWindow("Damage", 0)
        self.update()
        self.t.update()
    def tick(self):
        if super().tick():
            self.t.hp -= self.val
            self.t.update()
    def labelcont(self):
        return f"{self.name}: Duration: {self.rounds} rds, Damage: {self.val}"
    
class attack_drain(Status):
    name = "Attack Buff"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.rounds = InputWindow("Duration", 1)
        self.t.s.scedule(self.rounds,self.undo)
        self.t.s.scedule_during(0,self.rounds,self.tick)
        self.val = InputWindow("Buff", 0)
        self.t.dmgbuff += self.val
        self.update()
        self.t.update()
    def undo(self):
        self.t.dmgbuff -= self.val
        self.t.update()
    def labelcont(self):
        return f"{self.name}: Duration: {self.rounds} rds, Buff: {self.val}"
    
class attack_drain(Status):
    name = "Defense Buff"
    def __init__(self, tracker):
        super().__init__(tracker)
        self.rounds = InputWindow("Duration", 1)
        self.t.s.scedule(self.rounds,self.undo)
        self.t.s.scedule_during(0,self.rounds,self.tick)
        self.val = InputWindow("Buff", 0)
        self.t.sldbuff += self.val
        self.update()
        self.t.update()
    def undo(self):
        self.t.sldbuff -= self.val
        self.t.update()
    def labelcont(self):
        return f"{self.name}: Duration: {self.rounds} rds, Buff: {self.val}"
    