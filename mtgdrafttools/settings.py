import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DATA_DIR = os.path.join(PROJECT_ROOT, '..', 'data')

SUPPORTED_EXPANSION_PATHS = {
    'dgm': os.path.join(DATA_DIR, 'DGM.txt'),
    'gtc': os.path.join(DATA_DIR, 'GTC.txt'),
    'm14': os.path.join(DATA_DIR, 'M14.txt'),
    'rtr': os.path.join(DATA_DIR, 'RTR.txt')
}
