import pandas as pd
import matplotlib.pyplot as plot


df = pd.read_csv(r'C:\Users\usuario\Desktop\Henry DS\M3\Clase 03\sad.csv')



plot.hist(x=df, bins=70, rwidth=1)
plot.show()

