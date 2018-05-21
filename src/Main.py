from src.AccTest import run_test
from src.utils.FileWriter import FileWriter

set_names = [
    '../sets/biodeg.csv',
    '../sets/dermatology.dat',
    '../sets/ring.dat',
    '../sets/segment.dat',
    '../sets/spectfheart.dat',
    '../sets/texture.dat',
    '../sets/vehicle.dat',
    '../sets/vowel.dat',
    '../sets/winequality-red.dat'
]

if __name__ == '__main__':
    FileWriter('cross_results.csv')

    for set_name in set_names:
        # run_test(set_name, 'fit')
        run_test(set_name, 'cross')
