#!/usr/bin/python3

class Node:

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value != None or type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise TypeError("data must be an integer")
        elif next_node != None or type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

class SinglyLinkedLIst:

    def __init__(self):
        

    def __str__(self):
        return xxxxxxxx


    def sorted_insert(self, value):

