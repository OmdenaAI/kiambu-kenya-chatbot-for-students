## Defining the Data Science Problem
Our dataset is organized into classes of tag names, sentence patterns, and responses. 

This indicates that the students' Chatbot receives instructions from students in form of sentence patterns made of words.
The bot classifies the sentence patterns according to class/tag name the sentence belongs to; then draws a response from that class as feedback to the student.

The dataset has tag names as labels to sentence patterns and responses classes/categories. We frame the data science problem as a Supervised Machine Learning problem.
Also, the dataset has tag name categories hence we will frame the data science task as a Classification Task.

In summary, the task entails training the chatbot on sentence Patterns (intents) so that the bot understands intents when asked by students. The task involves classifying sentence patterns according to tag names and drawing responses from respective tag name as feedback to the student

### Task-1 Goals
Task-1 has three goals:
1. Cleaning words in students’ instruction sentence patterns (tokenization and stemming)
2. Extracting features from the dataset
3. Encoding the words in sentence patterns into numerical values (array/matrix)

### Task-1 Details
- Read the dataset
- Extract training and output (predictions) features from the dataset
- Clean the dataset (tokenization and stemming)
- Build a library of words (our bot's vocabulary)
- Encode training and output features from words to numerical numbers
- Convert training and output features into arrays for modeling (Task-2)

### Information Table About Files:
|No.| Code/notebook file name | Description | Link |
| - | - | - | - |
| 1 | task-1-json-data-processing-and-cleaning.ipynb | code for cleaning and processing json file dataset  |   |
| 2 | task-1-excel-data-processing-and-cleaning.ipynb | code for cleaning and processing excel data file format|   |
| 3 |    |   |   |
