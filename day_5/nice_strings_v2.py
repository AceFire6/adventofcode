def repeated_letter(string):
    for i in xrange(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def contains_double_letter_pair(string):
    for i in xrange(len(string)-2):
        curr_pair = string[i:i+2]
        if curr_pair in string[i+2:]:
            return True
    return False

def count_nice_strings(strings):
    nice_string_count = 0
    for string in strings.split('\n'):
        if (repeated_letter(string) and
            contains_double_letter_pair(string)):
            nice_string_count += 1
    return nice_string_count
