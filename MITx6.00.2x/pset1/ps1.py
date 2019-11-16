###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time
import datetime

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    start = time.perf_counter_ns()
    trips = []
    # count = 0
    moved_cows = []
    sorted_cows = sorted(cows.items(), key=lambda kv: kv[1], reverse=True)
    # print(sorted_cows)
    while len(moved_cows) < len(cows):
        current_weight = 0
        cargo = []
        for cow_name, weight in sorted_cows:
            if cow_name not in moved_cows:
                # count += 1
                if current_weight + weight <= limit:
                    # del sorted_cows[count - 1]
                    current_weight += weight
                    cargo.append(cow_name)
                    moved_cows.append(cow_name)

        trips.append(cargo)
    end = time.perf_counter_ns() - start
    print(end / 1000000)  # convert nanoseconds to milliseconds
    return trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    names = []
    count = 0
    start = time.perf_counter_ns()
    # start = datetime.datetime.now()
    # start = time.time()
    for partition in get_partitions(sorted(cows.items(), key=lambda kv: kv[1], reverse=True)):
        # print("partition created", partition)
        count += 1
        include_partition = True
        for cow_name_array in partition:
            if sum([c[1] for c in cow_name_array]) > limit:
                include_partition = False
                break
            else:
                names.append([c[0] for c in cow_name_array])

        if include_partition:
            print("Valid partition: ", partition)
            trips = names
            names = []
            # break after first valid partition is found, which contains the least about of trips
            break
    end = time.perf_counter_ns() - start
    # end = datetime.datetime.now() - start
    # end = time.time()
    # print(end - start)
    print(end)
    print(end / 1000000)  # convert nanoseconds to milliseconds
    print("brute force1", count)
    return trips


def brute_force_cow_transport_2(cows,limit=10):
    trip = []
    count = 0
    # start = datetime.datetime.now()
    # start = time.time()
    start = time.perf_counter_ns()
    # for partition in sorted(get_partitions(sorted(cows.items(), key=lambda kv: kv[1], reverse=True)), reverse=True):
    # for partition in get_partitions(sorted(cows.items(), key=lambda kv: kv[1], reverse=True)):
    for partition in sorted(get_partitions(cows.items()),  key=lambda x: len(x)):
        # print("partition created", partition)
        count += 1
        include_partition = True
        for cow_name_array in partition:
            total_weight = 0
            names = []
            for c in cow_name_array:
                name, weight = c
                total_weight += weight
                if total_weight > limit:
                    include_partition = False
                    break
                else:
                    names.append(name)

            if not include_partition:
                break
            else:
                trip.append(names)

            # if sum([c[1] for c in cow_name_array]) > limit:
            #     include_partition = False
            # else:
            #     names = [c[0] for c in cow_name_array]

        if include_partition:
            print("Valid partition: ", partition)
            # trip.append(names)
            # break after first valid partition is found, which contains the least about of trips
            break
    end = time.perf_counter_ns() - start
    # end = datetime.datetime.now() - start
    # end = time.time()
    # print(end - start)
    print(end)
    print(end / 1000000)  # convert nanoseconds to milliseconds
    print("brute force 2", count)
    return trip


def brute_force_cow_transport_clean(cows, limit=10):
    start = time.perf_counter_ns()
    trip = []
    for partition in sorted(get_partitions(cows.items()), key=lambda x: len(x)):
        include_partition = True
        trip = []
        for cow_name_array in partition:
            total_weight = 0
            names = []
            for c in cow_name_array:
                name, weight = c
                total_weight += weight
                if total_weight > limit:
                    include_partition = False
                    break
                else:
                    names.append(name)

            if not include_partition:
                break
            else:
                trip.append(names)

        if include_partition:
            # all_options.append(trip)
            # break after first valid partition is found, which contains the least about of trips
            break

    end = time.perf_counter_ns() - start
    print(end / 1000000)  # convert nanoseconds to milliseconds
    return trip



# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)
print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))
# print(brute_force_cow_transport_2(cows, limit))
print(brute_force_cow_transport_clean(cows, limit))


# cows = {'Lotus': 40, 'Horns': 25, 'Boo': 20, 'Milkshake': 40, 'MooMoo': 50, 'Miss Bella': 25}
# print(brute_force_cow_transport_2(cows, 100))
# print(brute_force_cow_transport_clean(cows, 100))


'''
cargo = []
part_cargo_count = 0

for cow_name_array in partition:
    # print(cow_name_array)
    current_weight = 0
    for cow_name in cow_name_array:
        current_weight += cows[cow_name]
        # current_weight = [c[1] for c in cows if c[0] == cow_name]
        # cargo_weight += current_weight
        cargo.append(cow_name)

        if current_weight > limit:
            cargo = []
            break

    if len(cargo) == 0:
        break

    part_cargo_count += 1

if part_cargo_count == len(partition):
    trips.append(partition)
    
      # print(count)  # 115975
    # print(cows)


    start = time.time()
    for partition in get_partitions(sorted(cows.items(), key=lambda kv: kv[1], reverse=True)):
        # print(partition)
        count += 1

    end = time.time()
    print(end - start)  # 0.5056478977203369
    print(count)  # 115975
    print(cows)    
   
   
   
               if sum([c[1] for c in cow_name_array]) <= limit:
                trips.append([c[0] for c in cow_name_array])
            else:
    
'''


