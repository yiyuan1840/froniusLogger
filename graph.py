"""
Simple code to draw a graph of a day of power.
Requires matplotlib

On Fedora Linux: sudo dnf install python3-matplotlib

"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
import time

today = time.strftime("%Y_%m_%d")

INFILENAME = today + '.csv'


def main():
    datareader = csv.reader(open(INFILENAME,'r'), delimiter='\t')
    points = []
    for row in datareader:
        if len(row) > 1:
            watts = float(row[1])
            points.append(watts)


    plt.plot(points)
    plt.ylabel('Watt')
    plt.show()
    plt.savefig('wattgraph')


if __name__ == "__main__":
    main()