def is_solvable(words, result):
    unique_chars = set("".join(words) + result)

    if len(unique_chars) > 10:
        print("No solution")
        return None

    domains = {char: {str(i): True for i in range(10)} for char in unique_chars}
    character_map = {}

    def is_valid_assignment():
        word_values = [int("".join([str(character_map[c]) for c in word])) for word in words]
        result_value = int("".join([str(character_map[c]) for c in result]))

        return sum(word_values) == result_value

    def assign_value(char, value):
        character_map[char] = value
        for c in domains:
            domains[c][str(value)] = False

    def unassign_value(char, value):
        del character_map[char]
        for c in domains:
            domains[c][str(value)] = True

    def display_addition():
        print("The Solution of the given problem is shown below...\n")
        print("The Character Map is : \n")
        print(character_map, "\n")
        print("\nThe addition operation is illustrated below...\n")
        for word in words:
            word_value = "".join([str(character_map[c]) for c in word])
            print(f"{word_value.rjust(len(result))}")
        print("+" + "-" * (max(len(word) for word in words))) 
        # print(result, "\n")
        # print(character_map, "\n")# Separator line
        result_value = "".join([str(character_map[c]) for c in result])
        print(f"{result_value.rjust(len(result))}")
        print()

    def backtrack():
        if len(character_map) == len(unique_chars):
            if is_valid_assignment():
                return character_map

        char = min(filter(lambda c: c not in character_map, unique_chars), default=None, key=lambda c: len(domains[c]))

        if char is not None:
            for value in domains[char]:
                if domains[char][value]:
                    assign_value(char, int(value))
                    solution = backtrack()
                    if solution:
                        return solution
                    unassign_value(char, int(value))

        return None

    solution = backtrack()
    if solution:
        display_addition()
    else:
        print("No solution....")

# Example usage:
words_input = input("Enter the words separated by space: ").split()
result_input = input("Enter the result word: ")
is_solvable(words_input, result_input)