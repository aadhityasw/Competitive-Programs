
def populateCounts(end) :
    """
    Given the maximum number through which the table needs to be populated, we form the table.

    Parameters
    ----------
    end - the extent of continuous missing letters in string (or the length of the table needed)

    Return
    ------
    table - with i'th index pointing to the number of possible combinations possible for 'i' missing letters
    """

    # Initialize a table
    # Element at index i : (edge_same[i], edge_different[i])
    table = [(None, None), (25, 24)]

    # Populate the table till the given number
    for i in range(2, end + 1) :
        table.append((
            (25 * table[i-1][1]),
            ((24 * table[i-1][1]) +  (1 * table[i-1][0]))
        ))
    
    # Return the populated table
    return table


def getMissingConfiguration(s) :
    """
    Given a string, returns all the counts of concecutive missing values in the string, in the form of array.
    We also include another value indicating if the edges are same or different
    """

    # Initialize variables for computing and storing the values
    missing_counts = []
    n = len(s)

    # Iterate through the loop and find all the missing letter configurations
    i = 1
    while i < n-1 :
        if s[i] == '?' :
            c = 0
            left_edge = s[i-1]
            while i < n-1 and s[i] == '?' :
                c += 1
                i += 1
            right_edge = s[i]
            missing_counts.append((
                c, (True if left_edge == right_edge else False)
            ))
        else :
            i += 1
    
    # Return the missing congiguration
    return missing_counts


def solveInterrior(s) :
    """
    Given a string with defined edge characters, we find the number of possible ways in which we can fill the blanks.
    Assumption : First and last characters are filled

    Parameters
    ----------
    s - the string with defined edge letters

    Return
    ------
    count - the total number of possible ways to fill the blanks for this edge defined string
    """

    # Get the missing letters configuration from processing the string
    missing_count_configuration = getMissingConfiguration(s)

    # Initialize a variable for storing the overall count
    total_count = 1

    if len(missing_count_configuration) > 0 :

        # Find the maximum number of concecutive missing characters
        max_missing_count = max(missing_count_configuration, key=lambda x : x[0])[0]

        # Fill the DP table
        table = populateCounts(max_missing_count)

        # Compute for every missing configuration
        for (num_missing, same_edge) in missing_count_configuration :
            if same_edge :
                total_count *= table[num_missing][0]
            else :
                total_count *= table[num_missing][1]
    
    return total_count


def solve(s) :
    """
    Given a string with blanks, returns the number of possible ways to fill the blanks with some conditions

    Parameter
    ---------
    s - the string

    Return
    ------
    total_count - the total number of possible ways to fill the blanks
    """

    if len(s) == 0 :
        return 0
    if len(s) == 1 :
        if s == '?' :
            return 26
        return 1
    
    # Check for repeated characters
    n = len(s)
    for i in range(1, n) :
        if (s[i] != '?') and (s[i-1] != '?') and (s[i] == s[i-1]) :
            return 0
    
    # First and last characters filled
    if (s[0] != '?') and (s[-1] != '?') :
        # If first and last characters are not equal
        if (s[0] != s[-1]) :
            return 0
        
        # If first and last characters are equal
        return solveInterrior(s)
    
    # If only first character is filled
    if s[0] != '?' :
        # Copy the first character to the last
        s = s[:-1] + s[0]
        return solveInterrior(s)

    # If only the last character is filled
    if s[-1] != '?' :
        # Copy the last character to the first
        s = s[-1] + s[1:]
        return solveInterrior(s)
    
    # If both first and last characters are missing

    # If the string is just two characters long, and both are missing
    if s == '??' :
        return 0
    
    # Add the 2nd and the 2nd last characters if they are empty
    # The edge letters cannot be equal to these
    avoid_sets = set()
    if s[1] != '?' :
        avoid_sets.add(s[1])
    if s[-2] != '?' :
        avoid_sets.add(s[-2])
    
    # Variable to store the overall count
    total_count = 0

    # For every other letter possible, find the count
    for i in range(97, 123) :
        ch = ord(i)
        if ch not in avoid_sets :
            total_count += solveInterrior(ch + s[1:-1] + ch)
    
    # Return the total count
    return total_count



print(solve("abcd"))
print(solve("abc?"))
print(solve("a?za"))
print(solve("abca"))
print(solve("a??ba"))
print(solve("a???c?b?"))
print(solve("a????cb?"))
print(solve("a???c??b?"))
