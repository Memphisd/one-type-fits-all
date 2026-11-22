#!/bin/sh
# Every check of this repository, in about three minutes:
#   the witnesses (re-evaluation and independent checks), every printed number against its witness, and the
#   computations of earlier algorithms.  The column "published" of the restricted errors needs the authors' code:
#   REST_DEC=path/to/rest-dec sh run_all.sh
# jointtrees must be installed (README.md, "Install").
cd "$(dirname "$0")" || exit 1
python3 -m jointtrees verify witnesses
python3 recompute/check_numbers.py
cd comparisons
python3 single_nn_join.py
python3 stern.py
python3 three_sets.py
python3 both_may.py
if [ -n "$REST_DEC" ]; then
    python3 restricted_published.py "$REST_DEC"
fi
