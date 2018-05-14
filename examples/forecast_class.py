class Forecast:
    def __init__(self):
        self.info = {}

    def add(self, json,  path, key):
        a = json
        for i in path:
            a = a[i]
        if key not in self.info:
            self.info[key] = [a]
        else:
            self.info[key] += [a]

    def close(self):
        for i in self.info:
            self.info[i] = sum(self.info[i])/len(self.info[i])

    def __str__(self):
        return str(self.info)
