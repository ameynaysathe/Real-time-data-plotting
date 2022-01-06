import os
import time
import csv
import random

second = 0
minute = 0
hour = 0
Time = 0
Population = 0
Covid_Cases = 0

fieldnames = ["Time", "Population", "Covid_Cases"]

with open('database.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


while(True):

    with open('database.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "Time": Time,
            "Population": Population,
            "Covid_Cases": Covid_Cases
        }

        csv_writer.writerow(info)
        print(Time, Population, Covid_Cases)

        # Time += 4
        Population = Population + random.randrange(0, 10)

    print(" Time: %d : %d : %d "%(hour,minute,second))

    print(" Population: ", Population)
    print(" Covid Cases:", Covid_Cases)

    # time.sleep(4)
    second += 4
    Time += 4
    Population += 10
    Covid_Cases += 2
    time.sleep(4)

    if(second == 60):
        second = 0
        minute += 1
    if(minute == 60):
        minute = 0
        hour += 1;
    os.system('cls')