import os

datatext = open("datatext", "r")

### Lets read all the lines and assign it to a variable ###

try:
    data = datatext.readlines()[::]
except:
    print("Cant read the datatext")
finally:
    datatext.close()
# We need to seperate the wind speeds and directions from the data ###

speed_list = []
wind_direction_list = []

### Lets pull the wind speed and direction data from the txt file ###

try:
    for d in data:
        speed_list.append(d.split()[6])
        wind_direction_list.append(d.split()[5])

    # For taking out the 'speed' and 'direction' titles coming from the data.

    speed_list.pop(0)
    wind_direction_list.pop(0)
except:
    print("Couldn't appen the data to list")

    """Lets create a dictionary with directions as keys and their angles as their values
    C means no wind at the time of measurement, so any wind after that moment can't pass
    the neighbour check"""

Dirdict = {

    "C": 1000,
    "N": 0,
    "NNE": 22.5,
    "NE": 45,
    "ENE": 67.5,
    "E": 90,
    "ESE": 112.5,
    "SE": 135,
    "SSE": 157.5,
    "S": 180,
    "SSW": 202.5,
    "SW": 225,
    "WSW": 247.5,
    "W": 270,
    "WNW": 292.5,
    "NW": 315,
    "NNW": 337.5

}

Directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE",
              "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "C"]

### Time to define our Wind class. ###


class Wind():
    def __init__(self, speed, direction):
        self.speed = float(speed)
        self.direction = str(direction)

    def neighbour_check(self, other):
        """
        There are three possibilities for two winds to be considered as neighbours.
        1. The angle between them are 0, then they are at the same direction.
        2. The angle between them are 22.5, then their directions are adjacent.
        3. The angle 337.5 is a negative 22.5 in cartesian, because of the way we coded our
        direction dictionary we should accept this one too.


        """
        # Calculating angles between two winds
        angle = abs(Dirdict[self.direction] - Dirdict[other.direction])
        # Acceptable neighbourhood conditions mentioned above.
        neighbour_angles = [0, 22.5, 337.5]

        if angle in neighbour_angles:
            return 1
        else:
            return 0

    @staticmethod
    def wind__status(a, b):
        if a == 0 and b == 1:
            Fortune_status.append("Starts")
        elif a == 1 and b == 1:
            Fortune_status.append("Continues")
        elif a == 1 and b == 0:
            Fortune_status.append("Stops")
        elif a == 0 and b == 0:
            Fortune_status.append("StartsStops")

        @staticmethod
        def add_five(a):
            return a + 5


counter = 0
Fortune_hours = []


def wind_status(a, b):
    global counter
    if a == 0 and b == 1:
        Fortune_status.append("Starts")
        counter = 1
    elif a == 1 and b == 1:
        Fortune_status.append("Continues")
        counter += 1
    elif a == 1 and b == 0:
        Fortune_status.append("Stops")
        counter += 1
        Fortune_hours.append(counter)
        return counter
    elif a == 0 and b == 0:
        Fortune_status.append("StartsStops")
        counter = 1
        Fortune_hours.append(counter)
        return counter


Wind_list = []
Neighbour_status = []
Fortune_status = []


for i in range(len(wind_direction_list) - 1):
    Wind_list.append(Wind(speed_list[i], wind_direction_list[i]))

for i in range(len(Wind_list) - 1):
    if Wind.neighbour_check(Wind_list[i], Wind_list[i + 1]) == True:
        Neighbour_status.append(1)
    else:
        Neighbour_status.append(0)

for i in range(len(Neighbour_status) - 1):
    wind_status(Neighbour_status[i], Neighbour_status[i + 1])

Hour_distribution = {}
Direction_distribution = {}
i = 1
while i <= max(Fortune_hours):
    Hour_distribution[str(i)] = str(Fortune_hours.count(i))
    i += 1

for d in Directions:
    x = Directions[Directions.index(d)]
    y = wind_direction_list.count(x)
    Direction_distribution[x] = y

with open("results", "w") as results:
    results.write(f"""

Total measured wind count : {len(data)}
        
Wind Hour Distribution : {Hour_distribution}
        
Wind Direction Distribution : {Direction_distribution}
""")
