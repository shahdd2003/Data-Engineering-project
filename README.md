# Data-Engineering-project
Data Engineering DEPI
Data engineering is the practice of designing, constructing, and maintaining the systems and architecture that enable the collection, storage, transformation, and retrieval of data for analysis and reporting. It serves as the backbone of data processing workflows, ensuring that data is accurately prepared and accessible for data scientists, analysts, and applications.
#pipeline
pipeline is an organized, automated workflow that enables the efficient movement, transformation, and management of data across various stages, tools, and environments within Azure’s ecosystem. Pipelines are crucial in data engineering, application deployment, and continuous integration/continuous deployment (CI/CD) processes.
Key Types of Pipelines in Azure
Azure Data Factory Pipelines: Designed for data integration and transformation, these pipelines help orchestrate and automate data workflows across different data stores and services. They are often used for ETL (Extract, Transform, Load) processes.

Data Flow: Data flows are activities in a pipeline that allow for complex data transformations without writing code. They enable tasks like data cleansing, aggregation, and transformations.
Activities: Activities are individual tasks within a pipeline, such as copy, move, data transformation, or data load.
Triggers: Triggers allow pipelines to run on a schedule or when a specific event occurs.
Azure DevOps Pipelines: Used primarily for CI/CD, DevOps pipelines enable automated code testing, building, and deployment.

Build Pipelines: These pipelines compile code, run tests, and create deployable artifacts. They allow developers to ensure their code works before deployment.
Release Pipelines: Release pipelines automate the deployment of applications to different environments, such as staging or production, managing testing and approvals.
Synapse Pipelines: Synapse Analytics offers pipelines for complex data engineering workflows that handle big data and large-scale analytical processes.

Data Movement: Synapse pipelines move large datasets across different environments (e.g., from an on-premises server to cloud storage).
Orchestration: They schedule and orchestrate data transformations and machine learning tasks as part of analytics solutions.
Key Features of Azure Pipelines
Source Control Integration: Pipelines in Azure integrate with popular source control tools like GitHub, Azure Repos, and Bitbucket, enabling automated workflows directly from source control.
Parameterization and Variables: Allows users to dynamically pass values to different pipeline components, making workflows more flexible and reusable.
Monitoring and Logging: Azure pipelines provide comprehensive monitoring, logging, and alerting, helping identify issues quickly and ensure workflows run smoothly.
Linked Services and Datasets: Data Factory and Synapse pipelines use linked services to connect to data stores (like SQL databases or Azure Blob Storage) and datasets to define data schemas.
Integration with Other Azure Services: Azure pipelines can integrate with services like Azure Machine Learning, Power BI, Logic Apps, and more, allowing seamless, end-to-end workflows.
Use Cases for Azure Pipelines
ETL and Data Integration: Move data from different sources, transform it as needed, and load it into a centralized database or data warehouse.
Automated Deployments: CI/CD pipelines automate application deployments to cloud environments, ensuring quick and reliable updates.
Big Data Processing: Synapse pipelines orchestrate large-scale data processing tasks, such as data ingestion and machine learning model training.
Azure pipelines are versatile and are used extensively to automate, orchestrate, and simplify data and application workflows within the Azure cloud.
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
