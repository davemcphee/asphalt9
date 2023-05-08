import argparse
import logging

import nxbt
from nxbt.bluez import find_devices_by_alias

from asphalt9.macros import COMPLETE_MP1_LOOP

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger("asphalt9")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--new-controller",
        required=False,
        default=False,
        action="store_true",
        help="create a new virt controller"
    )
    return parser.parse_args()


def reconnect_target(args):
    target = None
    if not args.new_controller:
        LOG.info("--new-controller set, re-connecting to known switch")
        target = find_devices_by_alias("Nintendo Switch")
    else:
        LOG.info("--new-controller not set, attempting to create new controller")
    return target


def main():
    args = get_args()

    nx = nxbt.Nxbt()
    target = reconnect_target(args)

    LOG.debug("attempting to create controller")
    ci = nx.create_controller(
        nxbt.PRO_CONTROLLER,
        reconnect_address=target,
    )

    LOG.debug("waiting for connection")
    nx.wait_for_connection(ci)

    if args.mp1:
        race_count = 0
        while True:
            nx.macro(ci, COMPLETE_MP1_LOOP)
            race_count += 1
            LOG.info(f"race no. {race_count} complete, restarting...")





