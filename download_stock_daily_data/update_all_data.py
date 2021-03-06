from data_base.mongodb import MongoDB_io
import download_stock_daily_data.get_capital_data
import download_stock_daily_data.get_industry_stocks
import download_stock_daily_data.get_post_market_data
import download_stock_daily_data.get_real_market_data
import download_stock_daily_data.get_trade_day
import download_stock_daily_data.get_zz500_weight
import download_stock_daily_data.get_adj_factor


m = MongoDB_io()
download_stock_daily_data.get_capital_data.insert_capital_data()
download_stock_daily_data.get_industry_stocks.insert_industry_stock()
download_stock_daily_data.get_post_market_data.insert_price_data('post')
download_stock_daily_data.get_real_market_data.insert_price_data()
download_stock_daily_data.get_trade_day.insert_trade_date_data()
download_stock_daily_data.get_zz500_weight.insert_zz500_weight()
download_stock_daily_data.get_adj_factor.insert_adj_factor()