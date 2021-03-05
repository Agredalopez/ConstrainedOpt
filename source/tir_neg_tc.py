import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

tir_tc = pd.read_csv('data/base_tc.csv')

tir_tc.columns.tolist()

tir_tc["FLG_NEG"] = np.where(tir_tc['TIR']<0,1,0)

def plot_distr(df, var, target):
  title = "Análisis de distribución de la variable {v}".format(v=var)
  plt.figure(figsize=(15,8))
  ax = sns.kdeplot(df[var][df[target] == 1], color="lightcoral", shade=True)
  sns.kdeplot(df[var][df[target] == 0], color="darkturquoise", shade=True)
  plt.legend(['Tir Negativa', 'Tir Positiva'])
  plt.title(title)
  ax.set(xlabel=var)
  plt.xlim(df[var].quantile(0.005),df[var].quantile(0.995))
  return  plt.show()

plot_distr(tir_tc[tir_tc['CREDIT_CARD']=='MASIVA'],"SCORE","FLG_NEG")
plot_distr(tir_tc[tir_tc['CREDIT_CARD']=='MASIVA'],"INGRESO","FLG_NEG")
plot_distr(tir_tc[tir_tc['CREDIT_CARD']=='MASIVA'],"LINEA","FLG_NEG")
plot_distr(tir_tc[tir_tc['CREDIT_CARD']=='MASIVA'],"SUELDO_AHORRO_12M","FLG_NEG")
plot_distr(tir_tc[tir_tc['CREDIT_CARD']=='MASIVA'],"DEUDA_NOBCP_TC_CEF_0","FLG_NEG")
plot_distr(tir_tc[tir_tc['CREDIT_CARD']=='MASIVA'],"DEUDA_SBS_TC_CEF_0","FLG_NEG")
plot_distr(tir_tc[tir_tc['CREDIT_CARD']=='MASIVA'],"EDAD","FLG_NEG")
plot_distr(tir_tc[tir_tc['CREDIT_CARD']=='MASIVA'],"RCC_BAL_ALL_TRADE_LINES","FLG_NEG")

variables = ['SCORE','INGRESO','LINEA','SUELDO_AHORRO_12M','DEUDA_NOBCP_TC_CEF_0','DEUDA_SBS_TC_CEF_0','EDAD','ANT_LABORAL','MTHS_PASIVOS_12M_1000','MTHS_PAS_ACT_24_1000','MTHS_PSASV_24M_100','RCC_NBR_ALL_TRADE_LINES','RCC_BAL_ALL_TRADE_LINES']
tir_tc.groupby(['CREDIT_CARD','FLG_NEG'])[variables].describe().T.reset_index()

def box_plot(df=tir_tc,var="SCORE", x='CREDIT_CARD',cat = 'FLG_NEG'):
    p = df[var].quantile(1)
    df_c = df[df[var]<=p]
    my_order = ['MASIVA','CLASICA','ORO','PLATINUM','SIGNATURE','INFINITE']
    sns.set_theme(style="ticks", palette="pastel")
    sns.boxplot(x=x, y=var,
                hue=cat, palette=["darkturquoise", "lightcoral"], order=my_order,
                data=df_c)
    sns.despine(offset=14, trim=True)
    plt.suptitle('Gráfico de Perfilamiento de cada Plástico por {var}'.format(var=var), fontsize=20)
    plt.show()

box_plot(var='MTHS_PAS_ACT_24_1000')

tir_tc.FLG_NEG.value_counts()/len(tir_tc)
tir_tc[tir_tc.FLG_NEG==1]['CREDIT_CARD'].value_counts()
tir_tc['CREDIT_CARD'].value_counts()