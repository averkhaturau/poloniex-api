__author__ = 'andrey.samokhvalov21@yandex.ru'

CHART_DATA_PERIODS = [300, 900, 1800, 7200, 14400, 86400]
CURRENCY_PAIRS_OLD = [
    'BTC_HUC', 'BTC_CNMT', 'BTC_UNITY', 'BTC_BITS', 'BTC_SWARM', 'BTC_NXT', 'BTC_GMC', 'BTC_BITCNY', 'BTC_BLOCK',
    'XMR_LTC', 'BTC_EMC2', 'BTC_POT', 'BTC_DOGE', 'BTC_RIC', 'BTC_XCR', 'BTC_SC', 'BTC_RDD', 'BTC_PIGGY', 'BTC_EXP',
    'BTC_XPM', 'USDT_ETH', 'BTC_SYNC', 'BTC_XPB', 'BTC_PPC', 'BTC_XCH', 'BTC_ABY', 'BTC_MINT', 'USDT_DASH', 'BTC_XRP',
    'BTC_DIEM', 'XMR_DSH', 'BTC_XEM', 'USDT_XMR', 'BTC_VTC', 'BTC_XDP', 'BTC_STR', 'BTC_GRS', 'BTC_DGB', 'BTC_FLT',
    'BTC_XC', 'BTC_HZ', 'BTC_CLAM', 'USDT_XRP', 'BTC_XBC', 'XMR_HYP', 'BTC_NOTE', 'BTC_INDEX', 'BTC_MMNXT', 'BTC_NAUT',
    'USDT_LTC', 'BTC_SYS', 'USDT_STR', 'BTC_FLO', 'BTC_MYR', 'XMR_BTCD', 'BTC_BBR', 'XMR_BLK', 'BTC_RBY', 'BTC_LTBC',
    'BTC_MAID', 'BTC_1CR', 'BTC_BTM', 'BTC_GEMZ', 'BTC_NOXT', 'BTC_FCT', 'BTC_OMNI', 'BTC_FLDC', 'BTC_VRC', 'XMR_DASH',
    'BTC_XUSD', 'BTC_MMC', 'BTC_BTS', 'BTC_PTS', 'BTC_EXE', 'BTC_IOC', 'BTC_SDC', 'BTC_QORA', 'XMR_MNTA', 'BTC_XMG',
    'BTC_C2', 'XMR_XDN', 'BTC_BELA', 'BTC_BITUSD', 'XMR_NXT', 'BTC_BURST', 'BTC_MRS', 'USDT_BTC', 'BTC_BCN', 'BTC_XMR',
    'BTC_GRC', 'BTC_CURE', 'BTC_NEOS', 'BTC_BTCD', 'BTC_QBK', 'BTC_NOBL', 'BTC_MCN', 'XMR_BBR', 'BTC_XCN', 'BTC_NBT',
    'BTC_XDN', 'BTC_YACC', 'BTC_QTL', 'BTC_LQD', 'BTC_NAV', 'BTC_NMC', 'BTC_NSR', 'BTC_MIL', 'BTC_FIBRE', 'BTC_WDC',
    'BTC_ADN', 'BTC_ARCH', 'BTC_VIA', 'XMR_BCN', 'XMR_DIEM', 'BTC_GEO', 'BTC_XCP', 'BTC_BLK', 'BTC_ETH', 'BTC_DASH',
    'XMR_IFC', 'BTC_XST', 'BTC_SILK', 'XMR_QORA', 'BTC_BCY', 'BTC_VNL', 'XMR_MAID', 'USDT_NXT', 'BTC_CGA', 'BTC_PINK',
    'BTC_SJCX', 'BTC_LTC', 'BTC_GAP', 'BTC_HYP', 'BTC_DAO', 'BTC_LSK'
]

CURRENCY_PAIRS = [
    'BTC_QTL', 'ETH_STEEM', 'XMR_BTCD', 'BTC_BLK', 'BTC_BCY', 'BTC_NBT', 'BTC_BTM', 'BTC_LTC', 'BTC_ETH', 'BTC_RBY',
    'XMR_BCN', 'BTC_SDC', 'BTC_NOTE', 'BTC_LSK', 'BTC_BURST', 'BTC_PPC', 'BTC_SC', 'BTC_RADS', 'BTC_XCN', 'BTC_FCT',
    'XMR_BBR', 'XMR_QORA', 'BTC_ETC', 'XMR_LTC', 'BTC_LBC', 'BTC_XEM', 'XMR_BLK', 'BTC_SYS', 'BTC_BITCNY', 'BTC_SBD',
    'BTC_DOGE', 'ETH_REP', 'BTC_GAME', 'BTC_XRP', 'BTC_BLOCK', 'BTC_HUC', 'BTC_EMC2', 'BTC_SYNC', 'BTC_XVC', 'BTC_XDN',
    'XMR_DASH', 'BTC_C2', 'BTC_BELA', 'BTC_DGB', 'BTC_XMR', 'BTC_VIA', 'BTC_XCP', 'BTC_BCN', 'BTC_MYR', 'BTC_XST',
    'BTC_BTCD', 'BTC_FLDC', 'BTC_XMG', 'ETH_ETC', 'BTC_NXT', 'BTC_LTBC', 'BTC_EXP', 'BTC_SJCX', 'BTC_NEOS', 'BTC_1CR',
    'BTC_OMNI', 'USDT_ETC', 'BTC_HZ', 'BTC_AMP', 'BTC_UNITY', 'XMR_ZEC', 'BTC_PINK', 'BTC_DASH', 'USDT_DASH', 'BTC_NAUT',
    'BTC_BITS', 'USDT_STR', 'BTC_VTC', 'ETH_LSK', 'USDT_BTC', 'BTC_RDD', 'BTC_MMNXT', 'XMR_MAID', 'BTC_CURE', 'ETH_ZEC',
    'BTC_DIEM', 'BTC_XPM', 'BTC_DCR', 'BTC_STR', 'BTC_NOBL', 'BTC_POT', 'BTC_XBC', 'BTC_NAV', 'USDT_XMR', 'BTC_FLO',
    'USDT_XRP', 'BTC_MAID', 'BTC_BBR', 'BTC_RIC', 'XMR_DIEM', 'USDT_LTC', 'BTC_GEO', 'USDT_ETH', 'BTC_IOC', 'BTC_QORA',
    'XMR_NXT', 'BTC_NSR', 'BTC_ZEC', 'BTC_VOX', 'BTC_NMC', 'USDT_ZEC', 'BTC_ARDR', 'USDT_REP', 'USDT_NXT', 'BTC_CLAM',
    'BTC_GRC', 'BTC_BTS', 'BTC_REP', 'BTC_VRC', 'XMR_XDN', 'BTC_STEEM', 'BTC_QBK'
]

#AVAILABLE_SUBSCRIPTIONS = CURRENCY_PAIRS[:]
AVAILABLE_SUBSCRIPTIONS = [
    'footer',
    'ticker',
    'trollbox',
    'alerts',
    'heartbeat',
]
