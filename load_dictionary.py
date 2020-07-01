import sys

# takes in file name or directory path to file
def load(file):
    try:
        with open(file, 'r') as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            for i in range(len(loaded_txt)):
                loaded_txt[i] = loaded_txt[i].lower()
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)




