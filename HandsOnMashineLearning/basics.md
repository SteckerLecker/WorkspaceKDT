# Machine Learning Basics

## 1. What is machine learning?
Machine learning is a subfield of artificial intelligence that focuses on creating algorithms that can learn from data and improve their performance over time without being explicitly programmed. These algorithms identify patterns in large datasets and use those patterns to make predictions or decisions. Essentially, it allows computers to learn from experience, much like humans do.

## 2. Can you name four types of applications where it shines?
Machine learning excels in a wide range of applications. Four notable examples include:
- **Image and speech recognition**, where it identifies objects or understands spoken language.
- **Natural language processing**, for tasks like language translation and sentiment analysis.
- **Recommendation systems**, used by platforms like Netflix and Amazon to suggest products or content.
- **Predictive analytics**, which helps in forecasting stock prices or identifying potential fraud.

## 3. What is a labeled training set?
A labeled training set is a dataset where each instance is paired with its corresponding correct output or "label."  
Example: In an image classification task, a labeled training set would consist of thousands of pictures, each one tagged with a label like "cat," "dog," or "car."

## 4. What are the two most common supervised tasks?
The two most common supervised learning tasks are:
- **Classification**: Predicting a categorical label (e.g., "spam" or "not spam").
- **Regression**: Predicting a continuous numerical value (e.g., predicting the price of a house).

## 5. Can you name four common unsupervised tasks?
Four common unsupervised tasks are:
- **Clustering**
- **Dimensionality reduction**
- **Association rule learning**
- **Anomaly detection**

## 6. What type of algorithm would you use to allow a robot to walk in various unknown terrains?
You would typically use a **Reinforcement Learning** algorithm. It learns by trial and error, receiving rewards for desired actions and penalties for undesired ones.

## 7. What type of algorithm would you use to segment your customers into multiple groups?
A **clustering algorithm** (e.g., K-Means, DBSCAN) is used to automatically group customers with similar characteristics without needing pre-defined labels.

## 8. Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem?
Spam detection is a **supervised learning** problem. The model is trained on labeled data (e.g., "spam" or "not spam") to learn the patterns of spam emails.

## 9. What is an online learning system?
An **online learning system** (or incremental learning) learns data incrementally as it arrives.  
It updates the model continuously, making it ideal for real-time applications like stock prediction or recommendation systems.

## 10. What is out-of-core learning?
**Out-of-core learning** is used when the dataset is too large to fit into memory.  
The model is trained incrementally on small data chunks loaded from disk.

## 11. What type of algorithm relies on a similarity measure to make predictions?
An **instance-based learning** algorithm (e.g., k-Nearest Neighbors) uses a similarity measure to compare new instances to existing ones in the training set.

## 12. What is the difference between a model parameter and a model hyperparameter?
- **Model parameters** are learned during training (e.g., weights in a neural network).
- **Model hyperparameters** are set before training (e.g., learning rate, number of clusters).

## 13. What do model-based algorithms search for? What is the most common strategy they use to succeed? How do they make predictions?
Model-based algorithms search for the **optimal set of parameters** that minimize a **cost function**.  
Once trained, they use these parameters to make predictions via a learned mathematical function.

## 14. Can you name four of the main challenges in machine learning?
1. Insufficient or poor-quality data  
2. Non-representative training data  
3. Overfitting the training data  
4. Underfitting due to overly simple models  

## 15. If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name three possible solutions?
This is **overfitting**.  
Three possible solutions:
- Simplify the model
- Gather more training data
- Apply regularization techniques

## 16. What is a test set, and why would you want to use it?
A **test set** is a dataset kept separate from training data. It provides an **unbiased evaluation** of how well the model generalizes to unseen data.

## 17. What is the purpose of a validation set?
A **validation set** is used to fine-tune **hyperparameters** and compare model versions without touching the test set. It helps prevent overfitting through data snooping.

## 18. What is the train-dev set, when do you need it, and how do you use it?
A **train-dev set** (development set) is a subset of training data used to check for overfitting or data distribution mismatches.  
It helps diagnose if poor performance comes from high variance or a data shift.

## 19. What can go wrong if you tune hyperparameters using the test set?
You may **overfit to the test set**, leading to **optimistically biased** results that don’t reflect real-world performance.
