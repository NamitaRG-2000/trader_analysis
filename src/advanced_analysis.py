# Additional analysis examples:

# Win rate by sentiment
merged['is_profitable'] = merged[pnl_column] > 0
print("\nWin Rate by Sentiment:")
print(merged.groupby('classification')['is_profitable'].mean())

# Leverage analysis
print("\nAverage Leverage by Sentiment:")
print(merged.groupby('classification')['leverage'].mean())

# Long vs Short performance
print("\nPerformance by Trade Side:")
print(merged.groupby(['classification', 'side'])[pnl_column].mean())

# Save advanced results to file
with open('advanced_analysis.txt', 'w') as f:
    f.write("=== ADVANCED ANALYSIS RESULTS ===\n\n")
    
    # Win rates
    win_rates = merged.groupby('classification')['is_profitable'].mean()
    f.write("WIN RATES BY SENTIMENT:\n" + win_rates.to_string() + "\n\n")
    
    # Leverage
    leverage = merged.groupby('classification')['leverage'].mean()
    f.write("AVERAGE LEVERAGE BY SENTIMENT:\n" + leverage.to_string() + "\n\n")
    
    # Long/Short performance
    side_perf = merged.groupby(['classification', 'side'])[pnl_column].mean()
    f.write("PERFORMANCE BY TRADE SIDE:\n" + side_perf.to_string() + "\n")