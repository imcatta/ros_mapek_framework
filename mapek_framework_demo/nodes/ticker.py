#!/usr/bin/env python
from mapek_framework.utils import Ticker

def main():
    ticker = Ticker('ticker', 'tick', 0.2)
    ticker.spin()

if __name__ == '__main__':
    main()
