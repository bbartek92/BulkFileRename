import logic_layer

class Printer:
    def __init__(self, path, mode, ext):
        self.changer = logic_layer.Changer(path, mode, ext)

    def print_proposition(self):
        self.matches =  self.changer.get_matches()
        for match in self.matches:
            print(match, 'renamed to: ', self.matches[match])

    def change(self):
        self.changer.commit()