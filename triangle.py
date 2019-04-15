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


class NumberTriangle:

    def __init__(self, number_list_of_lists=None, max_dimensions=3, randomize=True):
        self.sequence_list = list()
        if number_list_of_lists:
            for sub_list in number_list_of_lists:
                self.sequence_list.append(sub_list)
        elif randomize:
            for dimension in range(max_dimensions + 1):
                if dimension:
                    sequence = [randint(-100, 100) for _ in range(dimension)]
                    self.sequence_list.append(sequence)
        else:
            value = 0
            for dimension in range(max_dimensions):
                sequence = list()
                for cell in range(dimension):
                    sequence.append(value)
                    value += 1
                self.sequence_list.append(sequence)

    def __str__(self):
        string = 'Triangle\n'
        string += str([sequence for sequence in self.sequence_list])
        string += '\n' + '-' * 50
        return string


if __name__ == '__main__':
    triangle = NumberTriangle(max_dimensions=15)
    print(triangle)

    new_triangle = NumberTriangle(number_list_of_lists=[[-14], [-64, -100], [-94, 95, 69]])
    print(new_triangle)


