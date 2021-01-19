# exif-interpolate
A project to batch edit exif data interpolated over a date range - To give order Google Photos uploads

Tested working on Python 3.8.5
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
python3 batch-edit.py --input ~/FB/JP2
```