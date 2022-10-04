#! /usr/bin/python

import sys
import requests as r
import os
import wget
import argparse as ap

def main(args):
    base_url = "https://i.4cdn.org/{0}/".format(args.board)                                # 4chan image url formatted with user specified board
    req_url = "https://a.4cdn.org/{0}/thread/{1}.json".format(args.board, args.thread)
    req = r.get(req_url)                                                                   # 4chan api url, formateed with user specified board and thread
    fn_list = valid_urls([[args.width],[args.height]], req.json()['posts'], args.ratio)    # uses valid_urls to create a dict of image files and filenames
    count = 1                                                                              # Initialize counter

    if not os.path.isdir(args.output):                                                     # Checks if output directory exists and creates it if not
        os.makedirs(args.output)

    for fn in fn_list:                                                                     # loops throuch all the dictionary keys
        url = os.path.join(base_url, fn)                                                   # Creates the 4chan image url
        out = os.path.join(args.output, fn_list[fn])                                       # Creates the output url
        print("{0}/{1} : {2}".format(count, len(fn_list), fn_list[fn]))                    # Prints a counter of current image and images left as well as the filename
        wget.download(url, out)                                                            # Downloads the image to output directory
        print("\n")
        count+=1

# Iterates through json results of request and depending on the filters
# returns a list of valid picture filenames
def valid_urls(res, json, aspect_ratio):
    urls = {}
    ar = False
    if aspect_ratio != 0:                       # determines if aspect ratio is specified by user
        ar = True                               # sets ar to True
        aspect_ratio = aspect_ratio.split(":")  # splits aspect ratio into an array  of two parts

    for post in json:
        if 'filename' in post.keys():                                                           # Determines if there is a picture in the post
            if not ar:                                                                          # If aspect ratio isn't specified
                if len(res) > 0 and (post['w'] in res[0]) and (post['h'] in res[1]):            # If height and width matches user
                    urls[str(post["tim"]) + post["ext"]] = post["filename"] + post["ext"]       # Add file key to dict with filename as the value
                elif res[0][0] == 0 and res[1][0] == 0:                                         # If resolution isn't specified
                    urls[str(post["tim"]) + post["ext"]] = post["filename"] + post["ext"]       # Add file key to dict with filename as the value
            else:
                if int(aspect_ratio[0]) / int(aspect_ratio[1]) == post['w'] / post['h']:        # Image aspect ratio matches user defined one
                    urls[str(post["tim"]) + post["ext"]] = post["filename"] + post["ext"]       # Add file key to dict with filename as the value

    return urls

if __name__ == "__main__":
    parser = ap.ArgumentParser(description="Take arguments")
    parser.add_argument("-t", "--thread",
            help="Url of the thread you want to download",
            required=True )
    parser.add_argument("-b", "--board",
            help="enter the board the thread is on",
            required=True)
    parser.add_argument("-H", "--height",
            type=int,
            help="Height of the resolution you want",
            default=0)
    parser.add_argument("-W", "--width",
            type=int,
            help="width of the resolution you want",
            default=0)
    parser.add_argument("-o", "--output",
            help="directory to output the pictures",
            default=os.path.join(os.path.expanduser("~"), "Pictures/chan/"))
    parser.add_argument("-r", "--ratio",
            help="Select ratio of the image you need. Eg, 16:10",
            default=0)
    args = parser.parse_args()
    main(args)
