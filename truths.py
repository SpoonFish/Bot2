truths = []
btruths = []
with open('truths.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith('--'):
            btruths.append(line[2:-1])
        truths.append(line[:-1])
    if len(btruths) > 0:
        truths = btruths