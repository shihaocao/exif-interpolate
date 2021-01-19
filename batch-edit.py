from os import listdir
from os.path import isfile, join
import argparse
import exif

def main(args):
    mypath = args["input"]
    
    input_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    input
    for file_name in input_files:
        with open(mypath+file_name, 'rb') as image_file:
            if file_name.endswith('.mp4'):
                print("mp4 rip")
            elif file_name.endswith('.jpg'):
                unpacked = exif.Image(image_file)
                print(unpacked.has_exif)
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='provide arguments for batch convert')

    parser.add_argument('--input', help='input dir, please use absolute, with trailing slash', default="./input/")
    parser.add_argument('--mutate', help='If true, it will modify the exif data in place', default=True)

    args = vars(parser.parse_args())
    
    main(args)
