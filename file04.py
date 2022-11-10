def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file 
    m=[]
    for i in data:
        if i.isalpha():
            m.append(i)
    return m
print(main(open('txt_file/data04.txt').read()) )