class HashSet(HashMap):
    # Чтобы не реализовывать заново почти весь функционал,
    # здесь используется реализация HashMap.
    # Минус этого подхода - для значения (value),
    # хоть нам оно и не нужно, все равно выделяется память

    def __iter__(self):
        # возвращаем ключи
        for bucket in self.buckets:
            for (key, value) in bucket:
                yield key

    def append(self, key):
        # используем функционал HashMap,
        # но вместо значения - None
        self[key] = None

    def __contains__(self, key):
        # далее аналогично
        try:
            _ = self[key]
            return True
        except KeyError:
            return False

    def intersection(self, other):
        # пересечение
        result = HashSet()
        for key in self:
            if key in other:
                result.append(key)
        return result

    def union(self, other):
        # объединение
        result = HashSet()
        for key in self:
            result.append(key)
        for key in other:
            result.append(key)
        return result

    def __sub__(self, other):
        # разность
        result = HashSet()
        for key in self:
            if key not in other:
                result.append(key)
        return result

    def __repr__(self):
        return str([x for x in self])

if __name__ == '__main__':
    # ---------- HashMap ----------
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