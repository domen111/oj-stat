# Contributing
Contributions are appreciated in the form of pull requests. However, to maintain code readability and maintainability, some guidelines have been set. *Your pull request will likely be rejected if it does not merge these guidelines, so please read them carefully.*

### Style
* Don't use semicolon at the and of one line.
* Use tab as indent.
* Unix-style line endings should be used (`\n`).
* Please leave a blank line at the end of each file.

### OJ supporting
It's welcomed to add new online judge fetcher to the project. Before sending pull request, please check the following guidelines.
* It's suggested to use `requests` module when you fetch online data.
* Please add your OJ name in `/oj/oj.py` and `README.md`.
