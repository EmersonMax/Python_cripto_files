from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("crip.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "cripto",
    options = options,
    version = "1.0",
    description = 'Descricao do seu arquivo',
    executables = executables
)