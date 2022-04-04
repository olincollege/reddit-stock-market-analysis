# Stonks - A Reddit Story

### Contributors: Andrew DeCandia, Emma Fox, and Shamama Sirroon

This project creates a way to determine whether /r/wallstreetbets gives accurate predictions of what stocks will be good to invest in. We compare the ROI of recommended stocks to the S&P 500.

We make use of multiple APIs in order to obtain data from Reddit and Alpaca Markets.

## Set Up

To be able to run these files, you should pip install the following libraries and packages:
* `pip install alpaca_trade_api`
* `pip install datetime`
* `pip install matplotlib`
* `pip install pandas`
* `pip install pmaw`
* `pip install re`

In order to set up the Alpaca Market API, you need to set up credentials and log in. Our credentials are in a file that is ignored by Git. The website for the Alpaca Market API is linked: https://alpaca.markets/docs/api-references/market-data-api/stock-pricing-data/. The GitHub also has more information on how to set up using the API: https://github.com/alpacahq/alpaca-trade-api-python. The PMAW API does not require credentials.