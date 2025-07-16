# Analysis of Wallet Credit Scores

## Score Distribution

Below is the distribution of wallet credit scores (0-1000) after running the scoring model:

![Score Distribution Histogram](#)

| Score Range | Number of Wallets |
|-------------|-------------------|
| 0-100       |                   |
| 100-200     |                   |
| 200-300     |                   |
| 300-400     |                   |
| 400-500     |                   |
| 500-600     |                   |
| 600-700     |                   |
| 700-800     |                   |
| 800-900     |                   |
| 900-1000    |                   |

## Behavioral Insights

### Low Score Wallets (0-300)
- Typically exhibit risky or bot-like behavior.
- High liquidation events, low or no repayments, short activity span.
- Often borrow without repaying or redeeming.

### High Score Wallets (700-1000)
- Consistent, responsible usage: regular deposits, repayments, and diverse asset interactions.
- Long activity span, high transaction frequency, low or no liquidations.
- Repay/borrow and redeem/deposit ratios close to or above 1.

## Notable Patterns
- [Add any interesting findings or outliers here.]

## Recommendations
- Use these scores to identify reliable users, potential bots, or risky actors.
- The scoring model can be further refined with more data or domain knowledge. 