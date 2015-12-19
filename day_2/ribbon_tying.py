def calculate_ribbon_length(box_dimensions_list):
    total_length = 0
    for box_dimensions in box_dimensions_list.split('\n'):
        dimensions = sorted([int(i) for i in box_dimensions.split('x')])
        total_length += (2 * (dimensions[0] + dimensions[1]) +
                        reduce(lambda x, y : x * y, dimensions))
    return total_length
        
        
