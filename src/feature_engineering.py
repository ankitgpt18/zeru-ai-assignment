import pandas as pd
import numpy as np
from collections import defaultdict

def extract_wallet_features(transactions):
    """
    Given a list of transaction dicts, return a DataFrame of wallet-level features.
    """
    # Group transactions by wallet
    wallet_tx = defaultdict(list)
    for tx in transactions:
        wallet = tx.get('userWallet', None)
        if wallet:
            wallet_tx[wallet].append(tx)

    features = []
    for wallet, txs in wallet_tx.items():
        actions = [t.get('action', None) for t in txs]
        action_counts = pd.Series(actions).value_counts().to_dict()
        # Amounts by action
        amounts_by_action = defaultdict(list)
        for t in txs:
            action = t.get('action', None)
            amount = None
            if 'actionData' in t and isinstance(t['actionData'], dict):
                amount = t['actionData'].get('amount', None)
            if amount is not None:
                try:
                    amounts_by_action[action].append(float(amount))
                except Exception:
                    pass
        # Time features
        timestamps = [pd.to_datetime(t.get('timestamp', None), unit='s', errors='coerce') for t in txs if t.get('timestamp', None)]
        timestamps = [t for t in timestamps if pd.notnull(t)]
        if timestamps:
            activity_span = (max(timestamps) - min(timestamps)).total_seconds() / (60*60*24)  # days
            tx_frequency = len(timestamps) / (activity_span + 1e-6)
        else:
            activity_span = 0
            tx_frequency = 0
        # Asset diversity
        assets = set()
        for t in txs:
            if 'actionData' in t and isinstance(t['actionData'], dict):
                asset = t['actionData'].get('assetSymbol', None)
                if asset:
                    assets.add(asset)
        # Liquidation events
        liquidation_count = action_counts.get('liquidationcall', 0)
        # Repay/Borrow ratio
        repay = sum(amounts_by_action.get('repay', []))
        borrow = sum(amounts_by_action.get('borrow', []))
        repay_borrow_ratio = repay / borrow if borrow > 0 else 0
        # Redeem/Deposit ratio
        redeem = sum(amounts_by_action.get('redeemunderlying', []))
        deposit = sum(amounts_by_action.get('deposit', []))
        redeem_deposit_ratio = redeem / deposit if deposit > 0 else 0
        # Feature dict
        feat = {
            'wallet': wallet,
            'n_tx': len(txs),
            'n_deposit': action_counts.get('deposit', 0),
            'n_borrow': action_counts.get('borrow', 0),
            'n_repay': action_counts.get('repay', 0),
            'n_redeem': action_counts.get('redeemunderlying', 0),
            'n_liquidation': liquidation_count,
            'total_deposit': deposit,
            'total_borrow': borrow,
            'total_repay': repay,
            'total_redeem': redeem,
            'activity_span_days': activity_span,
            'tx_frequency_per_day': tx_frequency,
            'asset_diversity': len(assets),
            'repay_borrow_ratio': repay_borrow_ratio,
            'redeem_deposit_ratio': redeem_deposit_ratio,
        }
        features.append(feat)
    return pd.DataFrame(features) 