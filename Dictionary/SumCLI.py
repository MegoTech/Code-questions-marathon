#you are given a sesquence of commands: "cp" "ls" "rm" and index "!<number>".
#like ["cp", "ls", "mv", "!2", "!1", "ls", "!3", "!6"]
#the index is the index of the command in the list that you need to execute.
#return list that first element represent the number of times you need to execute the command "cp
#and the second element represent the number of times you need to execute the command "ls"
#and the third element represent the number of times you need to execute the command "mv"
#more examples:
#["ls", "cp", "mv", "mv", "mv", "mv","!1", "!3", "!6"] -> [1, 3, 4]

def comennds_num(comends):
    commands = {"cp": [], "ls": [], "mv": []}
    for i in range(len(comends)):
        place = 0
        if comends[i][0] == "!":
            place = int(comends[i][1:])
        if comends[i] == "cp" or place in commands["cp"]:
            commands["cp"].append(i + 1)
        elif comends[i] == "ls" or place in commands["ls"]:
            commands["ls"].append(i + 1)
        elif comends[i] == "mv" or place in commands["mv"]:
            commands["mv"].append(i + 1)

    return [len(commands[keyM]) for keyM in commands.keys()]

#~~~~~~~~~~~~~~~~~~test~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    if comennds_num(["cp", "ls", "mv", "!2", "!1", "ls", "!3", "!6"]) == [1, 2, 1]:
        print("pass 1 test")
    else:
        print("fail 1 test")