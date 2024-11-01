def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
l=['a','b','c','d','e','f']
n=len(l)
x=l[n::-1]
print(x)