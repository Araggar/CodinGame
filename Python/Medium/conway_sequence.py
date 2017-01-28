r = int(raw_input())
l = int(raw_input())

last_line = [r]

for i in xrange(1,l):
    count = 0
    build = []
    last_element = ''
    
    for element in last_line:
        if last_element == '':
            last_element = element
        if element == last_element:
            count += 1
        else:
            build.append((count, last_element))
            last_element = element
            count = 1
            
    build.append((count, element))   
    last_line = []

    for c, e in build:
        last_line.append(c)
        last_line.append(e)
    
for num in last_line:
    print num,
