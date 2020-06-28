sample_list = [1,2,3,4,5,6,7,8,9,10]

def find_square(sample_list):
    print("\nSquare numbers of the sample list:")
    square_numbers_list = list(map(lambda x: x**2, sample_list))
    print(square_numbers_list)
    print("\r")

def find_cube(sample_list):
    print("\nCube numbers of the sample list:")
    cube_numbers_list = list(map(lambda x: x**3, sample_list))
    print(cube_numbers_list)

find_square(sample_list)
find_cube(sample_list)