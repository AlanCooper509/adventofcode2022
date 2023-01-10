import sys

class ElfItems:
    items = []
    sum = None
    def __init__(self, items):
        """
        Gets various statistics based off of input item values
        """
        self.items = items
        self.sum = sum(items)

def main(fname):
    # read from file 
    input = None
    with open(fname, "r+") as file:
        input = file.read()

    if input == None:
        return

    # separate elves by double newline separators
    elves = input.split("\n\n")

    # separate each elf's items by single newline separator and cast as int to send into data structure
    elfValues = []
    for elf in elves:
        items = elf.split('\n')
        itemValues = [int(item) for item in items]
        elfValues.append(ElfItems(itemValues))

    # get maximum item sum from data structure
    maxSum = max(elfItems.sum for elfItems in elfValues)
    print(maxSum)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1:
        print("Error: input filename not passed in as an argument")
    elif len(args) > 1:
        print("Error: too many input arguments passed in")
    else:
        main(args[0])