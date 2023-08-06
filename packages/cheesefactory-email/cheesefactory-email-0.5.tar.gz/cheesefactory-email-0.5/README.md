# cheesefactory-email

-----------------

#### An easier way to send an Email.
[![PyPI Latest Release](https://img.shields.io/pypi/v/cheesefactory-email.svg)](https://pypi.org/project/cheesefactory-email/)
[![PyPI status](https://img.shields.io/pypi/status/cheesefactory-email.svg)](https://pypi.python.org/pypi/cheesefactory-email/)
[![PyPI download month](https://img.shields.io/pypi/dm/cheesefactory-email.svg)](https://pypi.python.org/pypi/cheesefactory-email/)
[![PyPI download week](https://img.shields.io/pypi/dw/cheesefactory-email.svg)](https://pypi.python.org/pypi/cheesefactory-email/)
[![PyPI download day](https://img.shields.io/pypi/dd/cheesefactory-email.svg)](https://pypi.python.org/pypi/cheesefactory-email/)


### Features

**Note:** _This package is still in beta status. As such, future versions may not be backwards compatible and features may change. Parts of it may even be broken._

TODO

### Create an Email object and send

```python
from cheesefactory_email import Email

mail = Email(
      recipients=['bob@example.com',],
      host='localhost',
      port='25',
      username='emailuser',
      password='emailpassword',
      sender='tom@example.com',
      subject='Fishing trip',
      body='Dear Bob,\nHow was the fishing trip?\n\nTom',
      use_tls=False,
      attachments=['file1.txt', 'file2.txt']
)
```