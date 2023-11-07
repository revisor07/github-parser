import datetime
import numpy
import os

s_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Talent Games', 
  'time_vs_commits', 'MSFT_stocks.txt')
c_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Talent Games', 
  'time_vs_commits', 'MSFT_commits.txt')

#take datetime, separate by "-" into year, month, day
sample_size = 364
stock_list = []
commit_list = []
stocks_raw = []
commits_raw = []
with open(s_path) as s:
  stocks_raw = s.readlines()
with open(c_path) as c:
  commits_raw = c.readlines()

prev_stock = float(stocks_raw[0].split("\t")[1])
i = 1;
#stocks
for i in range (sample_size):
  #out of bounds
  if i >= len(stocks_raw):
    stock_list.insert(i, 0)
    continue
  line = stocks_raw[i].split("\t")
  date_string = line[0]
  stock = float(line[1])
  dt = datetime.datetime.strptime(date_string,"%Y-%m-%d")
  dt0 = datetime.datetime(dt.year, 2, 1)
  day = (dt - dt0).days
  if i == day:
    stock_list.insert(i, stock-prev_stock)
    prev_stock = stock
  else:
    stock_list.insert(i, 0)
    
#commits
for i in range (sample_size):
  #out of bounds
  if i >= len(commits_raw):
    commit_list.insert(i, 0)
    continue
  line = commits_raw[i].split("\t")
  date_string = line[0]
  commits = float(line[1])
  dt = datetime.datetime.strptime(date_string,"%Y-%m-%d")
  dt0 = datetime.datetime(dt.year, 2, 1)
  day = (dt - dt0).days
  if i == day:
    commit_list.insert(i, commits)
  else:
    commit_list.insert(i, 0)

#print stock_list[1:]
#print commit_list[1:]
print numpy.corrcoef(stock_list[1:],commit_list[1:])
