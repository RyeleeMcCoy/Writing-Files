#-----------------------------
#Writing files
#Ryelee McCoy
#To show an example for accessing and reading external files such as .txt
#text files that are in the same folder as the python file are easily found
#other text files stored in their own folder will need a path to thier location
#-----------------------------


#----------------------Functions-------------------------

def writing_to():
    file2 = open('Poem.txt', 'w')
    print("Opening File")
    file2.write("Roses are red\n")
    file2.write("Violets are blue\n")
    
    
    file2.write("For the 85th time\n")
    file2.write("Stop calling hard drives CPU's")
    file2.close()
    print("File Closed")
    
def read_all():
    file  = open('Poem.txt', 'r')
    all_lines = file.read()
    print(all_lines)
    file.close()
    
 
def other_inputs():
    name = input("What do you want to name this file? ")
    sport = input("What is your Favorite sport? ")
    file = name + '.txt'
    save = open(file, 'w') 
    save.write("User ")
    save.write(name + " ")
    save.write("favorite sport is ")
    save.write(sport + "!")
    save.close() #closes the file
    
    
def main():
    writing_to()
    input("> ")
    read_all()
    input("> ")
    other_inputs()

main()