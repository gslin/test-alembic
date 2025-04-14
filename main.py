#!/usr/bin/env python3

from alembic import command
from alembic.config import Config

def main():
    config = Config('alembic.ini')
    command.upgrade(config, 'head')

if __name__ == "__main__":
    main()
