# exif-interpolate
A project to batch edit exif data interpolated over a date range - To give order Google Photos uploads

## Use Case (Exact Only)
When you download an archive of images from Facebook through the user data access portal, it gives you 
a bunch of images without Exif data. This means if you upload them to GooglePhotos, you are at the mercy of the upload
order to order your photos. 

To remedy this, I created this tool which sets a datetime string within an Exif data block such that
when the phots are uploaded to GooglePhotos, atleast they will be in order.

The reference order assumes that the first substring (before the first underscore) is a total ordering
that represents the order in which photos are uploaded to the Facebook servers, which serve as a pseudo 
reference for when they were taken.

## Notes

It will not write to ExifData to mp4's but I think Facebook does not wipe the Exif data block of mp4's ...?

Tested working on Python 3.8.5.

It is able to set exif data, even if the exif data block doesn't exist. Create for adding exif data to
Facebook chat images.

### PRE-OPS

I used `mogrify` to change all png files to jpg files just to simplify things. This package should be available via
```
sudo apt-get install imagemagick
mogrify -format jpg *.png
```

### FB DOWNLOAD

Go into your user account data on facebook, and request a data download of all your phots and messages.
The messages are the important one. If you have a lot of photos/messages, it might generate multiple zip files to
download. Extract them all. Here's an example command that I use to retrieve photos from a particular folder.
The purpose of this is to collect all the FB images into one folder. I have no idea how FB splits images into particular folders,
but the idea is you need to merge them into one target folder.
```
cp facebook-shihaocao5.4/messages/inbox/hammockhomies_kvox9tyodg/photos/* homies/
```

Here's a helpful command to list out the number of items in a folder that end in .jpg
```
ls -1 *.jpg | wc -l
```

This is how you delete all files that end in `.png`
```
rm *.png
```

Then within your collected folder make sure to change all png's to jpgs if needed, and delete the old pngs
too. Now your can use the included script to `exif-interpolate` things.

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