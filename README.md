Python Progressbar
====

Python3 Utilities

## Install

```
python setup.py install
```

## Usage

### Progressbar

```
import time
from pyutils.progressbar import progressbar

for i in progressbar(range(100)):
  time.sleep(0.1)
```

### Logger

```
from pyutils.logger import logger

printl = logger('test.txt')
printl('test')
```

## Licence

[MIT](https://github.com/gauzesya/pyutils/blob/master/LICENSE)

## Author

[gauzesya](https://github.com/gauzesya)
