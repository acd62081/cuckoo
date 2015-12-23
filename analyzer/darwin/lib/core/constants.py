# Copyright (C) 2010-2014 Claudio Guarnieri.
# Copyright (C) 2014-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os
from tempfile import gettempdir
from ..common.rand import random_string

ROOT = os.path.join(gettempdir() + os.sep, random_string(6, 10))

PATHS = {
    "root"   : ROOT,
    "logs"   : os.path.join(ROOT, "logs"),
    "files"  : os.path.join(ROOT, "files"),
    "shots"  : os.path.join(ROOT, "shots"),
    "memory" : os.path.join(ROOT, "memory"),
    "drop"   : os.path.join(ROOT, "drop")
}
