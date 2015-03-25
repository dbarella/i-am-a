#!/usr/bin/env bash

if [[ $# -eq 0 ]]; then
  for _ in `seq 10`; do python i_am.py; done
else
  for _ in `seq "$1"`; do python i_am.py; done
fi
