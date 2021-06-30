import heapq


class Test:
    def test(self):
        # create minheap
        minheap = []
        heapq.heapify(minheap)
        print(minheap)

        # add element
        heapq.heappush(minheap, 10)
        heapq.heappush(minheap, 8)
        heapq.heappush(minheap, 9)
        heapq.heappush(minheap, 2)
        heapq.heappush(minheap, 1)
        heapq.heappush(minheap, 11)
        print(minheap)

        # peek
        print(minheap[0])

        # delete
        heapq.heappop(minheap)

        # size
        print(len(minheap))

        # iteration
        while len(minheap) != 0:
            print(heapq.heappop(minheap))


if __name__ == '__main__':
    Test().test()
