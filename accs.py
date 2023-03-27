import discord
accs = []
class Acc():
    def __init__(self, name, vars) -> None:
        self.name = name
        self.vars = vars
with open("accs.txt", "r+", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line.replace('\n', '')
        indx1 = line.find(':')
        name = line[:indx1]
        rest = line[indx1+1:].split(';')
        vars = {}
        for r in rest:
            t = r.split(',')
            try: vars[t[0]] = int(t[1]) 
            except: vars[t[0]] = t[1]
        acc = Acc(name, vars)
        accs.append(acc)
    pass

def save():
    with open("accs.txt", "w+", encoding="utf-8") as f:
        for acc in accs:
            var_string = ''
            for var in acc.vars:
                var_string+=f"{var},{acc.vars[var]};"
            var_string = var_string[:-1]
            f.write(f"{acc.name}:{var_string}\n")
    return discord.File("accs.txt")

def get_acc(name) -> Acc:
    for acc in accs:
        if acc.name == name:
            return acc