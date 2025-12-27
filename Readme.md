# Information_converter

This project is a Python application designed to classify and convert between different numeric formats (binary, decimal, and hexadecimal). It was created as a learning exercise to practice machine learning and data conversion techniques using a forest classifier model.

## Overview

The **Information_converter** tool can:

- Detect whether an input number is binary, decimal, or hexadecimal.
- Convert between these numeric formats.
- Use a machine learning model (forest classifier) to make predictions with about **94% accuracy**.

This project was inspired by an extra credit assignment for IB Computer Science HL. Originally the task was to build functions that convert binary to decimal and hexadecimal — but this project expands that with all combinations and adds a simple AI classifier.

## Files in this Repo

| File | Description |
|------|-------------|
| `data_converter.py` | Main script for converting numbers and using the classifier |
| `python_converter.py` | Python helper functions for numeric conversions |
| `binary_decimal_hex_null_dataset.csv` | Dataset used to train the classifier |
| `numeric_format_training_clean.csv` | Cleaned training data |
| `numeric_format_training_int_pandas.csv` | Training data in integer format |
| `README.md` | This file |  

## How It Works

1. The project uses a **forest classifier** machine learning model to determine the format of a numeric input (binary, decimal, or hex).  
2. Once the format is predicted, it converts the input into other numeric formats.  
3. The model was trained on formatted numeric datasets to reach ~94% prediction accuracy.

## Getting Started

### Requirements

Make sure Python 3.x is installed.

You may need to install required libraries — e.g., `scikit-learn`, `pandas`, etc. You can do this with:

```bash
pip install scikit-learn pandas
