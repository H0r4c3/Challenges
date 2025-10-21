'https://py.checkio.org/en/mission/price-research/share/68b08725d563e5b727dfb96028e59670/'


def create_dictionary(reg):
    states_dict = dict()
    states_dict = {tup[0]: (tup[1] / tup[2]) for tup in reg}
    # states_dict = {a: b / c for a, b, c in reg}

    return states_dict


def filter_regions(reg: list[tuple[str, float, float]]) -> list[str]:
    states_dict = create_dictionary(reg)
    print(states_dict)

    # Find keys with values >= 0.7
    result = [key for key, value in states_dict.items() if value <= 0.7]

    # If no keys found, return ["*"]
    if not result:
        return ["*"]

    # Return either a single key or list of keys
    return result


print("Example:")
# print(filter_regions([("AM", 7.00, 10.00), ("RS", 7.01, 10.00)]))

# These "asserts" are used for self-checking
assert filter_regions([("AM", 7.0, 10.0), ("RS", 7.01, 10.0)]) == ["AM"]
assert filter_regions(
    [("SP", 4.9, 5.8), ("RJ", 4.7, 5.7), ("PR", 4.6, 5.6)]) == ["*"]
assert filter_regions(
    [("SC", 5.2, 5.72), ("MT", 4.22, 6.1), ("AL", 5.55, 6.2), ("GO", 4.3, 6.25)]
) == ["MT", "GO"]

print("The mission is done! Click 'Check Solution' to earn rewards!")
