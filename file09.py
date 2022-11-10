def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    m=[]
    for i in data:
        if i.isdigit():
            m.append(int(i))
    return min(m)
print(main(open('txt_file/data09.txt').read()))