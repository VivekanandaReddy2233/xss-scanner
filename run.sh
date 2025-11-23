#!/usr/bin/env bash
# Usage: ./run.sh <url> <comma-separated-params> [GET|POST]
set -e
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <url> <comma-separated-params> [GET|POST]"
  exit 1
fi

URL="$1"
PARAMS="$2"
METHOD="${3:-GET}"

python -m venv .venv
# Activate venv (works on bash; on Windows use .venv\Scripts\activate)
source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate 2>/dev/null || true
pip install -r requirements.txt

python -m scanner.cli --url "$URL" --params "$PARAMS" --method "$METHOD" --out report.html

echo "Report available at: report.html"
