x = 0
while x<= 5:
    print(x)
    x = x+1

count = 7
while count < 1:
    print("hello world")


#the general format for openeing a file is

file_variable = open(filename, mode)


# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform the analysis.


# Close the file.
election_data.close()