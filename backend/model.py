import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


def read_image(file):
    return np.array(Image.open(file).convert("RGB"))
def process_image(img):
    X_img=np.reshape(img,(img.shape[0]*img.shape[1],img.shape[2]))
    return X_img    
def kMeans_init_centroid(X,K):
    m,n=X.shape
    randindx=np.random.permutation(m)
    centroids=X[randindx[:K]]
    return centroids
def closest_centroids(X,centroids):
    m,n=X.shape
    K=centroids.shape[0]
    distances = np.sum((X[:, None] - centroids)**2, axis=2)
    idx = np.argmin(distances, axis=1)
    return idx
def compute_centroids(X,idx,K):
    m,n=X.shape
    centroids=np.zeros((K,n))
    for i in range(K):
        cnt=0
        for j in range(m):
            if(idx[j]==i):
                centroids[i]+=X[j]
                cnt+=1
        if(cnt >0):
         centroids[i]=centroids[i]/cnt
        else:
            centroids[i] = X[np.random.randint(m)]
    return centroids
def runKmeans(X,init_centroids,num_iters):
    m,n=X.shape
    K=init_centroids.shape[0]
    centroids=init_centroids
    idx=np.zeros(m,dtype=int)
    for i in range(num_iters):
        idx=closest_centroids(X,centroids)
        centroids=compute_centroids(X,idx,K)
    return centroids,idx
def base(file,k=16):
    img=read_image(file)
    X_img=process_image(img)
    K=k
    max_iter=10
    init_centroids=kMeans_init_centroid(X_img,K)
    centroids,idx=runKmeans(X_img,init_centroids,max_iter)
    idx=closest_centroids(X_img,centroids)
    X_recovered=centroids[idx,:]
    X_recovered=np.reshape(X_recovered,img.shape)
    return (X_recovered / 255.0).clip(0, 1)





        
