f = open('trial.txt','r')
content = f.readlines()
count = 0
total = [0]
for line in content:
    count += int(line)
    total.append(int(count))
print('Part 1 =',count)

x = 0
while x < 1037:
    count += int(content[x]) 
    if count in total:
        print('Part 2 =',count)
        break
    total.append(int(count))
    if x == 1036:
        x = -1
    x += 1
    
    
