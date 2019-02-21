import json
import re

myfile = open("tweets_output.txt")
text = myfile.read()
pat = re.compile(r"#(\w+)")
hashes =  pat.findall(text)

hashtags = open('hashtags_output.txt', 'a')
hashtags.write('\n'.join(hashes))
hashtags.close()

