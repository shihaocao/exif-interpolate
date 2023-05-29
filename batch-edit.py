from os import listdir
from os.path import isfile, join
import argparse
from PIL.ExifTags import TAGS
from PIL import Image
import piexif
import datetime
import concurrent.futures

def generate_exif_data(time_generator, num_files):
    exif_bytes_list = []
    for _ in range(num_files):
        exif_ifd = {
            piexif.ExifIFD.DateTimeOriginal: str(time_generator.get_next_time()),
        }
        exif_dict = {"Exif": exif_ifd}
        exif_bytes = piexif.dump(exif_dict)
        exif_bytes_list.append(exif_bytes)
    return exif_bytes_list

def process_file(file_name, mypath, exif_bytes):
    fn = mypath + file_name
    im = Image.open(fn)
    
    im.save(fn, exif=exif_bytes)
    print(f"Wrote to: {file_name}")

def main(args):
    # get the files
    mypath = args["input"]
    input_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    num_files = len(input_files)
    
    # construct time generator
    time_generator = TimeGenerator(int(args['start_yr']), int(args['end_yr']), num_items=num_files)

    if args['fb_sort']:
        input_files = sorted(input_files, key=lambda x: int(x.split('_')[0]))

    exif_bytes_list = generate_exif_data(time_generator, num_files)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        file_futures = []
        for file_name, exif_bytes in zip(input_files, exif_bytes_list):
            file_futures.append(executor.submit(process_file, file_name, mypath, exif_bytes))

        for future in concurrent.futures.as_completed(file_futures):
            future.result()

class TimeGenerator:
    def __init__(self, start_year, end_year, num_items):
        # Jan 01, start_year
        self._my_time = datetime.datetime(start_year, 5, 28, hour=4)
        self._end_time = datetime.datetime(start_year, 5, 28, hour=6)
        
        # Used to increment time
        self._time_incr = (self._end_time - self._my_time) / num_items

    def get_next_time(self):
        ret = self._my_time
        self._my_time = self._my_time + self._time_incr
        return ret

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='provide arguments for batch convert')
    parser.add_argument('--input', help='input dir, please use absolute, with trailing slash', default="./input/")
    parser.add_argument('--mutate', help='If true, it will modify the exif data in place', default=True)
    parser.add_argument('--start-yr', help='Start year, inclusive', default=2015)
    parser.add_argument('--end-yr', help='End year, inclusive', default=2020)
    parser.add_argument('--fb-sort', help='Assuming images are named Facebook-wise', action='store_true')

    args = vars(parser.parse_args())
    print(args)
    
    main(args)
