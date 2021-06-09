class Test:
    def test(self):
        stack = []

        stack.append(1)
        stack.append(2)
        stack.append(3)

        # get top element
        print(stack[-1])

        # remove top element
        temp = stack.pop()
        print(temp)

        # get length
        len(stack)

        # is empty
        len(stack) == 0

        # iterator
        while len(stack) > 0:
            temp = stack.pop()
            print(temp)
