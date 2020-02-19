import numpy as np
import os
from grayplots.cli.run import _get_parser


def grayplots():
    print('hey')


def _main(argv=None):
    options = _get_parser().parse_args(argv)
    grayplots(**vars(options))


if __name__ == '__main__':
    _main()
