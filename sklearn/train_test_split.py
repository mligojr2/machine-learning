'''
Help Site Link : https://www.bitdegree.org/learn/train-test-split
train_test_split is a function in Sklearn model selection for splitting data arrays into two subsets: for training data and for testing data. With this function, you don't need to divide the dataset manually.

By default, Sklearn train_test_split will make random partitions for the two subsets. However, you can also specify a random state for the operation.

Parameters:
    train_test_split(X, y, train_size=0.*,test_size=0.*, random_state=*)

    1. X, y. The first parameter is the dataset you're selecting to use.
    2. train_size. This parameter sets the size of the training dataset. There are three options: None, which is the default, Int, which requires the exact number of samples, and float, which ranges from 0.1 to 1.0.
    3. test_size. This parameter specifies the size of the testing dataset. The default state suits the training size. It will be set to 0.25 if the training size is set to default.
    4. random_state. The default mode performs a random split using np.random. Alternatively, you can add an integer using an exact number.

'''

# Use of train_test_split:
#1. Fisrt you need to have a dataset to split. You can stay by making list of number using range() like this:

X = list(range(15))
# print(x)   

# Then, We add more code to make another list of square values of numbers in x:
y = [x*x for x in X]
# print(y)

# =============================================================================
# Now, let's apply the train_test_split function. Here, we set the train size to 65% of the entire dataset. Remember to write 0.65.
# =============================================================================

import sklearn.model_selection as model_selection
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y, train_size=0.65, test_size=0.35, random_state=101)
print ("X_train: ", X_train)
print ("y_train: ", y_train)
print("X_test: ", X_test)
print ("y_test: ", y_test)

# =============================================================================
# You can set only the test_size as the train_size will adjust accordingly. You can also set the random_state to 0 as shown below:
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
# =============================================================================
