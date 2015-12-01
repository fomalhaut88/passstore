import os
import json

from AESCipher import AESCipher



class PassStorage(object):
    def __init__(self, path, password):
        self._path = path
        self._password = password
        self._cipher = AESCipher(self._password)
        self._data = {}

        try:
            self.load()

        except (UnicodeDecodeError, ValueError):
            raise Exception("Invalid password")


    def load(self):
        if os.path.exists(self._path):
            with open(self._path, "rb") as f:
                encrypted = f.read()
                js_data = self._cipher.decrypt(encrypted)
                self._data = json.loads(js_data)
        else:
            self.save()


    def save(self):
        with open(self._path, "wb") as f:
            js_data = json.dumps(self._data)
            encrypted = self._cipher.encrypt(js_data)
            f.write(encrypted)


    def changepass(self, oldpass, newpass):
        if oldpass == self._password:
            self._password = newpass
            self._cipher = AESCipher(self._password)
            self.save()
            return True

        else:
            return False


    def rows(self):
        return self._data.keys()


    def add(self, title):
        if title not in self._data:
            self._data[title] = {}
            self.save()
            return True
        else:
            return False


    def remove(self, title):
        if title in self._data:
            del self._data[title]
            self.save()
            return True
        else:
            return False


    def modify(self, title, key, value):
        if title in self._data:
            self._data[title][key] = value
            self.save()
            return True
        else:
            return False


    def delkey(self, title, key):
        if title in self._data and key in self._data[title]:
            del self._data[title][key]
            return True
        else:
            return False


    def keys(self, title):
        return self._data[title].keys()


    def value(self, title, key):
        return self._data[title][key]
