import os
import json
import csv

directory = "results"

file_prefix = "result_"
file_format = ".json"

#N = 2165.0
N = 5049.0

# DATA TABLES:
# 1 - General Stats
#	Overall AUC
#	AUC race group 0
#	AUC race group 1
#	FPR race group 0
#	FPR race group 1
# 	FNR race group 0
#	FNR race group 1
#	Precision Race group 0
#	Precision Race group 1
#	Recall Race group 0
#	Recall Race group 1


# 2 - ROC Table
#	Array of Recall by threshold race group 0
#	Array of Recall by threshold race group 1
#	Array of FPR by threshold race group 0
#	Array of FPR by threshold race group 1

def main():
    # For each result file:
    for filename in os.listdir(directory):

        # assume filename is format "result_<weight as decimal>.json"
        weight = float(filename[0: (len(filename) - len(".json"))])

        # Open as JSON
        with open(directory + '/' + filename, 'r') as file:

            # Load raw data file
            data = json.load(file)

        # Parse out General Stats
        new_stats_row = [
            weight,
            data["auc"],
            data["auc race group 0"],
            data["auc race group 1"],
            data["fpr race group 0"],
            data["fpr race group 1"],
            data["fnr race group 0"],
            data["fnr race group 1"],
            data["precision race group 0"],
            data["precision race group 1"],
            data["recall race group 0"],
            data["recall race group 1"],
        ]

        # Parse out ROC data
        new_roc = [
            [weight],
            data["recall_th race group 0"],
            data["fp_th race group 0"],
            data["recall_th race group 1"],
            data["fp_th race group 1"],
        ]

        # Turn raw FP count to FPR for each threshold and race group.
        for x in range(len(new_roc[2])):
            new_roc[2][x] /= N
            new_roc[4][x] /= N

        # Write to new row (add column for this round's pos_weight) in csv.
        # One for General Stats table and one for ROC tables.
        with open("metrics.csv", 'a') as metric:
            writer = csv.writer(metric)
            writer.writerow(new_stats_row)

        with open("roc.csv", 'a') as roc_file:
            writer = csv.writer(roc_file)
            writer.writerows(new_roc)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
