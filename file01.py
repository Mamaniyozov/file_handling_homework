def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    list1=[]
    for i in data.split(','):
        list1.append(int(i))
    return list1
print(main(open('txt_file/data01.txt').read()))
    # Read data from file