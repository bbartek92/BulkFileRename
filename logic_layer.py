import os
import re

class Changer:
    def __init__(self, path, mode, ext):
        self.path = path
        self.mode = mode
        self.ext = ext
        self.matches = {}
        self.counter = 0

    def get_matches(self):
        content = os.listdir(self.path)
        for i in content:
            if os.path.isfile(os.path.join(self.path, i)):
                if re.match(self.ext, i):
                    self.matches[i] = self.change(i)
        return self.matches

    def change(self, name):
        self.counter += 1
        name, ext = os.path.splitext(name)
        if self.mode == 'lower':
            return name.lower() + ext
        elif self.mode == 'upper':
            return name.upper() + ext
        else:
            if re.match('.*0{3}.*', self.mode):
                parts = re.split('0{3}', self.mode)
                if len(parts) != 1:
                    return '{:03d}'.format(self.counter).join(parts) + ext
                else:
                    return parts[0] + '{:03d}'.format(self.counter) + ext
            else:
                return self.mode + '{:03d}'.format(self.counter) + ext

    def commit(self):
        for match in self.matches:
            os.rename(os.path.join(self.path, match),
                      os.path.join(self.path, self.matches[match]))