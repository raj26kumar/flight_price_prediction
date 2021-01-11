from numpy.lib.shape_base import split


duration = ['2h 50m', '7h 25m', '19h 0m', '5h 25m', '4h 45m', '2h 25m', '15h 30m', '21h 5m', '25h 30m', '7h 50m', '13h 15m', '2h 35m', '2h 15m', '12h 10m', '2h 35m', '26h 35m', '4h 30m', '22h 35m', '23h 0m', '20h 35m']

duration_hours = []
duration_mins = []
for i in range(len(duration)):
    duration_hours.append(int(duration[i].split(sep = "h")[0]))    # Extract hours from duration 
    duration_mins.append(int(duration[i].split(sep = "m")[0].split()[-1])) 

#d= (duration[0].split(sep="m")[0].split())
#duration_mins.append(d)
print(duration_hours)