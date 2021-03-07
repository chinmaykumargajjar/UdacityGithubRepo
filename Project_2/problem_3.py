class Node:

    def __init__(self, frequency, character, child_num):
        self.character = character
        self.frequency = frequency
        self.left_child = None
        self.right_child = None
        self.child_num = child_num

    def set_left_child(self, left_child):
        self.left_child = left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_char(self):
        return self.character

    def get_freq(self):
        return self.frequency

    def has_left_child(self):
        if self.left_child is None:
            return False
        else:
            return True

    def has_right_child(self):
        if self.right_child is None:
            return False
        else:
            return True

    def set_child_num(self, num):
        self.child_num = num

    def get_child_num(self):
        if self.child_num is not None:
            return str(self.child_num) + ""
        else:
            return ""

    def info(self):
        #print("char, freq,  childnum", self.character, self.frequency, self.child_num)
        pass

test_node = Node(11, "D", 0)
#print(test_node.get_char())
#print(test_node.get_freq())
# test_node.set_child_num(1)
#print(test_node.get_child_num())
#print(test_node.info())

test_node_left = Node(12, "C", 1)
test_node_right = Node(6, "T", 0)
#print("has_left", test_node.has_left_child(), "has_right", test_node.has_right_child())

test_node.set_left_child(test_node_left)
test_node.set_right_child(test_node_right)

#print("has_left", test_node.has_left_child(), "has_right", test_node.has_right_child())

#print("left_char", test_node.get_left_child().get_char())
#print("right_char", test_node.get_right_child().get_char())


########
class Tree:

    def __init__(self, node):
        self.head = node

    def get_head(self):
        return self.head

#####
# Priority Queue
# Add operation that automatically adds item and and sorts from lower to higher
# POP operation that removes two minimum counts from queue
class PriorityQueue:

    def __init__(self):
        self.list = list()

    def add(self, item):
        self.list.append(item)
        self.list.sort(key=lambda x: x.frequency, reverse=False)

    def pop(self):
        if len(self.list) > 1:
            return self.list.pop(0), self.list.pop(0)
        elif len(self.list) == 1:
            return self.list.pop(0), Node(None, None, None)
        else:
            return None

    def size(self):
        return len(self.list)


queue = PriorityQueue()

node1 = Node(1, None, None)
node2 = Node(2, None, None)
node3 = Node(3, None, None)

queue.add(node3)
queue.add(node2)
queue.add(node1)

result_0 = queue.pop()
result_1 = queue.pop()
#print(result_0[0].frequency, result_0[1].frequency)
#print(result_1[0].frequency, result_1[1].frequency)


#######
import sys


def get_huffman_code(char, frequency, tree, code):
    # Traverse the tree
    if tree:
        if tree.get_child_num().isdigit():
            code = code + tree.get_child_num()

        if tree.get_char() == char:
            # #print(code)
            return code

        result = get_huffman_code(char, frequency, tree.get_left_child(), code)
        if not result:
            result = get_huffman_code(char, frequency, tree.get_right_child(), code)
        return result


node_2d_0 = Node(2, "D", 0)
node_3b_1 = Node(3, "B", 1)

node_5 = Node(5, None, 0)
node_5.set_left_child(node_2d_0)
node_5.set_right_child(node_3b_1)
node_6e_1 = Node(6, "E", 1)

node_11 = Node(11, None, 0)
node_11.set_left_child(node_5)
node_11.set_right_child(node_6e_1)

node_7a_0 = Node(7, "A", 0)
node_7c_1 = Node(7, "C", 1)

node_14 = Node(14, None, 1)
node_14.set_left_child(node_7a_0)
node_14.set_right_child(node_7c_1)

node_25 = Node(25, None, None)
node_25.set_left_child(node_11)
node_25.set_right_child(node_14)

code = ""
code = get_huffman_code("C", 7, node_25, code)
#print(code)

######
def find_char(temp_list, tree):
    current = tree
    lst = list()
    lst.extend(temp_list)

    while len(lst) > 0:
        pop_item = lst.pop(0)
        if pop_item == '1':
            current = current.get_right_child()
        else:
            current = current.get_left_child()
    if current.get_char():
        #print(temp_list, current.get_char())
        pass
    return current.get_char()

#########
def huffman_encoding(data):
    # Count frequency of all characters
    items_count = dict()
    for char in data:
        if char in items_count:
            items_count[char] = items_count[char] + 1
        else:
            items_count[char] = 1

    queue = PriorityQueue()
    for character, frequency in items_count.items():
        node = Node(frequency, character, None)
        queue.add(node)

    result = queue.pop()
    # while result: #TestCode
    #   #print(result[0].character, result[0].frequency)
    #    #print(result[1].character, result[1].frequency)
    #    result = queue.pop()
    continueLoop = True
    # Build tree using queue
    while continueLoop:

        # #print(result[1].character, result[0].character)
        if queue.size() <= 0:
            continueLoop = False
        # Build a Node and put into Tree, if both results are there
        if result[1]:
            new_freq = result[0].frequency + result[1].frequency
            merge_node = Node(new_freq, None, None)
            # Set left and right children
            if result[0].frequency <= result[1].frequency:
                result[0].set_child_num(0)
                merge_node.set_left_child(result[0])
                result[1].set_child_num(1)
                merge_node.set_right_child(result[1])
            else:
                result[1].set_child_num(0)
                merge_node.set_left_child(result[1])
                result[0].set_child_num(1)
                merge_node.set_right_child(result[0])

            queue.add(merge_node)
        result = queue.pop()
    tree = result[0]

    encoded_data = ""
    # Change of hashtable vales to Huffmancode
    # #print("_______")
    for character, frequency in items_count.items():
        huffman_code = get_huffman_code(character, frequency, tree, "")
        items_count[character] = huffman_code
        # #print(character, frequency, huffman_code)

    for char in data:
        encoded_data = encoded_data + items_count[char]

    return encoded_data, tree
    # Result[0] should be the total merged node


def huffman_decoding(data, tree):
    decoded = ""
    data_list = [x for x in data]

    temp_list = list()
    while len(data_list) > 0:
        temp_list.append(data_list.pop(0))
        char = find_char(temp_list, tree)
        if char:
            decoded = decoded + char
            temp_list = list()
    return decoded


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


#####
