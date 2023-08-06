# ctail = colored tail

ctail is a command line script used to show the last lines of a file adding color to provided regular expressions.


```
ctail$ ctail -h
usage: ctail [-h] [-d] [-l NLINES] [-f] [-s] file_path [reg_exes [reg_exes ...]]

positional arguments:
  file_path           path of the file
  reg_exes            regular expressions to colour on the file (default: None)

optional arguments:
  -h, --help          show this help message and exit
  -d                  color date times in format: yyyy-mm-dd HH:MM:SS (default: False)
  -l NLINES           how many last lines show from file (default: 10)
  -f, --follow        output appended data as the file grows (default: False)
  -s, --show-regexes  show applied regular expresions (default: False)
```

# Install

```
pip install ctail
```