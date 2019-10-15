# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from collections import OrderedDict
import json
import time

import arrow
import requests


def main():
    data = OrderedDict()
    today = arrow.utcnow().floor('day').replace(days=-1)
    for ago in range(1, 365):
        for retry in range(5):
            try:
                date = today.replace(days=-ago).format("YYYYMMDD")
                print "Fetching {} ...".format(date)
                r = requests.get("http://hckrnews.com/data/{date}.js".format(date=date))
                data[date] = r.json()
                time.sleep(30)
            except Exception, e:
                print str(e)
            else:
                break

    with open('data.json', 'w') as f:
        f.write(json.dumps(data, indent=4))






if __name__ == '__main__':
    main()
