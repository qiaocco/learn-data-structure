class ArrayTest:
    def test(self):
        # 创建
        a = []

        # 添加元素 O(1)
        a.append("a")
        a.append("b")
        a.append("c")

        # insert O(n)
        a.insert(0, "0")

        # 访问元素 O(1)
        print(a[0])

        # 修改 O(1)
        a[0] = "aaa"
        print(a)

        # 删除O(n)
        a.remove("a")
        print(a)
        # O(1)
        a.pop()

        # 遍历 O(n)
        for item in a:
            print(item)

        # 查找 O(n)
        a.index("b")

        # 排序 O(NlogN)
        a.sort()


ArrayTest().test()
