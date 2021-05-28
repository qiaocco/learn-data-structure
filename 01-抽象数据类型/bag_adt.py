class Bag:
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self._items = list()

    def add(self, item):
        if len(self._items) >= self.maxsize:
            raise Exception("Full")
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag(maxsize=3)
    bag.add(1)
    bag.add(2)
    bag.add(3)
    assert len(bag) == 3
    # bag.add(4) # Full
    bag.remove(3)
    assert len(bag) == 2
    for item in bag:
        print(item)


if __name__ == "__main__":
    test_bag()
