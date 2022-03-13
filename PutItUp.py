
def GetItOn():
    with open('MoreTrueOutput.txt', 'a') as the_file:
        the_file.truncate(0)
    with open("output.txt") as file:
        lines = file.readlines()
        print(lines)
        with open('TrueOutput.txt', 'a') as the_file:
            the_file.truncate(0)
            for i in range(len(lines)):
                lines[i]=(("Server_"+str(i)+"	")+lines[i])
                the_file.write(lines[i])
                