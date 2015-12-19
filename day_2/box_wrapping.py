def calculate_wrapping_paper(box_dimensions_list):
    total_paper = 0
    for box_dimensions in box_dimensions_list.split('\n'):
        l, w, h = [int(i) for i in box_dimensions.split('x')]
        sides = [l*w, w*h, h*l]
        total_paper += sum(2*i for i in sides) + min(sides)
    return total_paper
