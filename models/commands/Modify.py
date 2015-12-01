from Command import Command



class Modify(Command):
    title = "modify"


    def __init__(self, pass_storage, title, key, value):
        super(Modify, self).__init__(pass_storage)
        self._title = title
        self._key = key
        self._value = value


    def execute(self):
        ok = self._pass_storage.modify(self._title, self._key, self._value)
        if ok:
            return "Row {0} has been modified successfully.".format(self._title)
        else:
            return  "Can't modify the row {0}. Row {0} doesn't exist.".format(self._title)
