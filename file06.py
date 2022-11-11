def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file
    m=[]
    
    
    for i in data:
        m.append(len(i))

    return m
print(main(open('txt_file/data06.txt').read().split('\n')))
