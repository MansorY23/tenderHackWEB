import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Загрузка CSV-файла в DataFrame
df = pd.read_csv('Логи.csv')


# Преобразование текстовых описаний ошибок в числовые признаки с использованием TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df['log'])

# Кластеризация ошибок с использованием K-Means
num_clusters = 8 # Выберите количество кластеров
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(tfidf_matrix)
df['Кластер'] = kmeans.labels_

# Сегментация по кластерам
for cluster in range(num_clusters):
    cluster_errors = df[df['Кластер'] == cluster]

    # Создание отдельного DataFrame для каждого кластера
    cluster_df = pd.DataFrame(cluster_errors)

    # Сохранение DataFrame в CSV-файл
    cluster_df.to_csv(f'кластер_{cluster}.csv', index=False)

