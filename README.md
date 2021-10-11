# datim

Data as an image.

- [Installation](#installation)

- [Usage](#usage)

- [Details](#details)

- [Potential Improvement](#potential-improvement)

- [License](#license)

## Installation

```
pip install "git+https://github.com/markjoshwel/datim.git"
```

## Usage

datim has two commands, `datim` which converts data into images and `imdat`
which converts converted data now represented as images back into the original
data.

```shell
$ datim
usage: datim [-h] [-o] [-s] input output
```

```shell
$ imdat
imdat: datim [-h] [-o] [-s] input output
```

- `input`
  input file path

- `output`
  output file path

- `-h, --help`
  help message

- `-o, --overwrite`
  overwrite without confirmation

- `-s, --silent`
  do not use [tqdm](https://github.com/tqdm/tqdm) even if available

- `-o, --original`
  do not compress data using zlib

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
