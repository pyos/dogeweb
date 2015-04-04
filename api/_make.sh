#!/usr/bin/env bash
for f in *.in; do
  d="${f%.*}"
  d="${d#_}"
  if [ "$d" = "index" ]; then
    t="index.html"
    d="dogeweb"
    x=0
  else
    mkdir -p "$d"
    t="$d/index.html"
    x=1
  fi

  echo "$f -> $t"
  python3 -m dg _compile.dg "$x" "$d" < "$f" > "$t"
done
