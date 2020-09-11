import scrapy


class GetdataItem(scrapy.Item):
    _id = scrapy.Field()

    macro_country = scrapy.Field()
    macro_gdp = scrapy.Field()
    macro_gdp_yoy = scrapy.Field()
    macro_gdp_qoq = scrapy.Field()
    macro_interest = scrapy.Field()
    macro_inflation = scrapy.Field()
    macro_jobless = scrapy.Field()
    macro_budget = scrapy.Field()
    macro_debt_to_gdp = scrapy.Field()
    macro_cur_acc = scrapy.Field()
    macro_population = scrapy.Field()

    cur_name = scrapy.Field()
    cur_price = scrapy.Field()
    cur_delta_now = scrapy.Field()
    cur_delta_day = scrapy.Field()
    cur_delta_week = scrapy.Field()
    cur_delta_month = scrapy.Field()
    cur_delta_year = scrapy.Field()
    cur_data_date = scrapy.Field()

    stocks_ticker = scrapy.Field()
    stocks_name = scrapy.Field()
    stocks_price = scrapy.Field()
    stocks_delta_now = scrapy.Field()
    stocks_delta_day = scrapy.Field()
    stocks_delta_week = scrapy.Field()
    stocks_delta_month = scrapy.Field()
    stocks_delta_year = scrapy.Field()
    stocks_data_date = scrapy.Field()

    index_name = scrapy.Field()
    index_price = scrapy.Field()
    index_delta_now = scrapy.Field()
    index_delta_day = scrapy.Field()
    index_delta_week = scrapy.Field()
    index_delta_month = scrapy.Field()
    index_delta_year = scrapy.Field()
    index_data_date = scrapy.Field()

    commodities_name = scrapy.Field()
    commodities_price = scrapy.Field()
    commodities_delta_now = scrapy.Field()
    commodities_delta_day = scrapy.Field()
    commodities_delta_week = scrapy.Field()
    commodities_delta_month = scrapy.Field()
    commodities_delta_year = scrapy.Field()
    commodities_data_date = scrapy.Field()

    bonds_name = scrapy.Field()
    bonds_price = scrapy.Field()
    bonds_delta_now = scrapy.Field()
    bonds_delta_day = scrapy.Field()
    bonds_delta_week = scrapy.Field()
    bonds_delta_month = scrapy.Field()
    bonds_delta_year = scrapy.Field()
    bonds_data_date = scrapy.Field()

    cian_variables = scrapy.Field()
    cian_pic = scrapy.Field()

    irn_pic = scrapy.Field()

    news_variables = scrapy.Field()
    news_rubric = scrapy.Field()
    news_topic = scrapy.Field()
    news_resume = scrapy.Field()
    news_href = scrapy.Field()
    news_text = scrapy.Field()
