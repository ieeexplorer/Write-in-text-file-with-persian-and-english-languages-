try:
    f = open("test.txt",'w',encoding = 'utf-8')
    # perform file operations
 
    f.write("this is a writing test in 2 languages  این یک تست نوشتن به دو زبان می باشد!")
    f.close()
    
    #open and read the file after the appending:
    f = open("test.txt", "r")
    print(f.read())
   
finally:
   f.close()