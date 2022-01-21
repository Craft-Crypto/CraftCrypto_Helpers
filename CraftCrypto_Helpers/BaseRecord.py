from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class BaseRecord:
    # Base Information
    childs: list[dict] = field(default_factory=lambda: [])  # Follow up trades, DCA Trades, etc. changes to list
    my_id: str = '0'
    symbol: str = 'BTC/USD'
    exchange: str = 'Binance'
    ex_icon: str = 'Binance_icon.png'
    coin: str = 'BTC'
    pair: str = 'USD'
    candle: str = '1m'
    status: str = ''
    active: bool = False
    sold: bool = False
    error: str = ''
    last_update: str = ''

    # Amount to Buy
    pair_per: str = ''
    pair_amt: str = ''
    pair_minmult: str = ''

    # Selling Parameters
    take_profit_per: str = '0'
    take_profit_price: str = '0'
    stop_per: str = '0'
    stop_price: str = '0'
    trail_per: str = '0'
    trail_price: str = '0'
    dca_buyback_per: str = '0'
    dca_buyback_price: str = '0'

    # Trade Details
    trade_amount: str = '0'
    buy_price: str = '0'
    sold_price: str = '0'
    gl_per: str = '0'
    now_price: str = '0'
    trade_id: str = '0'
    buy_trade_id: str = '0'
    sell_trade_id: str = '0'
    kind: str = ''  # market, limit, loop, strat name for basic, NEED TO PUT ADVANCED
    is_buy: bool = True  # false is sell
    ready_sell: bool = False  # for all the trading data
    leverage: str = '0'
    sell_now: bool = False
    buy_now: bool = False

    # Trading Pair Details
    coin_bal: str = '0'
    pair_bal: str = '0'
    coin_min_trade: str = '0'
    cost_min_trade: str = '0'
    precision: str = '.1111111111'
    trade_vol: str = '0'
    average_buys: str = '0'
    average_sells: str = '0'
    average_per_gain: str = '0'
    num_trades: str = '0'
    num_buys: str = '0'
    num_sells: str = '0'
    buy_vol: str = '0'
    sell_vol: str = '0'

    # Technical Indicator Data
    ema: str = ''  # Length
    ema_val: str = ''  # Value of EMA now
    ema_percent: str = ''  # Amount to modify EMA
    ema_buy: bool = False
    ema_sell: bool = False

    sma: str = ''
    sma_val: str = ''
    sma_buy: bool = False
    sma_sell: bool = False
    sma_percent: str = ''

    ema_cross_fast: str = ''
    ema_cross_slow: str = ''
    ema_cross_val_fast: str = ''
    ema_cross_val_slow: str = ''
    ema_cross_buy: bool = False
    ema_cross_sell: bool = False

    sma_cross_fast: str = ''
    sma_cross_slow: str = ''
    sma_cross_val_fast: str = ''
    sma_cross_val_slow: str = ''
    sma_cross_buy: bool = False
    sma_cross_sell: bool = False

    ema_sma_cross_fast: str = ''
    ema_sma_cross_slow: str = ''
    ema_sma_cross_val_fast: str = ''
    ema_sma_cross_val_slow: str = ''
    ema_sma_cross_buy: bool = False
    ema_sma_cross_sell: bool = False

    rsi_val: str = ''
    rsi_buy: str = ''
    rsi_sell: str = ''

    bb_width_val: str = ''
    bb_under_val: str = ''
    bb_over_val: str = ''
    bb_buy: str = ''  # %above/below upper band
    bb_sell: str = ''

    macd_val: str = ''
    macd_signal_val: str = ''
    macd_cross_buy: bool = False
    macd_cross_sell: bool = False
    macd_0_buy: bool = False
    macd_0_sell: bool = False
    macd_color_buy: bool = False
    macd_color_sell: bool = False

    stoch_cross_buy: bool = False
    stoch_cross_sell: bool = False

    stoch_k_val: str = ''
    stoch_d_val: str = ''
    stoch_val_buy: bool = False
    stoch_val_sell: bool = False

    psar_val: str = ''
    psar_cross_buy: bool = False
    psar_cross_sell: bool = False

