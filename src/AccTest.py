from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

from src.Classifier import solve
from src.utils.DataSet import DataSet
from src.utils.FileWriter import FileWriter

layers = [
    [150, 100, 50],
    [100, 50, 10],
    [100, 50],
    [70, 35],
    [30, 10],
]
activations = ['relu', 'tanh']
bayeses = {
    'GaussianNB': GaussianNB(),
    'BernoulliNB': BernoulliNB()
}
neighbours = [2, 3, 5, 10, 15]


def write_header(file_name):
    FileWriter().append(file_name)
    FileWriter().nl()

    [FileWriter().append(str(layer) + '_' + activation) for layer in layers for activation in activations]
    [FileWriter().append(key) for key, _ in bayeses.items()]
    [FileWriter().append('knn_' + str(neighbour)) for neighbour in neighbours]

    FileWriter().nl()


def run_test(file_name):
    DataSet().load_data(file_name)
    write_header(file_name)

    for _ in range(1):
        DataSet().randomize_set()

        [FileWriter().append(solve(MLPClassifier(solver='lbfgs', activation=activation, hidden_layer_sizes=layer)))
            for layer in layers for activation in activations]
        [FileWriter().append(solve(bayes)) for _, bayes in bayeses.items()]
        [FileWriter().append(solve(KNeighborsClassifier(neighbour))) for neighbour in neighbours]

        FileWriter().nl()
    FileWriter().nl()
