import sklearn.cluster as skc 
from sklearn import datasets
import matplotlib.pyplot as plt 
from sklearn.metrics import davies_bouldin_score
import numpy as np  
import cv2
a=0
x=[]
y=[]
new_val=[]
clusters=[]
img_g=[]
val=[]
simi=[]
im = cv2.imread(r'C:\Users\Dell\Downloads\imagens\cars3.jpg', cv2.IMREAD_GRAYSCALE)
#ret,im= cv2.threshold(im,190,255,cv2.THRESH_BINARY)
for i in range ((len(im))):
    for j in range (len(im[0])):
        if  int(im[i][j])<5 or int(im[i][j]<220):
            img_g.append(([i,j,im[i][j]]))
for k in range (33,38):
    k_means=skc.KMeans(n_clusters=k,max_iter=20,precompute_distances=True).fit(img_g)
    a=k_means.inertia_
    val.append(k_means.cluster_centers_)
    simi.append(davies_bouldin_score(img_g,k_means.labels_))
    new_val.append(a)
    clusters.append(k)
'''
ang,angu=[],[]
angu=np.linalg.norm(new_val)
normalized=new_val/angu
clust=np.linalg.norm(clusters)
clusters=clusters/clust

for i in range(len(normalized)):
      cosa=clusters[i]/((clusters[i]**2)+(normalized[i]**2))
      ang.append(cosa)
b=0
angulosrel=[]

for i in range (1,len(ang)):
    try:
        ang1=ang[i]/b
        b=ang[i]

    except ZeroDivisionError or RuntimeWarning:
        pass
        
    angulosrel.append(ang1)

m=angulosrel.index(min(angulosrel))
'''
m=simi.index(min(simi))
print(simi)

for k in range(len(val[m])):

    x.append(val[m][k][0])
    y.append(val[m][k][1])

plt.scatter(y,x,c='r')
plt.imshow(im,cmap='gray')

print(m + clusters[0])

plt.show()
