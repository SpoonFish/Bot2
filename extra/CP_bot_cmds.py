
import datetime
with open("Bot/configs.txt", "r") as f:
    cp_file = f.readlines(99)[1].replace('\n', '')
print(f'Current CP sheet: {cp_file}\n')

class CPsheet():
    sheet_dict = {
        'members': [],
        'modifiers': [],
    }
    def check_account_overlap(name):
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                return 1
        return 0


    def add_user(u, name, i_balance):
        if name == 'no': return 'You must enter a user name /CP adduser <name#0000> <balance>'
        if i_balance == 'no': return 'You must enter an inital balance /CP adduser <name#0000> <balance>'
        if len(name) < 6:
            return('Name too short')
        if name[-5] != '#' or name [-4:].isdigit() == False:
            return('Name is required in the format <name#discord tag [4 digits]>')
        if i_balance.isdigit() == False and round(float(i_balance)) < 0:
            return('Balance must be an intetger above -1')
        if CPsheet.check_account_overlap(name):
            return('Account already exists')
        CPsheet.sheet_dict['members'].append([name, i_balance])
        write_sheet()
        log(f'{u} added account {name} with {i_balance} CP')
        return(f'successfuly added {name} to the sheet with a balance of {round(float(i_balance))} CP')
        print('')
        return 1


    def remove_user(u, name):
        if name == 'no': return 'You must enter a user name /CP removeuser <name#0000>'
        if not CPsheet.check_account_overlap(name): return('Account does not exist')
        j = 0
        can_remove = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                can_remove = 1
                break
            j+=1
        name = CPsheet.sheet_dict['members'][j][0]
        bal = CPsheet.sheet_dict["members"][j][1]
        if can_remove: CPsheet.sheet_dict['members'].pop(j)

        l = 0
        can_remove = 0
        try:
            for i in CPsheet.sheet_dict['modifiers']:
                if i[0] == name:
                    can_remove = 1
                    break
                l+=1
            if can_remove: CPsheet.sheet_dict['modifiers'].pop(l)
        except:
            pass
        write_sheet()
        log(f'{u} removed account {name}. They had {bal} CP')
        return f'{name}\'s account was removed. They had {bal} CP'

    def get_inv(name):
        if name == 'no': return 'You must enter a user name /CP invuser <name#0000>'
        if not CPsheet.check_account_overlap(name): return('Account does not exist')
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
                    
        if to_check: 
            return CPsheet.sheet_dict['members'][j][4]


    def inv_user(name):
        if name == 'no': return 'You must enter a user name /CP invuser <name#0000>'
        if not CPsheet.check_account_overlap(name): return('Account does not exist')
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
                    
        if to_check: 
            nameP = CPsheet.sheet_dict['members'][j][0]
            lst = ''''''
            for i in CPsheet.sheet_dict['members'][j][4]:
                lst += f'{i}\n'
            return(f'{nameP} has {len(CPsheet.sheet_dict["members"][j][4])-1} items in their inventory:\n{lst}')

    def check_user(name):
        if name == 'no': return 'You must enter a user name /CP checkuser <name#0000>'
        if not CPsheet.check_account_overlap(name): return('Account does not exist')
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
                    
        if to_check: 
            nameP = CPsheet.sheet_dict['members'][j][0]
            bal = CPsheet.sheet_dict['members'][j][1]
            pearls = CPsheet.sheet_dict['members'][j][3]
            print("")
            bal2 = (f'{nameP} has a balance of {bal} CP\n{nameP} has {pearls} pearls')

        j = 0
        to_check = 0
        print("")
        try:
            for i in CPsheet.sheet_dict['modifiers']:
                if i[0] == name:
                    to_check = 1
                    break
                j+=1
            if to_check: 
                mult = CPsheet.sheet_dict['modifiers'][j][1]
                percent = CPsheet.sheet_dict['modifiers'][j][2]
                return(f'''{bal2}
{nameP} recieves {percent}% {mult} CP''')
            else:
                return(f'''{bal2}
{nameP} has no modifiers''')

        except:
            print(f'''{bal2}
{nameP} has no modifiers''')
        print("")

    def change_user_bal(u, name, amount, orig):
        if name == 'no': return 'You must enter a user name /CP changebal <name#0000> <amount> <use modifier: y/n>'
        if amount == 'no': return 'You must enter an amount /CP changebal <name#0000> <amount> <use modifier: y/n>'
        if orig == 'no': return 'You must specify whether to use modifer (y) or not (n) /CP changebal <name#0000> <amount> <use modifier: y/n>'
        if not CPsheet.check_account_overlap(name): return('Account does not exist')
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
                    
        if to_check: 
            nameP = CPsheet.sheet_dict['members'][j][0]
            bal = CPsheet.sheet_dict['members'][j][1]
            amount = (float(amount))


        print("")
        try:
            l = 0
            to_check = 0
            for i in CPsheet.sheet_dict['modifiers']:
                if i[0] == name:
                    to_check = 1
                    break
                l+=1
            if to_check: 
                inputX = 0
                mult = CPsheet.sheet_dict['modifiers'][l][1]
                percent = int(CPsheet.sheet_dict['modifiers'][l][2])
                if mult == 'more':
                    amount2 = round(amount*(1+percent/100))
                else:
                    amount2 = round(amount*(1-percent/100))

                amount = round(amount)
                if orig == 'n':
                    n = int(CPsheet.sheet_dict['members'][j][1]) + amount2
                else:
                    n = int(CPsheet.sheet_dict['members'][j][1]) + amount

            else:
                print(f'{nameP} has no modifiers')
                n = int(CPsheet.sheet_dict['members'][j][1]) + amount

        except:
            print(f'{nameP} has no modifiers')
            n = int(CPsheet.sheet_dict['members'][j][1]) + amount

        CPsheet.sheet_dict['members'][j][1] = str(round(n))
        write_sheet()

        if orig == 'n':
            orig = 'no'
        else:
            orig = 'a'
        
        log(f'{u} changed {name}\'s balance to {str(round(n))} CP using {orig} modifier')
        return(f'Changed {nameP}\'s balance to {CPsheet.sheet_dict["members"][j][1]} CP')
        print("")
        
    def change_user_name(u, name, new_name):
        if name == 'no': return 'You must enter a user name /CP changename <name#0000> <new name#0000>'
        if new_name == 'no': return 'You must enter a new name /CP changename <name#0000> <new name#0000>'
        if not CPsheet.check_account_overlap(name): return('Account does not exist')
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
                    
        if to_check: 
            nameP = CPsheet.sheet_dict['members'][j][0]
            valid = 0
            if len(new_name) < 6:
                return('Name too short')
            if new_name[-5] != '#' or new_name [-4:].isdigit() == False:
                return('Name is required in the format <name#discord tag [4 digits]>')
            if CPsheet.check_account_overlap(new_name):
                return('Name already taken')
            CPsheet.sheet_dict['members'][j][0] = new_name
            write_sheet()
            log(f'{u} changed {name}\'s name to {new_name}')
            return(f'Changed {name}\'s name to {new_name}')


        print("")

    def add_user_mod(u, name, ml, percent2):
        if name == 'no': return 'You must enter a user name /CP addmod <name#0000> <more/less> <percent>'
        if ml == 'no': return 'You must specify whether the modifier gives (more) or (less) CP /CP addmod <name#0000> <more/less> <percent>'
        if percent2 == 'no': return 'You must enter percentage to modify by /CP addmod <name#0000> <more/less> <percent>'
        if not CPsheet.check_account_overlap(name): return('Account does not exist')
        to_check = 0
        prev = 0
        j = 0

        print("")
        try:
            j = 0
            to_check = 0
            for i in CPsheet.sheet_dict['modifiers']:
                if i[0] == name:
                    to_check = 1
                    break
                j+=1
            if to_check: 
                mult = CPsheet.sheet_dict['modifiers'][j][1]
                percent = int(CPsheet.sheet_dict['modifiers'][j][2])
                prev = 1

        except:
            pass

        try:
            CPsheet.sheet_dict['modifiers'].pop(j)
        except:
            pass
        CPsheet.sheet_dict['modifiers'].append([name, ml, str(percent2)])
        write_sheet()
        log(f'{u} added a modifier of {percent2}% {ml} CP to {name}')
        if prev == 1:
            return(f'Replaced {name}\'s modifier of {percent}% {mult} CP with {percent2}% {ml} CP')
        else:
            return(f'Added a modifier for {name} of {percent2}% {ml} CP')
        print("")

    def list_users():
        if len(CPsheet.sheet_dict['members']) == 0:
            return('There are no users')
        lst = ''''''
        for i in CPsheet.sheet_dict['members']:
            lst += f'{i[0]} - {i[1]} CP\n'
        return lst

    def remove_user_mod(u, name):
        if name == 'no': return 'You must enter a user name /CP removemod <name#0000>'
        if not CPsheet.check_account_overlap(name): return('Account does not exist')
        to_check = 0
        j = 0

        print("")
        try:
            j = 0
            to_check = 0
            for i in CPsheet.sheet_dict['modifiers']:
                if i[0] == name:
                    to_check = 1
                    break
                j+=1
            if to_check: 
                mult = CPsheet.sheet_dict['modifiers'][j][1]
                percent = int(CPsheet.sheet_dict['modifiers'][j][2])
                CPsheet.sheet_dict['modifiers'].pop(j)
                write_sheet()
                log(f'{u} removed a modifier of {percent}% {mult} CP from {name}')
                return(f'Removed {name}\'s modifier of \'{percent}% {mult} CP\'')

            else:
                return(f'{name} has no modifiers')
                

        except:
            return(f'{name} has no modifiers')
        
        
        print("")
    def get_bal(name):
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
        if to_check:
            CP = CPsheet.sheet_dict['members'][j][1]
            return int(CP)
        else: return -1

    def get_spins(name):
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
        if to_check:
            spins = CPsheet.sheet_dict['members'][j][2]
            return f'You have **{spins}** spins left'
            
    def add_inv_silent(name, item):
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
        if to_check:
            CPsheet.sheet_dict['members'][j][4].append(item)
            write_sheet()
        else:
            return 'Account does not exist'

    def add_spin(name):
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
        if to_check:
            spins = int(CPsheet.sheet_dict['members'][j][2])
            spins += 1
            CPsheet.sheet_dict['members'][j][2] = str(spins)
            write_sheet()
            return name+' now has '+str(spins)+' spins'
        else:
            return 'Account does not exist, Please contact a staff member to fix this'

    def add_spin_silent(name, amount):
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
        if to_check:
            spins = int(CPsheet.sheet_dict['members'][j][2])
            spins += amount
            CPsheet.sheet_dict['members'][j][2] = str(spins)
            write_sheet()

    def add_pearls(name, amount):
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
        if to_check:
            pearls = int(CPsheet.sheet_dict['members'][j][3])
            pearls += amount
            CPsheet.sheet_dict['members'][j][3] = str(pearls)
            write_sheet()

    def use_spin(name):
        to_check = 0
        j = 0
        for i in CPsheet.sheet_dict['members']:
            if i[0] == name:
                to_check = 1
                break
            j+=1
        if to_check:
            spins = int(CPsheet.sheet_dict['members'][j][2])
            if spins > 0:
                spins -= 1
                CPsheet.sheet_dict['members'][j][2] = str(spins)
                write_sheet()
            else:
                return 'You have no spins left'
        else:
            return 'Account does not exist'
        
        
def init_sheet(cp_file):
    with open("Bot/"+cp_file, "r") as f:
        line = '#'
        mode = 'members'
        while line != '': # '%' is end of file
            line = f.readline()
            line = line[:-1] # remove newline
            if line == '' or line[0] == '#': # '#' is comment
                if line.startswith('#Modifiers'):
                    mode = 'modifiers'
            else:
                if mode == 'members':
                    lst = line.split(',')[:4]
                    lst.append(line.split(',')[4:])
                    CPsheet.sheet_dict['members'].append(lst)
                elif mode == 'modifiers':
                    CPsheet.sheet_dict['modifiers'].append(line.split(','))
    #print(CPsheet.sheet_dict)
init_sheet(cp_file)

def write_sheet():
    with open("Bot/"+cp_file, "w") as f:
        f.write('#CP sheet\n')
        f.write('#\n')
        f.write('#Members:  (name, balance, spins, pearls, [inventory])\n')
        f.write('#\n')
        for i in CPsheet.sheet_dict['members']:
            for item in i:
                if isinstance(item, list):
                    f.write(','.join(item))
                else:
                    f.write(item+',')
            f.write('\n')
        f.write('#\n')
        f.write('#Modifiers for certain members:  (name, more/less, percentage)\n')
        f.write('#\n')
        for i in CPsheet.sheet_dict['modifiers']:
            f.write(','.join(i) + '\n')
    print('Saved')
    print("")

def log(string):
    with open("Bot/log.txt", "a") as f:
        dt = datetime.datetime.now()
        f.write(f'{dt.strftime("%Y-%m-%d %H:%M:%S")} {string}\n')


