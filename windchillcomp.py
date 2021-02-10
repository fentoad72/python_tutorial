
from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_windchill

# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed': 7, 'windchill': 12}

# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed': float, 'windchill':float}

# Read data from file
data = read_data(columns,types=types)

# Running the function to compute wci
windchill = [compute_windchill(t,w) for t,w in zip(data['tempout'],data['windspeed'])]

# DEBUG
#for wc_data, wc_comp in zip(data['windchill'],windchill):
#    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data -wc_comp:.5f}')

#OUTPUT comparison of data
print_comparison('WINDCHILL',data['date'],data['time'],data['windchill'],windchill)
