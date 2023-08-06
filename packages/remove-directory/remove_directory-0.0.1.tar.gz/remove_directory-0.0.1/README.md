# remove_directory

Function to recursively remove a non-empty directory. Posted by Boris on [stackexchange][SE].

## Dependencies

None

## Usage

```
from pathlib import Path
from remove_directory import rmdir

p = Path("/path/to/directory")
rmdir(p)
```


## Installation

### Pip

```
pip install remove_directory
```

### Developer's Installation

You can clone the repository and install it with `pip install -e /path/to/local/repository`.

[SE]: https://stackoverflow.com/questions/13118029/deleting-folders-in-python-recursively/49782093#49782093
