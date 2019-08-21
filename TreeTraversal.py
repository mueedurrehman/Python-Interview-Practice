#Traversal
#Note while True
#Note you are using if and elif
def inOrder(tree):
    stack = []
    results = []
    current = tree #Important so original tree is not modified
    while True:
        if tree is not None:
            stack.append(tree)
            current = current.left
        elif current is None and stack != []:
                current = stack.pop()
                results.append(current)
                current = current.right
        elif current is None and stack == []:
                return results

def preOrder(tree):
    if tree is None:
        return
    stack = []
    results = []
    stack.append(tree)
    while len(stack) > 0:
        current = stack.pop()
        results.append(current)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

