import re 

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

    matches = pattern.finditer(contents) # will return multiple we can use sub()
   # matches = pattern.findall(contents) # only gruops/ multiple group in tuples
   # matches = pattern.match(contents) #at the beginning / no need for loop  can direct print  print(matches)
   # matches = pattern.search(contents) # no need for loop, can direct print  print(matches)

    subb = pattern.sub(r'\1\2', contents)



    for match in matches:
        print(match)
        
    for match in matches:
    print(match.group(2))
    
    
    #print("geeks", end =" ")
