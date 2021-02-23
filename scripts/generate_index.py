STARTING_INDEX = 160
ENDING_INDEX = 180
FILE_NAME = "index.txt"

def generate(start, end, file_name) :
    """
    Given the starting and the ending index anf the neme of the file, we print the indices in the format in that file.
    """

    formatted_indices = ""

    for i in range(start, end+1) :
        formatted_indices += f"| {i} | [](/q{i}) |\n"

    with open(file_name, 'w') as file :
        file.write(formatted_indices)
    
    print("Indices have been written in the file")



generate(STARTING_INDEX, ENDING_INDEX, FILE_NAME)