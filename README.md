
# Rectified Point Flow: Generic Point Cloud Pose Estimation Lab

This repository contains a Streamlit application designed to provide an interactive platform for exploring and comparing different evaluation metrics for pairwise point cloud registration. The application highlights the performance of Rectified Point Flow (RPF) against various baseline methods.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Evaluation Metrics Explained](#evaluation-metrics-explained)
- [Rigidity Preservation](#rigidity-preservation)
- [How to Run Locally](#how-to-run-locally)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction
Point cloud registration is a fundamental problem in 3D computer vision and robotics, aiming to find the optimal rigid transformation (rotation and translation) that aligns two partially overlapping point clouds. This Streamlit application serves as an educational and analytical tool to visualize and understand the performance of different algorithms, with a special focus on Rectified Point Flow (RPF).

## Features
- **Interactive Metric Comparison**: Compare Rotation Error (RE), Translation Error (TE), and Recall metrics across different methods and datasets.
- **Rigidity Preservation Analysis**: Visualize and understand Root Mean Square Error (RMSE) and Overlap Ratio (OR) in the context of rigidity preservation.
- **Dynamic Filtering**: Select datasets and registration methods to customize visualizations.
- **Conceptual 3D Visualization**: A simulated 3D plot to conceptually illustrate point cloud alignment.
- **Clear Explanations**: In-app markdown text and tooltips provide definitions and interpretations of metrics and concepts.

## Evaluation Metrics Explained

### Rotation Error (RE)
The angular difference in degrees between the predicted rotation and the ground-truth rotation.
Formula: $$RE = \arccos\left(\frac{\text{trace}(R_{pred}^T R_{gt}) - 1}{2}\right) \times \frac{180}{\pi}$$
**Interpretation**: Lower RE indicates higher accuracy in rotation estimation.

### Translation Error (TE)
The Euclidean distance in centimeters between the predicted translation and the ground-truth translation.
Formula: $$TE = \| t_{pred} - t_{gt} \|_2$$
**Interpretation**: Lower TE indicates higher accuracy in translation estimation.

### Recall@5°
The percentage of successful registrations where the Rotation Error (RE) is below or equal to 5 degrees.
**Interpretation**: Higher recall indicates better robustness to rotational challenges.

### Recall@1cm
The percentage of successful registrations where the Translation Error (TE) is below or equal to 1 cm.
**Interpretation**: Higher recall indicates better robustness to translational challenges.

## Rigidity Preservation

Rigidity preservation is crucial in point cloud registration to ensure that the internal structure and distances within a point cloud are maintained after transformation.

### Root Mean Square Error (RMSE)
Quantifies the average magnitude of the errors between transformed points and their ground truth positions.
Formula: $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \| \mathbf{p}_{i,transformed} - \mathbf{p}_{i,groundtruth} \|^2}$$
Where:
- $N$ is the number of corresponding points.
- $\| \mathbf{p}_{i,transformed} - \mathbf{p}_{i,groundtruth} \|^2$ is the squared Euclidean distance between the $i$-th transformed point and its corresponding ground truth point.
**Interpretation**: A lower RMSE indicates higher accuracy and better preservation of the original shape.

### Overlap Ratio (OR)
Measures the proportion of points in one point cloud that overlap with points in another after registration, given a certain distance threshold.
**Interpretation**: A higher OR signifies that a larger portion of the point clouds are successfully aligned.

## How to Run Locally

To run this Streamlit application on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\\Scripts\\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

    The application will open in your default web browser at `http://localhost:8501`.

## Project Structure
```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── application_pages/
    ├── __init__.py
    ├── metric_comparison.py
    └── rigidity_preservation.py
```

-   `app.py`: The main Streamlit application file, handles navigation and general layout.
-   `requirements.txt`: Lists all Python dependencies.
-   `Dockerfile`: Provides instructions for building a Docker image of the application.
-   `README.md`: This file, providing an overview and instructions.
-   `application_pages/`: Directory containing individual Streamlit page logic.
    -   `metric_comparison.py`: Logic and visualizations for comparing different metrics.
    -   `rigidity_preservation.py`: Logic and visualizations for rigidity preservation analysis.

## Contributing
(Placeholder for contribution guidelines)

## License
© 2025 QuantUniversity. All Rights Reserved. The purpose of this demonstration is solely for educational use and illustration. Any reproduction of this demonstration requires prior written consent from QuantUniversity.

## Acknowledgments
This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.
