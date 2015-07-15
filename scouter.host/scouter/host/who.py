#!/usr/bin/env python

#
# original code from 
#    https://github.com/giampaolo/psutil/blob/master/examples/
#
# Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
A clone of 'who' command; print information about users who are
currently logged in.
$ python examples/who.py
giampaolo       tty7            2014-02-23 17:25  (:0)
giampaolo       pts/7           2014-02-24 18:25  (:192.168.1.56)
giampaolo       pts/8           2014-02-24 18:25  (:0)
giampaolo       pts/9           2014-02-27 01:32  (:0)
"""

from datetime import datetime

import psutil


from scouter.lang.pack import *
from scouter.lang.value import *


def main():
    users = psutil.get_users()
    for user in users:
        print("%-15s %-15s %s  (%s)" % (
            user.name,
            user.terminal or '-',
            datetime.fromtimestamp(user.started).strftime("%Y-%m-%d %H:%M"),
            user.host))
if __name__ == '__main__':
    main()
    
def process(param):
    pack = MapPack()
    nameList = pack.newList("name")
    terminalList = pack.newList("terminal")
    startedList = pack.newList("started")
    hostList = pack.newList("host")
    users = psutil.users()
    for user in users:
        nameList.addStr(user.name)
        terminalList.addStr(user.terminal or '-')
        startedList.addStr(datetime.fromtimestamp(user.started).strftime("%Y-%m-%d %H:%M"))
        hostList.addStr(user.host)
    return pack
