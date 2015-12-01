from Command import Command



class Add(Command):
    title = "add"


    def __init__(self, pass_storage, title):
        super(Add, self).__init__(pass_storage)
        self._title = title


    def execute(self):
        ok = self._pass_storage.add(self._title)
        if ok:
            return "Row {0} has been added successfully.".format(self._title)
        else:
            return  "Can't add the row {0}. Row {0} already exists.".format(self._title)
