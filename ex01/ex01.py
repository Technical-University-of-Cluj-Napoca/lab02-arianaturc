import sys
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_dictionary = defaultdict(list)

    for s in strs:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        dict_key = tuple(freq)
        anagram_dictionary[dict_key].append(s) #if the key does not exist, it creates a list for the new key

    return list(anagram_dictionary.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))