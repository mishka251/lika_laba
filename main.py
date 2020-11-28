from math import exp

from data_classes import InputData
from search_methods import *
from variants import lika_data, test

print(test)
print()
methods = [PassiveBlockSearch(), BlockSearch(), BinarySearch(), Dihotomy(), GoldenFraction(), Fibonachy(),
           TangentMethod()]
for method in methods:
    print(method(test))
    print()
