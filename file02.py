def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    

# Read data from file
    m=0
    for i in data:
        m+=1
    return m
print(main(open('txt_file/data02.txt').read()))