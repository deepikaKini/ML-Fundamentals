# Machine Learning Fundamentals

Welcome to the **Machine Learning Fundamentals** course repository! This guide covers core concepts and practices in machine learning, offering insights into essential techniques, best practices, and resources for further learning. I add my understanding of basic and advanced concepts I have been learning over the years, here. (Bad memory!). This repo and doc will help me revise concepts whenever needed.

---

### **Personal Notes**

### 1. **Data Preprocessing**
- **Handling Missing Data**: Use techniques like mean/mode/median imputation, or consider more advanced techniques like KNN or regression imputation.
- **Encoding Categorical Variables**: Machine learning models perform better with numeric data. Common encoding techniques include:
   - **Label Encoding**: Assigns a unique numeric value to each category (useful for ordinal data).
   - **One-Hot Encoding**: Creates binary columns for each category (ideal for nominal data).
   - **Target Encoding**: Maps categories to the mean of the target variable for each category.
- **Scaling Features**: Standardization and normalization improve model performance, especially for distance-based algorithms (e.g., KNN, SVM).

### 2. **Exploratory Data Analysis (EDA)**
- **Descriptive Statistics**: Summarize data distribution with mean, median, standard deviation, etc.
- **Data Visualization**: Select plots based on feature-target relationships:
   - **Numerical vs. Numerical**: Scatter plots, correlation heatmaps.
   - **Categorical vs. Numerical**: Box plots, violin plots.
   - **Categorical vs. Categorical**: Count plots, mosaic plots.
- **Feature Relationships**: Understand interactions between features using pair plots, histograms, and KDE plots.
- **Handling Imbalanced Data**: Use techniques like resampling (oversampling/undersampling) or synthetic data generation (SMOTE) to address imbalance.

### 3. **Feature Engineering**
- **Creating New Features**: Combine existing features (remove id columns and redundant columns) or create polynomial features to capture complex relationships.
- **Feature Selection**: Use techniques like correlation analysis, Recursive Feature Elimination (RFE), and tree-based feature importance to reduce dimensionality.
- **Dimensionality Reduction**: Apply PCA(EIGEN) , LDA to reduce complexity, especially for high-dimensional data. (Curse of Dimensionality!)

### 4. **Model Selection and Evaluation**
- **Choosing the Right Model**: Based on data type, problem type, and model interpretability.
   - **Logistic Regression**: For binary and categorical regression.
   - **Decision Trees & Random Forests**: Suitable for non-linear relationships, interpretable models.
   - **Support Vector Machines (SVM)**: Effective for high-dimensional spaces.
   - **K-Nearest Neighbors (KNN)**: Simple, intuitive, but sensitive to feature scaling.
- **Model Evaluation Metrics**: Use appropriate metrics based on the problem:
   - **Classification**: Accuracy, Precision, Recall, F1-score, ROC-AUC.
   - **Regression**: Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE).
- **Cross-Validation**: Use k-fold cross-validation to ensure model robustness and avoid overfitting.

### 5. **Handling Imbalanced Data**
- **Resampling Techniques**:
   - **Oversampling**: Duplicate examples in the minority class.
   - **Undersampling**: Reduce the majority class examples.
   - **Synthetic Minority Over-sampling Technique (SMOTE)**: Generates synthetic samples for the minority class.
- **Algorithm-Based Solutions**:
   - **Class Weights Adjustment**: In algorithms like logistic regression and random forests, adjust class weights to handle imbalance.
   - **Ensemble Techniques**: Methods like AdaBoost and Random Forest can be tuned to focus on minority classes.

### 6. CONCEPTS / TERMS:
- Gaussian distribution, Mahalanobis distance ( and other distance metrics)
- Otsu (clustering), occam's razor, No free lunch theorem, Mercer's theorem
- M estimate for Bayes
- Bagging Boosting
- Cross validation
- Bias vs Variance
- FLD
- XOR problem

---

### Additional Resources

- [Data Mining Map by Saed Sayad](https://www.saedsayad.com/data_mining_map.htm): A comprehensive guide to data mining techniques and their applications.
- **Books**:
   - *“Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow”* by Aurélien Géron 
   - *“Pattern Recognition and Machine Learning”* by Christopher Bishop
   - [*"INTRODUCTION TO LINEAR ALGEBRA"* by Gilbert Strang](https://students.aiu.edu/submissions/profiles/resources/onlineBook/Y5B7M4_Introduction_to_Linear_Algebra-_Fourth_Edition.pdf)
   - [*"An Introduction to Statistical Learning"* by Hastie et al.](https://www.statlearning.com/)
   - [*"The Elements of Statistical Learning"* by Hastie et al.](https://www.sas.upenn.edu/~fdiebold/NoHesitations/BookAdvanced.pdf)
- **Online Courses**:
   - **Coursera**: [Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning)
   - **Udemy Paid**: [Machine Learning A-Z]
-  **OTHER RESOURCES**:
  - Statistics and Probability for Data Science Textbook PDF - https://lnkd.in/gSqmf53r
  - Free A/B Testing Course by Google - https://lnkd.in/gC46WKrA
  - Stanford Algorithms Specialization - https://lnkd.in/gEwzS5sN
  - Deep Learning by Ian Goodfellow Textbook - https://lnkd.in/g_EUDGHa
  - Reinforcement Learning: An Introduction by Sutton and Barto PDF - https://lnkd.in/gkrtv6HP
