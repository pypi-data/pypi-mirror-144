from enum import Enum, auto


class APIType(Enum):
    CFS = auto()
    FINANCIAL_CONTRACTS = auto()
    STREAMING_FINANCIAL_CONTRACTS = auto()
    CURVES_AND_SURFACES = auto()
    HISTORICAL_PRICING = auto()
    ESG = auto()
    PRICING = auto()
    STREAMING_PRICING = auto()
    OWNERSHIP = auto()
    CHAINS = auto()
    STREAMING_TRADING = auto()
    STREAMING_BENCHMARK = auto()
    STREAMING_CUSTOM = auto()
    DATA_GRID = auto()
    NEWS = auto()
    DISCOVERY = auto()
    ESTIMATES = auto()
