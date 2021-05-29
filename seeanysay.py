#!/usr/bin/python3
# This will generate the seeandsay riddle.
import argparse

def generate(existing):
    current_value = existing[0]
    counter = 0
    return_value = ""

    for i in existing:
        if i == current_value:
            counter += 1
        else:
            return_value += str(counter) + str(current_value)
            current_value = i
            counter = 1
    return return_value

def generate_pattern(start, iterations):
    generate_result = start
    for _ in range(0, iterations):
        generate_result += generate(generate_result)

    return generate_result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create the speak-and-say riddle.')
    parser.add_argument('--start', type=str,
                        help='The start of the sequence', default="1121")
    parser.add_argument('--iterations', type=int, default=10,
                        help='Number of iterations')

    args = parser.parse_args()

    result = generate_pattern(args.start, args.iterations)
    print(result)
