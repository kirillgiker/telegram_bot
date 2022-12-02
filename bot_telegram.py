from aiogram import Bot, Dispatcher, executor, types
import os
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import schedule
import time

API_TOKEN = "" # telegram bot api

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

symbol_btcusd = "BTC/USD" #for sma99 / twelvedata symbols
symbol_ethusd = "ETH/USD"
symbol_bnbusd = "BNB/USD"

pair_name_btcusd = "BTC-USD" #for sma33 / yahoofinance symbols
pair_name_bnbusd = "BNB-USD"
pair_name_ethusd = "ETH-USD"
pair_tickerbtcusd = yf.Ticker(pair_name_btcusd) #yahoofinance pair data
pair_tickerbnbusd = yf.Ticker(pair_name_bnbusd)
pair_tickerethusd = yf.Ticker(pair_name_ethusd) 
apikey = "" # apikey from twelvedata.com
def sma33(pair_name): #data with sma33 / 15 min
    pair = yf.download(pair_name, period="1wk", interval="15m")
    result = pair['Close'].rolling(33).mean()
    return result
def sma99(symbol, apikey):  #request with sma99 / 45 min  $*$*$*$* NOT USING $*$*$*$*$*$*$
    url = "https://api.twelvedata.com/ma?symbol=" + symbol + "&interval=45min&time_period=99&apikey=" + apikey
    answer = requests.get(url) 
    json = answer.json()
    return json["values"][0]["ma"]
a = True
@dp.message_handler(commands=["start"])
async def alltime(message: types.Message):
    while a: # endless loop
        pair_tickerbtcusd = yf.Ticker(pair_name_btcusd) #yahoofinance pair data
        pair_tickerbnbusd = yf.Ticker(pair_name_bnbusd)
        pair_tickerethusd = yf.Ticker(pair_name_ethusd) 
        databtc = float(pair_tickerbtcusd.info['regularMarketPrice'])
        databnb = float(pair_tickerbnbusd.info['regularMarketPrice'])
        dataeth = float(pair_tickerethusd.info['regularMarketPrice'])
        btc_usd33 = float(sma33(pair_name_btcusd)[-1])
        bnb_usd33 = float(sma33(pair_name_bnbusd)[-1])
        eth_usd33 = float(sma33(pair_name_ethusd)[-1])
        if databtc > btc_usd33: #btc flags
            flagbtc33 = True
        if databtc < btc_usd33:
            flagbtc33 = False
        if databnb > bnb_usd33: #bnb flags
            flagbnb33 = True
        if databnb < bnb_usd33:
            flagbnb33 = False
        if dataeth > eth_usd33: #eth flags
            flageth33 = True
        if dataeth < eth_usd33:
            flageth33 = False
        time.sleep(1)
        btc_usd33 = float(sma33(pair_name_btcusd)[-1])
        bnb_usd33 = float(sma33(pair_name_bnbusd)[-1])
        eth_usd33 = float(sma33(pair_name_ethusd)[-1])
        pair_tickerbtcusd = yf.Ticker(pair_name_btcusd) #yahoofinance pair data
        pair_tickerbnbusd = yf.Ticker(pair_name_bnbusd)
        pair_tickerethusd = yf.Ticker(pair_name_ethusd) 
        databtc = float(pair_tickerbtcusd.info['regularMarketPrice'])
        databnb = float(pair_tickerbnbusd.info['regularMarketPrice'])
        dataeth = float(pair_tickerethusd.info['regularMarketPrice'])
        if databtc > btc_usd33 and not(flagbtc33):
            flagbtc33 = True
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "btc/usd пробил sma33 снизу")
        if databtc < btc_usd33 and flagbtc33:
            flagbtc33 = False
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "btc/usd пробил sma33 сверху")
        if databnb > bnb_usd33 and not(flagbnb33):
            flagbnb33 = True
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "bnb/usd пробил sma33 снизу")
        if databnb < bnb_usd33 and flagbnb33:
            flagbnb33 = False
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "bnb/usd пробил sma33 сверху")
        if dataeth > eth_usd33 and not(flageth33):
            flageth33 = True
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "eth/usd пробил sma33 снизу")
        if dataeth < eth_usd33 and flageth33:
            flageth33 = False
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "eth/usd пробил sma33 сверху")
        time.sleep(1)
        btc_usd33 = float(sma33(pair_name_btcusd)[-1])
        bnb_usd33 = float(sma33(pair_name_bnbusd)[-1])
        eth_usd33 = float(sma33(pair_name_ethusd)[-1])
        pair_tickerbtcusd = yf.Ticker(pair_name_btcusd) #yahoofinance pair data
        pair_tickerbnbusd = yf.Ticker(pair_name_bnbusd)
        pair_tickerethusd = yf.Ticker(pair_name_ethusd) 
        databtc = float(pair_tickerbtcusd.info['regularMarketPrice'])
        databnb = float(pair_tickerbnbusd.info['regularMarketPrice'])
        dataeth = float(pair_tickerethusd.info['regularMarketPrice'])
        if databtc > btc_usd33 and not(flagbtc33):
            flagbtc33 = True
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "btc/usd пробил sma33 снизу")
        if databtc < btc_usd33 and flagbtc33:
            flagbtc33 = False
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "btc/usd пробил sma33 сверху")
        if databnb > bnb_usd33 and not(flagbnb33):
            flagbnb33 = True
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "bnb/usd пробил sma33 снизу")
        if databnb < bnb_usd33 and flagbnb33:
            flagbnb33 = False
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "bnb/usd пробил sma33 сверху")
        if dataeth > eth_usd33 and not(flageth33):
            flageth33 = True
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "eth/usd пробил sma33 снизу")
        if dataeth < eth_usd33 and flageth33:
            flageth33 = False
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "eth/usd пробил sma33 сверху")
        time.sleep(1)
        btc_usd33 = float(sma33(pair_name_btcusd)[-1])
        bnb_usd33 = float(sma33(pair_name_bnbusd)[-1])
        eth_usd33 = float(sma33(pair_name_ethusd)[-1])
        pair_tickerbtcusd = yf.Ticker(pair_name_btcusd) #yahoofinance pair data
        pair_tickerbnbusd = yf.Ticker(pair_name_bnbusd)
        pair_tickerethusd = yf.Ticker(pair_name_ethusd) 
        databtc = float(pair_tickerbtcusd.info['regularMarketPrice'])
        databnb = float(pair_tickerbnbusd.info['regularMarketPrice'])
        dataeth = float(pair_tickerethusd.info['regularMarketPrice'])
        if databtc > btc_usd33 and not(flagbtc33):
            flagbtc33 = True
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "btc/usd пробил sma33 снизу")
        if databtc < btc_usd33 and flagbtc33:
            flagbtc33 = False
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "btc/usd пробил sma33 сверху")
        if databnb > bnb_usd33 and not(flagbnb33):
            flagbnb33 = True
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "bnb/usd пробил sma33 снизу")
        if databnb < bnb_usd33 and flagbnb33:
            flagbnb33 = False
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "bnb/usd пробил sma33 сверху")
        if dataeth > eth_usd33 and not(flageth33):
            flageth33 = True
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "eth/usd пробил sma33 снизу")
        if dataeth < eth_usd33 and flageth33:
            flageth33 = False
            with open("id.txt") as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    await bot.send_message(user_id, "eth/usd пробил sma33 сверху")

executor.start_polling(dp, skip_updates=True)
