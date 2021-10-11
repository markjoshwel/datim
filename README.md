# datim

Data as an image.

- [Installation](#installation)

- [Usage](#usage)

- [Optional Features](#optional-features)

- [Details](#details)

- [Potential Improvement](#potential-improvement)

- [License](#license)

## Installation

```
pip install "git+https://github.com/markjoshwel/datim.git"
```

For [optional features](#optional-features), use this instead:

```
pip install "datim[optional] @ git+https://github.com/markjoshwel/datim.git"
```

## Usage

datim has two commands, `datim` which converts data into images and `imdat`
which converts converted data now represented as images back into the original
data.

```
$ datim
usage: datim [-h] [-o] [-s] [-nc] input output

turns any file into an image

positional arguments:
  input               input file path
  output              output file path

optional arguments:
  -h, --help          show this help message and exit
  -o, --overwrite     overwrite without confirmation
  -s, --silent        do not use tqdm even if available
  -nc, --no-compress  do not compress data using zlib
```

```
$ imdat
usage: imdat [-h] [-o] [-s] [-nc] input output

turns previously converted images into the original file

positional arguments:
  input               input file path
  output              output file path

optional arguments:
  -h, --help          show this help message and exit
  -o, --overwrite     overwrite without confirmation
  -s, --silent        do not use tqdm even if available
  -nc, --no-compress  do not compress data using zlib
```

## Optional Features

- **[tqdm](https://github.com/tqdm/tqdm) Support**

  If `tqdm` is installed, a progress bar is shown during image generation
  (`datim`) and image reversal (`imdat`).

## Details

An image created by datim is made up by the following:
`[header][data][trailing random data]`

- `[header]`

  This is made up of a base15 hex array (0-E) denoting the length of the
  (compressed) data hex array. It is then suffixed with a hex `F`, acting as a
  delimiter betweeen the `[header]` and `[data]` sections. This method of
  storing the data hex array was chosen as to not use the alpha layer, which
  would increase the resulting image file size.

- `[data]`

  The (compressed) data is expressed naturally as its hexidecimal counterparts.

- `[trailing random data]`

  After the `[data]` hex array, there are trailing randomly generated hex
  chars. This is done purely for cosmetics.

## Potential Improvement  

- **Efficient Sizing**

  There may be a way to figure the smallest possible width and height values
  from the total length of the (compressed) hex array rather than ceiling the
  length and square rooting it, which may help reduce size.

## License

datim is unlicensed with [The Unlicense](https://unlicense.org).
