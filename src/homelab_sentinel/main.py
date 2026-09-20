import argparse
import sys

from homelab_sentinel.system import (
    get_status,
)


def main() -> None:
    parser = argparse.ArgumentParser("homelab-sentinel")

    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser("check")
    check_parser.set_defaults(func=check)

    status_parser = subparsers.add_parser("status")
    status_parser.set_defaults(func=status)

    args = parser.parse_args()


    args.func()


def check() -> None:
    status = get_status()

    print(f"CPU: {status['cpu']['usage']}% | {status['cpu']['state']}")
    print(f"RAM: {status['memory']['usage']}% | {status['memory']['state']}")
    print(f"Storage: {status['storage']['usage']}% | {status['storage']['state']}")


def status() -> None:
    severity = {
        "OK": 0,
        "WARNING": 11,
        "CRITICAL": 12,
    }

    status = get_status()

    highest = "OK"

    for component in status.values():
        state = component["state"]
        if severity[state] > severity[highest]:
            highest = state

    print(highest)

    sys.exit(severity[highest])


if __name__ == "__main__":
    main()
