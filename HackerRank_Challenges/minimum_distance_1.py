'https://www.geeksforgeeks.org/minimum-distance-between-any-two-equal-elements-in-an-array/'

# Python3 program to find the minimum distance
# between two occurrences of the same element
 
# Function to find the minimum
# distance between the same elements
def minimumDistance(a):
 
    # Create a HashMap to
    # store (key, values) pair.
    hmap = dict()
    minDistance = 10**9
 
    # Initialize previousIndex
    # and currentIndex as 0
    previousIndex = 0
    currentIndex = 0
 
    # Traverse the array and
    # find the minimum distance
    # between the same elements with map
    for i in range(len(a)):
 
        if a[i] in hmap:
            currentIndex = i
 
            # Fetch the previous index from map.
            previousIndex = hmap[a[i]]
 
            # Find the minimum distance.
            minDistance = min((currentIndex -
                        previousIndex), minDistance)
 
        # Update the map.
        hmap[a[i]] = i
 
    # return minimum distance,
    # if no such elements found, return -1
    if minDistance == 10**9:
        return -1
    return minDistance
 
# Driver code
if __name__ == '__main__':
     
    # Test Case 1:
    a1 = [1, 2, 3, 2, 1 ]
    print(minimumDistance(a1))
 
    # Test Case 2:
    a2 = [3, 5, 4, 6, 5,3]
    print(minimumDistance(a2))
 
    # Test Case 3:
    a3 = [1, 2, 1, 4, 1 ]
    print(minimumDistance(a3))