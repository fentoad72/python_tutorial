
# Initialize my data variable
data = {'date':[], 'time':[], 'tempout':[]}

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
        split_line = line.split()    #whitespace   
        data['date'].append(split_line[0])
        data['time'].append(split_line[1])
        data['tempout'].append(split_line[2])

