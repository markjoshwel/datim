# datim 2.0.0

Data as an image.

- [Installation](#installation)
- [Usage](#usage)
- [Optional Features](#optional-features)
- [Details](#details)
- [Potential Improvement](#potential-improvement)
- [License](#license)

## Installation

```
pip install datim
```

## Usage

datim has four commands:


- `datim`
- `imdat`
- `datimp`
- `imdatp`

`datim` and `imdat` check whether the compiled variant of datim is installed.
If unavailable, it will fallback to the pure Python variant of datim.
`datimp` and `imdatp` _exclusively_ use the pure Python variant of the module.

```
$ datim
usage: datim [-h] [-o] [-np] [-nc] [-na] input output

turns any file into an image

positional arguments:
  input               input file path
  output              output file path

optional arguments:
  -h, --help          show this help message and exit
  -o, --overwrite     overwrite without confirmation
  -np, --no-progress  do not use tqdm
  -nc, --no-compress  do not compress data
  -na, --no-alpha     do not use alpha channel
```

```
$ imdat
usage: imdat [-h] [-o] [-np] [-nc] [-na] input output

turns previously converted images into the original file

positional arguments:
  input               input file path
  output              output file path

optional arguments:
  -h, --help          show this help message and exit
  -o, --overwrite     overwrite without confirmation
  -np, --no-progress  do not use tqdm
  -nc, --no-compress  do not compress data
  -na, --no-alpha     do not use alpha channel
```

## Optional Features

- **[tqdm](https://github.com/tqdm/tqdm) Support**

  If `tqdm` is installed, a progress bar is shown during image generation
  (`datim`) and image reversal (`imdat`).

## Details

An image created by datim is made up by the following:
`[header][data][trailing random data]`

- `[header] -> "<length of [data] hex array encoded in base15 hex>F"`

  This is made up of a base15 hex array (0-E) denoting the length of the
  (compressed) data hex array. It is then suffixed with a hex `F`, acting as a
  delimiter betweeen the `[header]` and `[data]` section. This method of
  storing the data hex array was chosen as to not use the alpha layer, which
  would increase the resulting image file size.

- `[data]`

  The (compressed) data is expressed naturally as its hexidecimal counterparts.

- `[trailing 0s]`

  After the `[data]` hex array are trailing `0`s. Before 2.0.0, trailing data
  were randomly generated for cosmetic purposes, but was removed due for
  performance.

## License

datim is unlicensed with [The Unlicense](https://unlicense.org).
