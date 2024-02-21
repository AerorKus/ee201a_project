#/bin/csh

# this runs both checkers. Use the args for strip checker.

python3 ./checkers/perf_checker.py $argv
python3 ./checkers/strip_checker.py $argv
