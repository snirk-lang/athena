"""
CI bot for Snirk development.

Usage:
    athena run-travis (pre | check | cron | deploy) [--local]
    athena run-aws [--local]
    athena (-h | --help)
    athena --version

Options:
    -h --help   Show this information.
    --version   Display version information.
    --local     Run travis or aws options locally.

"""
from docopt import docopt
import json
import travis
from travis.info import TravisInfo

def main(args):
    print(json.dumps(args))
    local = args.get("--local") is not None
    if args.get("run-travis"):
        travis_info = TravisInfo(local)
        if args.get("check"):
            travis.check.run(travis_info)
if __name__ == "__main__":
    args = docopt(__doc__, version="Athena 0.1")
    main(args)
