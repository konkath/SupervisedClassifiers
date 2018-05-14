from random import randrange
from re import split

from src.utils.Singleton import Singleton


class DataSet(metaclass=Singleton):
    data_set = []
    results = []

    def __init__(self, split_p=.7):
        self.split = split_p

    # Knuth-Fisher-Yates algorithm
    def randomize_set(self):
        for old_index in range(len(self.data_set)):
            new_index = randrange(old_index, len(self.data_set))
            if old_index == new_index:
                continue

            self.data_set[old_index], self.data_set[new_index] = self.data_set[new_index], self.data_set[old_index]
            self.results[old_index], self.results[new_index] = self.results[new_index], self.results[old_index]

    def get_data_sets(self):
        """ :return: training_set, verification_set, training_result, verification_result """

        split_place = int(len(self.data_set) * self.split)
        return self.data_set[:split_place], self.data_set[split_place:], \
            self.results[:split_place], self.results[split_place:]

    def load_data(self, file_name):
        self.data_set = []
        self.results = []

        with open(file_name, 'r') as f:
            for line in f.readlines():
                if line[0] != '@':
                    line = line.replace('\n', '')
                    values = split("[,;]", line)

                    self.data_set.append([float(value) for value in values[:-1]])
                    self.results.append(values[-1:][0])

        # self.data_set = MinMaxScaler(feature_range=(0, 1)).fit_transform(self.data_set)
