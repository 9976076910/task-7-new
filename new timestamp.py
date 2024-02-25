import datetime 
  
# to get  date & time
# current date as f_name. 
f_name = datetime.datetime.now() 
  
# creating empty file 
def create_file(): 

    with open(f_name.strftime("%d %B %Y")+".txt", "w") as file: 
        file.write("3rd febrary 2024") 
  
# Driver Code 
create_file() 
