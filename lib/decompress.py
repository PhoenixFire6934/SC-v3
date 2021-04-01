from zstandard import decompress

class SCv3Decompressor():
    def __init__(self, data):
        self.data = data


    def decompressSC(self):
        self.format = self.data[:2]
        self.data = self.data[2:]

        self.version = int.from_bytes(self.data[:4], byteorder='big')
        self.data = self.data[4:]

        self.md5HashLength = int.from_bytes(self.data[:4], byteorder='big')
        self.data = self.data[4:]

        self.md5Hash = self.data[:self.md5HashLength].hex()
        self.data = self.data[self.md5HashLength:]

        print(f"\nFILE INFO:\n\nFormat: {self.format}\nVersion: {self.version}\nMD5: {self.md5Hash}\n")

        try:
            self.decompressedData = decompress(self.data)
            print("Successfully decompressed your data!")
        except Exception as e:
            print(e)

        return self.decompressedData



    def setup(self, filename):
        self.decompressedData = self.decompressSC()

        self.outFile = open(filename, 'wb')
        self.outFile.write(self.decompressedData)
        self.outFile.close()