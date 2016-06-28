from sklearn.neighbors import NearestNeighbors
import numpy as np



k=3


raw_data = np.loadtxt('ffm_tr_knn_data.txt')
train = raw_data[:,0:(raw_data.shape[1]-1)]
label = raw_data[:,(raw_data.shape[1]-1)]
del raw_data
nbrs = NearestNeighbors(n_neighbors=k, algorithm='kd_tree').fit(train)

raw_data = np.loadtxt('ffm_te_knn_data.txt');
test = raw_data[:,0:(raw_data.shape[1]-1)]
test_label= raw_data[:,(raw_data.shape[1]-1)]
size=test.shape[0];
distances, indices = nbrs.kneighbors(test)
knn_est = np.mean(np.reshape(label[indices.ravel()], indices.shape), 1)
distances = np.mean(distances, 1)
print "rmse =", np.sqrt(np.mean((test_label - knn_est)**2))
np.savetxt('knn_te_pred.txt', np.concatenate((knn_est,distances)).reshape((2,size)).T)
