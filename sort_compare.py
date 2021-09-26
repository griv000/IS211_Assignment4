import random
import time


def insertion_sort(a_list):
    start_time = time.time()
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end_time = time.time()
    time_diff = end_time - start_time
    return time_diff


def shell_sort(a_list):
    start_time = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end_time = time.time()
    time_diff = end_time - start_time
    return time_diff


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value


def python_sort(a_list):
    start_time = time.time()
    a_list.sort()
    end_time = time.time()
    time_diff = end_time - start_time
    return time_diff


def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def main():
    list_sizes = [500, 1000, 5000]
    total_time_count = {'Insertion Sort':0.0,'Shell Sort': 0.0,'Python Sort':0.0}

    for myList in list_sizes:
        num_to_go = 100
        while num_to_go > 0:
            total_time_count['Insertion Sort'] += insertion_sort(get_me_random_list(myList))
            total_time_count['Shell Sort'] += shell_sort(get_me_random_list(myList))
            total_time_count['Python Sort'] += python_sort(get_me_random_list(myList))
            num_to_go -= 1

        print("\nFor list of", myList, "items:")

        for myItem in total_time_count:
            myAvg = total_time_count[myItem]/100
            print(myItem,"took%10.7f seconds to run, on average" % myAvg)


if __name__ == "__main__":
    main()