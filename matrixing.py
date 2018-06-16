# function based full dice roller with statistics
import random
#ask Bette if there is anything else I am messing up on
print("welcome to the dice roller 2018, an example roll is 2d4 + 3d6 - 4\n")

minimum_val = 0 # these are for statistics
max_val = 0


def xdx_eval(given_str, sign):
    try:
        global minimum_val, max_val
        total_val = 0
        split_index = given_str.index("d")
        num_of_dies = int(given_str[:split_index])
        die_val = int(given_str[split_index + 1:])
        if num_of_dies != 1:
            print("\nrolling {} {} sided dice...".format(num_of_dies, die_val))
        else:
            print("\nrolling {} {} sided die...".format(num_of_dies, die_val))
        for _ in range(num_of_dies):  # number of times to roll the dice
            if get_avg:
                if sign:
                    minimum_val += 1
                    max_val += die_val
                else:
                    minimum_val -= die_val
                    max_val -= 1
            current_roll = random.randint(1, die_val)  # most important line
            if current_roll == die_val:
                print("You got the maximum roll of {0}!".format(current_roll))
            else:
                print("You rolled a {1} out of {0}".format(die_val, current_roll))
            total_val += current_roll
        return total_val
    except ValueError:
        print("That input was not valid, try again using notation like 2d8-3d5+5")


def sign_pls(first_dig):
    if first_dig.isdecimal():
        return True
    elif "+" in first_dig:
        return True
    elif "-" in first_dig:  # I can't bring myself to turn this into an else
        return False


def operator_index(strong):  # gets the index of the next required split
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


def string_sorter(die_choose):
    global minimum_val, max_val, get_avg
    grand_tot = 0
    grp_amt = die_choose.count("+")
    neg_amt = die_choose.count("-")
    for i in range(grp_amt + neg_amt + 1): # +1 for if it is just a number
        if die_choose. replace(" ", "") == "":
            break
        front_sign = sign_pls(die_choose[0])
        if not die_choose[0].isnumeric():
            die_choose = die_choose[1:]  # gets rid of +- at start of  string
        next_indx = operator_index(die_choose)
        is_negative = -1
        if front_sign:
            is_negative = 1
            print("+" + die_choose[:next_indx])
        if die_choose[:next_indx].isdecimal():  # if the next thing is a number
            if front_sign:
                print("+"+die_choose[:next_indx])
            else:
                print("-" + die_choose[:next_indx])
            grand_tot += int(die_choose[:next_indx]) * is_negative
            minimum_val += int(die_choose[:next_indx]) * is_negative
            max_val += int(die_choose[:next_indx]) * is_negative
        else:
            try:
                grand_tot += xdx_eval(die_choose[:next_indx], front_sign)*is_negative
            except TypeError:
                print()
                return
        die_choose = die_choose[next_indx:]

    if get_avg:
        print("\nthe maximum possible roll for {} is:".format(repeat_saver), max_val)
        print("the minimum roll is:", minimum_val)
        print("the average roll is:", (max_val + minimum_val)/2)
    print("\nyour total roll is:", grand_tot, "\n")
    # return grand_tot # is for being part of bigger system of files


def main():
    global minimum_val, max_val, get_avg, repeat_saver
    while True:  # is there a better thing to put this as?
        input_die = input("enter the number and type of dice you would like "
            "to roll, type 'quit' to quit, hit enter to redo the last roll "
            "or 'avg' to see the probability of your last roll \n")
        if "quit" in input_die:
            return
        input_die.replace(" ", "")
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
                string_sorter(repeat_saver)
                continue
            else:
                print("you need to put in a calculation before finding its average\n")
                continue
        else:
            get_avg = False
        repeat_saver = input_die
        string_sorter(input_die)


main()
