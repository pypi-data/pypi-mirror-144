# provide_directory

Function to create the given path, including potential parent directories. Returns a bool if at leas one directory as been created.

## Dependencies

None

## Usage

```python
from pathlib import Path
from provide_dir import provide_dir

needed_path = Path("/path/to/directory/with/subdirectories")

try:
    was_created = provide_path(needed_path)
    if was_created:
        print(f"{needed_path} was successfully created")
    else:
        print(f"{needed_path} already exists")
except FileExistsError:
    print(f"Cannot create {needed_path} because it already exists as a file")
```

## Installation

### Pip

```
pip install provide_dir
```

### Developer's Installation

You can clone the repository and install it with `pip install -e /path/to/local/repository`.
