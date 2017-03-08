---
title: iPython Notebooks, Spyder IDE, IO
duration: "1:5"
creator:
    name: 
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) iPython Notebooks, Spyder IDE, IO

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Demonstrate how to use the notebook, code vs Markdown mode
- Contrast utility of a notebook vs Spyder IDE
- Show how to save and share the notebook via Jupyter
- Use the csv library

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Install Anaconda
- Create an Anaconda environment with iPython Notebook installed
- From iPython Notebook, install Jupyter

## Tools

Anaconda is a completely free Python distribution. It includes more than 400
of the most popular Python packages for science, math, engineering, and data analysis.
[Anaconda](https://www.continuum.io/downloads)

iPython Notebook is an interactive computational environment, in which you
can combine code execution, rich text, mathematics, plots and rich media.
[iPython Notebook](http://ipython.org/notebook.html)

The Jupyter Notebook is a web application that allows you to create and share
documents that contain live code, equations, visualizations and explanatory text.
Uses include: data cleaning and transformation, numerical simulation,
statistical modeling, machine learning and much more.
[Jupyter](http://jupyter.org/)

Spyder IDE is an open source integrated development environment ofr scientific porgramming in Python. Spyder includes a notepad space for writing code, a connected kernal for executing that code, and other panes and tools that assist the development process (including variable explorer).

### Launch a Jupyter Notebook

Let's walkthrough launching a notebook. Using your newfound terminal commands, navigate to the repository where this lesson exists and launch a Jupyter Notebook. We'll create a notebook in the code folder. Title it something unique--your name is a good bet.

```bash
jupyter-notebook
```

### Jupyter Notebook Code v Markdown

Let's play around with iPython Notebook first to get a feel for it.

The notebook starts off in the "Code" mode, which means that the cell is ready to accept
any code we write. Let's toggle it to "Markdown" mode. Practice writing a cell of code and
then a cell of Markdown and run it. Remember the [markdown guide](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

Next, click through the dropdown menus: File, Edit, View, Insert, Cell, Kernel, and Help,
just to get a look at what's available. Don't worry, you'll become more familiar with
these through usage.

Let me show you how to use Jupyter to display an .ipynb file in
[Jupyter's NBviewer](https://nbviewer.jupyter.org/). Remember, it must be PUBLICLY
available and not PRIVATE in order to work. Now, create your own Jupyter/iPython Notebook,
upload it to your GitHub account, make it publicly available, and then view it through
Jupyter's NBviewer.

### Launch Spyder

Let's walkthrough creating a Python file and then editing it in Spyder. Create a python file in the code folder.Title it something unique--your name is a good bet.

```bash
touch test.py
```

```bash
Spyder test.py
```

## Demo: csv module

Let's take a look at the Python csv module. The csv module’s reader and
writer objects read and write sequences. We'll be using a small Sales data set
to practice. Let's read a csv file first, using the following [demo code](./code/w1-3.2-demo.ipynb).

In iPython notebook type:

```python
import csv
print 'Opening File. Data: '
print ''
with open('sales.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
f.close()
print ''
print 'file closed'   # Always remember to close the file after writing to it!
```

The output will be the contents of sales.csv file. Now, let's write to a csv file.

In iPython notebook type:

```python
print 'Adding the following record: '
data = ['123456', 'cosmos', 'neil', 'lucy', 'universe', '1', '1,000,000', 'presented']
print ''
print data
with open('sales.csv', 'a') as fp:
    a = csv.writer(fp, delimiter=',')
    fp.write('\n')
    a.writerows([data])

fp.close()
print ''
print 'file closed'    # Always remember to close the file after writing to it!
```

Now, let's see the file again, with the data you just added:

```python
print 'The new data that was just added, can be seen on the last line: '
with open('sales.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

f.close()
print ''
print 'file closed'
```

## Conclusion
Today we were introduced to Anaconda, iPython Notebook, Jupyter, and how to read and write csv files.
Nice. Next we'll be introduced to NumPy. Sounds like fun!


## Resources

- Markdown guide [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Advanced Jupyter Notebook tips [here](https://blog.dominodatalab.com/lesser-known-ways-of-using-notebooks/)


