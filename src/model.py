import numpy as np
import pandas as pd

def score_wallets(features_df):
    """
    Assign a credit score (0-1000) to each wallet based on engineered features.
    Returns a DataFrame with wallet and score columns.
    """
    df = features_df.copy()
    # Start with a base score
    score = np.full(len(df), 500.0)
    # Reward responsible actions
    score += 0.1 * df['n_deposit']
    score += 0.2 * df['n_repay']
    score += 0.1 * df['asset_diversity']
    score += 0.05 * df['activity_span_days']
    score += 0.1 * df['tx_frequency_per_day']
    score += 0.2 * df['repay_borrow_ratio'] * 10
    score += 0.1 * df['redeem_deposit_ratio'] * 10
    # Penalize risky actions
    score -= 0.3 * df['n_liquidation']
    score -= 0.1 * (df['n_borrow'] - df['n_repay']).clip(lower=0)
    # Penalize very low activity
    score[df['n_tx'] < 3] -= 100
    # Clamp score to [0, 1000]
    score = np.clip(score, 0, 1000)
    return pd.DataFrame({'wallet': df['wallet'], 'score': score.round(2)}) 