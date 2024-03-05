# Deploy-Machine-Learning-Model-For-Diabetes-Prediction using Support Vector Machine (SVM)

This project is aimed at predicting diabetes in individuals using a Support Vector Machine classifier trained on the PIMA Diabetes Dataset.

## Project Overview

Diabetes is a chronic disease that affects millions of people worldwide. Early detection and management of diabetes are crucial for preventing complications and improving the quality of life for affected individuals. Machine learning techniques can aid in diagnosing diabetes based on various factors such as glucose levels, blood pressure, BMI, etc.

In this project, we use the Support Vector Machine (SVM) algorithm to build a predictive model that can classify individuals as diabetic or non-diabetic based on their health parameters.

## Dataset

We use the PIMA Diabetes Dataset, which contains various health parameters of individuals along with their diabetic status (0 for non-diabetic and 1 for diabetic). The dataset consists of the following features:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI (Body Mass Index)
- DiabetesPedigreeFunction
- Age

## Project Structure

- **Data Collection and Analysis**: This section involves loading and exploring the dataset to gain insights into the data distribution and statistical measures.

- **Train Test Split**: The dataset is split into training and testing sets to evaluate the performance of the model.

- **Training the Model**: We train the Support Vector Machine classifier on the training data.

- **Model Evaluation**: The accuracy of the model is evaluated using both training and testing data.

- **Making Predictions**: We make predictions on new data using the trained model.

- **Saving the Trained Model**: The trained SVM model is saved using the pickle library for future use.

## Dependencies

- pandas
- numpy
- scikit-learn
- pickle

## Instructions for Use

1. Clone the repository:

   ```
   git clone <repository_url>
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the notebook/script to train the model and make predictions.

4. Modify the input data in the prediction section to make predictions for different individuals.

## Future Improvements

- Explore other machine learning algorithms for comparison.
- Perform hyperparameter tuning to optimize model performance.
- Incorporate additional features for improved prediction accuracy.

## Contributors

- [Abhinav Maheshwaram]([https://github.com/your_username](https://github.com/AbhinavMaheshwaram/-Deploy-Machine-Learning-Model-For-Diabetes-Prediction)https://github.com/AbhinavMaheshwaram/-Deploy-Machine-Learning-Model-For-Diabetes-Prediction)

## License

This project is licensed under the [MIT License](LICENSE).
