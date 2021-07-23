from datetime import datetime
import pandas as pd
import csv

transactions = pd.read_csv(r'data/transactions.csv', index_col=0)
transactions = transactions.fillna(0)
contracts = pd.read_csv(r'data/contracts.csv', index_col=0)
contracts = contracts[contracts.is_active != 0]

profit_df = pd.merge(left=contracts, right=transactions, left_on="client_id", right_on="client_id")

profit_df["calc_amount"] = profit_df["total_amount"] - ((profit_df["total_amount"] * profit_df["discount_percentage"]) / 100)
profit_df["profit"] = ((profit_df["calc_amount"] * profit_df["percentage"]) / 100)
print(profit_df)

profit_total = profit_df["profit"].sum()
print('Lucro Total da Acquirer LTDA: ' + str(profit_total))

persist_data = datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), profit_total
with open('data/output.csv', 'w', encoding='UTF8') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(persist_data)