import hashlib
from Crypto.Cipher import AES
from Crypto import Random



class AESCipher:
    BS = 32


    def __init__(self, key):
        self._key = hashlib.sha256(key.encode()).digest()


    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self._key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(raw)


    def decrypt(self, enc):
        iv = enc[:AES.block_size]
        cipher = AES.new(self._key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode("utf8")


    def _pad(self, s):
        return s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)


    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
