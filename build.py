# type: ignore

import platform


try:
    # check for pypy
    if platform.python_implementation() == "PyPy":
        raise ImportWarning()

    # check for mypy
    from mypyc.build import mypycify

    def build(setup_kwargs):
        setup_kwargs.update(
            {
                "ext_modules": mypycify(["datimc.py"]),
            }
        )

        return True


except ImportError:
    print("mypyc is not installed, datim will not be compiled.")

except ImportWarning:
    print("PyPy detected, datim will not be compiled.")

else:

    def build(setup_kwargs):
        return False
