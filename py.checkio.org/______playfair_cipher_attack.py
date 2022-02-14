'https://py.checkio.org/en/mission/playfair-cipher-attack/share/3d4b62b955c8fedf5f7a004001047145/'

'''
Playfair cipher used a 5x5 key table filled with 25 letters of English alphabet in random order (letter J is omitted). 
Message is broken up into pairs of letters (each pair must consist of two different letters, 
otherwise letter X is inserted between them). Then each bigram is encrypted according to following rules:

1. If both letters are in the same row of key table, each is replaced by the letter to it's immediate right (the last column wraps around to the first);

2. If the letters appear in the same column - each is replaced with the one below it (the bottom row wraps around to the top);

3. If the letters are at diagonally opposite corners of a rectangle, they are replaced with letters at other two corners. 
The order is important - the first letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair
'''

def playfair_attack(plaintext: str, cryptogram: str) -> str:
    # your code here
    return ""


if __name__ == "__main__":
    print("Example:")
    print(
        playfair_attack(
            "sixcrazykingsvowedtoabolishmyquitepitifulioust",
            "zlgrcekqztvoolunhbvkemsvlzadnpzflrqlvlhwtluzkl",
        )
    )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        playfair_attack(
            "sixcrazykingsvowedtoabolishmyquitepitifulioust",
            "zlgrcekqztvoolunhbvkemsvlzadnpzflrqlvlhwtluzkl",
        )
        == "vklprhcrixbpzebc"
    )

    assert (
        playfair_attack(
            "pythonsxstandardlibraryisveryextensiveofferingawiderangeofstuffx",
            "aiwblarskwphydowzehmhoieksxlixgwvufxlvzqvizxbehdycxlphyxzqkwcvsi",
        )
        == "dmhfiulxgbxvqhyx"
    )

    assert (
        playfair_attack(
            "zombiesquicklyatetwelveofmyneighboursx",
            "uzuywyksmzdcvhfgtnftonbnkfevywlgxzmxzd",
        )
        == "xnzpchtyrfcwpkth"
    )

    print("Coding complete? Click 'Check' to earn cool rewards!")