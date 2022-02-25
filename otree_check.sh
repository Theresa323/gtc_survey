#!/usr/bin/env bash
echo "Check for active oTree instance(s)"

echo "- Running prodserver processes:"
pgrep -f prodserver

if pgrep -f prodserver > /dev/null; then
   echo "- Shutting down active processes:"
   sudo pkill -f prodserver
fi
