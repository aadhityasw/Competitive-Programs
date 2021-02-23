INPUT_FILE_NAME = "../questions/README.md"
TEMPORARY_FILE_NAME = "./readme.txt"


def make_changes(line) :
    """
    Given a line of the input file, we make the necessary changes and then return the same line.
    """

    # Converts "| 1 | [Game Of Names](/q1_game_of_names) |" into "| 1 | [Game Of Names](./q1_game_of_names) |"
    index = line.find("/q")

    if index >= 0 :
        modifiedLine = line[:index] + '.' + line[index:]
    else :
        modifiedLine = line

    return modifiedLine


def modify_file(input_file_name, temp_file_name) :
    """
    Given a file name performs a change and prints the output in a temporary file.
    """

    modifiedLines = ""

    with open(input_file_name, 'r') as file :
        for line in file :
            modifiedLines += make_changes(line)

    with open(temp_file_name, 'w') as file :
        file.write(modifiedLines)
    
    print(f"Modified text has been written in the file {temp_file_name}")



modify_file(INPUT_FILE_NAME, TEMPORARY_FILE_NAME)
