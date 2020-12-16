# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 9:30
# @Author  : fsf
# @FileName: fetch-face.py
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import  fetch_lfw_people
faces = fetch_lfw_people()


random_indexes = np.random.permutation(len(faces.data))
X = faces.data[random_indexes]
example_faces = X[:36,:]

def plot_faces(faces):

	fig, axes = plt.subplots(6, 6, figsize=(10,10),
	subplot_kw = {'xticks':[], 'yticks':[]},
	gridspec_kw = dict(hspace=0.1,wspace=0.1))
	for i, ax in enumerate(axes.flat):
		ax.imshow(faces[i].reshape(62, 47), cmap = "bone")
	plt.show()
print(plot_faces(example_faces))
