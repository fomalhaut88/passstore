from Command import Command



class Remove(Command):
    title = "remove"


    def __init__(self, pass_storage, title):
        super(Remove, self).__init__(pass_storage)
        self._title = title


    def execute(self):
        ok = self._pass_storage.remove(self._title)
        if ok:
            return "Row {0} has been removed successfully.".format(self._title)
        else:
            return  "Can't remove the row {0}. Row {0} doesn't exist.".format(self._title)
