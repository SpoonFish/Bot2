lst = []
with open('extra/messages.txt', 'r') as f:
    lines = f.readlines(1000)
    for line in lines:
        line = line[:-1]
        if line == '': continue
        lst.append(line)

with open('extra/messages_convert.txt', 'w') as f:
    for line in lst:
        f.write(line)
        f.write('\n')