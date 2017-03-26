# tzconverter

This is a simple program which takes a csv file or pipe
on stdin containing Lat, Long, and a UTC epoch millisecond
timestamp and appends a localized epoch millisecond timestamp.

The program writes the output back to stdout, where you can
pipe it into another program or file.

```sh
$ pip install -r requirements.txt
$ cat example.csv
39.5501, 105.7821, 1479573036083
  ^         ^           ^
  |         |           |
 Lat       Long      UTC TIME


$ cat example.csv | python localize.py
39.5501, 105.7821, 1479573036083,1479543876083
  ^         ^           ^              ^
  |         |           |              |
 Lat       Long      UTC TIME      LOCAL TIME
```

You can customize which column is used for Lat, Long by doing:

```
# This will use column `3` for lat and column `6` for long
$ cat otherfile.csv | python localize.py --cols=3,6
```

You can customize the column used for the timestamp with the `--tscol` option.
