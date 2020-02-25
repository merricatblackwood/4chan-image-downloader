import sys
import requests as r
import os
import wget
import argparse as ap

def main(args):

    base_url = "https://i.4cdn.org/{0}/".format(args.board)
    req = r.get("https://a.4cdn.org/{0}/thread/{1}.json".format(args.board,
        args.thread))
    fn_list = valid_urls([[args.width],[args.height]], req.json()['posts'], args.ratio)
    count = 1
    if not os.path.isdir(args.output):
        os.makedirs(args.output)
    for fn in fn_list:
        url = os.path.join(base_url, fn)
        out = os.path.join(args.output, fn_list[fn])
        print("{0}/{1} : {2}".format(count, len(fn_list), fn_list[fn]))
        wget.download(url, out)
        print("\n")
        count+=1

def valid_urls(res, json, aspect_ratio):
    urls = {}
    for post in json:
        if 'filename' in post.keys():
            if aspect_ratio == 0:
                if len(res) > 0 and (post['w'] in res[0]) and (post['h'] in res[1]):
                    urls[str(post["tim"]) + post["ext"]] = \
                            post["filename"] + post["ext"]
                elif res[0][0] == 0 and res[1][0] == 0:
                    urls[str(post["tim"]) + post["ext"]] = \
                            post["filename"] + post["ext"]
            else:
                aspect_ratio = aspect_ratio.split("/")
                if aspect_ratio[0] / aspect_ratio[1] == post['w'] / post['h']:
                    urls[str(post["tim"]) + post["ext"]] = \
                            post["filename"] + post["ext"]
                    

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
            help="Select ratio of the image you need"
            default=0)
    args = parser.parse_args()
    main(args)
