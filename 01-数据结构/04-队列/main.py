from collections import deque


class Test:
    def test(self):
        queue = deque()

        # add element
        queue.append(1)
        queue.append(2)
        queue.append(3)
        print(deque)

        # get the head of the queue
        temp = queue[0]
        print(temp, queue)

        # remove head element
        temp2 = queue.popleft()
        print(temp2)  # 1

        print(len(queue))

        while len(queue) != 0:
            temp = queue.popleft()
            print(temp)




Test().test()
