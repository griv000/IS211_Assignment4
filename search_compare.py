import random
import time


def sequential_search(a_list,item):
    start_time = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end_time = time.time()
    time_diff = end_time - start_time
    return found, time_diff


def ordered_sequential_search(a_list,item):
    a_list.sort()
    start_time = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    end_time = time.time()
    time_diff = end_time - start_time
    return found, time_diff


def binary_search_iterative(a_list,item):
    a_list.sort()
    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end_time = time.time()
    time_diff = end_time - start_time
    return found, time_diff
    

def binary_search_recursive(a_list,item):
    a_list.sort()
    start_time = time.time()

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

    end_time = time.time()
    time_diff = end_time - start_time
    return found, time_diff


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def main():
    list_sizes = [500, 1000, 5000]
    total_time_count = {'Sequential Search':0.0,'Ordered Sequential Search': 0.0, 
    'Binary Search Iterative':0.0, 'Binary Search Recursive':0.0}

    for myList in list_sizes:
        num_to_go = 100
        while num_to_go > 0:
            total_time_count['Sequential Search'] += sequential_search(get_me_random_list(myList),99999999)[1]
            total_time_count['Ordered Sequential Search'] += ordered_sequential_search(get_me_random_list(myList),99999999)[1]
            total_time_count['Binary Search Iterative'] += binary_search_iterative(get_me_random_list(myList),99999999)[1]
            total_time_count['Binary Search Recursive'] += binary_search_recursive(get_me_random_list(myList),99999999)[1]
            num_to_go -= 1

        print("\nFor list of", myList, "items:")

        for myItem in total_time_count:
            myAvg = total_time_count[myItem]/100
            print(myItem, "took%10.7f seconds to run, on average" % myAvg)


if __name__ == "__main__":
    main()