
# -*- coding: utf-8 -*-
import re
import sys

from tensorflow.tools.compatibility.tf_upgrade_v2_main import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
