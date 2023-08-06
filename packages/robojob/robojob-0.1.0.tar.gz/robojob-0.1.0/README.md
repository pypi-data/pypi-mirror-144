

```python
import logging

from job import JobExecution

logging.basicConfig(level="DEBUG")

def hello(name):
    print(f"Hello {name}!")

with JobExecution("hello") as ctx:
    ctx.execute(hello, name="world")
```
