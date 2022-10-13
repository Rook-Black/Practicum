# Description of the problem

Customers leave Beta-Bank every month. Little by little, but noticeable. The management of the bank decided that it was better to keep old customers than to attract new ones.
It is necessary to train the model to predict whether the client will leave the bank or not.

# Description of data

**Features**

* RowNumber — Row index in data
* CustomerId — Unique client id
* Surname — Last name
* CreditScore — Credit rating
* Geography — Country of residence
* Gender
* Age
* Tenure — How many years a person has been a bank client
* Balance — Account balance
* NumOfProducts — Numbers of bank product used by the client
* HasCrCard — Availability of a credit card
* IsActiveMember — Client activity
* EstimatedSalary

**Target**

* Exited — The fact thet the client left

# Used library

1. pandas 
2. sklearn
3. matplotlib
4. warnings

# What was done

- The data was analyzed, omissions and duplicates were found.
- Necessary columns for training are selected.
- Categorical values have been coded.
- Numerical values are given to one scale.
- Several models were trained and the best one was selected.

# Result

As a result, we got a `random forest` model that could predict the client's departure with 85% probability.
