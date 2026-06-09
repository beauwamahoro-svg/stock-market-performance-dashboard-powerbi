import yfinance as yf

tickers = ["MRVL", "NVDA", "AMD", "MSFT", "SPY"]

data = yf.download(
    tickers,
    start="2020-01-01",
    auto_adjust=True,
    progress=False
)

long_df = (
    data.stack(level=1)
    .reset_index()
    .rename(columns={"level_1": "Ticker"})
)

print(long_df.head())

long_df.to_csv("analysis_of_selected_stocks", index=False)

print("File saved!")