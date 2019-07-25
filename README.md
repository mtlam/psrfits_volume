## psrfits_volume.py

A small command-line script to calculate the data volume of a PSRFITS file.


#### Example usage:

```shell
user@computer: python psrfits_volume.py

(nsubint, npol, nchan, nbin) = (1800, 4, 512, 2048)
15.13 GB

user@computer: python psrfits_volume.py --tobs 3600 

Setting nsubint = 3600.0 s / 1.0 s = 3600
(nsubint, npol, nchan, nbin) = (3600, 4, 512, 2048)
30.27 GB

user@computer: python psrfits_volume.py --tobs 3600 --bw 800.0 --powertwo

Setting nsubint = 3600.0 s / 1.0 s = 3600
Setting nchan = 800.0 MHz / 2.0 MHz -> 256 (nearest power)
(nsubint, npol, nchan, nbin) = (3600, 4, 256, 2048)
15.13 GB

user@computer: python psrfits_volume.py -q --tobs 3600 --bw 800.0 --powertwo
15.13 GB
```

#### Help:

~~~~
usage: python psrfits_volume.py [-h] [-q] [--nsubint NSUBINT] [--npol NPOL]
                                [--nchan NCHAN] [--nbin NBIN] [--tobs TOBS]
                                [--tsubint TSUBINT] [--bw BW]
                                [--chanbw CHANBW] [--nulow NULOW]
                                [--nuhigh NUHIGH] [--powertwo]

Calculate the data volume of a PSRFITS file

Printing options:
  -h, --help         show this help message and exit
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