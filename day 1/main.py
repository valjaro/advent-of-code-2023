# # Part 1
with open('day 1\input.txt') as f:
    lines = f.readlines()
    numbers = []
    for line in lines:
        line = line.strip()
        for i in line:
            if i.isdigit():
                n = i
                break
        for y in range(len(line) - 1, -1, -1):
            if line[y].isdigit():
                m = line[y]
                break
        numbers.append(int(n + m))
print(sum(numbers))

# #### ###Part 2
with open('day 1\input.txt') as f:
    words_to_check = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    words_values = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    numbers = []

    for line in f:
        line = line.strip()

        first_occurrence_index = float('inf')
        first_occurrence_word = None
        last_occurrence_index = -1
        last_occurrence_word = None

        for word in words_to_check:
            index = line.find(word)
            if index != -1 and index < first_occurrence_index:
                first_occurrence_index = index
                first_occurrence_word = word

            rindex = line.rfind(word)
            if rindex != -1 and rindex > last_occurrence_index:
                last_occurrence_index = rindex
                last_occurrence_word = word

        if first_occurrence_word and last_occurrence_word:
            if first_occurrence_word in words_values:
                first_occurrence_word = words_values[first_occurrence_word]
            if last_occurrence_word in words_values:
                last_occurrence_word = words_values[last_occurrence_word]

            numbers.append(int(first_occurrence_word + last_occurrence_word))

print(sum(numbers))

