import struct
from hashlib import md5
from zstandard import compress

class SCv3Compressor():
    def __init__(self, data):
        self.data = data

    def compressSC(self):
        try:
            self.compressedData = compress(self.data)
            print("\nSuccessfully compressed your data!")
        except Exception as e:
            print(e)

        self.format = b'SC'
        self.version = struct.pack('>I', 3)
        self.md5Hash = md5(self.compressedData).digest()
        self.md5HashLength = struct.pack('>I', len(self.md5Hash))

        print(f"\nFILE INFO:\n\nFormat: {self.format}\nVersion: {int.from_bytes(self.version, byteorder='big')}\nMD5: {self.md5Hash.hex()}\n")

        self.header = self.format + self.version + self.md5HashLength + self.md5Hash
        self.data = self.header + self.compressedData

        return self.data


    def setupCompression(self, filename):
        self.compressedData = self.compressSC()

        self.outFile = open(filename, 'wb')
        self.outFile.write(self.compressedData)
        self.outFile.close()
