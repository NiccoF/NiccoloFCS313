"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Nicco Faelnar, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: nvf89
"""

import sys

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------
RESET_CHAR = "\u001b[0m"  # Code to reset the terminal color
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
}
BLOCK_CHAR = "\u2588"  # Character code for a block


def colored(text, color):
    """Wrap the string with the color code."""
    color = color.strip().lower()
    if color not in COLOR_DICT:
        raise ValueError(color + " is not a valid color!")
    return COLOR_DICT[color] + text


def print_block(color):
    """Print a block in the specified color."""
    print(colored(BLOCK_CHAR, color) * 2, end="")


# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------


class Node:
    """
    Represents a node in a singly linked list.

    Instance Variables:
        data: The value or data stored in the node.
        next: The reference to the next node in the linked list (None by default).
    """

    def __init__(self, data, next=None):
        """
        Initializes a new node with the given data and a reference to the next node.

        Args:
            data: The data to store in the node.
            next: Optional; the next node in the linked list (None by default).
        """
        self.data = data
        self.next = next


class StackError(Exception):
    """StackError"""
    # pass


class Stack:
    """Stack"""
    def __init__(self):
        self._top = None
        self._size = 0

    def peek(self):
        """shows what item is on top"""
        if self.is_empty():
            raise StackError("Peek from empty stack.")
        return self._top.data

    def push(self, item):
        """places an item on top"""
        new_node = Node(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1

    def pop(self):
        """returns the top item"""
        if self.is_empty():
            raise StackError("Pop from empty stack.")
        removed_data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return removed_data

    def is_empty(self):
        """if it's empty"""
        return self._top is None

    def size(self):
        """returns number of elements"""
        return self._size


class QueueError(Exception):
    """QueueError"""
    # pass


class Queue:
    """
    A class that implements a queue using a singly linked list with a tail.

    Instance Variables:
        _front: The beginning node of the queue.
        _rear: The end node of the queue.
        _size: The number of elements in the queue.
    """

    def __init__(self):
        """
        Initializes an empty queue with no elements.
        """
        self._front = None
        self._rear = None
        self._size = 0

    def peek(self):
        """
        Returns the value at the front of the queue without removing it.

        Raises:
            QueueError: If the queue is empty, raises "Peek from empty queue.".

        Returns:
            The data stored in the front node of the queue.
        """
        if self.is_empty():
            raise QueueError("Peek from empty queue.")
        return self._front.data

    def enqueue(self, item):
        """
        Enqueues a new item at the end of the queue.

        Args:
            item: The data to put at the end of queue.
        """
        new_node = Node(item)
        if self.is_empty():
            self._front = new_node
        else:
            self._rear.next = new_node
        self._rear = new_node
        self._size += 1

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.

        Raises:
            QueueError: If the queue is empty, raises "Dequeue from empty queue.".

        Returns:
            The data from the front node of the queue.
        """
        if self.is_empty():
            raise QueueError("Dequeue from empty queue.")
        front_data = self._front.data
        self._front = self._front.next
        if self._front is None:  # If queue becomes empty
            self._rear = None
        self._size -= 1
        return front_data

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self._size == 0

    def size(self):
        """
        Returns the number of items in the queue.

        Returns:
            The size of the queue as an integer.
        """
        return self._size


class ColoredVertex:
    """Class for a graph vertex."""

    def __init__(self, index, x, y, color):
        self.index = index
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    def add_edge(self, vertex_index):
        """Add an edge to another vertex."""
        self.edges.append(vertex_index)

    def visit_and_set_color(self, color):
        """Set the color of the vertex and mark it visited."""
        self.visited = True
        self.prev_color = self.color
        self.color = color
        print("Visited vertex " + str(self.index))

    def __str__(self):
        return f"index: {self.index}, color: {self.color}, x: {self.x}, y: {self.y}"


class ImageGraph:
    """Class for the graph."""

    def __init__(self, image_size):
        self.vertices = []
        self.image_size = image_size

    def print_image(self):
        """Print the image formed by the vertices."""
        img = [
            ["black" for _ in range(self.image_size)] for _ in range(self.image_size)
        ]

        # Fill img array
        for vertex in self.vertices:
            img[vertex.y][vertex.x] = vertex.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # Print new line/reset color
        print(RESET_CHAR)

    def reset_visited(self):
        """Reset the visited flag for all vertices."""
        for vertex in self.vertices:
            vertex.visited = False

    # Create the adjacency matrix.
    # Return the matrix at the end
    def create_adjacency_matrix(self):
        """
        Creates and returns the adjacency matrix for the graph.

        post: return a 2D list of integers representing the adjacency matrix.
        """
        matrix = [[0 for _ in range(5)] for _ in range(5)]
        for vertex in self.vertices:
            for edge in vertex.edges:
                matrix[edge[0]][edge[1]] = 1
        return matrix

    def bfs(self, start_index, color):
        """
        You must implement this algorithm using a Queue.

        Performs a Breadth-First Search (DFS) starting from a given vertex, changing
        all vertices that are adjacent and share the same color as the starting
        vertex's color to the given color. Think of how an image bucket fill will
        only change all same colored pixels that are in contact with each other.

        Do not remove the first 2 statements we provide.
        you may choose to call print_images in this method debugging yourself


        This method assumes that the pre conditions have been handled before
        calling this method.

        pre: start_index is a valid integer representing the index of the starting
             vertex in the vertices instance variable.
             color: The color to change vertices to during the DFS traversal

        post: every vertex that matches the start index's color will be recolored
              to the given color
        """

        self.reset_visited()
        print("Starting BFS; initial state:")
        self.print_image()

        original_color = self.vertices[start_index].color
        vert_queue = Queue()
        vert_queue.enqueue(self.vertices[start_index])
        while not vert_queue.is_empty():
            current = vert_queue.dequeue()
            for edge in current.edges:
                if edge[1].color == original_color:
                    edge.color = color
                    vert_queue.enqueue(edge[1])
            current.color = color


    def dfs(self, start_index, color):
        """
        You must implement this algorithm using a Stack WITHOUT using recursion.

        Performs a Depth-First Search (DFS) starting from a given vertex, changing
        all vertices that are adjacent and share the same color as the starting
        vertex's color to the given color. Think of how an image bucket fill will
        only change all same colored pixels that are in contact with each other.

        Do not remove the first 2 statements we provide.
        you may choose to call print_images in this func method debugging yourself


        This method assumes that the pre conditions have been handled before
        calling this method.

        pre: start_index is a valid integer representing the index of the starting
             vertex in the vertices instance variable.
             color: The color to change vertices to during the DFS traversal

        post: every vertex that matches the start index's color will be recolored
              to the given color
        """

        self.reset_visited()
        print("Starting DFS; initial state:")
        self.print_image()

        original_color = self.vertices[start_index].color
        # adj_matrix = self.create_adjacency_matrix
        vert_stack = Stack()
        vert_stack.push(self.vertices[start_index])
        while not vert_stack.is_empty():
            current = vert_stack.pop()
            for edge in current.edges:
                if edge[1].color == original_color:
                    edge.color = color
                    vert_stack.push(edge[1])
            current.color = color


def create_graph(data):
    """
    Creates a Graph object from the given input data and parses the starting
    position and search color.

    pre: data is the entire inputted data as a single string.

    post: a tuple containing the ImageGraph instance, the starting position,
          and the search color.
    """
    line_list = []
    # split the data by new line
    line_list = data.split("\n")
    # get size of image and number of vertices
    size = int(line_list[0])
    num_vertices = int(line_list[1])
    # create the ImageGraph
    new_graph = ImageGraph(size)
    # create vertices - vertex info has the format "x,y,color"
    for i in range(num_vertices):
        vert_list = line_list[i+2].split(",")
        x = int(vert_list[0])
        y = int(vert_list[1])
        color = vert_list[2]
        new_graph.vertices.append(ColoredVertex(i, x, y, color))
    # create edges between vertices - edge info has the format "from_index,to_index"
    # connect vertex A to vertex B and the other way around
    num_edges = int(line_list[num_vertices + 2])
    for i in range(num_edges):
        edge_vertex_indexes = line_list[num_vertices + 3 + i].split(",")
        new_graph.vertices[int(edge_vertex_indexes[0])].add_edge(int(edge_vertex_indexes[1]))
    # read search starting position and color
    last_line_list = line_list[len(line_list) - 1].split(",")
    start_position = int(last_line_list[0])
    start_color = last_line_list[1]
    # return the ImageGraph, starting position, and color as a tuple in this order.
    return (new_graph, start_position, start_color)

def main():
    """
    The main function that drives the program execution.

    This function will not be tested, but you should
    implement it to test your code visually.
    """

    # read all input as a single string.
    data = sys.stdin.read()

    # create graph, passing in data
    new_graph_items = create_graph(data)
    new_graph = new_graph_items[0]
    start_pos = new_graph_items[1]
    start_color = new_graph_items[2]
    # print adjacency matrix in a readable format (maybe row by row)
    matrix = new_graph.create_adjacency_matrix()
    for row in matrix:
        print(row)
    # run bfs
    new_graph.bfs(start_pos, start_color)
    # reset by creating graph again
    new_graph_items = create_graph(data)
    new_graph = new_graph_items[0]
    start_pos = new_graph_items[1]
    start_color = new_graph_items[2]
    # run dfs
    new_graph.dfs(start_pos, start_color)

if __name__ == "__main__":
    main()
