import pkgutil
from pkgutil_learn1 import commands

for fileFinder, name, is_pkg in pkgutil.iter_modules(commands.__path__):
    print(fileFinder)
    print(name)
    print(is_pkg)