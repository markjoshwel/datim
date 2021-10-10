This repository is a template repository for Public Domain repositories.

Placeholders:
- `{project-name}`: Project formal name
- `{project-link}`: Project line, with https:// prefix

Please adjust the README accordingly.

# {project-name}

## Contributing

### Contributor License Agreement

{project-name} is unlicensed with [The Unlicense](https://unlicense.org), and
thus contributors must include a waiver with their submission. There are two
methods of doing so:

#### AUTHORS Commit

In the `AUTHORS` file, create a new entry with your name (real name preferred),
and append the following block of text, indented.

```
I dedicate any and all copyright interest in this software to the
public domain. I make this dedication for the benefit of the public at
large and to the detriment of my heirs and successors. I intend this
dedication to be an overt act of relinquishment in perpetuity of all
present and future rights to this software under copyright law.
```

Example:

```
Mark Joshwel
    I dedicate any and all copyright interest in this software to the
    public domain. I make this dedication for the benefit of the public at
    large and to the detriment of my heirs and successors. I intend this
    dedication to be an overt act of relinquishment in perpetuity of all
    present and future rights to this software under copyright law.
```

#### Signed Waiver + AUTHORS Commit

In the respository root, sign the `WAIVER` file using GPG.

```
gpg --no-version --armor --sign WAIVER
```

Then in the `AUTHORS` file, create a new entry with your name as per GPG key,
and append the contents of the signed WAIVER, indented.

Example:

```
Mark Joshwel
    -----BEGIN PGP MESSAGE-----

    owGVU39MlGUcP+SH8RabLi8BVz2XSkUnVqMNndEaXHlrOcYSLRJ83vd97u7h7t7n
    eN735XZdbjV/FG0mC2dZSMBQyU3MjhZjLcRg2mA7ypkZOmm6QtN0Abq8gr7Pe6BW
    f/XHbfc8z/f7/fz6vg1ZqTYp5fLpk5nH5JGfUw6mynLGumfdFa5yjFdfW4xKWCjC
    qddnoDCmdYQjD+NoVTTEWQ1RjGUBqvk3FUuSG6lEpQo2CMJaBH4qwoEAUm51U80g
    nOjiDzJ8VEc68xhhzAkyGFwQKWTKAaoglQUx1QqQGwWxnyRLZ0ZTplnoUI1kohEP
    NRDzWMeZZmxIAcy9xMJPzoVmg9Mg0azaYAT5COW6VaCbikJ0nXFdwAmCogsApTsA
    YYos5iEG4g2EFWsOJyC81qS6z5oMmkKEh4hhUiMi3kG7FAK54lFAeUzDBKmWFXqS
    2Z0WmJoKzt42K4DDBZL0EpuRqs9y92ssHCDqjEAZSBCPUzwoTAOVsikogzgYSSj0
    conBQKoBHcjENHyME+iLoCBBYKSoA2CIFRhyFkQhTuE6zLhfR2EfVXzgiw/XEQm0
    Uw+FMtGCAzpLxnjL+GRqydihQmMGuCuLDRFilQCmQV0CDbclAgkmGKIQ5gYl+v/Q
    qwl0ldZR1cQBJ5JNnWqQoxPEerFGX7OCcyKvSEwT+TiF2CQanEREPqxbe/rf/ZRA
    xr8NdVrwboQ9HsqDQBIbcApTWHCh1FrUfzRIVolwwkINUx0C0RQzKAOGWlCfEkuz
    pUi2++9zpKnRsdiKx5sWn3ENjc1+helzxLdnkzLnzd48mHGP7dSe/N3xF0sSxb3P
    dQ0NPpVV8dCB5XfH7JemV03bs/odjvXovd8mH8Vzc9nQosZnyi/bE/avj/8V31DY
    f/WL1rVNf5RmyEdXHorOaa8q29sysQ+3fLx11Dx8doT0jm5++e0fTztjk+9s6cz+
    vfjowqXL/fFT3Wnff4qHB84vLfmw9dDmfSemtq776fzGirFzOem/PDa+sqs7VLDb
    17TNG/vB7XikL/2akli2veRN46MnEo1dY221n9hGGp4euZl/pOdS89wl40ZR/Gru
    1GRHfc25zg3Xb2Q3V/tjV7LVje1hJfO7+fE3Ul3jozvm3Xyy6oXpDmXX/sIlr7bZ
    bVUDhffu/DLPbDnQvG28Nnbi3QVn8v2uu8rWtB3fkvrwQFl3W19vu716eLD8g2/f
    2uONogsVJ4u+WrG2o+GVnrM5fEflhcr6av/q/Xne9Z9ff791U81gv+Oz9p6LfxaX
    HnRFn+cxR2Wnv6qoMTdxeKLvSuSbRWziSG7OwotSXsuvg8P+vVM5C14P66XsgRvH
    tu/8Gw==
    =YcTU
    -----END PGP MESSAGE-----
```

## License

{project-name} is unlicensed with [The Unlicense](https://unlicense.org).
