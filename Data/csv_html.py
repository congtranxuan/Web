import pandas as pd
# Load data..
data = "cities.csv"
cities = pd.read_csv(data)
cities.rename(columns={'Unnamed: 0':'Citi_ID'},inplace=True)
cities.set_index("Citi_ID")
cities.to_html('data_pandas.html')