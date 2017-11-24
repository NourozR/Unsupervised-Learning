import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt 

# FUNCTION FOR 2D VISUALIZATION USING t-SNE
def T_SNE(dataset, lr = 200):
	model = TSNE(learning_rate = lr)
	features = model.fit_transform(dataset)
	features_x = features[:,0]
	features_y = features[:,1]
	return features_x, features_y

# IMPORTING IRIS DATASET AND PROCESSING
data = pd.read_csv('iris.csv')
data['Species'] = data['Species'].astype('category')
data['Species'] = data['Species'].cat.codes
my_data = data.iloc[:, 1:5]	

# APPLY t-SNE ON UNLABELLED DATASET
xs, ys = T_SNE(my_data)	
# PLOT t-SNE 2D PLOT
plt.scatter(xs, ys, c=data['Species'])
plt.show()


