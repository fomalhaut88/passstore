from Command import Command



class Delkey(Command):
    title = "delkey"


    def __init__(self, pass_storage, title, key):
        super(Delkey, self).__init__(pass_storage)
        self._title = title
        self._key = key


    def execute(self):
        ok = self._pass_storage.delkey(self._title, self._key)

        if ok:
            return "The key has been removed."
        else:
            return "The key not found."
