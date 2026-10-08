# K-Means Clustering

A Python implementation of the **K-Means clustering algorithm**, developed in two versions: a procedural implementation and an object-oriented implementation.

The project loads a two-dimensional dataset, initializes random centroids, assigns points to the nearest centroid, recalculates cluster centroids, and repeats the process until the centroid movement falls below a defined threshold or the maximum number of iterations is reached.

## Features

- K-Means clustering from scratch
- Euclidean distance calculation
- Random centroid initialization
- Iterative cluster assignment and centroid recalculation
- Loss/convergence measurement based on centroid movement
- 2D data visualization with Matplotlib
- Configurable number of clusters
- Configurable iteration limit and convergence threshold
- Procedural and OOP implementations

## Technologies

- **Python 3**
- **Matplotlib**
- **Math**
- **Random**
- **Object-Oriented Programming**

## Implementations

### `kmeans.py`

A procedural implementation of K-Means using standalone functions for:

- Reading the dataset
- Initializing centroids
- Assigning points to clusters
- Recalculating centroids
- Calculating the loss value
- Visualizing the resulting clusters

### `kmeans_oop.py`

An object-oriented version of the same algorithm built around the `KMeans` class.

The class stores the dataset, centroids, clusters, configuration, and algorithm state, while methods handle each stage of the clustering process.

## Algorithm

For each iteration, the algorithm performs the following steps:

1. Initialize `K` centroids from randomly selected data points.
2. Calculate the Euclidean distance from every point to each centroid.
3. Assign every point to its nearest centroid.
4. Recalculate each centroid as the mean of the points assigned to that cluster.
5. Calculate the total movement of the centroids.
6. Repeat until convergence or the iteration limit is reached.

The default configuration is:

```text
K = 6
Maximum iterations = 50
Convergence threshold = 0.0001
```

## Dataset

The project includes a two-dimensional dataset in `data.csv`.

Each data point contains two numerical coordinates:

```text
x,y
```

The included dataset contains **352 data points**.

## Output

The scripts first display the original data points and then display the resulting clusters after K-Means converges.

The console also reports the loss value for each iteration:

```text
Epoch = 1
Loss Function = ...

Epoch = 2
Loss Function = ...
```

## Project Structure

```text
K-Means-Clustering/
├── data.csv
├── kmeans.py
├── kmeans_oop.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.9+
- Matplotlib

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Running the Project

Clone the repository:

```bash
git clone https://github.com/Jandyi/K-Means-Clustering.git
cd K-Means-Clustering
```

Run the procedural implementation:

```bash
python kmeans.py
```

Run the object-oriented implementation:

```bash
python kmeans_oop.py
```

## Project Information

- **Status:** Completed
- **Developed:** 2026
