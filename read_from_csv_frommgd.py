import csv

csv_file = open('trees.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

# Skip first row if it only contains the column headers
next(csv_reader)
max_height = 0
max_volume = 0

for row in csv_reader:
    Index, Girth, Height, Volume = row
    if int(Height) > max_height:
        max_height = int(Height)
    if float(Volume) > max_volume:
        max_volume = float(Volume)
print("Heighest tree was {} feet high.".format(max_height))
print("Heighest tree was {} cubic feet.".format(max_volume))

csv_file.close()