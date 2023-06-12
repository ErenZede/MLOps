import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

housing = pd.read_csv("housing.csv")


# print(housing.info())

# print(housing["ocean_proximity"].value_counts())

#housing.hist(bins=50, figsize=(12,8))
# plt.show()

shuffled_indexes = np.random.permutation(len(housing))

test_set_count = int(len(housing) * 0.25)

train_set, test_set = housing.iloc[shuffled_indexes[test_set_count:]
                                   ], housing.iloc[shuffled_indexes[:test_set_count]]


print(len(train_set))
print(len(test_set))
