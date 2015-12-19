import os

def make_folders(gitkeep=False):
    day_temp = 'day_%d'
    for i in range(25):
        i += 1
        day_f = day_temp % i
        if not os.path.exists(day_f):
            os.mkdir(day_f)
        if gitkeep:
            gitkeep_f = os.path.join(day_f, '.gitkeep')
            if not os.path.exists(gitkeep_f):
                open(gitkeep_f, 'w').close()
