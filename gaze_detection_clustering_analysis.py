
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_cluster(dataset_path):
    # Load the dataset
    df = pd.read_csv(dataset_path)

    # Basic EDA: Summary statistics and missing values
    print(df.describe())
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Identify numerical features for clustering
    numerical_features = [col for col in df.columns if df[col].dtype in ['float64', 'int64'] and not col.lower().endswith('id')]
    
    # Apply K-Means clustering
    X = df[numerical_features].dropna()
    kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
    df['Cluster'] = kmeans.labels_

    # Visualization
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=numerical_features[0], y=numerical_features[1], hue='Cluster', data=df, palette='viridis')
    plt.title('Cluster Visualization')
    plt.xlabel(numerical_features[0])
    plt.ylabel(numerical_features[1])
    plt.legend(title='Cluster')
    plt.grid(True)
    plt.show()

    # Save the modified dataset with cluster labels
    output_path = dataset_path.replace('.csv', '_with_clusters.csv')
    df.to_csv(output_path, index=False)
    print(f'Modified dataset saved to: {output_path}')

if __name__ == "__main__":
    dataset_path = 'gaze_detection_20_03.csv'  # Change this to the path of your dataset
    load_and_cluster(dataset_path)
