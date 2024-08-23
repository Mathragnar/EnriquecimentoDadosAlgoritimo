Data Enrichment Algorithm

This Python project performs data enrichment and analysis on a CSV file containing financial market data (likely price bars with open and close prices). The project aims to:

Classify Bars: Classifies price bars based on their open and close prices, assigning them a result of 0 (down), 1 (up), or 2 (doji/no change).

Enrich Data: Adds date and time information to the classified bars, enriching the dataset.

Analyze Results: Calculates and displays the count and percentage of each classification result.

Data Balancing: Allows the user to remove a specified number of bars classified as "2" (no change) to potentially balance the dataset.

Shuffle Data: Shuffles the enriched data randomly to create a randomized dataset, which can be useful for machine learning applications.

Classes:

The project utilizes three main classes:

Central_enriquecimento_dados_algoritmo: The main class that orchestrates the entire process, utilizing the other classes and handling user input.

ProcessamentoDeDados_ClassificacaoResultado0_1_2 (Specifically, the BarClassifier class within this file):

Reads the input CSV file.

Classifies each bar based on open/close prices and assigns a result (0, 1, or 2).

Adds date and time information from the input data.

Saves the enriched data to a new CSV file.

DadosPorcentagemContagemEmbaralhamento (Specifically, the DataProcessor class within this file):

Reads the enriched data CSV file.

Calculates and prints the count and percentage of each result (0, 1, 2).

Provides functionality to remove rows with the result "2".

Shuffles the data and saves it to a new randomized CSV file.

How it Works:

Data Classification: The BarClassifier analyzes historical price bars, classifying the current bar based on its open/close price relationship to previous bars and its own price action.

Data Enrichment: Date and time information from the input data are added to the classified data.

Result Analysis: The DataProcessor analyzes the classification results, providing counts and percentages.

Data Balancing: The user can optionally remove some rows with the "2" classification to balance the dataset.

Data Shuffling: The DataProcessor shuffles the enriched data for potential use in machine learning applications where randomized data is essential.

Potential Uses:

Financial Market Analysis: Understanding price action patterns and their frequency.

Machine Learning: Creating a labeled dataset for training machine learning models to predict market movements.

Algorithmic Trading: Developing and backtesting trading strategies based on identified patterns.
