# 🏦 Aave V2 Wallet Credit Scoring

![repo public](https://img.shields.io/badge/repo-public-brightgreen)

---

## 📚 About This Project

This repository is my submission for the Zeru AI Engineer Internship assignment round.

It demonstrates my ability to design, implement, and analyze a robust, transparent credit scoring system for DeFi wallets using real Aave V2 transaction data. The solution is fully original, interpretable, and designed for extensibility.

---

## 🧠 Methodology & Approach

- **Feature Engineering:**  
  Extract wallet-level features from raw transaction data, including:
  - Action counts (deposits, borrows, repays, etc.)
  - Total and average amounts per action
  - Activity span and transaction frequency
  - Asset diversity
  - Behavioral ratios (repay/borrow, redeem/deposit)
  - Liquidation events

- **Scoring Model:**  
  A clear, rule-based model rewards responsible DeFi behavior (repaying, diverse assets, long activity) and penalizes risky or bot-like actions (liquidations, excessive borrowing, inactivity).  
  Scores are mapped to the 0-1000 range for easy interpretation.

- **Analysis:**  
  Score distributions and wallet behavior insights are provided in `analysis.md`, including a histogram and a breakdown of wallet behaviors by score range.

---

## 🗂️ Project Structure

```
.
├── data/
│   └── user-wallet-transactions.json
├── src/
│   ├── feature_engineering.py
│   ├── model.py
│   ├── score_wallets.py
│   └── analyze_scores.py
├── output/
│   ├── wallet_scores.csv
│   └── score_distribution.png
├── analysis.md
├── readme.md
└── requirements.txt
```

---

## ⚡ How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Score the wallets:**
   ```bash
   python src/score_wallets.py --input data/user-wallet-transactions.json --output output/wallet_scores.csv
   ```

3. **Analyze the results:**
   ```bash
   python src/analyze_scores.py
   ```
   - This will generate a score distribution plot and print insights for your report.

---

## 📊 Analysis

- See `analysis.md` for:
  - Score distribution table and histogram
  - Behavioral insights for low, mid, and high score wallets
  - Notable patterns and recommendations

---

## 🧩 Extensibility

- The scoring logic is modular and can be easily updated in `src/model.py`.
- Additional features can be engineered in `src/feature_engineering.py`.

---

## 🔍 Transparency

- All scoring rules are documented in code and this README.
- No black-box models: every score is explainable and reproducible.

---

*For any questions or suggestions, feel free to open an issue or contact me via GitHub.* 