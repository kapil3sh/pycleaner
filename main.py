import import_utils as iu
import eda_utils as eu

path = 'train.csv'

df = iu.file_import(path)

x = eu.get_info(df)

