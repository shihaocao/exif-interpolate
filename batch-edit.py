from os import listdir
from os.path import isfile, join
import argparse

def main(args):
    mypath = args["input"]
    
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(onlyfiles)
    print(args['mutate'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='provide arguments for batch convert')

    # agent parameters
    parser.add_argument('--input', help='input dir', default="./input/")
    parser.add_argument('--mutate', help='If true, it will modify the exif data in place', default=True)

    args = vars(parser.parse_args())
    
    main(args)
