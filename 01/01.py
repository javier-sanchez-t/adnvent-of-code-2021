def read_file(fileName):
    file = open(fileName)
    array = []

    for line in file:
        array.append(int(line))

    file.close();
    return array


def analyze_measurements(measurements):
    increments = 0
    for index in range(len(measurements)-1):
        if measurements[index] > measurements[index-1]:
            increments += 1
    return increments


def analyze_sum_measurements(measurements):
    # It will be an error with previous sum if the data contains less than 3 elements
    previous_sum = measurements[0]+measurements[1]+measurements[2]
    new_sum = 0
    increments = 0
    for index in range(1, len(measurements)-2):
        new_sum = measurements[index]+measurements[index+1]+measurements[index+2]
        if new_sum > previous_sum:
            increments += 1
        previous_sum = new_sum
    return increments


measurements = read_file('data.txt')
# puzzle1
print(analyze_measurements(measurements))
# puzzle2
print(analyze_sum_measurements(measurements))
