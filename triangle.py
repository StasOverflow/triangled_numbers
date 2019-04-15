from random import randint


class Node:

    def __init__(self, value=0, index=0, depth=0,
                 left_child=None, right_child=None):
        self.value = value
        self.index = index
        self.depth = depth
        self.left_child = left_child
        self.right_child = right_child
        self.most_valuable_child = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def left_child_insert(self, node):
        self.left_child = node

    def right_child_insert(self, node):
        self.right_child = node

    @property
    def has_children(self):
        """Check if has at least 1 active child"""
        if self.left_child is not None or self.right_child is not None:
            return True
        else:
            return False

    def get_child_list(self):
        child_list = list()
        if self.left_child is not None:
            child_list.append(self.left_child)
        if self.right_child is not None:
            child_list.append(self.right_child)
        return child_list

    def calculate_sum(self):
        child_value = 0
        if self.has_children:
            children = self.get_child_list()

            # Say most valuable child is the first one
            self.most_valuable_child = children[0]
            for child in children:
                if child.calculate_sum() > self.most_valuable_child.calculate_sum():
                    self.most_valuable_child = child

            child_value = self.most_valuable_child.value

        return self.value + child_value

    def __repr__(self):
        indexed = False
        if indexed:
            string = ('(' + '{:>2}'.format(self.depth) + ',' + '{:>2}'.format(self.index) + ') ')
        else:
            string = ''
        string += '{:>4}'.format(self.value)
        return string

    def __str__(self):
        string = '{:>4}'.format(self.value) + '\n'
        if self.has_children:
            string += '{:>4}'.format(self.left_child.value) + ' ' + '{:>4}'.format(self.right_child.value)
        return string


class NumberTriangle:

    def __init__(self, number_list_of_lists=None, max_depth=3, randomize=True):
        self.sequence_list = list()
        if number_list_of_lists:
            for dimension, sub_list in enumerate(number_list_of_lists):
                sequence = [Node(value=value,
                                 depth=dimension, index=index) for index, value in enumerate(sub_list)]
                self.sequence_list.append(sequence)
        elif randomize:
            # +1 here, because 0th dimension cannot be iterated, so start with 1
            for dimension in range(max_depth):
                if dimension:
                    sequence = [Node(value=randint(0, 100),
                                     depth=dimension-1, index=index) for index in range(dimension)]
                    self.sequence_list.append(sequence)
        else:
            value = 0
            for dimension in range(max_depth):
                sequence = list()
                for index in range(dimension):
                    sequence.append(Node(value=value, depth=dimension, index=index))
                    value += 1
                self.sequence_list.append(sequence)
        self._bind_children()

    def _bind_children(self):
        for sequence_num, sequence in enumerate(self.sequence_list[:-1]):
            for index, node in enumerate(sequence):
                node.left_child_insert(self.sequence_list[sequence_num + 1][index])
                node.right_child_insert(self.sequence_list[sequence_num + 1][index + 1])
            # print(index)
            pass

    def __str__(self):
        string = 'Triangle\n'
        for sequence in self.sequence_list:
            string += str(sequence) + '\n'
        string += '\n' + '-' * 50
        return string


if __name__ == '__main__':
    triangle = NumberTriangle(max_depth=15)
    print(triangle)
    print(triangle.sequence_list[4][1])
    print(triangle.sequence_list[13][1])

    new_triangle = NumberTriangle(number_list_of_lists=[[14], [64, 100], [94, 95, 69]])
    print(new_triangle)

    # new_triangle.calculate_sum()

