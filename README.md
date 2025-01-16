
# Boosting Sales With Data: An E-Commerce Recommender System

This project implements a machine learning-based recommender system in an e-commerce setting to enhance user experience and boost sales. By analyzing user behavior, preferences, and historical data, the system provides personalized product suggestions through content-based filtering models.

## Overview

Recommender systems are critical for improving user engagement and increasing sales in e-commerce. This project integrates a content-based filtering approach using product titles to suggest similar items based on user input. 

Key outcomes:
- **Increased sales** through targeted recommendations.
- **Heightened user engagement** with personalized experiences.
- **Improved customer satisfaction** via relevant product suggestions.

## Key Features

- **Machine Learning**: Content-based filtering using TF-IDF and K-Means clustering.
- **Similarity Metrics**: Leverages cosine similarity for recommending products.
- **Web Interface**: Built with Flask for easy user interaction.
- **Data Handling**: Preprocessed product data for efficient clustering and recommendations.

## Technologies and Tools Used

- **Programming Language**: Python
- **Libraries**: Flask, Pandas, Scikit-learn, Spacy
- **Modeling Techniques**: TF-IDF Vectorization, K-Means Clustering, Cosine Similarity
- **Web Framework**: Flask
- **Tools**: Jupyter Notebook, HTML/CSS (for front-end integration)

## Steps and Workflow

### 1. Data Preprocessing
- Loaded product data from a CSV file and cleaned it by removing null values.
- Utilized TF-IDF vectorization to transform product titles into numerical representations.

### 2. Model Development
- Implemented K-Means clustering to group similar products into clusters.
- Tuned the number of clusters for optimal grouping and recommendations.

### 3. Recommender System
- Developed a function to identify similar products based on cosine similarity within clusters.
- Integrated the recommender system with a Flask-based web interface.

### 4. Web Interface
- Created a simple web application to allow users to input a product and view recommendations.
- Displayed the recommended products dynamically on the interface.

### 5. Testing and Deployment
- Tested the application with diverse product inputs to ensure reliable recommendations.
- Deployed the Flask app for interactive usage.

## How to Run the Project

1. **Prerequisites**:
   - Python 3.x installed on your system.
   - Libraries: Flask, Pandas, Scikit-learn, Spacy.

2. **Steps**:
   - Clone this repository to your local machine.
   - Place your dataset as `test.csv` in the same directory as `app.py`.
   - Run the following command to start the Flask application:
     ```bash
     python app.py
     ```
   - Open your browser and navigate to `http://127.0.0.1:5000/`.

3. **Usage**:
   - Enter a product name in the input field.
   - View similar product recommendations on the screen.

## Future Enhancements

- Expand the dataset to include more diverse product attributes.
- Implement additional recommendation techniques such as collaborative filtering or hybrid models.
- Enhance the UI for better user interaction.
- Optimize model performance for larger datasets.

## Results and Impact

The integration of this recommender system demonstrated significant potential in boosting e-commerce sales, improving user engagement, and enhancing overall customer satisfaction. It showcases the impactful application of machine learning in transforming the online retail industry.

---

