#!/usr/bin/env python
# -*- coding: utf-8 -*-
from WebPage import app
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT","8888"))
    app.run("127.0.0.1",port, threaded=False)

