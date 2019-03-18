#!/usr/bin/env python
j=Job()
j.application.exe = File('dockerex.py')
j.submit()
