class Block:
    type = "default"
    breakable = True
    transparent = False
    collectable = True

    def __init__(self, t):
        self.changeType(t)

    def update(self):
        if self.type == "bedrock":
            self.breakable = False
        if self.type == "sky" or self.type == "water":
            self.transparent = True
        if self.type == "sky" or self.type == "leaves" or self.type == "bedrock" or self.type == "water" \
                or self.type == "grass":
            self.collectable = False

    def changeType(self, t):
        self.type = t
        self.update()
