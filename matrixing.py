# function based full dice roller with statistics
import random


def roll_it(die):
    return random.randint(1, die)


minimum_val = 0
max_val = 0


def xdx_eval(given_str, sign):
    try:
        global minimum_val, max_val
        total_val = 0
        split_index = given_str.index("d")
        num_of_dies = int(given_str[:split_index])
        die_val = int(given_str[split_index + 1:])
        for tro in range(num_of_dies):
            if sign:
                minimum_val += 1
                max_val += die_val
            else:
                minimum_val -= die_val
                max_val -= 1
            current_roll = roll_it(die_val)
            if current_roll != die_val:
                print("You rolled a {0} and got a {1}".format(die_val, current_roll))
            else:
                print("You got the maximum roll of {0}!".format(current_roll))
            total_val += current_roll
        return total_val
    except ValueError:
        print("That input was not valid, try again using notation like 2d8-3d5+5")
        # inp_chooser()

def sign_pls(first_dig):
    if first_dig.isdecimal():
        return True
    elif "+" in first_dig:
        return True
    elif "-" in first_dig:
        return False

def operator_index(strong):
    pos_incl = "+" in strong
    neg_incl = "-" in strong
    if pos_incl:
        where_pos = strong.index("+")
    if neg_incl:
        where_neg = strong.index("-")
    if pos_incl and not neg_incl:
        return where_pos
    elif neg_incl and not pos_incl:
        return where_neg
    elif pos_incl and neg_incl:
        if where_neg < where_pos:
            return where_neg
        else:
            return where_pos
    else:
        return len(strong)


repeat_saver = ""
get_avg = False

def inp_chooser():
    global get_avg
    global repeat_saver
    global minimum_val, max_val
    while True:
        input_die = input("enter the number and type of dice you would like to roll? type 'quit' to quit, hit"
                           " enter to redo the last roll or avg to see the probability of your last roll \n")
        if "quit" in input_die:
            return
        if input_die == "":
            input_die = repeat_saver
            if input_die == "":
                print("you don't have a calculation to redo, try again\n")
                continue
            print("redoing", repeat_saver)

        if "avg" in input_die:
            if repeat_saver != "":
                get_avg = True
                minimum_val = max_val = 0
                main_func(repeat_saver)
                continue
            else:
                print("you need to put in a calculation before finding its average\n")
                continue
        else:
            get_avg = False
        repeat_saver = input_die

        '''if "d" not in input_die and "avg" not in input_die:
            print("That input was not valid, try again using notation like 2d8-3d5+5")
            continue'''
        main_func(input_die)


def main_func(die_choose):
    global minimum_val, max_val, get_avg
    grand_tot = 0
    grp_amt = die_choose.count("+")
    neg_amt = die_choose.count("-")
    for i in range(grp_amt + 1 + neg_amt):
        front_sign = sign_pls(die_choose[0])
        if not die_choose[0].isnumeric():
            die_choose = die_choose[1:]
        next_indx = operator_index(die_choose)
        if die_choose[:next_indx].isdecimal():
            if front_sign:
                print("+"+die_choose[:next_indx])
                grand_tot += int(die_choose[:next_indx])
                minimum_val += int(die_choose[:next_indx])
                max_val += int(die_choose[:next_indx])
            else:
                print("-" + die_choose[:next_indx])
                grand_tot -= int(die_choose[:next_indx])
                minimum_val -= int(die_choose[:next_indx])
                max_val -= int(die_choose[:next_indx])
            print("INPUT IS CURRENTLY", die_choose)
        else:
            try:
                if front_sign:
                    grand_tot += xdx_eval(die_choose[:next_indx], True)
                else:
                    grand_tot -= xdx_eval(die_choose[:next_indx], False)
            except TypeError:
                print()
                return
        die_choose = die_choose[next_indx:]
        if die_choose. replace(" ", "") == "":
            break
        # print(die_choose) this is to check if it is truncating properly
    if get_avg:
        print("\nthe maximum possible roll for {} is:".format(repeat_saver), max_val)
        print("the minimum roll is:", minimum_val)
        print("the average roll is:", (max_val + minimum_val)/2)
    print("\nyour total roll is:", grand_tot, "\n")
    #return grand_tot

inp_chooser()