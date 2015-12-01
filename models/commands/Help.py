from Command import Command



class Help(Command):
    title = "help"


    def execute(self):
        output = "Available commands:\n"

        cmd_cls_list = self._get_commands_cls()

        for cmd_cls in cmd_cls_list:
            params = cmd_cls.__init__.func_code.co_varnames[2:]
            output += "{0} {1}\n".format(
                cmd_cls.title,
                " ".join(
                    "[%s]" % p.upper()
                    for p in params
                )
            )

        return output
