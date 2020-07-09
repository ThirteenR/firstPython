import yaml


class conf:
    http = {}
    model = ''
    db = {}
    csv = {}

    def __init__(self, path):
        with open(path, "rb") as y:
            data = yaml.safe_load_all(y)
            self.http = list(data)[0]['http']
            self.model = list(data)[0]['model']
            self.db = list(data)[0]['db']
            self.csv = list(data)[0]['csv']


if __name__ == "__main__":
    conf("spider.yaml")
