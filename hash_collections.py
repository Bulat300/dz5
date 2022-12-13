class ListNode:
    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):

        self.head = None
        self.tail = None

    def append(self, key, value):
        if self.tail:
            self.tail.next_node = ListNode(key, value)
            self.tail = self.tail.next_node
        else:
            self.head = ListNode(key, value)
            self.tail = self.head

    def get(self, key):
        node = self.head
        while node:
            if node.key == key:
                return node
            node = node.next_node

        return None

    def __iter__(self):
        node = self.head
        while node:
            yield node.key, node.value
            node = node.next_node

    def delete(self, key) -> bool:
        if self.head is None:
            return False


        if self.head.key == key:
            if self.head.next_node is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next_node
            return True


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


class HashMap:
    def __init__(self, size=100):

        self.size = size
        self.buckets = [LinkedList() for _ in range(size)]

    def __setitem__(self, key, value):
        bucket = self.buckets[hash(key) % self.size]
        node = bucket.get(key)
        if node:
            node.value = value
        else:
            bucket.append(key, value)

    def __delitem__(self, key):
        bucket = self.buckets[hash(key) % self.size]
        if not bucket.delete(key):
            raise KeyError

    def __getitem__(self, key):
        bucket = self.buckets[hash(key) % self.size]
        node = bucket.get(key)
        if node:
            return node.value
        raise KeyError


class HashSet(HashMap):
    def __iter__(self):

        for bucket in self.buckets:
            for (key, value) in bucket:
                yield key

    def append(self, key):
        self[key] = None

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except KeyError:
            return False

    def intersection(self, other):
        result = HashSet()
        for key in self:
            if key in other:
                result.append(key)
        return result

    def union(self, other):
        result = HashSet()
        for key in self:
            result.append(key)
        for key in other:
            result.append(key)
        return result

    def __sub__(self, other):
        result = HashSet()
        for key in self:
            if key not in other:
                result.append(key)
        return result

    def __repr__(self):
        return str([x for x in self])

if __name__ == '__main__':

    m = HashMap()
    try:
        print(m[2], 'error')
    except KeyError:
        print('key 2 not found')

    m['test'] = 1
    assert m['test'] == 1
    m['test'] = 2
    assert m['test'] == 2

    del m['test']
    try:
        print(m['test'], 'error')
    except KeyError:
        print('key "test" not found')

    # ---------- HashSet ----------
    s1 = HashSet()
    s1.append(1)
    s1.append(2)
    print(s1, 'it must be [1, 2]')
    s1.append(1)
    print(s1, 'it must be [1, 2]')
    del s1[1]
    print(s1, 'it must be [2]')
    assert not (1 in s1)
    assert 2 in s1

    s2 = HashSet()
    s2.append(1)
    s2.append(2)
    s2.append(3)

    print(s2.union(s1), 'it must be [1, 2, 3]')
    print(s2.intersection(s1), 'it must be [2]')
    print(s2 - s1, 'it must be [1, 3]')