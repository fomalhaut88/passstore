from Command import Command


class ChangePass(Command):
    title = "changepass"


    def __init__(self, pass_storage, oldpass, newpass):
        super(ChangePass, self).__init__(pass_storage)
        self._oldpass = oldpass
        self._newpass = newpass


    def execute(self):
        ok = self._pass_storage.changepass(self._oldpass, self._newpass)
        if ok:
            return "The password has been changed."
        else:
            return "Invalid old password."
