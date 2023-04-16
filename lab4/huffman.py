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

    # Heap
    heap = {}


print(huffman(string))
