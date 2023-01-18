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

def parse_crates(crates):
    """
    ** NOTE: NO INPUT VALIDATION **
    This relies on the "labels" of the "crates" being on the bottom row of text, and in a specific column position.
    The input must also have strictly alpha characters aligned in the same matching column of each \n separated row.
    Alpha characters should not exist elsewhere.
    """
    layers = crates.split('\n')
    
    # process bottom row of text (the "labels") and remove it from the layers
    labels = layers[-1]
    layers = layers[:-1]

    # create a map to save the char position index for each label
    label_idx = {}
    stacks = {}
    for pos, char in enumerate(labels):
        if char != ' ':
            label_idx[pos] = char
            stacks[char] = []
    
    # append crates to corresponding labels in order as lists
    for layer in reversed(layers):
        for pos, char in enumerate(layer):
            if char.isalpha():
                stacks[label_idx[pos]].append(char)
    
    return stacks

def move_crates(stacks, procedures):
    for procedure in procedures:
        # parse procedure
        numbers = [int(i) for i in procedure.split() if i.isdigit()]
        if len(numbers) != 3:
            print(f"ERROR: invalid procedure '{procedure}'")
        
        # explicitly written out to separate variables for readability
        count = numbers[0]
        src = str(numbers[1])
        dest = str(numbers[2])
        
        # pop from src list and push onto the dest list, 'count' times
        for i in range(count):
            stacks[dest].append(stacks[src].pop())

    return stacks

def get_top_layers(stacks):
    output = ''
    for label, crates in stacks.items():
        output += crates[-1]
    return output

def main(fname, part=1):
    input = read_input(fname)
    
    tokens = input.split('\n\n')
    crates = tokens[0]
    procedures = tokens[1].split('\n')

    stacks = parse_crates(tokens[0])
    stacks = move_crates(stacks, procedures)
    output = get_top_layers(stacks)
    print(output)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1:
        print("Error: input filename not passed in as an argument")
    elif len(args) == 1:
        main(args[0])
    elif len(args) == 2:
        if args[1] not in ['1', '2']:
            print("Error: second arg should be '1' or '2'")
        else:
            main(args[0], int(args[1]))
    elif len(args) > 2:
        print("Error: too many input arguments passed in")