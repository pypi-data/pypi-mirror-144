<h1>Data_FolderSplit</h1>   
_____________________________________________  

Segregate the data table in a csv file into folders containing sub folders of sliced/ segmented data for a physical representation of a decision tree.


_____________________________________________

<h2>Instructions.</h2>  

To install the package, perform:  

```python
pip install Data_FolderSplit
```
 
How to use the methods:  

<h3>1. To create the folder structure:  </h3>

```python
#Importing Library.
import Data_FolderSplit as DFS

# filepath -> File path for the csv.
# max_uniques -> Max uniques allowed.
# output_folderpath -> Folder within which sub folders will be formed.

#For example:
filepath = r'D:\Everything\is\BS\Datasheet1.csv'
max_uniques = 4
output_folderpath = r'D:\ChesterBennington\is\a\Legend'


#To create the folders with sub folders.
using_maxUniques(filepath, max_uniques, output_folderpath)
```


_____________________________________________

<h3>Have fun. :-) </h3>