#!/usr/bin/env bash

#watchmedo auto-restart -d . -p '*.py' -R -- pytest -s $1
when-changed -v -r -1 -s ./ "py.test -s $1"
