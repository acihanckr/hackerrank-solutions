#start
from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for att, value in attrs:
            value = value if value else 'None'
            print('-> ' + att + ' > ' + value)
            
    def handle_endtag(self, tag):
        pass
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for att, value in attrs:
            value = value if value else 'None'
            print('-> ' + att + ' > ' + value)
            
n = int(input())
html_text = ''

for _ in range(n):
    html_text +=input()+'\n'
parser = MyHTMLParser()
parser.feed(html_text)
#end