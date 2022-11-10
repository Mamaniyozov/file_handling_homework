def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
# Read data from file
    m=0
    
    for i in data: 
        if i.isdigit():
            m+=int(i)
            
            
    return m
print(main(open('txt_file/data07.txt').read()))