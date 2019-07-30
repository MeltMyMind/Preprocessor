# PreProHelper
A nice handy tool to quickly preprocess datasets.

<img src = "https://imgur.com/tla9Hk3.png" />

## Motivation 

In my young datascience carreer, I have spent quite some time with preprocessing datasets. I noticed that I was doing the same tedious tasks over and over again, which became boring and time consuming. Therefore I created a nice little tool to help anybody with preprocessing csv files for machine learning. I'm still working on it as I want to integrate many more functionalties, but it can be used already nonetheless. 


## Main functionalities 

**Numerical to Categorical**
Changes the numbers in a column to strings.

**Categorical to Numerical**
Labelencodes the strings in a column to numbers. Ie. ("Cat", "Dog", "Mouse", "Cat") becomes (0, 1, 2, 0).

**Categorical to Dummy**
Creates a single column out of the 

**Dummy to Categorical**
One-hot encodes all unique values in a column and creates a seprate column for each value. 

**Dummy to Boolean**
Changes the 1 and 0 in a column to True and False. 

**Boolean to Dummy**
Changes the True and False in a column to 1 and 0. 



## Setup:

**Running the file:**
The setup is fairly simple, since it is only one python file "PreproHelper.py" which one needs to run. After running the file, a new window will open, which the user can then use to preprocess his/her dataset. 

The file can either be run directly in any IDE such as Pycharm or Visualstudio or it can be run through the terminal/command line by cd'ing to the corresponding directory and then running the file (ex. python PreproHelper.py). 

**Installing packages/dependencies:**
The file needs a few packages in order to run. They are all listed in the *requirements.txt* file.
To install all the necessary dependencies, use pip in the terminal/command line  by first cd'ing to the directory where you put *requirements.txt* and the running: 

pip install -r requirements.txt

## Description:

**Import dataset:**

Type in the name of the dataset in the directory you want to import (ex: mydataset.csv). If you want to change the directory, please click on the button Change Dir.  

<img src="https://imgur.com/6uJdq2t.png"/>

Note: Currently only csv's are supported. Other file types will be implemented shortly. 


**Overview:**


