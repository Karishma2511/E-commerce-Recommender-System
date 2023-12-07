from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import spacy

app = Flask(__name__)

product = pd.read_csv('test.csv', encoding='latin-1')
product = product.dropna()
vectorizer = TfidfVectorizer(stop_words='english')
X1 = vectorizer.fit_transform(product["product_title"])
true_k = 10
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    product = request.form['product']
    recommended_products = similar_products(product, num_recommendations=5)
    return render_template('index.html', product=product, recommendations=recommended_products)

def similar_products(search_term, num_recommendations=5):
    Y = vectorizer.transform([search_term])
    prediction = model.predict(Y)
    cluster_center = model.cluster_centers_[prediction[0]]
    similarities = cosine_similarity(X1, cluster_center.reshape(1, -1))
    sim_scores = list(enumerate(similarities))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    product_indices = [score[0] for score in sim_scores]
    recommended_product_titles = product.iloc[product_indices]["product_title"].tolist()
    return recommended_product_titles

if __name__ == '__main__':
    app.run(debug=True)