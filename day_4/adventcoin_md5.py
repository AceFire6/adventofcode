from hashlib import md5

def find_advent(start_string):
    num = 0
    winning_hash = ''
    while not winning_hash.startswith('00000'):
        hasher = md5()
        hasher.update(start_string)
        hasher.update(str(num))
        winning_hash = hasher.hexdigest()
        num += 1
    return num - 1
    
