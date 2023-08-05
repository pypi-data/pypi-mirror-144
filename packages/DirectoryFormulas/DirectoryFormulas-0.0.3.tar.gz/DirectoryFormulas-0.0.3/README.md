python3 setup.py sdist
ls -lah dist
pip3 install /Users/frankie/PycharmProjects/PycharmProjectsShared/TradingProject/Directory_Library/dist/DirectoryFormulas-0.0.1.tar.gz

twine upload dist/DirectoryFormulas-0.0.2.tar.gz

# Directory Formula
A small demo library for a Medium publication about publishing libraries.

### Installation
```
pip install DirectoryFormula
```

### Get started
Get your Directory:

```Python
from DirectoryFormula import DirX

# Instantiate a Multiplication object
DirX.Directory()

# Call the multiply method
DirX.DirectoryLocal()

DirX.DirectoryCloud()

DirX.FileOrder(Mininbars) # integer needed
# Fldict = {1:'-A-',5:'-B-',10:'-C-',15:'-D-',30:'-E-'}
# FileOrder = (Fldict.get(Mininbars))
DirX.DivByZero_int(a,b)
DirX.DivByZero_float(a,b)

DirX.RunCSV_Saver(fromdate, DirectoryTrigger)
```
