from Command import Command



class Value(Command):
    title = "value"


    def __init__(self, pass_storage, title, key):
        super(Value, self).__init__(pass_storage)
        self._title = title
        self._key = key


    def execute(self):
        value = self._pass_storage.value(self._title, self._key)
        return value
