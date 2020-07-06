import numpy as np
import pandas as pd

df = pd.read_csv('/home/dell/Downloads/ml-hw4/Data.csv', header=None)

#print df
def distance(x1,x2,y1,y2):
	d=np.sqrt((x1-x2)**2 + (y1-y2)**2)
	return d
x_c1=5
x_c2=10
y_c1=5
y_c2=10

def kmeans():
	threshold=distance(x_c1,x_c2,y_c1,y_c2)
	print threshold
	points_=[]
	k=0
	for row_index,row in df.iterrows():
		d1=distance(row[0],x_c1,row[1],y_c1)
		d2=distance(row[0],x_c2,row[1],y_c2)
		if d1>threshold and d2>threshold:
			print row[0] ,row[1]
			points_.append(row_index)
			k=k+1

	df_withoutoutlier=df.drop(points_)
	df_withoutoutlier.to_csv('df_withoutoutlier.csv', index=False, header=False)
#kmeans
#lable d1 ->0
#labled2 ->1
	data=df_withoutoutlier.values
	#print df_withoutoutlier
	size=data.shape[0]
	lable=np.zeros((size,1))
	i=0
	for row_index,row in df_withoutoutlier.iterrows():
		d1=distance(row[0],x_c1,row[1],y_c1)
		d2=distance(row[0],x_c2,row[1],y_c2)
		if d1>d2:
			lable[i]=1
			i+=1
		else:
			lable[i]=0
			i+=1
	
	data=np.concatenate((data,lable),axis=1)
	print data
kmeans()
