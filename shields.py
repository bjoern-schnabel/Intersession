from items import Shield

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
