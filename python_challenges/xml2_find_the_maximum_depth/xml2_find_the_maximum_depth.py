import xml.etree.ElementTree as etree

#start
def find_depth(elem):
    if len(list(elem)) == 0:
        return 0
    else:
        return max([find_depth(c) for c in elem]) +1
#end
maxdepth = 0
def depth(elem, level):
    global maxdepth
    maxdepth = find_depth(elem)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)