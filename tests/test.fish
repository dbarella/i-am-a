#!/usr/bin/env fish

if set -q argv
  for _ in (seq $argv[1])
    python i_am.py
  end
else
  for _ in (seq 10)
    python i_am.py
  end
end
