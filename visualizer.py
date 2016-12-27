import inspect
import RecViz


def fib(n):
    x = RecViz.EnableLogging(inspect.currentframe())
    if(n==0):
        return x.LogAndReturn(0)
    elif(n==1):
        return x.LogAndReturn(1)
    return x.LogAndReturn(fib(n - 1) + fib(n - 2))


def binary_search(value, items, low=0, high=None):
    """
    Binary search function.
    Assumes 'items' is a sorted list.
    The search range is [low, high)
    """
    x = RecViz.EnableLogging(inspect.currentframe())
    high = len(items) if high is None else high
    pos = low + (high - low) / len(items)

    if pos == len(items):
        return False
    elif items[pos] == value:
        return pos
    elif high == low:
        return False
    elif items[pos] < value:
        return binary_search(value, items, pos + 1, high)
    else:
        assert items[pos] > value
        return binary_search(value, items, low, pos)


def mergesort(aList):
    _mergesort(aList, 0, len(aList) - 1)

def _mergesort(aList, first, last):
    x = RecViz.EnableLogging(inspect.currentframe())
    # break problem into smaller structurally identical pieces
    mid = (first + last) / 2
    if first < last:
        _mergesort(aList, first, mid)
        _mergesort(aList, mid + 1, last)

    # merge solved pieces to get solution to original problem
    a, f, l = 0, first, mid + 1
    tmp = [None] * (last - first + 1)

    while f <= mid and l <= last:
        if aList[f] < aList[l]:
            tmp[a] = aList[f]
            f += 1
        else:
            tmp[a] = aList[l]
            l += 1
        a += 1

    if f <= mid:
        tmp[a:] = aList[f:mid + 1]

    if l <= last:
        tmp[a:] = aList[l:last + 1]

    a = 0
    while first <= last:
        aList[first] = tmp[a]
        first += 1
        a += 1

mergesort([-3, -2, -1, 1, 3, 4, 6, 8, 9, 10, 12])
fib(6)
binary_search(6, [-3, -2, -1, 1, 3, 4, 6, 8, 9, 10, 12])