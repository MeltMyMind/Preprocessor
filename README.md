# PreProHelper
A nice handy tool to quickly preprocess datasets.

<img src = "https://imgur.com/tla9Hk3.png" />

## Motivation 

In my young data science carreer, I have spent quite some time with preprocessing datasets. I noticed that I was doing the same tedious tasks over and over again, which became boring and time consuming. Therefore I created a nice little tool to help anybody with preprocessing csv files for machine learning. I'm still working on it as I want to integrate many more functionalties, but it can be used already nonetheless. 


## Main functionalities

To illustrate the basic funcionalities of the PreProHelper, the syntax *Columnname: (Columnentry, Columnentry, Columnentry)* is used. So for example *Animals: ("Dog", "Cat", "Mouse", "Bird")* would indicate a column with the Name *Animals* and the entries *"Dog", "Cat", "Mouse" and "Bird"*.

Also, one might notice that there are arrows pointing either to the right or left hand side below the various textboxes. These just indicate in which direction the column is going to be transformed. So if one selects a column in the *Categorical Columns* textbox and then clicks on the "---->" below, the selected column is transformed into a dummy column. Vice versa, if one clicked on  "<----" the selected column would turn into a numerical column. Therefore, I call these functions *Arrow Functions*.

### Arrow functions

**Numerical to Categorical**:
Changes the numbers in a column to strings.

Example: 
*DayOfTheWeek: (1, 2, 7, 3)* becomes *DayOfTheWeek: ("1", "2", "7", "3")*

**Categorical to Numerical**:
Labelencodes the strings in a column to numbers.

Example: 
*Animals: ("Cat", "Dog", "Mouse", "Cat")* becomes *Animals: (0, 1, 2, 0)*.

**Categorical to Dummy**:
One-hot encodes all unique values in a column and creates a separate column for each value.

Example: 
*Animals: ("Dog", "Mouse", "Cat", "Mouse")* becomes *Dog: (1, 0, 0, 0)* and *Cat: (0, 0, 1, 0)* and *Mouse: (0, 1, 0, 1)*

**Dummy to Categorical**:
Creates a single column out of multiple dummy encoded columns. 

Example: 
*Dog: (1, 0, 0, 0, 0)* and *Cat: (0, 0, 1, 0, 1)* becomes *Animals: ("Dog", "Unknown", "Cat", "Unknown", "Cat")*.

**Dummy to Boolean**:
Changes the 1 and 0 in a column to True and False. 

Example: 
*isAnimal: (1, 0, 1, 0, 1)* becomes *isAnimal: (True, False, True, False, True)*

**Boolean to Dummy**:
Changes the True and False in a column to 1 and 0. 

Example: 
*isAnimal: (True, False, True, False, True)* becomes *isAnimal: (1, 0, 1, 0, 1)*

### Other functions
To execute any of the other function, one always needs to press a button to trigger them. Here is short explanation of all the other functions: 

**Delete Column**:
Deletes a column from the dataset. 

Howto: Select a column from the textbox *All Columns of the dataset* and then click on the *Delete Column* button.

**Binning**:
Changes a numerical column into numerical bins.

Howto: First, select a column from the *Numerical Columns* textbox. Then type in the number of bins you want to create from these numerical columns (entry field below *Binning* button). At last, click on the button *Binning*.

**Rename**:
Renames any column. 

Howto: Select a column from the textbox *All Columns of the dataset*. Then, type n a new name for the column int the textfield below the *Rename* button. Then, click on *Rename* to rename the selected column. 

**Remove NAs**:
Deletes all rows in the dataset that contain any NAs

Howto: Simply click on the button *Remove NAs*.


## Setup

**Running the file:**
The setup is fairly simple, since it is only one python file "PreproHelper.py" which one needs to run. After running the file, a new window will open, which the user can then use to preprocess his/her dataset. 

The file can either be run directly in any IDE such as Pycharm or Visualstudio or it can be run through the terminal/command line by cd'ing to the corresponding directory and then running the file (ex. python PreproHelper.py). 

**Installing packages/dependencies:**
The file needs a few packages in order to run. They are all listed in the *requirements.txt* file.
To install all the necessary dependencies, use pip in the terminal/command line  by first cd'ing to the directory where you put *requirements.txt* and the running: 

pip install -r requirements.txt

## Getting started:

**Import dataset:**

Type in the name of the dataset in the directory you want to import (ex: mydataset.csv). If you want to change the directory, please click on the button Change Dir.  

<img src="https://imgur.com/JV6Np3F.png"/>

Note: Currently only csv's are supported. Other file types will be implemented shortly. 

**Main Overview:**

<img src="https://imgur.com/sn6gC5A.png"/>

The main overview shows the types of columns of the dataset. 

The **first textbox** (from the left) shows all columns in the dataset. 
Here, the user can perform various functions by selecting a column from the textbox and then clicking on either of the following buttons: 

*- Delete Column*

*- Rename*

The other four textboxes show the types of the various columns in the dataset. Namely: Numerical-, Categorical-, Dummy- and Boolean Columns. Under each textbox there are buttons, which transform the selected column/columns of the textbox above accordingly. See *Arrow functions* for a more detailed description. 

**Export newly created dataset:**

<img src= "https://imgur.com/BcT5lXt.png" />

Once you are done with preprocessing your dataset, you can export it. Simply type in the name of your new dataset (ie: newDataset.csv) and click on *Export Dataset*. As a nice feature, you can also standardise chosen numerical columns when exporting. First, click on the radiobutton "Standardise". Then, simply select as many columns as you want to standardise in the *Numerical Columns* textbox. Once you have selected the columns, you can click on the *Export Dataset* button. 

The dataset will be exported in your import directory. 


## Future Work:

Future functions will include: 

- Exporting as numpy array (ie. for using with Keras)
- Being able to import more datatypes
- Displaying information about the dataset and about individual columns
- Automatic preprocessing 
- Create program that people can download. 

## Bugs:

I'm sure yu will still encounter many bugs. Feel free to report them so I can steadily improve the PreProHelper. 
