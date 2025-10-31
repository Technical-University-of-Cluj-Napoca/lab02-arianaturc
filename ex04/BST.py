import sys
import urllib.request


class Node:

    def __init__(self, word: str):
        self.word = word
        self.left = None
        self.right = None

class BST:
    def __init__(self, source: str, **kwargs):
        self.root = None
        self.results = []

        words = []

        url = kwargs.get("url", False)
        file = kwargs.get("file", False)

        if url and file:
            sys.exit("URL and file can't be uses at the same time.")

        if url:
            with urllib.request.urlopen(source) as response:
                data = response.read().decode("utf-8")
                words = [w.strip() for w in data.splitlines() if w.strip()]
        elif file:
            with open(source, 'r', encoding="utf-8") as f:
                words = [w.strip() for w in f if w.strip()]

        if words:
            self.root = self._build_bst(sorted(words))

    def _build_bst(self, words):
        if not words:
            return None

        mid = len(words) // 2
        node = Node(words[mid])
        node.left = self._build_bst(words[:mid])
        node.right = self._build_bst(words[mid + 1:])
        return node

    def autocomplete(self, prefix: str) -> list[str]:
        self.results = []
        self._collect(self.root, prefix)
        return self.results

    def _collect(self, node: Node, prefix: str) -> None:
        if not node:
            return

        if node.word >= prefix:
            self._collect(node.left, prefix)

        if node.word.startswith(prefix):
            self.results.append(node.word)

        if node.word <= prefix or node.word.startswith(prefix):
                self._collect(node.right, prefix)

