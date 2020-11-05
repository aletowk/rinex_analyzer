# RINEX Analyzer

A simple RINEX file analyzer based on GEORINEX python lib.

## Usage:

```
python3 ./tp_read_rinex.py -f <RINEXFileNameWithPath>
```

I highly recommend you to use the 'LittleSample.20O' observation file as test because smallness.

After that the script will start on the 'compare signals loop' that will allow you to select one PRN from these contained in the RINEX file and two signals (PSR,ADR,SNR) to compare. So it will plot them and then perform some statistics about

## Install requirements
To make it works, you georinex lib and matplotlib library

```
pip install georinex
pip install matplotlib
```