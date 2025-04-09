from mymodule import generate_full_name
import mymodule

print(mymodule.generate_full_name('Asabneh', 'Yetayeh'))

import os
os.chdir('..')
print(os.getcwd())
print(os.listdir())
print(os.name)
import platform
print(platform.system())

import sys
print (sys.path)
print(sys.version)
print(sys.executable)
print(sys.platform)
sys.exit()
sys.path()
print(os.getcwd())

data = [0,0,1, 2, 2,2, 3, 4, 5, 5, 5, 6]
import statistics as stats
stats.mean(data)
stats.median(data)
stats.mode(data)
stats.stdev(data)
stats.variance(data)
min(data)
max(data)
stats.multimode(data)
stats.quantiles(data, n=4)
stats.NormalDist(mu=12, sigma=3).zscore(1.96)
stats.NormalDist(mu=12, sigma=3).inv_cdf(0.975)
stats.NormalDist(mu=12, sigma=3).pdf(1.96)
stats.NormalDist(mu=12, sigma=3).cdf(1.96)
stats.NormalDist(mu=12, sigma=3).samples(10)
dist = stats.NormalDist(mu=10, sigma=2)
print(dist.inv_cdf(0.975))  # Output: ~13.29
stats.NormalDist(mu=10, sigma=2).zscore(13.9199279)
coll=stats.NormalDist(mu=10, sigma=2).samples(20)
print(coll)

import math as m
m.factorial(5)
m.isnan(5)
m.log2(9)
m.sqrt(16)
16**0.5

import datetime as dt
print(dt.date.fromisoformat('2023-10-01'))

today = dt.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
dt.date.today().weekday

from datetime import date as d
d.today().weekday()
d.today().year
d.today().month

import random as r
r.random()
r.randint(1, 100)
r.randrange(1, 100)
r.choice(['a', 'b', 'c'])
r.sample(['a', 'b', 'c'], 2)
r.shuffle(['a', 'b', 'c'])
r.seed(1)
r.random()
r.randint(1, 100)
r.seed(42)

import string
string.ascii_lowercase
string.ascii_uppercase
string.ascii_letters
string.digits
string.punctuation
string.printable




characters = string.ascii_letters + string.digits + string.punctuation
password= ''.join(r.choice(characters,k=6))
print(password)