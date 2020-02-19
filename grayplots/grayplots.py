import os
import numpy as np
from grayplots.cli.run import _get_parser


def grayplots(data, mask, mot, outdir, polort, fwhm, range, percent, ordering, dim):
    
    n_datasets = len(data)

    print(data)

    if not os.path.isdir(outdir):
        os.mkdir(outdir)
        
    for data_idx in range(n_datasets):
        print(f'{data[data_idx]}')

#     # grayplot command
# 3dGrayplot -overwrite -mask mask4grayplot.FUNC.nii.gz -polort ${POLORTORDER} -fwhm ${FWHM} -range 3 -percent -prefix ${SUBJ}.Grayplot.jpg pb04.${SUBJ}.volreg.nii.gz
# ​
# echo -e "\e[32m ++ INFO: Computing demean and derivative of realignment parameters ...\e[39m"
# # compute de-meaned motion parameters (for use in regression)
# 1d_tool.py -overwrite -infile ${SUBJ}_Motion.1D -set_nruns 1 -demean -write ${SUBJ}_Motion_demean.1D
# # compute motion parameter derivatives (for use in regression)
# 1d_tool.py -overwrite -infile ${SUBJ}_Motion.1D -set_nruns 1 -derivative -demean -write ${SUBJ}_Motion_deriv.1D
# ​
# # Compute Framewise Displacement based on Euclidean Norm (as default in AFNI)
# echo -e "\e[32m ++ INFO: Computing Framewise Displacement based on Euclidean Norm (as default in AFNI) ...\e[39m"
# 1d_tool.py -overwrite -infile ${SUBJ}_Motion.1D -derivative -collapse_cols euclidean_norm -write ${SUBJ}_Motion_enorm.1D
# # Compute Framewise Displacement (as defined by Power)
# echo -e "\e[32m ++ INFO: Computing Framewise Displacement (as defined by Power) ...\e[39m"
# 1deval -overwrite -a ${SUBJ}_Motion_deriv.1D[0] -b ${SUBJ}_Motion_deriv.1D[1] \
#   -c ${SUBJ}_Motion_deriv.1D[2] -d ${SUBJ}_Motion_deriv.1D[3] \
#   -e ${SUBJ}_Motion_deriv.1D[4] -f ${SUBJ}_Motion_deriv.1D[5] \
#   -expr 'abs(a)+abs(b)+abs(c)+abs(d)+abs(e)+abs(f)' > ${SUBJ}_Motion_FD.1D
# ​
# # Compute RMS of motion derivative parameters
# echo -e "\e[32m ++ INFO: Computing Framewise Displacement based on RMS of realignment  derivative parameters ...\e[39m"
# 1deval -overwrite -a ${SUBJ}_Motion_deriv.1D[0] -b ${SUBJ}_Motion_deriv.1D[1] \
#   -c ${SUBJ}_Motion_deriv.1D[2] -d ${SUBJ}_Motion_deriv.1D[3] \
#   -e ${SUBJ}_Motion_deriv.1D[4] -f ${SUBJ}_Motion_deriv.1D[5] \
#   -expr 'sqrt( (a*a + b*b +c*c + d*d + e*e + f*f)/6 )' > ${SUBJ}_Motion_RMS.1D


def _main(argv=None):
    options = _get_parser().parse_args(argv)
    grayplots(**vars(options))


if __name__ == '__main__':
    _main()
