# Binary-Code-Detection
This project is developed for the SemEval 2026 Task 13 - Subtask A competition, which aims to detect whether a source code snippet is human-written or AI-generated.

## Overview
Our approach extracts lightweight style features and evaluates them on different machine learning models. We also apply the Adaptive Thresholding technique to improve model performance.

The workflow includes:
- Exploring and analyzing the competition dataset
- Extracting and evaluating style features
- Selecting the best-performing features
- Evaluating different models with and without Adaptive Thresholding

## Project structure
```
Binary-Code-Detection/
├── data/                       # Competition data
│   ├── train.parquet          
│   ├── validation.parquet
│   ├── test_sample.parquet
│   └── test.parquet 
├── extracted_features/         # The parquet files containing extracted features
│   ├── train.parquet          
│   ├── validation.parquet
│   ├── test_sample.parquet
│   └── test.parquet                
├── notebooks/                  # Notebooks  
│   ├── data_eda.ipynb          # Notebook for dataset EDA
│   ├── features.ipynb          # Notebook for features extraction and analysis
│   └── model.ipynb             # Notebook for evaluating different models on selected features
└── README.md
```

The parquet files in data/ can be downloaded at https://www.kaggle.com/competitions/sem-eval-2026-task-13-subtask-a/data.

## Features
- Blank line ratio.
- Whitespaces ratio.
- Paragraph's lines ratio.
- Paragraph's spaces ratio.
- Comment ratio.
- Comments per paragraph.
- Standard comment ratio.

## Models
- Linear model:
    + Logistic Regression.
- Deep Neural Network:
    + Multi-layer Perceptron.
- Tree-based model:
    + Random Forest.
    + Extreme Gradient Boosting.
    + Categorical Boosting.
    + Light Gradient Boosting Machine

## Authors
- [Huynh Gia Bao](https://github.com/baohg153)
- [Phan Huynh Minh Khoi](https://github.com/phmkhoi)
- [Nguyen Duc Tri](https://github.com/TriNguyen1208)