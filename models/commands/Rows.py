from Command import Command



class Rows(Command):
    title = "rows"


    def __init__(self, pass_storage, search=None):
        super(Rows, self).__init__(pass_storage)
        self._search = search


    def execute(self):
        rows = filter(
            lambda row: self._search is None or self._search in row,
            self._pass_storage.rows()
        )

        if rows:
            output = ""

            for title in rows:
                output += "%s\n" % title
                keys = self._pass_storage.keys(title)
                for key in keys:
                    if "pass" in key.lower():
                        value = "********"
                    else:
                        value = self._pass_storage.value(title, key)
                    output += "%+16s    %-32s\n" % (key, value)
                output += "\n"

            return output

        else:
            return "No rows found."
