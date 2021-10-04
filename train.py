class Train:
    def __init__(self, train_id, name, bogies, source, destination):
        self.train_id = train_id
        self.name = name
        self.bogies = bogies
        self.source = source
        self.destination = destination

    def get_name(self):
        return self.name

    def get_bogies(self):
        return self.bogies

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination
