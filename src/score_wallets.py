import argparse
import json
import pandas as pd
from feature_engineering import extract_wallet_features
from model import score_wallets

def main(input_path, output_path):
    print(f"Reading transactions from {input_path}...")
    with open(input_path, 'r') as f:
        transactions = json.load(f)
    print(f"Extracting features for {len(transactions)} transactions...")
    features_df = extract_wallet_features(transactions)
    print(f"Scoring {len(features_df)} wallets...")
    scores_df = score_wallets(features_df)
    print(f"Saving scores to {output_path}...")
    scores_df.to_csv(output_path, index=False)
    print("Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Score Aave V2 wallets based on transaction history.")
    parser.add_argument('--input', type=str, required=True, help='Path to input JSON file')
    parser.add_argument('--output', type=str, required=True, help='Path to output CSV file')
    args = parser.parse_args()
    main(args.input, args.output) 