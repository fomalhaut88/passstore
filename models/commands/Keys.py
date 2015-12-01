from Command import Command



class Keys(Command):
    title = "keys"


    def __init__(self, pass_storage, title):
        super(Keys, self).__init__(pass_storage)
        self._title = title


    def execute(self):
        keys = self._pass_storage.keys(self._title)
        if keys:
            return "\n".join(keys)
        else:
            return "No keys found."
