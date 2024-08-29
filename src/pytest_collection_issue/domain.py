
class Will(object):
    def real_property(self):
        return ["the family home"]

class Testament(object):
    def __init__(self):
        super().__init__()
        self.collections = ["stamp", "coin"]

    def personal_property(self):
        return [f"my {x} collection" for x in self.collections]