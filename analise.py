import pandas as pd

df = pd.read_csv("vendas.csv")

print(df.describe())

print(df.head())

total = df["total"].sum()
print(f"Total: {total}")

clientes = df.groupby("cliente")["total"].sum().sort_values(ascending=False)
print(clientes)

produtos = df.groupby("produto")["total"].sum().sort_values(ascending=False)
print(produtos)