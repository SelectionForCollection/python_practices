class Hash:
    table = []

    def __init__(self, key=None, value=None):
        if key is None and value is None:
            self.table = []
        else:
            self.key = key
            self.value = value

    def get_key(self):
        return self.key

    def set_key(self, new_key):
        self.key = new_key

    def get_value(self):
        return self.value

    def get_by_index(self, item):
        return self.table.__getitem__(item)

    def get_size(self):
        return len(self.table)

    def get_obj(self, index):
        return self.table.__getitem__(index)

    def set_value(self, new_value):
        self.value = new_value

    def add_item(self, element):
        self.table.append(element)

    def output(self):
        for e in self.table:
            print("Key - " + str(e.get_key()) + "; Value - " + str(e.get_value()))

    def find_by_key(self, key):
        for e in self.table:
            if e.get_key() == key:
                print("Key - " + str(e.get_key()) + "; Value - "
                      + str(e.get_value()))

    def find_by_value(self, value):
        for e in self.table:
            if e.get_value() == value:
                print("Key - " + str(e.get_key()) + "; Value - "
                      + str(e.get_value()))

    def change_key(self, element, new_key):
        for e in self.table:
            if element.get_value() == e.get_value():
                e.set_key(new_key)

    def change_value(self, element, new_value):
        for e in self.table:
            if element.get_key() == e.get_key():
                e.set_value(new_value)

    def remove_item(self, index):
        self.table.remove(index)


table = Hash()
table.add_item(Hash(12, 3))
table.add_item(Hash(14, 2))
table.add_item(Hash(15, 1))
table.add_item(Hash('df', "sdf5"))
table.output()
table.remove_item(table.get_obj(0))
print("")
table.output()
print("")
for i in range(0, table.get_size()):
    print(table.get_by_index(i).get_value())
print("")

table.find_by_key(12)
table.find_by_value("sdf5")
