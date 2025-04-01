import numpy as np  # linear algebra
import pandas as pd # data processing / CVS file I/O
import matplotlib.pyplot as plt # for scatter plot 
from matplotlib.colors import ListedColormap # for color map 

number_of_bachorette_parties  = 21

# import data 
file_path = '/Users/fionanicdao/loyola/dataMining/Sleep_project/Sleep_Efficiency.csv'
df_se =pd.read_csv(file_path)
column = df_se.columns
# print(column)

#import data 
file_path1 = '/Users/fionanicdao/loyola/dataMining/Sleep_project/Sleep_health_and_lifestyle_dataset.csv'
df_sh = pd.read_csv(file_path1)
column1 = df_sh.columns
# print(column1)

#import data 
file_path2 = '/Users/fionanicdao/loyola/dataMining/Sleep_project/Sleep_cycle_productivity.csv'
df_sc = pd.read_csv(file_path2)
columns2 = df_sc.columns
# print(columns2)

#import data 
file_path3 = '/Users/fionanicdao/loyola/dataMining/Sleep_project/Sleep_deprivation_dataset_detailed.csv'
df_sd = pd.read_csv(file_path3)
column3 = df_sd.columns
# print(column3)

index_drop_under18 = df_se[df_se['Age'] < 18 ].index
df_se = df_se.drop(index_drop_under18)
# print(df_se.head(20))
# print(index_drop_under18)
# for index in index_drop_under18:
#     print(df_se.iloc[index])
# data = {'Age': df_sc['Age']}
# df_age = pd.DataFrame(data)
# data_sh = {'Age':df_sh['Age']}
# print(data_sh)
# data = df_se['Age'] + df_sh['Age']# + df_sc['Age'] + df_sd['Age']
# data_age = {'Age' : data}
# df_age = pd.DataFrame(data_age)
# # print(df_age)
# print(len(df_se['Age']))
# print(len(df_sh['Age']))
# print(len(df_sc['Age']))
# print(len(df_sd['Age']))

age = df_se['Age'].tolist()
age1 = df_sh['Age'].tolist()
age2 = df_sc['Age'].tolist()
age3 = df_sd['Age'].tolist()
data = age + age1 +age2 + age3
# print(len(data))
# data = np.array(data)

group = []
# # print(data[65])


# df_age['Age Group'] = group
# print(len(group))
# print(type(data))
# print(len(data))
data = {'Age':data}
df_age = pd.DataFrame(data)
# print(df_age.loc[:,'Age'])
for index,row in df_age.iterrows() : 
    # print(age)
    if row['Age'] < 25:
        print(str(row['Age']) + 'young adults')
        group[index] = 'young adults'
    elif row['Age'] >= 25 and row['Age'] < 36  :
        print(str(row['Age']) + 'adults')
        group[index] = 'adults' 
    else:
        # print('older')
        group[index] = 'mid-age adults'
        
# df_age.to_csv('dfAGE.csv', index=False)
# df_age['Age Group'] = group
# gen1 = df_se['Gender'].tolist()
# gen2 = df_sh['Gender'].tolist()
# gen3 = df_sc['Gender'].tolist()
# gen4 = df_sd['Gender'].tolist()
# gender = gen1 + gen2 + gen3 + gen4
# df_age['Gender'] = gender

# print(df_age.columns)
# print(df_age) 
# # df_age = df_age._append(data_sh,ignore_index=True)
# my_bins = [18,26,34,44]

# n, _, patches = plt.hist(df_age['Age'], bins=my_bins,edgecolor = 'white',color='skyblue')
# plt.bar_label(patches)
# plt.xlabel('Age')
# plt.ylabel('count')
# plt.title('Count the Age distribution of all Datasets')
# plt.show()