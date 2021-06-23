class Test:
    def test(self):
        s = set()

        # add element
        s.add(10)
        s.add(3)
        s.add(5)
        s.add(2)
        s.add(2)
        print(s)

        # search
        res = 2 in s
        print(res)

        # size
        print(len(s))


if __name__ == '__main__':
    Test().test()
