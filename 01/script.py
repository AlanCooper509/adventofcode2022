import sys

def main(fname, maxCount=1):
    if (not isinstance(fname, str)):
        return
    if (not maxCount.isdigit()):
        return
    # read from file
    input = None
    with open(fname, "r+") as file:
        input = file.read()
    if input == None:
        return

    # separate elves by double newline separators
    elves = input.split("\n\n")

    # separate each elf's items by single newline separator and cast as ints that get summed together
    elfValues = []
    for elf in elves:
        elfItems = elf.split('\n')
        elfValue = sum([int(item) for item in elfItems])
        elfValues.append(elfValue)

    # remove maximum item sum from list
    topValues = []
    for i in range(int(maxCount)):
        highestSum = elfValues.pop(elfValues.index(max(elfValues)))
        topValues.append(highestSum)
    print(sum(topValues))

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1:
        print("Error: input filename not passed in as an argument")
    elif len(args) == 1:
        main(args[0])
    elif len(args) == 2:
        main(args[0], args[1])
    elif len(args) > 2:
        print("Error: too many input arguments passed in")
