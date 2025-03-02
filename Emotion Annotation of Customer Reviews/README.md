# Understanding Customer Preferences Through Emotion Annotation
## Project Overview
This project aims to understand customer preferences by analysing and annotating emotions in customer reviews. It involves a combination of manual annotation, automated emotion detection, and machine learning for emotion prediction.

The project showcases the application of Python NLP libraries, web scraping techniques, and advanced machine learning methodologies to extract insights from textual data.

## Project Highlights
1. **Data Collection**: 
Reviews were scraped from trusted sources like Yelp and Trustpilot.
Python's Requests and BeautifulSoup libraries were used for efficient data scraping.

2. **Emotion Annotation**:
Over 4,000 reviews were manually annotated with emotions such as Happiness, Sadness, Anger, and others.
A custom Python function was developed to annotate an additional 18,000 reviews automatically.

3. **Exploratory Data Analysis (EDA)**:
Insights into the spread of emotions across reviews were visualized using Matplotlib and Seaborn.
Word clouds were generated to highlight frequently used words for each emotion.

4. **Model Training**:
A machine learning model was built using Scikit-Learn to predict emotions in reviews.
The annotated dataset served as training data, and model performance was evaluated using metrics such as accuracy, recall, and F1-score.

5. **Outcome**:
Delivered actionable insights to improve customer satisfaction.
Built a reusable pipeline for emotion annotation and analysis.

## Steps
1. **Web Scraping**:
   - Used BeautifulSoup and Requests to scrape reviews from websites.
   - Handled edge cases such as pagination and special characters.

2. **Data Cleaning and Preprocessing**:
   - Removed duplicates, special characters, and stopwords using **NLTK**.
   - Tokenized and lemmatized text for better feature extraction.
   - Aspect Segmentation using MS Excel VBA and Spacy Library.

3. **Annotation**:
   - Manually annotated over 4k reviews in MS Excel.
   - Created a custom annotation function to classify over 18k reviews into distinct emotions in Python.
   - Measured inter-annotator agreement using **Cohen's Kappa**.

4. **EDA and Visualization**:
   - Generated **emotion distribution charts**.
   - Created **word clouds** to identify frequently used terms for each emotion.

5. **Machine Learning**:
   - Trained an **SVM classifier** for emotion prediction.
   - Used **TF-IDF Vectorization** for text feature extraction.

## Technologies
- **Web Scraping**: Requests, BeautifulSoup
- **NLP**: NLTK, Scikit-Learn, Spacy
- **Visualization**: Matplotlib, Seaborn, Wordcloud
- **Data Manipulation**: Pandas, NumPy
- **Annotation**: Microsoft Excel (for manual annotation)
- **Machine Learning**: Scikit-Learn (SVM)


## Outcome
- Created an annotated dataset of over 20k reviews.
- Delivered actionable insights for improving customer satisfaction.

## Visualizations
### 1. Manual Annotation in MS Excel
![Manual Annotation](Manual%20Annotation%20in%20MS%20Excel.png)

### 2. Result of Automated Annotation using Custom Function in Python
![Automated Annotation](Result%20of%20Automated%20Annotation%20in%20Python.png)

### 3. Snapshot of Model Training, Evaluation, and testing
![Model Training, Evaluation, and testing](Model%20Training,%20Evaluation,%20and%20Testing.png)

### 4. Emotion Distribution
![Emotion Distribution](Emotion%20Distribution.png)

### 5. Word Cloud for Negative Reviews
![Word Cloud for Negative Reviews](Word%20Cloud%20for%20Negative%20Reviews.png)

### 6. Word Cloud for Positive Reviews
![Word Cloud for Positive Reviews](Word%20Cloud%20for%20Positive%20Reviews.png)


## How to Run
1. **Navigate to the project directory**
   Copy and run the following link:
```
https://github.com/ChiomaScripts/My-Portfolio/tree/5848a1740119b36612f1662a00dad9d372378ffd/Emotion%20Annotation%20of%20Customer%20Reviews
```

2. **Install the required libraries.**
   
3. **Run the python files.**

