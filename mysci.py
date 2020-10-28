
# Initialize my data variable
data = []

# Read the datafile
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
#   data = datafile.read()

    #read the first 3 lines (header)
    # underscore is a placeholder variable used instead of i or j
    for _ in range(3):
        datafile.readline()

    #read and parse the rest of the file
    for line in datafile:
        datum = line.split()    #whitespace   
#       datum = line.split(',')  comma-separated       
#       datum = line.split(\t)   tab-separated    

        data.append(datum)

