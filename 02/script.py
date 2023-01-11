import sys

def get_points(round):
    """
    Convert the ABC / XYZ from char values into {0, 1, 2} for {R, P, S} respectively.
    Then, subtract opponent hand from yours and take the mod3 to determine the winner:
        - output of 2: you win
        - output of 1: you lose
        - output of 0: draw
    (note that in Python: -1 % 3 = 2, -2 % 3 = 1)
    
    Since the rewards are 0 for losing, 3 for draw, 6 for winning, do some math to automate this from the above output:
        - This can be done with the formula:
            result = ((|output - 2| - 1) % 3) * 3

        Given inputs from the set {0(draw), 1(lose), 2(win)} it maps to outputs {0(lose), 3(draw), 6(win)}
    """

    oppInput = round.split(' ')[0]
    youInput = round.split(' ')[1]
    oppValue = ord(oppInput) - ord('A') # ascii to {0, 1, 2} for {R, P, S}
    youValue = ord(youInput) - ord('X') # ascii to {0, 1, 2} for {R, P, S}
    
    # outputs: 2 for win, 1 for lose, 0 for draw
    output = (oppValue - youValue) % 3
    
    # map outputs to score values 6/3/0 for win/draw/lose using some ~fancy math~
    result = 3*((abs(output - 2) - 1) % 3)
    
    # bonus points: 1 for R, 2 for S, 3 for P
    bonus = youValue + 1
    
    return (result + bonus)

def read_input(fname):
    def fname_has_error(fname):
        if (not isinstance(fname, str) or not fname.endswith(".txt")):
            print("'.txt' filename string expected")
            return True
        return False

    # guard clauses for inputs to calling script
    if(fname_has_error(fname)):
        return

    # read content from input file (this is assumed to be properly formatted)
    input = None
    with open(fname, "r+") as file:
        input = file.read()
    return input

def main(fname):
    input = read_input(fname)
    rounds = input.split('\n')

    total = 0
    for round in rounds:
        total += get_points(round)

    print(total)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1:
        print("Error: input filename not passed in as an argument")
    elif len(args) == 1:
        main(args[0])
    elif len(args) > 1:
        print("Error: too many input arguments passed in")
