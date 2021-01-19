# exif-interpolate
A project to batch edit exif data interpolated over a date range - To give order Google Photos uploads

Tested working on Python 3.8.5.

It is able to set exif data, even if the exif data block doesn't exist. Create for adding exif data to
Facebook chat images.
### PRE-OPS

I used `mogrify` to change all png files to jpg files just to simplify things. This package should be available via
```
sudo apt-get install imagemagick
```

### INSTALL

Use a virtualenv if you want:
```
python3 -m venv venv
. venv/bin/activate
```

Install libraries:
```
pip install -r requirements.txt
```

### RUN

Example: 

```
python3 batch-edit.py --input ~/FB/JP3/ --start-yr 2017 --end-yr 2020
```

### ISSUES

Only supports sorting assuming the first part of the string name before the first `_`
is a sorting key. Useful for sorting images downloaded from Facebook chats

Only modifies images in place.

Some of the options in arg parse don't really do anything if they're not the output values, sorry haha