Steps to run the notebook in pyCharm:
1. Open 603_project_mkhan in PyCharm and Install the following packages;
a. jupyter
b. matplotlib
c.seaborn
d. pandas
e.plotly
f.findSpark
g.pyspark

In case of any other missing package, install it by its name from "Project Interpreter" page's add section
2. Download the csv files in the folder from "https://www.kaggle.com/pavanraj159/fifa-world-cup-1930-to-2014-data-analysis/data" (It has the additional
penalties csv file with the 3 csv files). The csv files are also too big to be submitted inside the folder.

Download spark-2.2.1 from https://spark.apache.org/releases/spark-release-2-2-1.html in the 603_project_mkhan folder
I downloaded it under the project but it's too big a file to submit under project data in Canvas.

If you are runniong the 2nd cell (Total Attendance by year using pyspark) 2nd time, make sure you comment the following lines.

sc =SparkContext()
because "Multiple spark contexts can't be run at once". Another option would be restarting the notebook.

2. Click the icon run to run the cell (alternatively, you can press ⇧⏎). PyCharm shows a dialog box, where you have to specify the URL where the Jupyter Notebook server will run:

In the dialog box that will pop up, click Cancel, and then click the Run Jupyter Notebook link:

Jupyter server runs in the console after you press "Run cell" again.
Refer to "https://www.jetbrains.com/help/pycharm/using-ipython-notebook-with-product.html" for further help.



To run it in the broweser:

1. Download the notebook.
2. Install jupyter and findspark using pip (command: "pip install jupyter" 
And "pip install findspark" from terminal)
FYI: To use pyspark, download spark-2.2.1 from https://spark.apache.org/releases/spark-release-2-2-1.html in the 603_project_mkhan folder
I downloaded it under the project but it's too big a file to submit under project data in Canvas.

If you are still having issues, add the following lines to you .bashrc and execute it by "source ~/.bashrc"

export SPARK_HOME=/.../spark-2.2.1-bin-hadoop2.7
export PATH=$SPARK_HOME/bin:$PATH


3. Go into the folder containing the notebook from "Terminal" in Mac and run "jupyter notebook"


5. Go to "Cell" on the top and click "Run all" to see the output for the whole notebook. You can also run each module separately.

FYI: If you are getting any import errors, make sure install it using pip. For example:
a. pip install numpy (To import numpy)
b. pip install matplotlib (To import matplotlib)
c. pip install pandas (To import pandas)
d. pip install seaborn (To import seaborn)
e. pip install plotly (To import plotly)
