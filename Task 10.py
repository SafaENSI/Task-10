# input: list of integers of "joltages"

# joltage starts at0
# the joltage of your device is max(joltage)+3
# connect the adapters to power your device
# adapters can connect to joltages (1)(2)(3) joltages
# => find the numbers of 3-gaps and the number of 1-gaps
import sys
from time import perf_counter


def read_file(file):
    try:
        with open(file, 'r') as file:
            content = file.read().strip().split("\n")
            content = list(map(int, content))
            content.append(0)  # joltages starts at 0
            content.append(max(content) + 3)
            content.sort()  # joltages of device is max(joltage)+3
            print(content)

    except:
        print('Error to read file')
        sys.exit()

    return content


if __name__ == "__main__":
    start_timer = perf_counter()
    input_data = read_file("data.txt")
    jolt_1 = 0
    jolt_3 = 0
    for i in range(len(input_data) - 1):
        jolt_x = input_data[i + 1] - input_data[i]
        if jolt_x == 1:
            jolt_1 += 1
        elif jolt_x == 3:
            jolt_3 += 1
    print("Part 1: the number of 1-jolt differences multiplied by the number of 3-jolt differences : " + str(
        jolt_1 * jolt_3))
    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)
