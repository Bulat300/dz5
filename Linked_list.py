class ListNode:
    def __init__(self, key, value):
        # каждый узел хранит ключ, значение и ссылку на следующий узел
        self.key = key
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        # храним ссылку на первый и последние узлы
        self.head = None
        self.tail = None

    def append(self, key, value):
        if self.tail:
            # если есть последний узел, то добавляем следующим узлом
            self.tail.next_node = ListNode(key, value)
            # и обновляем ссылку
            self.tail = self.tail.next_node
        else:
            # если нет, значит у нас пустой список,
            # создаем первый (и последний) узел
            self.head = ListNode(key, value)
            self.tail = self.head

    def get(self, key):
        node = self.head
        while node:
            # идем по узлам пока не встретим с нужным ключом
            if node.key == key:
                return node
            node = node.next_node
        # если не встретили, возвращаем None
        return None

    def __iter__(self):
        node = self.head
        while node:
            yield node.key, node.value
            node = node.next_node

    def delete(self, key) -> bool:
        if self.head is None:
            return False

        # если искомый элемент - первый
        if self.head.key == key:
            if self.head.next_node is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next_node
            return True

        # если искомый элемент - не первый
        node = self.head
        while node.next_node:
            next_node = node.next_node
            if next_node.key == key:
                if next_node == self.tail:
                    self.tail = node
                node.next_node = next_node.next_node
                return True
            node = node.next_node

        return False