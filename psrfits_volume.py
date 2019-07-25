'''
Michael T. Lam 2019

An easy utility for calculating the approximate volume of a PSRFITS file.
This will only calculate the internal data volume and no associated metadata volume.
'''

import argparse
from math import log, floor

DATA_byte = 2
DAT_byte = 4

# https://stackoverflow.com/a/18462760
class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass

parser = argparse.ArgumentParser(
    formatter_class=CustomFormatter,
    prog='python psrfits_volume.py',
    description='''Calculate the data volume of a PSRFITS file''')

group0 = parser.add_argument_group('Printing options')

group0.add_argument("-q", "--quiet", action="store_true", help='Quiet printing')

group1 = parser.add_argument_group('Dimension size parameters',
                                   'Directly specify the number of divisions along a given axis.')
group1.add_argument('--nsubint', type=int, default=1800, help='Number of subintegrations')
group1.add_argument('--npol', type=int, default=4, help='Number of polarizations')
group1.add_argument('--nchan', type=int, default=512, help='Number of channels')
group1.add_argument('--nbin', type=int, default=2048, help='Number of phase bins')

description = '''Specify the number of divisions based on observational parameters.
Changes in these will override the relevant parameters of the above.
These are evaluated in order.
'''

DEFAULT_TOBS = 1800.0
DEFAULT_TSUBINT = 1.0
DEFAULT_BW = 1000.0
DEFAULT_CHANBW = DEFAULT_BW / 512
DEFAULT_NULOW = 1000.0
DEFAULT_NUHIGH = 2000.0

group2 = parser.add_argument_group('Observation size parameters', description)

group2.add_argument('--tobs', type=float, default=DEFAULT_TOBS, help='Observation length (default: %(default)0.1f s)')
group2.add_argument('--tsubint', type=float, default=DEFAULT_TSUBINT, help='Subintegration length (default: %(default)0.1f s)')
group2.add_argument('--bw', type=float, default=DEFAULT_BW, help='Bandwidth (default: %(default)0.1f MHz)')
group2.add_argument('--chanbw', type=float, default=DEFAULT_CHANBW, help='Bandwidth (default: %(default)0.1f MHz)')
group2.add_argument('--nulow', type=float, default=DEFAULT_NULOW, help='Low frequency (high required; default: %(default)0.1f MHz)')
group2.add_argument('--nuhigh', type=float, default=DEFAULT_NUHIGH, help='High frequency (low required; default: %(default)0.1f MHz)')
group2.add_argument('--powertwo', default=False, action='store_true', help='Require the number of channels to be the closest lower (floor) power of two')
args = parser.parse_args()
#parser.print_help()

nsubint = args.nsubint
npol = args.npol
nchan = args.nchan
nbin = args.nbin

if not args.quiet: 
    print("")

# Test for other arguments
if args.tobs != DEFAULT_TOBS or args.tsubint != DEFAULT_TSUBINT:
    nsubint = floor(args.tobs/args.tsubint)
    if not args.quiet:
        print("Setting nsubint = %0.1f s / %0.1f s = %i"%(args.tobs, args.tsubint, nsubint))
mode = 0
if args.bw != DEFAULT_BW or args.chanbw != DEFAULT_CHANBW:
    nchan = floor(args.bw/args.chanbw)
    if args.powertwo:
        nchan = 2**floor(log(nchan, 2))
        mode = 1
    else:
        mode = 2
if args.nulow != DEFAULT_NULOW and args.nuhigh != DEFAULT_NUHIGH:
    if args.powertwo:
        nchan = 2**floor(log(args.nuhigh - args.nulow, 2))
        mode = 3
    else:
        nchan = int((args.nuhigh - args.nulow) / args.chanbw)
        mode = 4
if not args.quiet:
    if mode == 1:
        print("Setting nchan = %0.1f MHz / %0.1f MHz -> %i (nearest power)"%(args.bw, args.chanbw, nchan))
    elif mode == 2:
        print("Setting nchan = %0.1f MHz / %0.1f MHz = %i"%(args.bw, args.chanbw, nchan))
    elif mode == 3:
        print("Setting nchan -> %i (nearest power)"%(nchan))
    elif mode == 4:
        print("Setting nchan = (%0.1f MHz - %0.1f MHz) / %0.1f MHz = %if"%(args.nuhigh, args.nulow, args.chanbw, nchan))

DATA_size = nsubint*npol*nchan*nbin*DATA_byte
DAT_SCL_size = nsubint*npol*nchan*DAT_byte
DAT_OFFS_size = nsubint*npol*nchan*DAT_byte
DAT_WTS_size = nsubint*nchan*DAT_byte

total = DATA_size + DAT_SCL_size + DAT_OFFS_size + DAT_WTS_size
if not args.quiet:
    print("(nsubint, npol, nchan, nbin) = (%i, %i, %i, %i)"%(nsubint, npol, nchan, nbin))

if total >= 1e12:
    print("%0.2f TB"%(total / 1e12))
elif total >= 1e9:
    print("%0.2f GB"%(total / 1e9))
elif total >= 1e6: 
    print("%0.2f MB"%(total / 1e6))
elif total >= 1e3:
    print("%0.2f KB"%(total / 1e3))

if not args.quiet: 
    print("")

