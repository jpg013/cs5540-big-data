import json
import re

myfile = open("tweets_output.txt")
text = myfile.read()
#urls =re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
urls = re.findall("((www\.|http://|https://)(www\.)*.*?(?=(www\.|http://|https://|$)))", text)
#print urls
urlsfile = open("urls_output.txt", "a")
urlsfile.write('\n'.join(str(i) for i in urls))
urlsfile.close()

