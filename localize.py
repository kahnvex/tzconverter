import argparse
import csv
import datetime
import sys
import time

from timezonefinder import TimezoneFinder
from pytz import timezone, utc
from pytz.exceptions import UnknownTimeZoneError


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default=sys.stdin)
    parser.add_argument('--cols', type=int, nargs=2, default=(0, 1))
    parser.add_argument('--tzcol', type=int, default=2)

    return parser.parse_args()

def main(args):
    tf = TimezoneFinder()

    reader = csv.reader(args.input)

    for row in reader:
        naive_datetime = datetime.datetime.utcfromtimestamp(int(row[args.tzcol]) / 1000)
        tz = tf.timezone_at(lat=float(row[args.cols[0]]),
                            lng=float(row[args.cols[1]]))

        tz_obj = timezone(tz)
        aware_datetime = naive_datetime.replace(tzinfo=tz_obj)
        offset_aware_datetime = aware_datetime.astimezone(utc)
        row.append(str(int(offset_aware_datetime.timestamp() * 1000)))

        print(','.join(row))


if __name__ == '__main__':
    main(get_args())
