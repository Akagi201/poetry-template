import argparse
import asyncio


def parse_args():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args


async def main(args=None):
    print("hello micro-py")


if __name__ == "__main__":
    asyncio.run(main(parse_args()))