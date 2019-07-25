## psrfits_volume

A small command-line script to calculate the data volume of a PSRFITS file.

~~~~
usage: python psrfits_volume.py [-h] [-q] [--nsubint NSUBINT] [--npol NPOL]
                                [--nchan NCHAN] [--nbin NBIN] [--tobs TOBS]
                                [--tsubint TSUBINT] [--bw BW]
                                [--chanbw CHANBW] [--nulow NULOW]
                                [--nuhigh NUHIGH] [--powertwo]

Calculate the data volume of a PSRFITS file

optional arguments:
  -h, --help         show this help message and exit

Printing options:
  -q, --quiet        Quiet printing (default: False)

Dimension size parameters:
  Directly specify the number of divisions along a given axis.

  --nsubint NSUBINT  Number of subintegrations (default: 1800)
  --npol NPOL        Number of polarizations (default: 4)
  --nchan NCHAN      Number of channels (default: 512)
  --nbin NBIN        Number of phase bins (default: 2048)

Observation size parameters:
  Specify the number of divisions based on observational parameters.
  Changes in these will override the relevant parameters of the above.
  These are evaluated in order.

  --tobs TOBS        Observation length (default: 1800.0 s)
  --tsubint TSUBINT  Subintegration length (default: 1.0 s)
  --bw BW            Bandwidth (default: 1000.0 MHz)
  --chanbw CHANBW    Bandwidth (default: 2.0 MHz)
  --nulow NULOW      Low frequency (high required; default: 1000.0 MHz)
  --nuhigh NUHIGH    High frequency (low required; default: 2000.0 MHz)
  --powertwo         Require the number of channels to be the closest lower
                     (floor) power of two (default: False)
~~~~               