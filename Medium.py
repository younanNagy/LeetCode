
#6. Zigzag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows=[""]*numRows
        current_row=0
        direction="down"
        if numRows==1:
            return s
        for char_ in s:
            rows[current_row]+=char_
            if direction=="down":
                current_row=current_row+1
            else:
                current_row=current_row-1
                
            if current_row==numRows and direction=="down":
                direction="up"
                current_row=current_row-2
            elif current_row==-1 and direction=="up":
                direction="down"
                current_row=current_row+2
        result=""
        for row in rows:
            result+=row
        return result

  
# 12. Integer to Roman
    
class Solution:
    def intToRoman(self, num: int) -> str:
        latin_mapping={
            1000:"M",   
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I"
        }
        result=""
        number_of_latin=0
        for number in latin_mapping.items():
            value=number[0]
            number_of_latin=num//value
            
            result+=(number[1]*number_of_latin)   
            num=num%number[0]
            
        return result  
            
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validateNode(root:TreeNode,stack_):

    if not root:
        return stack_
    

    else:
        #left
        stack_=validateNode(root.left,stack_)
        top=stack_.pop()
        if top=="notValid":
            stack_.append(top)
            return stack_
        
        if top>=root.val:
            stack_.append("notValid")
            return stack_
        
        stack_.append(root.val)
        stack_=validateNode(root.right,stack_)

        return stack_

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack_=validateNode(root,[float(-inf)])
            
        return stack_.pop()!="notValid" 
        

        
        
#  99. Recover Binary Search Tree
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


        
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        def recover(root:TreeNode,left_b,right_b,root_ori,left_ori,right_ori):
            if not root:
                return
            if root.val<left_b.val:
                root.val,left_b.val=left_b.val,root.val
                root=root_ori
                left_b=left_ori
                right_b=right_ori
            elif root.val>right_b.val:
                root.val,right_b.val=right_b.val,root.val
                root=root_ori
                left_b=left_ori
                right_b=right_ori
        
            recover(root.left,left_b,root,root_ori,left_ori,right_ori)
            recover(root.right,root,right_b,root_ori,left_ori,right_ori)
            
        left_=TreeNode(val=float("-inf"))
        right_=TreeNode(val=float("inf"))
        recover(root,left_,right_,root,left_,right_)
   



# 146. LRU Cache
class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity_=capacity
        self.age=0
        self.aged_nodes=PriorityQueue()
    
    def get(self, key: int) -> int:
        value=self.cache.get(key)
        if value is None:
            return -1
        self.age=self.age+1
        self.cache[key][1]=self.age
        return self.cache[key][0]

    def removeLeastRecentlyUsed(self):
        min_age=float("inf")
        min_key=-1
        for key,age in self.cache.items():
            if age[1]<min_age:
                min_key=key
                min_age=age[1]
        
        if min_key!=-1:
            self.cache.pop(min_key)
        
    def put(self, key: int, value: int) -> None:
        if len(self.cache)==self.capacity_ and self.cache.get(key)is None:
            self.removeLeastRecentlyUsed()
        
        self.age=self.age+1
        self.cache[key]=[value,self.age]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
