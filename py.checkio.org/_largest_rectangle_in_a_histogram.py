'https://py.checkio.org/en/mission/largest-histogram/'

'''
You have a histogram. Try to find the size of the biggest rectangle you can build out of the histogram bars.

Input: A list of all rectangles’ heights on the histogram.

Output: Area of the biggest rectangle.
'''

def largest_histogram(histogram):
    return max(histogram)


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")

