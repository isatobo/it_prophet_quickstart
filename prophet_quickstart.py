# Python
import pandas as pd
from fbprophet import Prophet

df = pd.read_csv('example_wp_log_peyton_manning.csv')
df.head()

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast)

fig2 = m.plot_components(forecast)

fig1.savefig("Graphs/fig1.png")
fig2.savefig("Graphs/fig2.png")
