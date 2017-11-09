# Introduction:

This is the very simple implementation of Biplot, a useful function for unsupervised data analysis and clustering. This doesn't come with scikit-learn library. You can find it in typical R packages.

This is implemented using Pandas, Sklearn and Matplotlib.

Finally, this function has been implemented on Iris dataset for visulaization of possible clusters through biplot.

# Biplot:

Biplots are a type of exploratory graph used in statistics, a generalization of the simple two-variable scatterplot. A biplot allows information on both samples and variables of a data matrix to be displayed graphically. Samples are displayed as points while variables are displayed either as vectors, linear axes or nonlinear trajectories. In the case of categorical variables, category level points may be used to represent the levels of a categorical variable. A generalised biplot displays information on both continuous and categorical variables.

For more information, follow this [link](https://en.wikipedia.org/wiki/Biplot)

# Result:

![biplot](https://user-images.githubusercontent.com/24511419/32596087-4bdfd530-c55c-11e7-9e54-bcf16b617653.png)

The red lines are the projected eigenvectors on 2D plane. This method is so useful for visulaization of unsupervised learning problems. Here, blues points are all sample examples of the dataset. It clearly tells us the data should have three classes. 
