# class Hash:
#     table = []
#
#     def __init__(self, key=None, value=None):
#         if key is None and value is None:
#             self.table = []
#         else:
#             self.key = key
#             self.value = value
#
#     def get_key(self):
#         return self.key
#
#     def set_key(self, new_key):
#         self.key = new_key
#
#     def get_value(self):
#         return self.value
#
#     def set_value(self, new_value):
#         self.value = new_value
#
#     def add_item(self, element):
#         self.table.append(element)
#
#     def output(self):
#         for e in self.table:
#             print("Key - " + str(e.get_key()) + "; Value - " + str(e.get_value()))
#
#     def find_by_key(self, key):
#         for e in self.table:
#             if e.get_key() == key:
#                 print("Key - " + str(e.get_key()) + "; Value - "
#                       + str(e.get_value()))
#
#     def find_by_value(self, value):
#         for e in self.table:
#             if e.get_value() == value:
#                 print("Key - " + str(e.get_key()) + "; Value - "
#                       + str(e.get_value()))
#     # def change_key(self, value):
#     #     self.
#     #
#     # def remove_value(self, value):
#     #     self.table.remove(index)
#
#
# table = Hash()
# table.add_item(Hash(12, 3))
# table.add_item(Hash(14, 2))
# table.add_item(Hash(15, 1))
# table.add_item(Hash('df', "sdf5"))
# table.output()
# for qwe in table:
#     print(qwe)
# print("")
# table.find_by_key(12)
# table.find_by_value("sdf5")


class Dictionary:
    def __init__(self, dict_list=None):
        if dict_list:
            self.dict_list = dict_list
        else:
            self.dict_list = []

    def __str__(self):
        return str(self.dict_list)

    def __getitem__(self, item):
        for e in self.dict_list:
            if e[0] == item:
                return e[1]
        raise KeyError

    def __setitem__(self, key, value):
        for e in self.dict_list:
            if e[0] == key:
                self.dict_list.remove(e)
                self.dict_list.append((key, value))
                return
        self.dict_list.append((key, value))

    def __delitem__(self, key):
        for e in self.dict_list:
            if e[0] == key:
                self.dict_list.remove(e)
                return
        raise KeyError

    def size(self):
        return len(self.dict_list)


def main():
    a = Dictionary()
    a[1] = 'Ok'
    a[2] = 'q'
    a[1] = 0
    a[7] = 'p'
    a[10] = 1
    a[0] = 5
    a[3] = 2
    a['asd'] = 123
    print(a.size())
    print(a)
    print(a[8])
    b = Dictionary()
    print(b)


if __name__ == '__main__':
    main()
