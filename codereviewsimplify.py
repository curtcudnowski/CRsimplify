import numpy as np
import pandas as pd
import plotext
from sklearn.cluster import KMeans

def elbow(df):
    temp = df.drop(['exaddr', 'srcaddr', 'dstaddr', 'nexthop'], axis=1)
    X = temp.values
    inertia = []
    k_range = range(1, 20)

    for i in k_range:
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X)
        inertia.append(kmeans.inertia_)

    plotext.plot(k_range, inertia)
    plotext.show()

def kMeans(df):
    dataset = df.drop(['exaddr', 'engine_type', 'dstaddr', 'nexthop', 'input', 'tos', 'src_mask', 'dst_mask', 'src_as', 'dst_as'], axis=1)
    dataset = dataset.groupby(['srcaddr']).mean()
    mat = dataset.values

    km = KMeans(n_clusters=5)
    km.fit(mat)
    labels = km.labels_
    results = pd.DataFrame([dataset.index, labels]).T

    return results

def main():
    raw_data = pd.read_csv(input("Enter the path to the CSV file: "))

    print("Elbow")
    elbow(raw_data)

    print("KMeans")
    print(kMeans(raw_data))

main()
