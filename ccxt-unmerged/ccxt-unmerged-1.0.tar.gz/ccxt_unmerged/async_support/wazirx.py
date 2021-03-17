# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.base.exchange import Exchange
from ccxt.base.errors import ExchangeError


class wazirx(Exchange):

    def describe(self):
        return self.deep_extend(super(wazirx, self).describe(), {
            'id': 'wazirx',
            'name': 'WazirX',
            'countries': ['IN'],
            'version': 'v2',
            'has': {
                'CORS': True,
                'publicAPI': True,
                'privateAPI': False,
                'fetchMarkets': True,
                'fetchCurrencies': True,
                'fetchTickers': True,
                'fetchTicker': False,
                'fetchStatus': False,
                'fetchOHLCV': False,
                'fetchOrderBook': True,
                'fetchTrades': True,
            },
            'urls': {
                'logo': 'https://i0.wp.com/blog.wazirx.com/wp-content/uploads/2020/06/banner.png',
                'api': 'https://api.wazirx.com',
                'www': 'https://wazirx.com',
                'doc': 'https://github.com/WazirX/wazirx-api',
            },
            'api': {
                'public': {
                    'get': [
                        'market-status',
                        'tickers',
                        'depth',
                        'trades',
                    ],
                },
            },
            'exceptions': {
                'exact': {
                    '403': 'ab',
                },
            },
            'options': {
                'cachedMarketData': {},
            },
        })

    async def fetch_market_and_assets(self):
        markets = self.safe_value(self.options['cachedMarketData'], 'markets')
        assets = self.safe_value(self.options['cachedMarketData'], 'assets')
        if markets is not None and assets is not None:
            return self.options['cachedMarketData']
        response = await self.publicGetMarketStatus()
        self.options['cachedMarketData'] = response
        return response

    async def fetch_markets(self, params={}):
        marketAndAssets = await self.fetch_market_and_assets()
        markets = marketAndAssets['markets']
        #      {
        #             "baseMarket": "btc",
        #             "quoteMarket": "inr",
        #             "minBuyAmount": 0.001,
        #             "minSellAmount": 0.001,
        #             "fee": {
        #                 "bid": {
        #                     "maker": 0.001,
        #                     "taker": 0.0025
        #                 },
        #                 "ask": {
        #                     "maker": 0.001,
        #                     "taker": 0.0025
        #                 }
        #             },
        #             "basePrecision": 4,
        #             "quotePrecision": 2,
        #             "low": "460001.01",
        #             "high": "505000.0",
        #             "last": "480102.0",
        #             "open": 505002,
        #             "volume": "0.2071",
        #             "sell": "490000.0",
        #             "buy": "485001.0",
        #             "type": "SPOT"
        #             "Status": "active"
        #       },
        result = []
        for i in range(0, len(markets)):
            market = markets[i]
            baseId = self.safe_string(market, 'baseMarket')
            quoteId = self.safe_string(market, 'quoteMarket')
            id = None
            if baseId is not None and quoteId is not None:
                id = baseId + quoteId
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = None
            if base is not None and quote is not None:
                symbol = base + '/' + quote
            status = self.safe_value(market, 'status') is True if 'active' else False
            makerAndTakerFee = self.compute_maker_and_taker_fee(market)
            minBuyAmount = self.safe_float(market, 'minBuyAmount')
            minSellAmount = self.safe_float(market, 'minSellAmount')
            minAmount = minBuyAmount > minSellAmount if minSellAmount else minBuyAmount
            precision = {
                'amount': self.safe_integer(market, 'quotePrecision'),
            }
            limits = {
                'amount': {
                    'min': minAmount,
                },
            }
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': status,
                'taker': makerAndTakerFee['taker'],
                'maker': makerAndTakerFee['maker'],
                'percentage': True,
                'tierBased': False,
                'precision': precision,
                'limits': limits,
                'info': market,
            })
        return result

    async def fetch_currencies(self, params={}):
        marketAndAssets = await self.fetch_market_and_assets()
        assets = marketAndAssets['assets']
        #
        #        {
        #             "type": "inr",
        #             "name": "Rupee",
        #             "withdrawFee": 0,
        #             "minWithdrawAmount": 50,
        #             "maxWithdrawAmount": 50000,
        #             "minDepositAmount": 500,
        #             "confirmation": 5,
        #             "deposit": "enabled",
        #             "withdrawal": "enabled"
        #       },
        #
        result = {}
        for i in range(0, len(assets)):
            currency = assets[i]
            id = self.safe_string(currency, 'type')
            code = self.safe_currency_code(id)
            name = self.safe_string(currency, 'name')
            fee = self.safe_float(currency, 'withdrawFee')
            minWithdrawAmount = self.safe_float(currency, 'minWithdrawAmount')
            maxWithdrawAmount = self.safe_float(currency, 'maxWithdrawAmount')
            result[code] = {
                'id': id,
                'code': code,
                'name': name,
                'active': True,
                'fee': fee,
                'info': currency,
                'limits': {
                    'withdraw': {'min': minWithdrawAmount, 'max': maxWithdrawAmount},
                    'amount': {'min': None, 'max': None},
                    'price': {'min': None, 'max': None},
                    'cost': {'min': None, 'max': None},
                },
            }
        return result

    async def fetch_tickers(self, symbols=None, params={}):
        await self.load_markets()
        tickers = await self.publicGetTickers()
        # {
        #     "btcinr": {
        #         "base_unit": "btc",
        #         "quote_unit": "inr",
        #         "low": "472005.0",
        #         "high": "508102.0",
        #         "last": "508100.0",
        #         "open": 490000,
        #         "volume": "0.2709",
        #         "sell": "508100.0",
        #         "buy": "481000.0",
        #         "name": "BTC/INR",
        #         "at": 1536732262
        #     },
        #     ...
        # }
        #
        tickerIds = list(tickers.keys())
        result = {}
        for i in range(0, len(tickerIds)):
            ticker = tickers[tickerIds[i]]
            low = self.safe_float(ticker, 'low')
            high = self.safe_float(ticker, 'high')
            last = self.safe_float(ticker, 'last')
            open = self.safe_float(ticker, 'open')
            volume = self.safe_float(ticker, 'volume')
            ask = self.safe_float(ticker, 'sell')
            bid = self.safe_float(ticker, 'buy')
            timestamp = self.safe_timestamp(ticker, 'at')
            change = None
            average = None
            percentage = None
            if last is not None and open is not None:
                change = last - open
                average = self.sum(last, open) / 2
            if change is not None and open:
                percentage = (change / open) * 100
            symbol = None
            name = self.safe_string(ticker, 'name')
            if name is not None:
                if name in self.markets_by_id:
                    market = self.markets_by_id[name]
                    symbol = market['symbol']
                else:
                    [baseId, quoteId] = name.split('/')
                    base = self.safe_currency_code(baseId)
                    quote = self.safe_currency_code(quoteId)
                    symbol = base + '/' + quote
            else:
                baseId = self.safe_string(ticker, 'base_unit')
                quoteId = self.safe_string(ticker, 'quote_unit')
                base = self.safe_currency_code(baseId)
                quote = self.safe_currency_code(quoteId)
                symbol = base + '/' + quote
            result[symbol] = {
                'symbol': symbol,
                'info': ticker,
                'timestamp': timestamp,
                'datetime': self.iso8601(timestamp),
                'high': high,
                'low': low,
                'bid': bid,
                'bidVolume': None,
                'ask': ask,
                'askVolume': None,
                'vwap': None,
                'open': open,
                'close': last,
                'last': last,
                'previousClose': None,
                'change': change,
                'percentage': percentage,
                'average': average,
                'baseVolume': volume,
                'quoteVolume': None,
            }
        return result

    async def fetch_order_book(self, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'market': None,
        }
        if market is not None and self.safe_string(market, 'id') is not None:
            request = {
                'market': market['id'],
            }
        response = await self.publicGetDepth(self.extend(request, params))
        #
        #     {
        #          "timestamp":1559561187,
        #          "asks":[
        #                     ["8540.0","1.5"],
        #                     ["8541.0","0.0042"]
        #                 ],
        #          "bids":[
        #                     ["8530.0","0.8814"],
        #                     ["8524.0","1.4"]
        #                 ]
        #      }
        #
        timestamp = self.safe_timestamp(response, 'timestamp')
        return self.parse_order_book(response, timestamp)

    async def fetch_trades(self, symbol, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'market': None,
        }
        if market is not None and self.safe_string(market, 'id') is not None:
            request = {
                'market': market['id'],
            }
        response = await self.publicGetTrades(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    def parse_trade(self, trade, market=None):
        # [
        #     {
        #         "id": 1302646,
        #         "price": "8530.0",
        #         "volume": "0.3207",
        #         "funds": "2735.571",
        #         "market": "btcusdt",
        #         "created_at": "2019-06-03T17:03:41+05:30",
        #         "side": null
        #     }
        # ]
        id = self.safe_string(trade, 'id')
        timestamp = self.parse8601(self.safe_string(trade, 'created_at'))
        datetime = self.iso8601(timestamp)
        symbol = None
        if market is not None:
            symbol = market['symbol']
        side = self.safe_string(trade, 'side')
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'volume')
        cost = self.safe_float(trade, 'funds')
        return {
            'info': trade,
            'id': id,
            'timestamp': timestamp,
            'datetime': datetime,
            'symbol': symbol,
            'order': id,
            'type': None,
            'side': side,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': {
                'cost': None,
                'currency': None,
            },
        }

    def compute_maker_and_taker_fee(self, market):
        fee = self.safe_value(market, 'fee')
        if fee is None:
            return {
                'maker': 0,
                'taker': 0,
            }
        bidMakerFee = 0
        askMakerFee = 0
        bidTakerFee = 0
        askTakerFee = 0
        bid = self.safe_value(fee, 'bid')
        if bid is not None and bid != 0:
            bidMakerFee = self.safe_float(bid, 'maker')
            if bidMakerFee is None:
                bidMakerFee = 0
            bidTakerFee = self.safe_float(bid, 'taker')
            if bidTakerFee is None:
                bidTakerFee = 0
        ask = self.safe_value(fee, 'ask')
        if ask is not None and ask != 0:
            askMakerFee = self.safe_float(ask, 'maker')
            if askMakerFee is None:
                askMakerFee = 0
            askTakerFee = self.safe_float(ask, 'taker')
            if askTakerFee is None:
                askTakerFee = 0
        return {
            'maker': bidMakerFee * 0.5 + askMakerFee * 0.5,
            'taker': bidTakerFee * 0.5 + askTakerFee * 0.5,
        }

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'] + '/api' + '/' + self.version + '/' + path
        if params:
            url += '?' + self.urlencode(params)
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, statusCode, statusText, url, method, responseHeaders, responseBody, response, requestHeaders, requestBody):
        if statusCode != 200:
            feedback = self.id + ' ' + responseBody
            raise ExchangeError(feedback)
