import argparse
from grayplots import __version__


def _get_parser():
    # Argument parser based on tedana
    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    required.add_argument('-d',
                          dest='data',
                          nargs='+',
                          metavar='FILE',
                          type=str,
                          help=('Input data.'),
                          required=True)
    required.add_argument('-m',
                          dest='mask',
                          nargs='+',
                          metavar='FILE',
                          type=str,
                          help=('Mask of input data.'),
                          required=True)
    optional.add_argument('-dir',
                          dest='outdir',
                          nargs=1,
                          metavar='DIR',
                          type=str,
                          help='Output directory name (default = results).',
                          default='results')
    optional.add_argument('-v', '--version', action='version',
                          version=('%(prog)s ' + __version__))
    parser._action_groups.append(optional)
    return parser


if __name__ == '__main__':
    raise RuntimeError('grayplots/cli/run.py should not be run directly;\n'
                       'Please `pip install` grayplots and use the '
                       '`grayplots` command')
