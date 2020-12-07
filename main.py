
from search_methods import *
from variants import variant10, test

print(variant10)
print()
methods = [
    # PassiveBlockSearch(),
    # BlockSearch(),
     BinarySearch(),
    Dihotomy(),
    GoldenFraction(),
    # Fibonachy(),
    #TangentMethod(),
    ParabolMethod()
]

for method in methods:
    print(method(variant10))
    print()
