# 4chan-image-downloader
A 4chan image downloader which downloads all images in a thread. Images can be filtered by height x width or by ratio ( e.g 16:9 ). 
I mainly only use it for wallpapers.

## Dependencies

wget
requests
argparse

## usage
~~~~
usage: main.py [-h] -t THREAD -b BOARD [-H HEIGHT] [-W WIDTH] [-o OUTPUT]

Take arguments

optional arguments:
  -h, --help            show this help message and exit
  -t THREAD, --thread THREAD
                        Url of the thread you want to download
  -b BOARD, --board BOARD
                        enter the board the thread is on
  -H HEIGHT, --height HEIGHT
                        Height of the resolution you want
  -W WIDTH, --width WIDTH
                        width of the resolution you want
  -o OUTPUT, --output OUTPUT
                        directory to output the pictures
  -r RATIO, --ratio RATIO
                        Select ratio of the image you need. Eg, 16:10

~~~~
