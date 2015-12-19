def at_least_3_vowels(string):
    vowels = 'aeiou'
    vowel_count = 0
    for i in xrange(len(string)):
        if string[i] in vowels:
            vowel_count += 1
        if vowel_count >= 3:
            return True
    return False

def contains_letter_pair(string):
    for i in xrange(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def no_bad_parts(string):
    bad_parts = ('ab', 'cd', 'pq', 'xy')
    for bad_part in bad_parts:
        if bad_part in string:
            return False
    return True    

def count_nice_strings(strings):
    nice_string_count = 0
    for string in strings.split('\n'):
        if (at_least_3_vowels(string) and
            contains_letter_pair(string) and
            no_bad_parts(string)):
               nice_string_count += 1
            
    return nice_string_count
