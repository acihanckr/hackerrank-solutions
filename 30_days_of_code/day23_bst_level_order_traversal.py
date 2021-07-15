import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #start
        data_list = []
        node_list = [root]
        while len(node_list)>0:
            data_list += [node.data for node in node_list]
            new_node_list = []
            for node in node_list:
                if node.left: new_node_list.append(node.left)
                if node.right: new_node_list.append(node.right)
            node_list = new_node_list
        print(' '.join(map(str,data_list)))
        #end

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
