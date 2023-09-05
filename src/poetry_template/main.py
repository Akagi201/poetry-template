import argparse
from argparse import Namespace
import asyncio
import yaml


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
    print("parsing config: {args.config}")
    with open(args.config, "r") as config_file:
        config = yaml.safe_load(config_file)
    print("config: {}".format(config))


if __name__ == "__main__":
    asyncio.run(main(parse_args()))
