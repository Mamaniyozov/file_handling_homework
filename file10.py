def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    m=[]
    for i in data:
        m.append(len(i))
    return max (m)
print(main(open('txt_file/data10.txt').read().split('\n')))