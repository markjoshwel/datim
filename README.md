# datim

Data as an image.

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
  Help message

- `-o, --overwrite`
  Overwrite without confirmation

- `-s, --silent`
  Do not use [tqdm](https://github.com/tqdm/tqdm) even if available

## License

datim is unlicensed with [The Unlicense](https://unlicense.org).
