# Data-Engineering-project
Data Engineering DEPI
Data engineering is the practice of designing, constructing, and maintaining the systems and architecture that enable the collection, storage, transformation, and retrieval of data for analysis and reporting. It serves as the backbone of data processing workflows, ensuring that data is accurately prepared and accessible for data scientists, analysts, and applications.
# Modeling 
The model leverages an LSTM-based structure with several essential components:

- *LSTM Layers*: These layers are designed to identify patterns in sequences, capturing temporal relationships and context within the data.
- *Dense Layers*: These fully connected layers compress and refine the extracted features to produce final predictions.
- *Dropout Layers*: Added after key layers to reduce overfitting by temporarily "turning off" random neurons during training.
- *Output Layer*: A sigmoid activation function is used here to make binary decisions on stress levels.
- *Adam Optimizer*: With a learning rate of 0.0003, this optimizer adjusts network weights and includes gradient clipping to maintain training stability.

*Detailed Layer Structure*:
LSTM (128 units, return_sequences=True) → Dropout (50%) → LSTM (64 units) → Dense (128 units, ReLU) → Dropout (40%) → Dense (64 units) → Sigmoid Output Layer

*Why LSTM?*
LSTMs are ideal for handling sequential data because they retain essential information across long sequences, making them more effective for tasks needing temporal context than standard neural networks. Additionally, they reduce the impact of the vanishing gradient problem, leading to more stable and reliable training.

### Training & Evaluation

To optimize performance, the model was trained with these settings:

- *Epochs*: 150
- *Batch Size*: 16
- *Loss Function*: Binary Cross-Entropy
- *Metrics*: Accuracy and F1 Score

*Training Callbacks*:
- *ReduceLROnPlateau*: Lowers the learning rate if validation loss stops improving.
- *EarlyStopping*: Ends training if no improvements are seen for 10 epochs, restoring the model to its best state.

### Results

The model's performance was assessed using accuracy and F1 score, with separate training and evaluations conducted for male and female subjects across different activity types (e.g., EO, AC1). These results show the model’s effectiveness in identifying stress patterns from physiological data.  
