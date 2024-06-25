import pandas as pd

NGO_URL = "https://www.ngobureau.go.ug/ngos-search.php"

df = pd.read_html(NGO_URL)
print(df.head(15))
