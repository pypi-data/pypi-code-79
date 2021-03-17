# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
import json


class bitkub(Exchange):

    def describe(self):
        return self.deep_extend(super(bitkub, self).describe(), {
            'id': 'bitkub',
            'name': 'bitkub',
            'countries': ['TH'],
            'version': 'v1',
            'has': {
                'CORS': False,
                'fetchCurrencies': False,
                'fetchOHLCV': True,
                'withdraw': False,
                'publicAPI': True,
                'privateAPI': True,
                'fetchMarkets': True,
                'fetchTicker': True,
                'fetchTickers': True,
                'fetchOrderBook': True,
                'fetchTrades': True,
                'fetchMyTrades': True,
                'fetchBalance': True,
                'createOrder': True,
                'cancelOrder': True,
                'fetchDepositAddress': True,
            },
            'timeframes': {
                '1m': 60,
                '5m': 300,
                '15m': 900,
                '30m': 1800,
                '1h': 3600,
                '4h': 14400,
                '1d': 86400,
            },
            'urls': {
                'logo': 'https://www.bitkub.com/static/images/logo-white.png',
                'api': 'https://api.bitkub.com',
                'www': 'https://www.bitkub.com',
                'doc': 'https://github.com/bitkub/bitkub-official-api-docs',
                'fees': 'https://www.bitkub.com/fee/cryptocurrency',
            },
            'api': {
                'public': {
                    'get': [
                        'api/status',
                        'api/servertime',
                        'api/market/symbols',
                        'api/market/ticker',
                        'api/market/trades',
                        'api/market/bids',
                        'api/market/asks',
                        'api/market/books',
                        'api/market/tradingview',
                        'api/market/depth',
                    ],
                },
                'private': {
                    'post': [
                        'api/market/wallet',
                        'api/market/balances',
                        'api/market/place-bid',
                        'api/market/place-ask',
                        'api/market/place-ask-by-fiat',
                        'api/market/cancel-order',
                        'api/market/my-open-orders',
                        'api/market/my-order-history',
                        'api/market/order-info',
                        'api/crypto/addresses',
                        'api/crypto/withdraw',
                        'api/crypto/deposit-history',
                        'api/crypto/withdraw-history',
                        'api/crypto/generate-address',
                        'api/fiat/accounts',
                        'api/fiat/withdraw',
                        'api/fiat/deposit-history',
                        'api/fiat/withdraw-history',
                        'api/market/wstoken',
                        'api/user/limits',
                        'api/user/trading-credits',
                    ],
                },
            },
            'timeout': 5000,
            'rateLimit': 1000,
            'precision': {
                'price': 2,
                'amount': 8,
                'cost': 2,
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'taker': 0.0025,
                    'maker': 0.0025,
                },
            },
        })

    def fetch_markets(self, params={}):
        response = self.publicGetApiMarketSymbols(params)
        markets = response['result']
        result = []
        for i in range(0, len(markets)):
            market = markets[i]
            id = self.safe_string(market, 'symbol')
            currencySymbol = id.split('_')
            base = currencySymbol[1]
            quote = currencySymbol[0]
            baseId = base.lower()
            quoteId = quote.lower()
            symbol = base + '/' + quote
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'info': market,
                'active': True,
                'limits': {
                    'amount': {
                        'min': None,
                        'max': None,
                    },
                    'price': {
                        'min': None,
                        'max': None,
                    },
                    'cost': {
                        'min': 10,
                        'max': None,
                    },
                },
            })
        return result

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privatePostApiMarketBalances(params)
        markets = response['result']
        keyMarkets = list(markets.keys())
        result = {}
        free = {}
        result['info'] = markets
        for i in range(0, len(keyMarkets)):
            key = keyMarkets[i]
            market = markets[key]
            available = self.safe_float(market, 'available')
            reserved = self.safe_float(market, 'reserved')
            free[key] = available
            account = {
                'free': available,
                'used': reserved,
                'total': available + reserved,
            }
            result[key] = account
        return self.parse_balance(result)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        if limit is None:
            limit = 10
        request = {
            'sym': self.market_id(symbol),
            'lmt': limit,
        }
        response = self.publicGetApiMarketBooks(self.extend(request, params))
        orderbook = response['result']
        lastBidTime = orderbook['bids'][0][1]
        lastAskTime = orderbook['asks'][0][1]
        timestamp = lastBidTime if (lastBidTime > lastAskTime) else lastAskTime
        return self.parse_order_book(orderbook, timestamp * 1000, 'bids', 'asks', 3, 4)

    def parse_ticker(self, ticker, market=None):
        symbol = None
        if market is not None:
            symbol = market['symbol']
        timestamp = self.milliseconds()
        last = self.safe_float(ticker, 'last')
        change = self.safe_float(ticker, 'change')
        open = None
        average = None
        if (last is not None) and (change is not None):
            open = last - change
            average = (last + open) / 2
        baseVolume = self.safe_float(ticker, 'baseVolume')
        quoteVolume = self.safe_float(ticker, 'quoteVolume')
        vwap = None
        if quoteVolume is not None:
            if (baseVolume is not None) and (baseVolume > 0):
                vwap = quoteVolume / baseVolume
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(ticker, 'high24hr'),
            'low': self.safe_float(ticker, 'low24hr'),
            'bid': self.safe_float(ticker, 'highestBid'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'lowestAsk'),
            'askVolume': None,
            'vwap': vwap,
            'open': open,
            'close': last,
            'last': last,
            'previousClose': self.safe_float(ticker, 'prevClose'),
            'change': change,
            'percentage': self.safe_float(ticker, 'percentChange'),
            'average': average,
            'baseVolume': baseVolume,
            'quoteVolume': quoteVolume,
            'info': ticker,
        }

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'sym': market['id'],
        }
        response = self.publicGetApiMarketTicker(self.extend(request, params))
        return self.parse_ticker(self.safe_value(response, market['id']), market)

    def fetch_tickers(self, symbols=None, params={}):
        self.load_markets()
        response = self.publicGetApiMarketTicker(params)
        keys = list(response.keys())
        tickers = []
        for i in range(0, len(keys)):
            market = self.safe_value(self.markets_by_id, keys[i])
            tickers.append(self.parse_ticker(response[keys[i]], market))
        return self.filter_by_array(tickers, 'symbol', symbols)

    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'sym': market['id'],
            'int': self.timeframes[timeframe],
        }
        duration = self.timeframes[timeframe]
        timerange = duration * 1000
        if since is None:
            request['to'] = int(self.milliseconds() / 1000)
            request['frm'] = request['to'] - timerange
        else:
            request['frm'] = int(since / 1000)
            request['to'] = self.sum(request['frm'], timerange)
        ohlcv = self.publicGetApiMarketTradingview(self.extend(request, params))
        objOHLCV = list(ohlcv['c'] or [].values())
        length = len(objOHLCV)
        result = []
        for i in range(0, length):
            ts = self.safe_timestamp(ohlcv['t'], i)
            open = ohlcv['o'][i]
            high = ohlcv['h'][i]
            low = ohlcv['l'][i]
            close = ohlcv['c'][i]
            vol = ohlcv['v'][i]
            result.append([])
            newOHLCV = [ts, open, high, low, close, vol]
            result[i].append(newOHLCV)
        return result

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'sym': market['id'],
            'amt': self.amount_to_precision(symbol, amount),
            'rat': self.price_to_precision(symbol, price),
            'typ': type,
        }
        method = side == 'privatePostApiMarketPlaceBid' if 'buy' else 'privatePostApiMarketPlaceAsk'
        response = getattr(self, method)(self.extend(request, params))
        order = response['result']
        id = self.safe_string(order, 'id')
        return {
            'id': id,
            'info': order,
        }

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {}
        if symbol is not None:
            market = self.market(symbol)
            request = {
                'sym': market['id'],
                'id': id,
                'sd': params['sd'],
            }
        else:
            request = {
                'hash': id,
            }
        return self.privatePostApiMarketCancelOrder(self.extend(request, params))

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'sym': market['id'],
        }
        if since is not None:
            request['start'] = int(since / 1000)
            request['end'] = int(self.milliseconds() / 1000)
        if limit is not None:
            request['limit'] = limit
        response = self.privatePostApiMarketMyOrderHistory(self.extend(request, params))
        trades = response['result']
        result = []
        for i in range(0, len(trades)):
            id = self.safe_string(trades[i], 'txn_id')
            order = self.safe_string(trades[i], 'order_id')
            type = self.safe_string(trades[i], 'type')
            side = self.safe_string(trades[i], 'side')
            takerOrMaker = self.safe_value(trades[i], 'taken_by_me')
            price = self.safe_float(trades[i], 'rate')
            amount = self.safe_float(trades[i], 'amount')
            cost = float(price * amount)
            fee = self.safe_float(trades[i], 'fee')
            timestamp = self.safe_timestamp(trades[i], 'ts')
            result.append({
                'info': trades[i],
                'id': id,
                'timestamp': timestamp,
                'datetime': self.iso8601(timestamp),
                'symbol': symbol,
                'order': order,
                'type': type,
                'side': side,
                'takerOrMaker': takerOrMaker == 'taker' if True else 'maker',
                'price': price,
                'amount': amount,
                'cost': cost,
                'fee': fee,
            })
        return result

    def parse_trade(self, trade, market=None):
        timestamp = trade[0] * 1000
        side = None
        side = trade[3].lower()
        price = float(trade[1])
        amount = float(trade[2])
        cost = float(price * amount)
        return {
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': market['symbol'],
            'id': None,
            'order': None,
            'type': None,
            'takerOrMaker': None,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': None,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'sym': market['id'],
        }
        if limit is None:
            limit = 1
        request['lmt'] = limit
        response = self.publicGetApiMarketTrades(self.extend(request, params))
        trades = response['result']
        return self.parse_trades(trades, market, since, limit)

    def fetch_deposit_address(self, code, params={}):
        self.load_markets()
        response = self.privatePostApiCryptoAddresses(params)
        accounts = response['result']
        currency = None
        address = None
        tag = None
        for i in range(0, len(accounts)):
            currency = self.safe_string(accounts[i], 'currency')
            if code == currency:
                address = self.safe_string(accounts[i], 'address')
                tag = self.safe_string(accounts[i], 'tag')
                break
        return {
            'currency': currency,
            'address': address,
            'tag': tag,
            'info': accounts,
        }

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = '/' + path
        if api == 'public':
            if params:
                url += '?' + self.urlencode(params)
        elif api == 'private':
            self.check_required_credentials()
            query = self.extend(params, {
                'ts': self.nonce(),
            })
            request = self.json(query)
            signature = self.hmac(self.encode(request), self.encode(self.secret))
            body = self.json(self.extend(json.loads(request), {'sig': signature}))
            headers = {
                'X-BTK-APIKEY': self.apiKey,
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        else:
            url = '/' + path
        url = self.urls['api'] + url
        return {'url': url, 'method': method, 'body': body, 'headers': headers}
