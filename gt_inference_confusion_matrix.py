import pandas as pd
import numpy as np
import math
import os
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--gt_folder_path") # GT folder path
    parser.add_argument("--pred_folder_path") # Inference folder path
    parser.add_argument("--output_folder_path") # Folder path to output misclassification table
    args = parser.parse_args()

    gt_folder_path = args.gt_folder_path
    pred_folder_path = args.pred_folder_path
    output_folder_path = args.output_folder_path

    gt_files = os.listdir(gt_folder_path)

    for gt_file in gt_files:
        gt_file_path = os.path.join(gt_folder_path, gt_file)
        pred_file_path = os.path.join(pred_folder_path, gt_file)
        
        if os.path.isfile(pred_file_path):  
            gt_df = pd.read_csv(gt_file_path)
            del gt_df['phase']
            del gt_df['Frame_No.']
            pred_df = pd.read_csv(pred_file_path)
            del pred_df['phase']
            del pred_df['Frame_No.']

            columns = gt_df.columns

            result_df = pd.DataFrame(columns=['Tools', 'TP', 'TN', 'FP', 'FN', 'Accuracy', 'Error Rate', 'Recall',
                                            'Specificity', 'Precision', 'F1 Score'])

            for column in columns:
                gt_values = gt_df[column].values
                pred_values = pred_df[column].values

                tp = 0
                tn = 0
                fp = 0
                fn = 0

                for gt_value, pred_value in zip(gt_values, pred_values):
                    if gt_value == 1 and pred_value == 1:
                        tp += 1
                    elif gt_value == 0 and pred_value == 0:
                        tn += 1
                    elif gt_value == 0 and pred_value == 1:
                        fp += 1
                    elif gt_value == 1 and pred_value == 0:
                        fn += 1

                try:
                    accuracy = math.trunc((tp + tn) / (tp + tn + fp + fn) * 100) / 100 if (tp + tn + fp + fn) != 0 else 0.0
                    error_rate = math.trunc((fp + fn) / (tp + tn + fp + fn) * 100) / 100 if (tp + tn + fp + fn) != 0 else 0.0
                    sensitivity = math.trunc(tp / (tp + fn) * 100) / 100 if (tp + fn) != 0 else 0.0
                    specificity = math.trunc(tn / (tn + fp) * 100) / 100 if (tn + fp) != 0 else 0.0
                    precision = math.trunc(tp / (tp + fp) * 100) / 100 if (tp + fp) != 0 else 0.0
                    f1_score = math.trunc((2 * precision * sensitivity) / (precision + sensitivity) * 100) / 100 if (precision + sensitivity) != 0 else 0.0
                except ZeroDivisionError:
                    accuracy = 0.0
                    error_rate = 0.0
                    sensitivity = 0.0
                    specificity = 0.0
                    precision = 0.0
                    f1_score = 0.0

                result_df = result_df.append({'Tools': column,
                                            'TP': tp,
                                            'TN': tn,
                                            'FP': fp,
                                            'FN': fn,
                                            'Accuracy': accuracy,
                                            'Error Rate': error_rate,
                                            'Recall': sensitivity,
                                            'Specificity': specificity,
                                            'Precision': precision,
                                            'F1 Score': f1_score}, ignore_index=True)

            output_file_name = gt_file[:-4] + '_confusion_matrix.csv'
            output_file_path = os.path.join(output_folder_path, output_file_name)
            result_df.to_csv(output_file_path, index=False)

if __name__ == '__main__':
    main()