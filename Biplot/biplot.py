import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv('iris.csv')
my_data = (data.iloc[:, 1:5])

def Scaling(dataset):
    Scaling = MinMaxScaler(feature_range=(0,1))
    dataset = Scaling.fit_transform(dataset)
    dataset = pd.DataFrame(dataset)
    return dataset

def Biplot(dataset):
    n_col = len(dataset.columns)
    pca = PCA(n_components = n_col)
    pca.fit(dataset)
    xvector = pca.components_[0] 
    yvector = pca.components_[1]
    xs = pca.transform(dataset)[:, 0]
    ys = pca.transform(dataset)[:, 1]

    for i in range(len(xvector)):
        plt.arrow(0, 0, xvector[i]*max(xs), yvector[i]*max(ys),
              color='r', width=0.0005, head_width=0.0025)
        plt.text(xvector[i]*max(xs)*1.2, yvector[i]*max(ys)*1.2,
             list(dataset.columns.values)[i], color='r')
        
    for i in range(len(xs)):
        plt.plot(xs[i], ys[i], 'bo')
        plt.text(xs[i]*1.2, ys[i]*1.2, list(dataset.index)[i], color='b')

    plt.xlim(-1.1, 1.1)
    plt.ylim(-0.8, 0.8)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.show()

def run():
    data = my_data
    data = Scaling(data)
    Biplot(data)

if __name__ == '__main__':
     run()    

