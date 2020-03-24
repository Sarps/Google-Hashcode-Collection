import numpy as np


class BaseLoader:

    def __init__(self, filename):
        self.file = open(filename, "r")
        self.parse()
        self.close()

    def _readline(self):
        return self.file.readline().rstrip('\n')

    def _readlines(self, n):
        return list(map(lambda x: self._readline(), range(n)))

    def _readlinesAndSplit(self, n):
        return list(map(lambda x: self._readline().split(), range(n)))

    def _loadIntegers(self):
        return list(map(lambda x: int(x), self._readline().split()))

    def _loadIntegerMatrix(self, n):
        return list(map(
            lambda x: list(map(
                lambda y: int(y), self._readline().split()
            )),
            range(n)
        ))

    def _toNumpyArray(self, data, dtype=str):
        return np.array(data, dtype=dtype)

    def parse(self):
        pass

    def close(self):
        self.file.close()


class Loader(BaseLoader):

    def parse(self):
        self.B, self.L, self.D = self._loadIntegers()
        self.S = self._loadIntegers()

        self.K = list(map(
            lambda x: [self._loadIntegers(), self.presort()],
            range(self.L)
        ))
        self.K

        # self.photos = self._toNumpyArray(self.photos, [('type', str), ('tag_count', int), ('tags', list)])

    def presort(self):
        x = self._loadIntegers()
        k = [z for _, z in sorted(zip([self.S[i] for i in x], x), reverse=True)]
        return k


class Writer:

    def __init__(self, filename):
        self.file = open(filename, "w+")

    def writeSlidesLength(self, length):
        self.file.write(str(length) + "\n")

    def writeVerticalsAndHorizontals(self, verticals, horizontals):
        for v in verticals:
            self.file.write(str(v[0]) + " " + str(v[1]) + "\n")
        for h in horizontals:
            self.file.write(str(h) + "\n")

    def writeLine(self, line):
        self.file.write(line + "\n")

    def writeMatrix(self, matrix):
        for row in matrix:
            self.file.write(" ".join([str(i) for i in row]) + "\n")

    def close(self):
        self.file.close()


if __name__ == '__main__':
    example = Loader("files/a_example.txt")
    # print(example.photos)
