from os import listdir
from os.path import isfile, join
import argparse
from PIL.ExifTags import TAGS
from PIL import Image
import piexif
import datetime

def main(args):

    # get the files
    mypath = args["input"]
    input_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    num_files = len(input_files)    
    
    # construct time generator
    time_generator = TimeGenerator(int(args['start_yr']),int(args['end_yr']), num_items = num_files)

    if args['fb_sort']:
        input_files = sorted(input_files, key = lambda x: int(x.split('_')[0]))

    for file_name in input_files:
        print(file_name)
        
        fn = mypath+file_name
        im = Image.open(fn)
        
        # generate exif
        exif_ifd = {
            
            # call to time_generator
            piexif.ExifIFD.DateTimeOriginal: str(time_generator.get_next_time()),
            }

        exif_dict = {"Exif":exif_ifd}
        exif_bytes = piexif.dump(exif_dict)
        
        im.save(fn, exif=exif_bytes)

class TimeGenerator:
    def __init__(self, start_year, end_year, num_items):
        # Jan 01, start_year
        self._my_time = datetime.datetime(start_year, 1,1)
        self._end_time = datetime.datetime(end_year+1, 1,1)
        
        # Used to increment time
        self._time_incr = (self._end_time - self._my_time)/num_items

    def get_next_time(self):
        '''
        return the time
        then increment it up
        '''
        ret = self._my_time
        self._my_time = self._my_time + self._time_incr
        return ret

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='provide arguments for batch convert')

    parser.add_argument('--input', help='input dir, please use absolute, with trailing slash', default="./input/")
    parser.add_argument('--mutate', help='If true, it will modify the exif data in place', default=True)
    parser.add_argument('--start-yr', help='Start year, inclusive', default=2015)
    parser.add_argument('--end-yr', help='End year, inclusive', default=2020)
    parser.add_argument('--fb-sort', help='Assuming images are named facebook wise', default=True)

    args = vars(parser.parse_args())
    print(args)
    
    main(args)
