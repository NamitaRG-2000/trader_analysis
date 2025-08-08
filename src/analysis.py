import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 1. LOAD DATA
print("Loading data...")
fear_greed = pd.read_csv('data/raw/fear_greed.csv')
trades = pd.read_csv('data/raw/trades.csv')

# 2. PREPARE DATA
print("\nPreparing data...")
fear_greed['date'] = pd.to_datetime(fear_greed['timestamp'], unit='s').dt.date
trades['date'] = pd.to_datetime(trades['Timestamp'], unit='ms').dt.date

# 3. FIND THE CORRECT PNL COLUMN
print("\nSearching for PnL column in trades data...")
pnl_columns = [col for col in trades.columns if 'pnl' in col.lower() or 'profit' in col.lower() or 'loss' in col.lower()]

if not pnl_columns:
    print("\nERROR: No PnL-related columns found. Available columns:")
    print(trades.columns.tolist())
    pnl_column = input("\nPlease enter the exact column name for profit/loss: ")
else:
    pnl_column = pnl_columns[0]
    print(f"\nFound PnL column: '{pnl_column}'")

# 4. MERGE DATASETS
print("\nMerging datasets...")
merged = pd.merge(trades, fear_greed, on='date', how='left')

# 5. ANALYSIS
print("\n=== ANALYSIS RESULTS ===")
print(f"\nAverage PnL by Market Sentiment (using '{pnl_column}'):")
print(merged.groupby('classification')[pnl_column].mean())

print("\nTrade Count by Sentiment:")
print(merged['classification'].value_counts())

# 6. VISUALIZATIONS
print("\nCreating visualizations...")
plt.figure(figsize=(12, 6))

# Plot 1: Average PnL by Sentiment
plt.subplot(1, 2, 1)
merged.groupby('classification')[pnl_column].mean().plot(
    kind='bar', color=['red', 'orange', 'green', 'blue'])
plt.title(f'Average Profit/Loss by Market Sentiment\n(using {pnl_column})')
plt.ylabel('Average PnL (USD)')
plt.xticks(rotation=45)

# Plot 2: Trade Volume by Sentiment
plt.subplot(1, 2, 2)
merged['classification'].value_counts().plot(
    kind='pie', autopct='%1.1f%%', colors=['red', 'orange', 'green', 'blue'])
plt.title('Trade Distribution by Market Sentiment')

plt.tight_layout()
plt.savefig('analysis_results.png')
print("\n✔ Analysis complete! Results saved to 'analysis_results.png'")
plt.show()

# 7. SAVE PROCESSED DATA
merged.to_csv('processed_trades_with_sentiment.csv', index=False)
print("Processed data saved to 'processed_trades_with_sentiment.csv'")