# RINEX Analyzer

A simple RINEX file analyzer based on GEORINEX python lib.

## Usage:

```
python3 ./tp_read_rinex.py -f <RINEXFileNameWithPath>
```

I highly recommend you to use the 'LittleSample.20O' observation file as test because smallness.

After that you will see a list of available satellite inview from your RINEX file, choose a number of satellites from which you want to plot the observables. 

**Warning** Both for satellites, or observables, you NEED to type string exactly with the same format as it is printed before it let you make your choice.
For example, type :
```
G02
```
to print PRN 2
and 
```
C1C
```
to print pseudo range of L1 code

## Install requirements
To make it works, you georinex lib and matplotlib library

```
pip install georinex
pip install matplotlib
```