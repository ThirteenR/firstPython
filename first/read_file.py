class read_file:
    lines = ""

    def __init__(self, path):
        print("init")
        with open(path,"r+") as f:
            ll = f.readlines()
            self.lines = ll

    def get_lines(self):
        return self.lines