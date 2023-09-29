'https://py.checkio.org/en/mission/huffman-encode/share/e897d074b50c4e388bfaff16ffcbda33/'

'''
The simplest construction algorithm uses a priority queue where the node with lowest frequency is given highest priority.

Create a leaf node for each symbol and add it to the priority queue.
While there is more than one node in the queue:
Remove the two nodes of highest priority (lowest frequency) from the queue
Create a new internal node with these two nodes as children and with frequency equal to the sum of the two nodes' frequencies.
Add the new node to the queue.
The remaining node is the root node and the tree is complete.
'''

# https://github.com/arnab132/Huffman-Coding-Python/blob/main/huff.py

string = 'BADABUM'

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))



if __name__ == "__main__":
    print("Example:")
    print(huffman_encode("BADABUM"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert huffman_encode("BADABUM") == "1001110011000111"
    assert (
        huffman_encode("A DEAD DAD CEDED A BAD BABE A BEADED ABACA BED")
        == "1000011101001000110010011101100111001001000111110010011111011111100010001111110100111001001011111011101000111111001"
    )
    assert (
        huffman_encode("no devil lived on")
        == "100101111000001110010011111011010110001000111101100"
    )
    assert huffman_encode("an assassin sins") == "110111100110001100010111110001011110"

    print("Huffman Encode coding complete? Click 'Check' to earn cool rewards!")