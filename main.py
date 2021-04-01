from lib.decompress import SCv3Decompressor

inputFile  = input("Enter filename: ")
outputFile = input("Enter output filename: ")

with open(inputFile, 'rb') as f:
    data = f.read()

    decompressor = SCv3Decompressor(data)
    decompressor.setup(outputFile)