import os
import numpy as np
from grayplots.cli.run import _get_parser


def grayplots(data, mask, dir):
    
    n_datasets = len(data)


def _main(argv=None):
    options = _get_parser().parse_args(argv)
    grayplots(**vars(options))


if __name__ == '__main__':
    _main()
