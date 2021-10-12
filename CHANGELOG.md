# Changelog

## 2.0.0 (2021-10-13)

Codebase refactor, compilation and performance improvements

### Added

- Alpha channel support
- Compiled with mypyc (datimc), ~2.5x faster
- `datimc.h6_rgba` to convert RGB(A) hex codes to 3/4 integer tuples, replacing
  PIL.ImageColor.getcolor, which used regex
- `Behaviour.alpha` of type `bool` and default value `True`

### Changed

- Codebase refactor, static typing everywhere
- `datimc.gen` now appends zeros rather than randomly generated chars
- `str.index` operations during hex/b15 to int now use dictionary indexing
- `Behaviour.input` is now type `pathlib.Path`
- `Behaviour.output` is now type `pathlib.Path`
- `-s --silent` switch is now `-np --no-progress`
- `-na --no-alpha` for non RGBA output

### Removed

- `Behaviour.silent` due to `Behaviour.tqdm` doing its job, decide if the
  progress bar is needed

## 1.1.1 (2021-10-12)

### Added

- README in package

### Changed

- Progress bar text

## 1.1.0 (2021-10-12)

Minor changes

### Added

- `-nc --no-compress` switch for optional compressiom

### Changed

- Compression algorithm from zlib to lz4

## 1.0.0 (2021-10-11)

Working product
