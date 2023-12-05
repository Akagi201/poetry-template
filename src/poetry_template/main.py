import argparse
from argparse import Namespace
import asyncio
import yaml
from loguru import logger
import sys

logger.remove()
logger.add(
    sys.stderr,
    format='"timestamp":"{time}","level":"{level}","message":"{message}"',
    level="INFO",
)


def parse_args() -> Namespace:
    parser = argparse.ArgumentParser(description="Liquid Searcher")
    parser.add_argument(
        "--config",
        "-c",
        type=str,
        required=True,
        help="config file",
    )
    args = parser.parse_args()
    return args


async def main(args: Namespace):
    logger.info("parsing config file: {args.config}")

    with open(args.config, "r") as config_file:
        config = yaml.safe_load(config_file)
    logger.info("pared configs: {}".format(config))


if __name__ == "__main__":
    asyncio.run(main(parse_args()))
