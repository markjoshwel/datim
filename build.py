# type: ignore

import platform


try:
    # check for pypy
    if platform.python_implementation() == "PyPy":
        raise ImportError("PyPi detected")

    # check for mypy
    from mypyc.build import mypycify

except ImportError as e:
    print("There was an error during datim compilation:", e)

    def build(setup_kwargs):
        pass


else:

    def build(setup_kwargs):
        setup_kwargs.update(
            {
                "ext_modules": mypycify(["datimc.py"]),
            }
        )
