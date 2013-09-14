import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DATA_DIR = os.path.join(PROJECT_ROOT, '..', 'data')

SUPPORTED_EXPANSIONS = {
    'dgm': 'DGM.txt',
    'gtc': 'GTC.txt',
    'm14': 'M14.txt',
    'rtr': 'RTR.txt'
}
