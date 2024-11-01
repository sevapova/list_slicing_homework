def main(list1,n):
    """
    A list of several elements is given. Return all items except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
l=['a','b','c',1,2,3,4]
n=len(l)
x=l[0:6:2]
print(x)