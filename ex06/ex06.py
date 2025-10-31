import sys

import requests
from bs4 import BeautifulSoup


def dict_definition(word: str) -> str:

    url = f"https://dexonline.ro/definitie/{word}"


    try:
        response = requests.get(url)
        response.raise_for_status()

        s = BeautifulSoup(response.text, "html.parser")
        definition = s.find('span', class_='tree-def html')

        if not definition:
            return f"No definition found for '{word}'"

        definition_text = definition.get_text(strip=True)
        return definition_text

    except requests.exceptions.RequestException as e:
        return f"Error fetching definition: {e}"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: python ex06.py <word>")

    word = sys.argv[1]
    definition = dict_definition(word)
    print(definition)

