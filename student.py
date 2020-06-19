class Student:

    def __init__(self, data):
        items = data.split(',')

        self._sid = items[0]
        self._sname = items[1]
        self._skor = float(items[2])
        self._seng = float(items[3])
        self._smat = float(items[4])

    @property
    def sid(self):
        return self._sid