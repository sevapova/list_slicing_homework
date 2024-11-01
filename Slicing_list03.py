def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
ls=['a','b','c','d','e']
x=ls[-1::-1]
s = ls + x
print(s)