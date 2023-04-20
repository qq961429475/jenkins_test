import os

import yaml


def read_yalm(filename):
    filepath = os.path.dirname(os.path.dirname(__file__))
    with open(filepath + '/data/' + filename, 'r', encoding='utf-8') as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        return data
