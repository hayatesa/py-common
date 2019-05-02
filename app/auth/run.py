#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import dirname, join
import sys
sys.path.append(dirname(dirname(join(sys.path[0]))))


if __name__ == '__main__':
    from app.auth import app
    app.run(host='0.0.0.0', port=5001, debug=True, use_reloader=False)
