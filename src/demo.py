#!/usr/bin/env python
# -*- coding: utf-8 -*-

from huobi.client.market import MarketClient
from huobi.utils.log_info import LogInfo
from huobi.constant.definition import CandlestickInterval

market_client = MarketClient()


def main():
    list_obj = market_client.get_candlestick("btcusdt", CandlestickInterval.MIN5, 10)
    LogInfo.output_list(list_obj)


if __name__ == "__main__":
    main()
