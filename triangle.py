from random import randint


class Node:

    def __init__(self, number=0, index=0, depth=0):
        self._data = number
        self.index = index
        self.depth = depth
        self.left_child = None
        self.right_child = None
        self.bigger_child = None
        self.most_efficient_route = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def l_child_insert(self, node):
        self.left_child = node

    def r_child_insert(self, node):
        self.right_child = node

    @property
    def has_children(self):
        """Check if has at least 1 active child"""
        return self.left_child is not None or self.right_child is not None

    def get_child_list(self):
        child_list = list()
        if self.left_child is not None:
            child_list.append(self.left_child)
        if self.right_child is not None:
            child_list.append(self.right_child)
        return child_list

    def most_valuable_child_determine(self):
        if self.has_children:
            child_list = self.get_child_list()

            for child in child_list:
                child.most_valuable_child_determine()

            self.bigger_child = child_list[0]
            if self.bigger_child.calculate() < child_list[1].calculate():
                self.bigger_child = child_list[1]
        else:
            print('{0} has no children'.format(self))

    def calculate(self):
        """
        Summarize data from every most efficient child down the way

        :return: maximum sum from every most valuable downward nodes
        """
        child_value = 0
        if self.bigger_child:
            child_value = self.bigger_child.calculate()

            child_value = self.bigger_child.data

        return self.data + child_value

    def __repr__(self):
        indexed = False
        if indexed:
            string = ('(' + '{:>2}'.format(self.depth) + ',' +
                      '{:>2}'.format(self.index) + ') ')
        else:
            string = ''
        string += '{:>4}'.format(self.data)
        return string

    def __str__(self):
        string = '{:>4}'.format(self.data) + '\n'
        if self.has_children:
            string += '{:>4}'.format(self.left_child.data) + ' ' \
                      + '{:>4}'.format(self.right_child.data)
        return string


class NumberTriangle:

    def __init__(self, set_of_numbers=None, max_depth=3, randomize=True):
        self.sequences = list()
        if set_of_numbers:
            self._generate_certain_triangle(set_of_numbers)
        elif randomize:
            self._generate_random_triangle(max_depth)
        else:
            self._generate_default_triangle(max_depth)
        self._bind_children()

    def _generate_certain_triangle(self, set_of_numbers):
        for depth, sub_list in enumerate(set_of_numbers):
            sequence = [Node(number=value, depth=depth, index=index)
                        for index, value in enumerate(sub_list)]
            self.sequences.append(sequence)

    def _generate_random_triangle(self, max_depth):
        for depth in range(max_depth):
            # 0th depth cannot be iterated, hence start with 1
            if depth:
                sequence = [Node(number=randint(0, 100),
                                 depth=depth - 1,
                                 index=num)
                            for num in range(depth)]
                self.sequences.append(sequence)

    def _generate_default_triangle(self, max_depth):
        value = 0
        for depth in range(max_depth):
            sequence = list()
            for index in range(depth):
                node = Node(number=value, depth=depth, index=index)
                sequence.append(node)
                value += 1
            self.sequences.append(sequence)

    def _bind_children(self):
        for seq_index, sequence in enumerate(self.sequences[:-1]):
            for index, node in enumerate(sequence):
                node.l_child_insert(self.sequences[seq_index + 1][index])
                node.r_child_insert(self.sequences[seq_index + 1][index + 1])

    def __str__(self):
        string = 'Triangle\n'
        for sequence in self.sequences:
            string += str(sequence) + '\n'
        string += '\n' + '-' * 50
        return string


if __name__ == '__main__':
    triangle = NumberTriangle(max_depth=15)
    print(triangle)

    some_set = ([14], [64, 100], [94, 95, 69])
    new_triangle = NumberTriangle(set_of_numbers=some_set)
    print(new_triangle)
    new_triangle.sequences[0][0].most_valuable_child_determine()
    new_triangle.sequences[2][2].most_valuable_child_determine()
