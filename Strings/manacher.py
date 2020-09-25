def palindromic_length(center, diff, string):
    if (center - diff == -1 or center + diff == len(string)
            or string[center - diff] != string[center + diff]):
        return 0
    return 1 + palindromic_length(center, diff + 1, string)


def palindromic_string(input_string):
    max_length = 0

    new_input_string = ""
    output_string = ""

    for i in input_string[:len(input_string) - 1]:
        new_input_string += i + "|"
    new_input_string += input_string[-1]

    for i in range(len(new_input_string)):

        length = palindromic_length(i, 1, new_input_string)

        if max_length < length:
            max_length = length
            start = i

    for i in new_input_string[start - max_length:start + max_length + 1]:
        if i != "|":
            output_string += i

    return output_string


if __name__ == "__main__":
    n = input()
    print(palindromic_string(n))
