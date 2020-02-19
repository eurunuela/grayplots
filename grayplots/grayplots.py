import os
import numpy as np
from grayplots.cli.run import _get_parser


def grayplots(data, mask, mot, outidr, polort, fwhm, range_grayplot, percent, ordering, dim):

    n_datasets = len(data)
    n_mot = len(mot)

    if type(mask) is list:
        mask = mask[0]

    for data_idx in range(n_datasets):
        grayplot_command = (f'3dGrayplot -input {data[data_idx]} -overwrite -mask {mask} '
                            f'-prefix grayplot_{data_idx} -range {range_grayplot} '
                            f'-{ordering} -dimen {dim[0]} {dim[1]}')
        if polort != 0:
            grayplot_command = f'{grayplot_command} -polort {polort}'
        if fwhm != 0.0:
            grayplot_command = f'{grayplot_command} -fwhm {fwhm}'
        if percent:
            grayplot_command = f'{grayplot_command} -percent'

        print(grayplot_command)

    if mot is not None:
        for mot_idx in range(n_mot):
            demean_mopars_command = (f'1d_tool.py -overwrite -infile {mot[mot_idx]} -set_nruns 1 '
                                     f'-demean -write Motion_demean.1D')
            deriv_mopars_command = (f'1d_tool.py -overwrite -infile {mot[mot_idx]} -set_nruns 1 '
                                    f'-derivative -demean -write Motion_deriv.1D')
            fd_euclidean_command = (f'1d_tool.py -overwrite -infile {mot[mot_idx]} -derivative '
                                    f'-collapse_cols euclidean_norm -write Motion_enorm.1D')
            fd_power_command = (f'1deval -overwrite -a Motion_deriv.1D[0] -b Motion_deriv.1D[1] '
                                f'-c Motion_deriv.1D[2] -d Motion_deriv.1D[3] '
                                f'-e Motion_deriv.1D[4] -f Motion_deriv.1D[5] '
                                f'-expr "abs(a)+abs(b)+abs(c)+abs(d)+abs(e)+abs(f)" '
                                f'> Motion_FD.1D')
            rms_motion_command = (f'1deval -overwrite -a Motion_deriv.1D[0] -b Motion_deriv.1D[1] '
                                  f'-c Motion_deriv.1D[2] -d Motion_deriv.1D[3] '
                                  f'-e Motion_deriv.1D[4] -f Motion_deriv.1D[5] '
                                  f'-expr "sqrt( (a*a + b*b +c*c + d*d + e*e + f*f)/6 )" > '
                                  f'Motion_RMS.1D')


def _main(argv=None):
    options = _get_parser().parse_args(argv)
    grayplots(**vars(options))


if __name__ == '__main__':
    _main()
