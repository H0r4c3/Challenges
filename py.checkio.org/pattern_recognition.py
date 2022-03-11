'https://py.checkio.org/en/mission/matrix-pattern/'

'''
You should write a program to search a binary matrix (a pattern) within another binary matrix (an image). 
The recognition process consists of scanning the image matrix row by row (horizontal scanning) and when a pattern is located on the image, 
the program must mark this pattern. To mark a located pattern change 1 to 3 and 0 to 2. The result will be the image matrix with the located patterns marked.

The patterns in the image matrix are not crossed, because you should immediately mark the pattern.
'''

def checkio(pattern, image):
    # dimensions of pattern
    columns_pattern = len(pattern[0])
    rows_pattern = len(pattern)
    
    # dimensions of image
    columns_image = len(image[0])
    rows_image = len(image)
    
    for y in range(rows_image - rows_pattern + 1):
        for x in range(columns_image - columns_pattern + 1):
            image_sliced = list()
            for r in range(rows_pattern):
                image_sliced.append(image[y + r][x : x + columns_pattern])
            if image_sliced == pattern:
                for r in range(rows_pattern):
                    image[y + r][x : x + columns_pattern] = map(lambda x: x + 2, image[y + r][x : x + columns_pattern])
                    
    print(image)                
    return image





# Best Solution: 
# https://programtalk.com/vs2/?source=python/6903/checkio/Pattern%20Recognition.py

def checkio_(pattern, image):
    patternWidth = len(pattern[0])
    patternHeight = len(pattern)
    for y in range(len(image) - patternHeight + 1):
        for x in range(len(image[0]) - patternWidth + 1):
            tempMatrix = []
            # take sub matrix
            for i in range(patternHeight):
                tempMatrix.append(image[y + i][x:x + patternWidth])
            if tempMatrix == pattern:
                for i in range(patternHeight):
                    image[y + i][x:x + patternWidth] = map(lambda x: x + 2, image[y + i][x:x + patternWidth])
                    
    return image


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 0], [1, 1]],
                   [[0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                          [0, 3, 3, 0, 0],
                                          [3, 2, 1, 3, 2],
                                          [3, 3, 0, 3, 3],
                                          [0, 1, 1, 0, 0]]
    assert checkio([[1, 1], [1, 1]],
                   [[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]]) == [[3, 3, 1],
                                    [3, 3, 1],
                                    [1, 1, 1]]
    assert checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                         [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                         [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                         [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                         [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                         [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                         [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    print('Done!')