import os
import readline # it's necessary to make raw_input interactive
from getpass import getpass

from commands import Command, Exit
from models.errors import BaseError
from PassStorage import PassStorage



class ConsoleInterface(object):
    prompt = ">"

    path = os.path.join(
        os.path.expanduser("~"),
        ".passstorage",
        "storage"
    )


    def __init__(self):
        self._pass_storage = None
        password = None

        if not os.path.exists(self.path):
            dirname = os.path.dirname(self.path)
            if not os.path.exists(dirname):
                os.mkdir(dirname)

            print "Storage doesn't exist."
            while True:
                print "Please, enter a password for new storage."
                password1 = getpass()
                print "Repeat your password."
                password2 = getpass()

                if password1 == password2:
                    password = password1
                    break

                else:
                    print "Entered passwords are not identical. Try again."

        while True:
            try:
                if password is None:
                    password = getpass()

                self._pass_storage = PassStorage(self.path, password)

                break

            except Exception as exc:
                if str(exc) == "Invalid password":
                    print "Invalid password. Try again."
                    password = None

                else:
                    raise exc

    def run(self):
        while True:
            try:
                query = raw_input(self.prompt + " ").strip()

                if query:
                    command = Command.create(self._pass_storage, query)

                    if isinstance(command, Exit):
                        break

                    output = command.execute()

                    print output

            except BaseError as exc:
                print "Error:", exc.__class__.__name__
