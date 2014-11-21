#!/usr/bin/env python
# encoding: utf-8
"""A service to parse through a file structure and pass the tree to jottabox.util.compare.

Run by crontab at some interval.

"""
# This file is part of jottabox.
#
# jottabox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# jottabox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with jottabox.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2014 Håvard Gulldahl <havard@gulldahl.no>

import optparse, os, sys, logging
logging.basicConfig(level=logging.DEBUG)

from jottalib.JFS import JFS
from jottabox import jottacloud

if __name__=='__main__':
    jfs = JFS(os.environ['JOTTACLOUD_USERNAME'], password=os.environ['JOTTACLOUD_PASSWORD'])

    for onlylocal, onlyremote, bothplaces in jottacloud.compare(sys.argv[1], sys.argv[2], jfs):
        print onlylocal, onlyremote, bothplaces
        print "uploading %s onlylocal files" % len(onlylocal)
        for f in onlylocal:
            logging.debug("uploading new file: %s", f)
            jfs.up(f.jottapath, open(f.localpath))
