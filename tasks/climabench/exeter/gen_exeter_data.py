import pandas as pd
import ast
import numpy as np
import os 
from pathlib import Path
import argparse

# path="/home/rjalota/climabench_data/CARDS2_multisource_multilabel_data.csv"
# path = "/home/rjalota/climabench_data/data/training"

def get_claim_label(row):
    claim_labels = set()
    label_list = ast.literal_eval(row)
    for label in label_list:
        if not label.startswith('0'):
            claim_labels.add(label[0])
    print(claim_labels)
    if len(claim_labels) == 0 or len(claim_labels) > 1:
        return None
    return ','.join(list(claim_labels))

    # print(label)

def get_claim(row):
    if '0_0' not in row:
        # print(int(row[0])-1)
        return int(row[0])-1
    return None

def parse_args():
    parser = argparse.ArgumentParser(description='run binary classifer')
    parser.add_argument("--path", default="/home/rjalota/climabench_data/data/training", help="path to exeter training dir. containing train, test, validation splits") 
    parser.add_argument("--out", default="/home/rjalota/climabench_data", help="output directory path")  
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    for filename in os.listdir(args.path):
        print(filename)
        f = os.path.join(args.path, filename)
        df = pd.read_csv(f, header=0)
        # print(df.head())
        df['bin_label'] = df.apply(lambda row: 0 if '0_0' in row.claim else 1, axis = 1)
        df['claim_labels'] = df['claim'].map(get_claim) #.map(get_claim_label)
        print(df.bin_label.value_counts()) 
        print(df.claim_labels.value_counts()) 
        claim_df = df[['text', 'claim_labels']]
        binary_df = df[['text', 'bin_label']]
        print(len(claim_df))
        claim_df = claim_df.dropna()
        print(len(claim_df))
        claim_df['claim_labels'] = claim_df['claim_labels'].astype(int)
        print(claim_df.claim_labels.value_counts())
        Path(f"{args.out}/multi/").mkdir(parents=True, exist_ok=True)
        Path(f"{args.out}/binary/").mkdir(parents=True, exist_ok=True)
        claim_df.to_csv(f"{args.out}/multi/{filename}", index=False)
        binary_df.to_csv(f"{args.out}/binary/{filename}", index=False)
   # ---- #
    # claim_df = claim_df.sample(frac=0.3,random_state=200)
    # dev=claim_df.sample(frac=0.1,random_state=200)
    # test=claim_df.drop(dev.index)
    # dev.to_csv("/home/rjalota/climabench_data/multiclass_claims/dev.csv", index=False)
    # test.to_csv("/home/rjalota/climabench_data/multiclass_claims/test.csv", index=False)
    # print(f"--multiclass_claims--")
    # print(f"len(test): {len(test)}")
    # print(f"len(dev): {len(dev)}")
    # print("dev")
    # print(dev.claim_labels.value_counts()) 
    # print("test")
    # print(test.claim_labels.value_counts()) 
    # # ---- #
    # binary_df = binary_df.sample(frac=0.3,random_state=200)
    # dev=binary_df.sample(frac=0.1,random_state=200)
    # test=binary_df.drop(dev.index)
    # dev.to_csv("/home/rjalota/climabench_data/binary_claims/dev.csv", index=False)
    # test.to_csv("/home/rjalota/climabench_data/binary_claims/test.csv", index=False)
    # print(f"--binary_claims--")
    # print(f"len(test): {len(test)}")
    # print(f"len(dev): {len(dev)}")
    # print("dev")
    # print(dev.bin_label.value_counts()) 
    # print("test")
    # print(test.bin_label.value_counts()) 
    # 1041 - size of multilabel dataset
