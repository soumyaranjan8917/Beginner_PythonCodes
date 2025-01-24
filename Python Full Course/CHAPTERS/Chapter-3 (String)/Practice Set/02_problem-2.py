# Write a program ro fill in a letter given below with name & date.
# /*letter = '''
#         Dear <|Name|>,
#         You are selected!
#         <|Date|>
#         ''' 


letter = ''' Dear <|Name|>,
        You are selected!
        <|Date|>
        ''' 

print(letter.replace("<|Name|>", "Soumya").replace("<|Date|>", " 01 December"))
#  Chaining Process