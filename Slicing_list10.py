def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
l=['a','b',3,4,5,6,7,8]
n=len(l)
x=l[-8:n-3]
print(x)