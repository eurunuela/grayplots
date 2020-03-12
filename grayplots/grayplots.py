import os
import time
import numpy as np
import matplotlib.pyplot as plt
from grayplots.cli.run import _get_parser
from grayplots.reporting.generate_report import generate_report, generate_image


def grayplots(data, mask, figs, mot, outdir, polort, fwhm, range_grayplot, percent, ordering, dim):

    # Get amount of datasets and motion parameters
    if data is not None:
        n_datasets = len(data)

    # Generate output directory if it does not exist
    if not os.path.isdir(outdir):
        os.mkdir(outdir)

    # We assume the same mask works for the different datasets
    if (mask is not None) and (type(mask) is list):
        mask = mask[0]

    # Motion parameters-related calculations
    if mot is not None:
        n_mot = len(mot)
        for mot_idx in range(n_mot):
            if '1D' in mot[mot_idx]:
                #################################################################
                # Computes de-meaned motion parameters (to be used in regression)
                demean_mopars_output = os.path.join(outdir, 'Motion_demean.1D')
                demean_mopars_command = (f'1d_tool.py -overwrite -infile {mot[mot_idx]} -set_nruns 1 '
                                        f'-demean -write {demean_mopars_output}')
                print(f'Computing demeaned motion parameters for {mot[mot_idx]}...')
                os.system(demean_mopars_command)
                while not os.path.isfile(demean_mopars_output):
                    time.sleep(0.5)
                print(f'Demeaned motion parameters {mot[mot_idx]} saved '
                    f'in {demean_mopars_output}')

                #################################################################
                # Computes motion parameter derivatives (to be used in regression)
                deriv_mopars_output = os.path.join(outdir, 'Motion_deriv.1D')
                deriv_mopars_command = (f'1d_tool.py -overwrite -infile {mot[mot_idx]} -set_nruns 1 '
                                        f'-derivative -demean -write {deriv_mopars_output}')
                print(f'Computing motion parameter derivates for {mot[mot_idx]}...')
                os.system(deriv_mopars_command)
                while not os.path.isfile(deriv_mopars_output):
                    time.sleep(0.5)
                print(f'Motion parameter derivates {mot[mot_idx]} saved in {deriv_mopars_output}')

                #################################################################
                # Computes Framewise Displacement based on Euclidean Norm (default in AFNI)
                fd_euclidean_output = os.path.join(outdir, 'Motion_enorm.1D')
                fd_euclidean_command = (f'1d_tool.py -overwrite -infile {mot[mot_idx]} -derivative '
                                        f'-collapse_cols euclidean_norm -write {fd_euclidean_output}')
                print(f'Computing Framewise Displacement based on Euclidean Norm '
                    f'for {mot[mot_idx]}...')
                os.system(fd_euclidean_command)
                while not os.path.isfile(fd_euclidean_output):
                    time.sleep(0.5)
                print(f'Framewise Displacement based on Euclidean Norm of {mot[mot_idx]} saved '
                    f'in {fd_euclidean_output}')

                #################################################################
                # Computes Framewise Displacement (as defined by Power)
                fd_power_output = os.path.join(outdir, 'Motion_FD.1D')
                fd_power_command = (f'1deval -overwrite -a {deriv_mopars_output}[0] '
                                    f'-b {deriv_mopars_output}[1] -c {deriv_mopars_output}[2] '
                                    f'-d {deriv_mopars_output}[3] -e {deriv_mopars_output}[4] '
                                    f'-f {deriv_mopars_output}[5] '
                                    f'-expr "abs(a)+abs(b)+abs(c)+abs(d)+abs(e)+abs(f)" '
                                    f'> {fd_power_output}')
                print(f'Computing Framewise Displacement (as define by Power) for {mot[mot_idx]}...')
                os.system(fd_power_command)
                while not os.path.isfile(fd_power_output):
                    time.sleep(0.5)
                print(f'Framewise Displacement (as defined by Power) of {mot[mot_idx]} saved '
                    f'in {fd_power_output}')

                #################################################################
                # Compute RMS of motion derivative parameters
                rms_motion_output = os.path.join(outdir, 'Motion_RMS.1D')
                rms_motion_command = (f'1deval -overwrite -a {deriv_mopars_output}[0] '
                                    f'-b {deriv_mopars_output}[1] -c {deriv_mopars_output}[2] '
                                    f'-d {deriv_mopars_output}[3] -e {deriv_mopars_output}[4] '
                                    f'-f {deriv_mopars_output}[5] '
                                    f'-expr "sqrt( (a*a + b*b +c*c + d*d + e*e + f*f)/6 )" > '
                                    f'{rms_motion_output}')
                print(f'Computing RMS of motion derivative parameters for {mot[mot_idx]}...')
                os.system(rms_motion_command)
                while not os.path.isfile(rms_motion_output):
                    time.sleep(0.5)
                print(f'RMS of motion derivative parameters of {mot[mot_idx]} saved '
                  f'in {rms_motion_output}')
            else:
                mot_data = np.loadtxt(mot[mot_idx])
                plt.figure(figsize=(dim))
                plt.plot(mot_data)
                plt.xlabel('Time')
                plt.ylabel('Amplitude')
                plt.title(f'Motion')
                plt.savefig(os.path.join(outdir, f'motion_{mot[mot_idx]}.png'))

    # TODO: read FD and motion parameter files and plot them

    # Draws the grayplots with AFNI's 3dGrayplot for each dataset
    images_html = ''
    if data is not None:
        for data_idx in range(n_datasets):
            grayplot_output = os.path.join(outdir, f'grayplot_{data_idx}.png')
            grayplot_command = (f'3dGrayplot -input {data[data_idx]} -overwrite -mask {mask} '
                                f'-prefix {grayplot_output} -range {range_grayplot} '
                                f'-{ordering} -dimen {dim[0]} {dim[1]}')
            if polort != 0:
                grayplot_command = f'{grayplot_command} -polort {polort}'
            if fwhm != 0.0:
                grayplot_command = f'{grayplot_command} -fwhm {fwhm}'
            if percent:
                grayplot_command = f'{grayplot_command} -percent'

            print(f'Drawing grayplot for {data[data_idx]}...')
            os.system(grayplot_command)
            while not os.path.isfile(grayplot_output):
                time.sleep(0.5)
            print(f'Grayplot of {data[data_idx]} saved in {grayplot_output}')

            if mot is not None:
                title = f'Motion of {data[data_idx]}'
                images_html += generate_image(os.path.join(outdir, f'motion_{mot[data_idx]}.png'), dim, title)
            title = f'Grayplot of {data[data_idx]}'
            images_html += generate_image(os.path.join(outdir, f'grayplot_{data_idx}.png'), dim, title)

    if figs is not None:
        idx = 0
        for fig_path in figs:
            # TODO: extract filename for title
            if mot is not None:
                title = f'Motion'
                images_html += generate_image(os.path.join(outdir, f'motion_{mot[idx]}.png'), dim, title)
            title = f'Grayplot'
            images_html += generate_image(fig_path, dim, title)
            idx += 1

    generate_report(images_html, outdir)

    print('Finished!')


def _main(argv=None):
    options = _get_parser().parse_args(argv)
    grayplots(**vars(options))


if __name__ == '__main__':
    _main()
