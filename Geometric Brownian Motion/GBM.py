# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:16:44 2023

@author: soren
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import yfinance as yf


fig1, ax  = plt.subplots(1, 2, sharey=True)
# Request historical data for past 5 years
data = yf.Ticker("NVDA").history(period='11mo')
# Show info
#print(data.info())
prices = data["Open"].to_numpy()
logprices = np.log(prices)
logreturns = logprices[1:]-logprices[:-1]
firstperiod = logreturns[:logreturns.shape[0]//2]
mu = np.mean(firstperiod)
sigma = np.std(firstperiod)
trading_days = firstperiod.shape[0]
print(trading_days)

S0 = prices[trading_days+1]
n_sims = 10000
timesteps = trading_days
time = np.linspace(0,trading_days,timesteps+1)
print(time.shape)
dt =  time[1]-time[0]

pricekeeping = []
for i in range(n_sims):
    # np.random.seed(0)
    steps = (mu-(sigma**2)/2)*dt + sigma*np.random.normal(0, np.sqrt(dt), timesteps)
    path = S0*np.exp(np.cumsum(steps))
    path[0] = S0
    pricekeeping.append(path)
    ax[1].plot(time[:-1], path)
ax[1].plot(time[:-1], prices[trading_days+1:], color='k', label = 'Actual stock value')
ax[1].set_title("May 2023 - Nov 2023")
ax[1].legend()
ax[1].grid()

ax[0].set_title("December 2022 - May 2023")
ax[0].plot(time, prices[:trading_days+1], color='k', label = 'Actual stock value')
ax[0].legend()
ax[0].grid()
plt.tight_layout()
plt.show()

fig2, ax  = plt.subplots(2, 1)

MC=[]
for j in range(len(pricekeeping)):
    MC.append(pricekeeping[j][-1])
MC = np.array(MC)
mean = np.mean(MC)
std = np.std(MC)
accuracy = std/np.sqrt(n_sims)
ax[0].hist(MC, bins=50)
ax[0].set_xlabel("USD")
ax[0].set_ylabel("Probability density")
ax[0].set_title("Monte Carlo simulation of future stock price")
ax[0].axvline(prices[-1], label='actual value',color='k')
ax[1].hist(np.log(MC), bins=50)
ax[1].axvline(np.log(prices[-1]),label='actual value',color='k')
#ax[1].set_title("Monte Carlo simulation of future stock price")
ax[1].set_ylabel("Probability density")
ax[1].set_xlabel("Natural log of predicted stock price")
ax[0].legend()
ax[1].legend()
plt.show()

top = np.percentile(MC, 99)
bottom = np.percentile(MC,1)
print(top,bottom)
