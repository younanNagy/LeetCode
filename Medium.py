
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
            
            
            

           
