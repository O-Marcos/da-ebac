import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):

  gasolina = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="pastel")
  gasolina.set(title='Preço médio da gasolina', xlabel='Dia', ylabel='Venda');

  plt.savefig('gasolina.png')