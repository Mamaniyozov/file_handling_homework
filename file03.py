def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
 
# Read data from file
    m=[]

    for i in data:
        if i.isdigit():

            m.append(i)
    return m



s=open('txt_file/data03.txt').read()
print(main(s))