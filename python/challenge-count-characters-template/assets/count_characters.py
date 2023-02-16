def count_characters(input_string):
    character_count = {}
    for char in input_string:
        if char != " ":
            character_count[char] = character_count.get(char, 0) + 1
    return character_count
