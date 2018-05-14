from src.utils.DataSet import DataSet


def solve(classifier):
    training_set, verification_set, training_result, verification_result = DataSet().get_data_sets()

    classifier.fit(training_set, training_result)
    results = classifier.predict(verification_set)

    counter = 0
    for r1, r2 in zip(verification_result, results):
        counter += 1 if r1 == r2 else 0

    return counter / len(verification_result) * 100
