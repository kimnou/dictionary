## Python: Print a dictionary line by line
## students={'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
## Sample Output:
## Aex                                                                                                           
## class : V                                                                                                     
## rolld_id : 2                                                                                                  
## Puja                                                                                                          
## class : V                                                                                                     
## roll_id : 3 


dict={'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for i in dict:
    print(i)
    for j in dict[i]:
        print(j,':',dict[i][j])






