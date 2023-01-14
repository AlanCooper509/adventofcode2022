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

def main(fname, part=1):
    input = read_input(fname)

    pairs = input.split('\n')
    if part == 1:
        count = 0
        for pair in pairs:
            elf1 = pair.split(',')[0]
            elf1min = int(elf1.split('-')[0])
            elf1max = int(elf1.split('-')[1])
            elf2 = pair.split(',')[1]
            elf2min = int(elf2.split('-')[0])
            elf2max = int(elf2.split('-')[1])
            count += 1 if (elf1min <= elf2min and elf1max >= elf2max) or (elf2min <= elf1min and elf2max >= elf1max) else 0
        print(count)
    if part == 2:
        print("nyi")


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