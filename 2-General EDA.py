#: 1 General EDA
import pandas as pd
data_african = pd.read_csv("african_countries_dataset.csv")
data_african.head()
data_african.dtypes
data_african.shape  # 342081 rows, 41 columns

# Missing values
data_african.isnull().sum()  # DefaultChoice, NonDefaultChoice, DefaultChoiceIsOmission, Template, DescriptionShown
                             # Lefthand missing around 30000 cells, UserID missing 23 cells

#Copying dataset before I start manipulating the dataset
c_data_african = data_african
