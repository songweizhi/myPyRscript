import pandas as pd


def df_take_percentage_by_col(df_in_file, df_out_file):
    df_in = pd.read_csv(df_in_file, sep='\t', header=0, index_col=0)
    df_out = df_in.div(df_in.sum()) * 100
    df_out = df_out.round(3)
    df_out.to_csv(df_out_file, sep='\t')


df_in_file  = '/Users/songweizhi/Desktop/Sponge_r220/11_host_specificity_by_16S/Torsten_NC/S4_OTU_table.txt'
df_out_file = '/Users/songweizhi/Desktop/Sponge_r220/11_host_specificity_by_16S/Torsten_NC/S4_OTU_table_pct.txt'
df_take_percentage_by_col(df_in_file, df_out_file)

