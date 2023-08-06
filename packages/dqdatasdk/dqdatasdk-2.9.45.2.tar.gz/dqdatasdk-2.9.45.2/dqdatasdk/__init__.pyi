import dqdatasdk.services.financial
import dqdatasdk.services.market_data
import dqdatasdk.services.live_md_client
import dqdatasdk.services.basic
import dqdatasdk.services.get_capital_flow
import dqdatasdk.services.constant
import dqdatasdk.services.calendar
import dqdatasdk.services.factor
import dqdatasdk.services.concept
import dqdatasdk.services.xueqiu
import dqdatasdk.services.index
import dqdatasdk.services.ksh_auction_info
import dqdatasdk.services.future
import dqdatasdk.services.structured_fund
import dqdatasdk.services.convertible
import dqdatasdk.services.tmall
import dqdatasdk.services.options
import dqdatasdk.services.shenwan
import dqdatasdk.services.stock_status
import dqdatasdk.services.live
import dqdatasdk.client
import dqdatasdk.services.get_price

__version__: str = ...
init = dqdatasdk.client.init
reset = dqdatasdk.client.reset
initialized = dqdatasdk.client.initialized
concept_list = dqdatasdk.services.concept.concept_list
concept = dqdatasdk.services.concept.concept
concept_names = dqdatasdk.services.concept.concept_names
shenwan_industry = dqdatasdk.services.shenwan.shenwan_industry
shenwan_instrument_industry = dqdatasdk.services.shenwan.shenwan_instrument_industry
zx_industry = dqdatasdk.services.shenwan.zx_industry
zx_instrument_industry = dqdatasdk.services.shenwan.zx_instrument_industry
get_industry = dqdatasdk.services.shenwan.get_industry
get_instrument_industry = dqdatasdk.services.shenwan.get_instrument_industry
get_industry_mapping = dqdatasdk.services.shenwan.get_industry_mapping
industry_code = dqdatasdk.services.constant.IndustryCode
IndustryCode = dqdatasdk.services.constant.IndustryCode
sector_code = dqdatasdk.services.constant.SectorCode
SectorCode = dqdatasdk.services.constant.SectorCode
get_trading_dates = dqdatasdk.services.calendar.get_trading_dates
get_next_trading_date = dqdatasdk.services.calendar.get_next_trading_date
get_previous_trading_date = dqdatasdk.services.calendar.get_previous_trading_date
get_latest_trading_date = dqdatasdk.services.calendar.get_latest_trading_date
trading_date_offset = dqdatasdk.services.calendar.trading_date_offset
is_trading_date = dqdatasdk.services.calendar.is_trading_date
has_night_trading = dqdatasdk.services.calendar.has_night_trading
id_convert = dqdatasdk.services.basic.id_convert
instruments = dqdatasdk.services.basic.instruments
all_instruments = dqdatasdk.services.basic.all_instruments
sector = dqdatasdk.services.basic.sector
industry = dqdatasdk.services.basic.industry
get_future_contracts = dqdatasdk.services.basic.get_future_contracts


class futures:
    get_commission_margin = dqdatasdk.services.future.get_commission_margin
    get_contracts = dqdatasdk.services.basic.get_contracts
    get_dominant = dqdatasdk.services.future.get_dominant
    get_dominant_price = dqdatasdk.services.future.get_dominant_price
    get_member_rank = dqdatasdk.services.future.get_member_rank
    get_warehouse_stocks = dqdatasdk.services.future.get_warehouse_stocks
    get_contract_multiplier = dqdatasdk.services.future.get_contract_multiplier
    get_ex_factor = dqdatasdk.services.future.get_ex_factor


jy_instrument_industry = dqdatasdk.services.basic.jy_instrument_industry


class econ:
    get_factors = dqdatasdk.services.basic.get_factors
    get_money_supply = dqdatasdk.services.basic.get_money_supply
    get_reserve_ratio = dqdatasdk.services.basic.get_reserve_ratio


get_main_shareholder = dqdatasdk.services.basic.get_main_shareholder
get_current_news = dqdatasdk.services.basic.get_current_news
get_trading_hours = dqdatasdk.services.basic.get_trading_hours
get_private_placement = dqdatasdk.services.basic.get_private_placement
get_share_transformation = dqdatasdk.services.basic.get_share_transformation


class user:
    get_quota = dqdatasdk.services.basic.get_quota


get_update_status = dqdatasdk.services.basic.get_update_status
info = dqdatasdk.services.basic.info
get_basic_info = dqdatasdk.services.basic.get_basic_info


class convertible:
    all_instruments = dqdatasdk.services.convertible.all_instruments
    get_call_info = dqdatasdk.services.convertible.get_call_info
    get_cash_flow = dqdatasdk.services.convertible.get_cash_flow
    get_conversion_info = dqdatasdk.services.convertible.get_conversion_info
    get_conversion_price = dqdatasdk.services.convertible.get_conversion_price
    get_credit_rating = dqdatasdk.services.convertible.get_credit_rating
    get_indicators = dqdatasdk.services.convertible.get_indicators
    get_industry = dqdatasdk.services.convertible.get_industry
    get_instrument_industry = dqdatasdk.services.convertible.get_instrument_industry
    get_latest_rating = dqdatasdk.services.convertible.get_latest_rating
    get_put_info = dqdatasdk.services.convertible.get_put_info
    instruments = dqdatasdk.services.convertible.instruments
    is_suspended = dqdatasdk.services.convertible.is_suspended
    rating = dqdatasdk.services.convertible.rating


get_dominant_future = dqdatasdk.services.future.get_dominant_future
future_commission_margin = dqdatasdk.services.future.future_commission_margin
get_future_member_rank = dqdatasdk.services.future.get_future_member_rank
current_stock_connect_quota = dqdatasdk.services.stock_status.current_stock_connect_quota
get_stock_connect_quota = dqdatasdk.services.stock_status.get_stock_connect_quota
is_st_stock = dqdatasdk.services.stock_status.is_st_stock
_is_st_stock = dqdatasdk.services.stock_status._is_st_stock
is_suspended = dqdatasdk.services.stock_status.is_suspended
get_stock_connect = dqdatasdk.services.stock_status.get_stock_connect
get_securities_margin = dqdatasdk.services.stock_status.get_securities_margin
get_margin_stocks = dqdatasdk.services.stock_status.get_margin_stocks
get_shares = dqdatasdk.services.stock_status.get_shares
get_allotment = dqdatasdk.services.stock_status.get_allotment
current_snapshot = dqdatasdk.services.live.current_snapshot
get_ticks = dqdatasdk.services.live.get_ticks
current_minute = dqdatasdk.services.live.current_minute
get_live_ticks = dqdatasdk.services.live.get_live_ticks
get_price = dqdatasdk.services.get_price.get_price
LiveMarketDataClient = dqdatasdk.services.live_md_client.LiveMarketDataClient
get_all_factor_names = dqdatasdk.services.factor.get_all_factor_names
get_factor = dqdatasdk.services.factor.get_factor
get_factor_return = dqdatasdk.services.factor.get_factor_return
get_factor_exposure = dqdatasdk.services.factor.get_factor_exposure
get_style_factor_exposure = dqdatasdk.services.factor.get_style_factor_exposure
get_descriptor_exposure = dqdatasdk.services.factor.get_descriptor_exposure
get_stock_beta = dqdatasdk.services.factor.get_stock_beta
get_factor_covariance = dqdatasdk.services.factor.get_factor_covariance
get_specific_return = dqdatasdk.services.factor.get_specific_return
get_specific_risk = dqdatasdk.services.factor.get_specific_risk
get_index_factor_exposure = dqdatasdk.services.factor.get_index_factor_exposure
Financials = dqdatasdk.services.financial.Financials
financials = dqdatasdk.services.financial.Financials
get_financials = dqdatasdk.services.financial.get_financials
PitFinancials = dqdatasdk.services.financial.PitFinancials
pit_financials = dqdatasdk.services.financial.PitFinancials
get_pit_financials = dqdatasdk.services.financial.get_pit_financials
get_pit_financials_ex = dqdatasdk.services.financial.get_pit_financials_ex
get_fundamentals = dqdatasdk.services.financial.get_fundamentals
deprecated_fundamental_data = dqdatasdk.services.financial.deprecated_fundamental_data
current_performance = dqdatasdk.services.financial.current_performance
performance_forecast = dqdatasdk.services.financial.performance_forecast
Fundamentals = dqdatasdk.services.financial.Fundamentals
fundamentals = dqdatasdk.services.financial.Fundamentals
query = dqdatasdk.services.financial.query_entities
get_capital_flow = dqdatasdk.services.get_capital_flow.get_capital_flow
get_open_auction_info = dqdatasdk.services.get_capital_flow.get_open_auction_info
get_close_auction_info = dqdatasdk.services.get_capital_flow.get_close_auction_info
index_components = dqdatasdk.services.index.index_components
index_weights = dqdatasdk.services.index.index_weights
index_indicator = dqdatasdk.services.index.index_indicator
get_ksh_auction_info = dqdatasdk.services.ksh_auction_info.get_ksh_auction_info
get_split = dqdatasdk.services.market_data.get_split
get_dividend = dqdatasdk.services.market_data.get_dividend
get_dividend_info = dqdatasdk.services.market_data.get_dividend_info
get_ex_factor = dqdatasdk.services.market_data.get_ex_factor
get_turnover_rate = dqdatasdk.services.market_data.get_turnover_rate
get_price_change_rate = dqdatasdk.services.market_data.get_price_change_rate
get_yield_curve = dqdatasdk.services.market_data.get_yield_curve
get_block_trade = dqdatasdk.services.market_data.get_block_trade
get_exchange_rate = dqdatasdk.services.market_data.get_exchange_rate
get_temporary_code = dqdatasdk.services.market_data.get_temporary_code


class options:
    get_contract_property = dqdatasdk.services.options.get_contract_property
    get_contracts = dqdatasdk.services.options.get_contracts
    get_greeks = dqdatasdk.services.options.get_greeks




class fenji:
    get = dqdatasdk.services.structured_fund.get
    get_a_by_interest_rule = dqdatasdk.services.structured_fund.get_a_by_interest_rule
    get_a_by_yield = dqdatasdk.services.structured_fund.get_a_by_yield
    get_all = dqdatasdk.services.structured_fund.get_all


ecommerce = dqdatasdk.services.tmall.ecommerce


class xueqiu:
    history = dqdatasdk.services.xueqiu.history
    top_stocks = dqdatasdk.services.xueqiu.top_stocks


get_consensus_indicator = dqdatasdk.services.consensus.get_consensus_indicator
get_consensus_price = dqdatasdk.services.consensus.get_consensus_price
