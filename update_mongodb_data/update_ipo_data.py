from download_stock_daily_data.get_ipo_data_from_joinquant import *
from data_base.mongodb import MongoDB_io


if __name__=='__main__':
    m=MongoDB_io()
    m.remove_all_documents_from_mongodb()
    insert_ipo_data()
    pass
