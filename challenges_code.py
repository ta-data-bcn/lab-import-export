import pandas as pd

nasa = pd.read_json('data/nasa.json')
print(nasa.head())
print(nasa['fall'].value_counts())
nasa.to_json('data/nasa-output.json', orient='records')


cols = ['time', 'rad_flow', 'fpv_close', 'fpv_open', 'high', 'bypass', 'bpv_close', 'bpv_open', 'class']
tst_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/shuttle/shuttle.tst'
shuttle = pd.read_csv(tst_url, names=cols, sep=' ')
shuttle.to_csv('data/shuttle.csv', sep=',', header=False)

astronaut = pd.read_excel('data/astronauts.xls', engine='xlrd')
print(astronaut.head())
print(astronaut.columns)
print(astronaut['Undergraduate Major'].value_counts())
astronaut.to_csv('data/astronaut.csv', sep='\t')