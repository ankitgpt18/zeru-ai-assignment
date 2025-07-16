import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load scores
df = pd.read_csv('output/wallet_scores.csv')

# Plot histogram
plt.figure(figsize=(10,6))
plt.hist(df['score'], bins=np.arange(0, 1100, 100), edgecolor='black')
plt.title('Wallet Credit Score Distribution')
plt.xlabel('Score')
plt.ylabel('Number of Wallets')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('output/score_distribution.png')
plt.show(block=True)  # Keeps the plot window open

# Count wallets in each range
ranges = [(i, i+100) for i in range(0, 1000, 100)]
counts = []
for low, high in ranges:
    count = df[(df['score'] >= low) & (df['score'] < high)].shape[0]
    counts.append((f"{low}-{high}", count))
# Last bin: 900-1000 inclusive
counts[-1] = ("900-1000", df[(df['score'] >= 900) & (df['score'] <= 1000)].shape[0])

print("\nScore Range | Number of Wallets")
print("-------------------------------")
for r, c in counts:
    print(f"{r:<10} | {c}")

# Print some insights
print("\n--- Insights ---")
print("Low score wallets (0-300):")
print(df[df['score'] < 300].head())
print("\nHigh score wallets (700+):")
print(df[df['score'] >= 700].head())