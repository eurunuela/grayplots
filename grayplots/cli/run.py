import argparse
from grayplots import __version__


def _get_parser():
    # Argument parser based on tedana
    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional.add_argument('-d',
                          dest='data',
                          nargs='+',
                          metavar='FILE',
                          type=str,
                          help=('Input data (default = None).'),
                          default=None)
    optional.add_argument('-mask',
                          dest='mask',
                          nargs='+',
                          metavar='FILE',
                          type=str,
                          help=('Mask of input data (default = None).'),
                          default=None)
    optional.add_argument('-fig',
                          dest='figs',
                          nargs='+',
                          metavar='FILE',
                          type=str,
                          help=('Figures of already generated grayplots (default = None).'),
                          default=None)
    optional.add_argument('-mot',
                          dest='mot',
                          nargs='+',
                          metavar='MOT',
                          type=str,
                          help='Motion parameters of each input data (default = None).',
                          default=None)
    optional.add_argument('-dir',
                          dest='outdir',
                          nargs=1,
                          metavar='DIR',
                          type=str,
                          help='Output directory name (default = results).',
                          default='grayplots_temp')
    optional.add_argument('-polort',
                          dest='polort',
                          nargs=1,
                          metavar='POLORT',
                          type=int,
                          help='Polort value (int) for 3dGrayplot (default = 0).',
                          default=0)
    optional.add_argument('-fwhm',
                          dest='fwhm',
                          nargs=1,
                          metavar='FWHM',
                          type=float,
                          help='FWHM value for 3dGrayplot (default = 0.0).',
                          default=0.0)
    optional.add_argument('-range',
                          dest='range_grayplot',
                          nargs=1,
                          metavar='RANGE',
                          type=int,
                          help='Range value for 3dGrayplot (default = 3).',
                          default=3)
    optional.add_argument('-percent',
                          dest='percent',
                          action='store_true',
                          help='Percent option for 3dGrayplot (default = True).',
                          default=True)
    optional.add_argument('-ordering',
                          dest='ordering',
                          action='store',
                          choices=['pvorder', 'LJorder', 'peelorder', 'ijkorder'],
                          help=('Option for the ordering of voxels in the grayplot, '
                                'in the vertical direction (default = pvorder).'),
                          default='pvorder')
    optional.add_argument('-dim',
                          dest='dim',
                          nargs=2,
                          metavar='DIM',
                          type=int,
                          help='Output size of image in pixels for a dpi of 300 '
                               '(default = 1024, 512).',
                          default=[1024, 512])
    optional.add_argument('-v', '--version', action='version',
                          version=('%(prog)s ' + __version__))
    parser._action_groups.append(optional)
    return parser


if __name__ == '__main__':
    raise RuntimeError('grayplots/cli/run.py should not be run directly;\n'
                       'Please `pip install` grayplots and use the '
                       '`grayplots` command')
