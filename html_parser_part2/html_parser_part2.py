from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    #start
    def handle_comment(self, data):
        line = 'Multi-line' if '\n' in data else 'Single-line' 
        print(f'>>> {line} Comment')
        print(data)
          
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)        
    #end
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()