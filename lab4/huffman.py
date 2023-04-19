class Node:
    def __init__(self, val, char=None, left=None, right=None) -> None:
        self.val = val
        self.char = char
        self.left = left
        self.right = right


string = 'I love data structures'


def huffman(string):
    # Queue of characters
    queue = {}
    for c in string:
        if c not in queue:
            queue[c] = 1
        else:
            queue[c] += 1
    queue = list(queue.items())
    queue = sorted(queue, key=lambda q: q[1])

    pqueue = []
    for element in queue:
        pqueue.append(Node(element[1], element[0]))

    # Heap generation
    root = None
    while True:
        element1 = pqueue.pop(0)
        element2 = pqueue.pop(0)
        sum = element1.val + element2.val
        root = Node(sum, None, element1, element2)
        if len(pqueue) == 0:
            break

        to_append = True
        for i in range(len(pqueue)):
            if sum < pqueue[i].val:
                pqueue.insert(i, root)
                to_append = False
                break

        if to_append:
            pqueue.append(root)

    # Codes generation
    codes = {}


print(huffman(string))
