import sys

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

def find_duplicate(compart1, compart2):
    # guard clause just for good practice
    if len(compart1) != len(compart2):
        print("Error: compartments are different lenghts")
        return

    # hash map for runtime efficiency
    hashbrowns = {}
    for item in compart1:
        hashbrowns[item] = True
    for item in compart2:
        if item in hashbrowns:
            return item

def get_letter_value(dupe):
    # map a-z;A-Z to 1-26;33-58 by utilizing their ascii value mappings
    priority = ord(dupe.swapcase()) - ord('A') + 1
    
    # convert 33-58 range to 27-52 to correctly apply priorities
    if priority > 26:
        priority -= (ord('a') - ord('Z')) - 1
    
    return priority

def main(fname, part=1):
    input = read_input(fname)

    rucksacks = input.split('\n')
    sum = 0
    for rucksack in rucksacks:
        itemCount = int(len(rucksack))
        divider = int(itemCount/2)

        # guard clause on each rucksack entry
        if itemCount % 2 == 1 or itemCount < 2:
            print(f'Error: invalid rucksack {rucksack}')
            return

        # split rucksack into the two compartments
        compart1 = rucksack[: divider]
        compart2 = rucksack[divider :]
        
        dupe = find_duplicate(compart1, compart2)
        value = get_letter_value(dupe)
        print(f"{dupe}: {value}")
        sum += value

    print(sum)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1:
        print("Error: input filename not passed in as an argument")
    elif len(args) == 1:
        main(args[0])
    elif len(args) > 1:
        print("Error: too many input arguments passed in")