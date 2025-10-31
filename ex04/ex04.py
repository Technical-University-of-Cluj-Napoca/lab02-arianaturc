from BST import BST
from search_engine import search_loop

if __name__ == "__main__":
    bst = BST(
        "https://raw.githubusercontent.com/davidxbors/romanian_wordlists/refs/heads/master/wordlists/ro_50k.txt",
        url=True
    )
    search_loop(bst)
