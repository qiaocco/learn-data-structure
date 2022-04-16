# 图解 https://www.bilibili.com/video/BV1uh411o7Si?spm_id_from=333.337.search-card.all.click

class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if node.children[ch] is None:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def search_prefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if node.children[ch] is None:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.search_prefix(prefix) is not None


if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    param_2 = obj.search("ap")
    param_3 = obj.startsWith("app")
    print(param_2, param_3)
