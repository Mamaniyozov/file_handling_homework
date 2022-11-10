def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file
    m=0
    n=0
    k=[n,m]
    for i in data:
        if not i.isdigit():
            m+=1
    for s in data:
        if s.isdigit():
            n+=1
        k=[n,m]
    return k
print(main(open('txt_file/data05.txt').read()))