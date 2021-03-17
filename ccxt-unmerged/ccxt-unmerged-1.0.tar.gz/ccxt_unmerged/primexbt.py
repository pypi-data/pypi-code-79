# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
import math


class primexbt(Exchange):

    def describe(self):
        return self.deep_extend(super(primexbt, self).describe(), {
            'id': 'primexbt',
            'name': 'Prime XBT',
            'countries': ['SC'],  # Seychelles
            'version': 'v1',
            'userAgent': None,
            # 'rateLimit': 2000,
            'has': {
                'CORS': False,
                'createMarketOrder': False,
                'fetchTicker': False,
                'fetchTickers': False,
                'fetchOrderBook': True,
                'withdraw': False,
                'fetchDeposits': False,
                'fetchWithdrawals': False,
                'fetchTransactions': False,
                'createDepositAddress': False,
                'fetchDepositAddress': False,
                'fetchClosedOrders': False,
                'fetchTrades': False,
                'fetchOHLCV': False,
                'fetchOpenOrders': False,
                'fetchOrderTrades': False,
                'fetchOrders': False,
                'fetchOrder': False,
                'fetchMyTrades': False,
            },
            'timeframes': {},
            'urls': {
                'test': None,
                'logo': None,
                'api': {
                    'public': 'https://api.primexbt.com',
                    'private': 'https://api.primexbt.com',
                },
                'www': 'https://primexbt.com/',
                'doc': None,
                'fees': 'https://primexbt.com/fees',
                'referral': None,
                'websocket': ['wss://api.primexbt.com/v1/pws'],
            },
            'api': {
                'public': {
                    'get': [
                        'markets',
                        'dom',
                    ],
                },
                'private': {
                    'get': [],
                    'post': [],
                    'put': [],
                    'delete': [],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'maker': 0.0005,
                    'taker': 0.0005,
                },
                'funding': {
                    'tierBased': False,
                    'percentage': False,
                    'deposit': {},
                    'withdraw': {
                        'BTC': 0.0005,
                    },
                },
            },
            'exceptions': {
                'exact': {},
                'broad': {},
            },
            'options': {},
        })

    def fetch_markets(self, params={}):
        query = self.extend({
            'category': 'crypto',
        }, params)
        response = self.publicGetMarkets(query)
        # {
        #   "data": [
        #     {
        #        "name":              "BTC/USD",
        #        "base":              "BTC",
        #        "quote":             "USD",
        #        "last":              9274.1,
        #        "change":            -0.22,
        #        "price_scale":       1,
        #        "description":       "Bitcoin",
        #        "qty_scale":         2,
        #        "open":              9294.6,
        #        "turnover":          11979.695,
        #        "turnover_usd":      1.1033671229E8,
        #        "open_interest":     1705.34,
        #        "open_interest_btc": 1705.34,
        #        "price":             9274.1,
        #        "change24h":         -0.22,
        #        "priceScale":        1
        #     }
        #   ]
        # }
        data = response['data']
        result = []
        for i in range(0, len(data)):
            market = data[i]
            active = True
            id = market['name']
            baseId = market['base']
            quoteId = market['quote']
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            precision = {
                'amount': market['qty_scale'],
                'price': market['price_scale'],
            }
            limits = {
                'amount': {
                    'min': math.pow(10, -precision['amount']),
                    'max': None,
                },
                'price': {
                    'min': math.pow(10, -precision['price']),
                    'max': None,
                },
                'cost': {
                    'min': None,
                    'max': None,
                },
            }
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': active,
                'precision': precision,
                'limits': limits,
                'type': 'future',
                'spot': False,
                'swap': False,
                'future': True,
                'prediction': False,
                'info': market,
            })
        return result

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        if limit is not None:
            request['depth'] = limit
        response = self.publicGetDom(self.extend(request, params))
        # {
        #   "symbol": "BTC/USD",
        #   "sells":  [[9271, 178.90452476549999], ...],
        #   "bids":   [[9270.9, 282.15991329099995], ...],
        # }
        keys = ['bids','sells']
        for i in range(0, len(keys)):
            key = keys[i]
            # Each price has two entries with identical volumes; drop the duplicates
            response[key] = self.to_array(self.index_by(response[key], 0))
        return self.parse_order_book(response, None, 'bids', 'sells')

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'][api] + '/' + self.version + '/' + path
        if method == 'GET':
            if params:
                url += '?' + self.urlencode(params)
        return {'url': url, 'method': method, 'body': body, 'headers': headers}
