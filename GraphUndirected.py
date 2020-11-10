from Vertex import *


class GraphUndirected:
    def __init__(self):
        self.g = LinkedList()

    def vertexComparisson(self, node, vertexName):
        """
        :param node: Es un objeto de tipo nodo LinkedList
        :param vertexName: nombre del vertice a comparar
        :return: Retorna True si el vértice del nodo y el vertexName son iguales, de lo contrario
        retorna False
        """
        if isinstance(node, Node):
            vertex = node.value
            if "%s".strip() % vertex.name == "%s".strip() % vertexName:
                return True
            return False
        return False

    def add(self, vertexName):
        """

        :param vertexName: Nombre con el que se creara el nuevo vertice.
        :return: Retorna True si el vertice se agrego al grafo, False de lo contrario.
        """
        """
        Para agregar un nuevo vértice, el vértice a agregar no debe de existir previamente dentro de
        la lista enlazada.

        """
        if (not self.g.exists(vertexName, lambda a, b: self.vertexComparisson(a, b))):
            self.g.push(Vertex(vertexName))
            return True
        return False

    def edge(self, vertexNameA, vertexNameB):
        """

        :param vertexNameA: Nombre del vertice A.
        :param vertexNameB: Nombre del vertice B
        :return: True si se crean las aristas entre los vertices, False de lo contrario.
        """
        self.add(vertexNameA)
        self.add(vertexNameB)
        if not self.g.get(vertexNameA, lambda a, b: self.vertexComparisson(a, b)).value.edges.exists(vertexNameB,
                                                                                                     lambda a,
                                                                                                            b: self.vertexComparisson(
                                                                                                             a, b)):
            self.g.get(vertexNameA, lambda a, b: self.vertexComparisson(a, b)).value.edges.push(Vertex(vertexNameB))
            self.g.get(vertexNameB, lambda a, b: self.vertexComparisson(a, b)).value.edges.push(Vertex(vertexNameA))
            return True
        return False

    def __str__(self):
        result = []
        graph = self.g
        current = graph.first
        while (current):
            result += ["\tEl nodo %s tiene aristas con: %s" % (
            current.value.name, current.value.edges.print(lambda a: self.vertexName(a)))]
            current = current.next
        return "\n".join(result)

    def __len__(self):
        graph = self.g
        return len(graph)

    def vertexName(self, node):
        """

        :param node: Nodo de una lista enlazada que contiene un Vertice.
        :return:  retorna el VertexName de un vertice
        """
        vertex = node.value
        return vertex.name
