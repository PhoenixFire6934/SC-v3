from lib.decompression import SCv3Decompressor
from lib.compression import SCv3Compressor

def runTool(userOption, inputFile, outputFile):
    data = open(inputFile, 'rb').read()

    if userOption == '1':
        SCv3Decompressor(data).setupDecompression(outputFile)

    elif userOption == '2':
        SCv3Compressor(data).setupCompression(outputFile)

    else:
        print(f"Unexpected option: {userOption}")


if __name__ == '__main__':
    userOption = input("1 - Decompress\n2 - Compress\n\nEnter your option: ")
    inputFile  = input("Enter filename: ")
    outputFile = input("Enter output filename: ")

    runTool(userOption, inputFile, outputFile)