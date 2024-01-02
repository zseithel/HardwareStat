# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
import re
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum

Devices = Enum('Devices', ['Network','Processor','Memory: % in use','Memory: faults','Disk % use','Disk Queue Length'])

class Entry:
    def __init__(self, clock, category, units, value):
        self.category = category
        self.units = units
        self.clock = int(clock)
        self.value = float(value)
        self.category_id = None

        match category:
            case "network interface(realtek pcie 2.5gbe family controller)":
                self.category_id = 1
            case "processor(_total)":
                self.category_id = 2
            case "memory":
                match units:
                    case "% committed bytes in use :":
                        self.category_id = 3
                    case "cache faults/sec :":
                        self.category_id = 4
            case "physicaldisk(_total)":
                match units:
                    case "% disk time :":
                        self.category_id = 5
                    case "current disk queue length :":
                        self.category_id = 6
            case _:
                self.category_id = -1

    def __str__(self):
        return f'Entry time: {self.clock}, category: {self.category}, {self.units} {self.value}'

    def __repr__(self):
        return f'Entry time: {self.clock}, category: {self.category}, {self.units} {self.value}'


def gather_counter():
    # Use a breakpoint in the code line below to debug your script.
    local = time.strftime('%H%M', time.localtime())
    results = subprocess.run(['powershell', 'get-counter | select -ExpandProperty Readings'],capture_output=True)
    array = [x.decode('UTF-8') for x in results.stdout.splitlines()]
    string_array = [x for x in array if x != ""
                    and not (re.match(r'^\d+(?:\.\d+)$', x)) and not (re.match(r'^[0]$', x))]
    decimal_array = [x for x in array if (re.match(r'^\d+(?:\.\d+)$', x) is not None)
                     or (re.match(r'^[0]$', x))]
    data_array = [[local, y.split('\\')[3].strip(), y.split('\\')[4].strip(), x.strip()] for x, y in zip(decimal_array, string_array)]
    file_name = time.strftime('%m_%d',time.localtime())
    with open("data\\{0}.csv".format(file_name), 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for x in data_array:
            writer.writerow(x)


def read_data(date=time.strftime('%m_%d', time.localtime())):
    with open('data\\{0}.csv'.format(date))as file:
        reader = csv.reader(file, delimiter=',')
        entries = [Entry(row[0], row[1], row[2], row[3]) for row in reader]
        x = [x.clock for x in entries if x.category_id == 2]
        y = [x.value for x in entries if x.category_id == 2]
        plt.figure("processor(_total)")
        plt.subplot()
        plt.xlabel()
        plt.ylabel("% utilized")
        plt.plot(x, y, 'b--')
        plt.show()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gather_counter()
    read_data()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
