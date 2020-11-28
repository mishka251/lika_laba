
from search_methods import *
from variants import lika_data, test

print(lika_data)
print()
methods = [PassiveBlockSearch(), BlockSearch(), BinarySearch(), Dihotomy(), GoldenFraction(), Fibonachy(),
           TangentMethod(), ParabolMethod()]

for method in methods:
    print(method(lika_data))
    print()
