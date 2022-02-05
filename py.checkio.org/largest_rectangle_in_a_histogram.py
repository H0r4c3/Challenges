'https://py.checkio.org/en/mission/largest-histogram/'

'''
You have a histogram. Try to find the size of the biggest rectangle you can build out of the histogram bars.

Input: A list of all rectangles’ heights on the histogram.

Output: Area of the biggest rectangle.
'''

def largest_histogram(histogram):
    all_areas = list()
    h = len(histogram)
    for i in range(h):
        for j in range(i + 1, h + 1):
            length = len(histogram[i:j])
            height = min(histogram[i:j])
            area = length * height
            all_areas.append(area)
            #print(all_areas)
            
    return max(all_areas)



#https://py.checkio.org/mission/largest-histogram/publications/Moff/python-3/first/?ordering=most_voted&filtering=all

def largest_histogram(h):
    result = min(h) * len(h)
    for w in range(1, len(h)):
        for i in range(len(h) - w + 1):
            result = max(result, min(h[i:i + w]) * w)
    return result




if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")

