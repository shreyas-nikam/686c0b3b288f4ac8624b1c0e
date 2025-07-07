id: 686c0b3b288f4ac8624b1c0e_documentation
summary: Rectified Point Flow: Generic Point Cloud Pose Estimation Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Rectified Point Flow: Generic Point Cloud Pose Estimation Lab

## Introduction & Setup
Duration: 0:05:00

Welcome to the Rectified Point Flow (RPF) Analyzer codelab!

This lab guides you through the codebase of a Streamlit application designed to analyze and visualize the performance of point cloud registration methods, with a focus on Rectified Point Flow (RPF).

**What is Point Cloud Registration?**
Point cloud registration is a fundamental problem in 3D computer vision and robotics. Given two point clouds (sets of 3D points), the goal is to find a rigid transformation (rotation and translation) that aligns them optimally. This is crucial for tasks like 3D reconstruction, object recognition, localization, and mapping.

**Why is this Application Important?**
Evaluating and comparing different registration methods is key to understanding their strengths and weaknesses. This application provides an interactive platform to visualize standard evaluation metrics, helping researchers and developers assess performance quickly and intuitively.

**Concepts Covered:**
*   **Point Cloud Registration Metrics:** Understand key quantitative metrics used to evaluate registration accuracy and robustness (Rotation Error, Translation Error, Recall, RMSE, Overlap Ratio).
*   **Data Visualization with Plotly:** Learn how to use Plotly within Streamlit to create interactive charts for data analysis.
*   **Streamlit Application Structure:** See how a multi-page Streamlit application can be organized using separate modules.
*   **Interactive Data Filtering:** Implement filters to dynamically update visualizations based on user selections.

**Target Audience:**
This codelab is intended for developers and researchers familiar with Python and interested in 3D computer vision, robotics, or data visualization.

**Key Value:**
You will gain insights into the typical evaluation pipeline for point cloud registration methods and how to build an interactive tool to analyze such data using Streamlit and Plotly.

**Application Structure:**

The application is organized into three files:
*   `app.py`: The main entry point, handles navigation and overall layout.
*   `application_pages/metric_comparison.py`: Implements the "Metric Comparison Dashboard" page.
*   `application_pages/rigidity_preservation.py`: Implements the "Rigidity Preservation Analysis" page, including a conceptual 3D visualization.

Let's start by looking at the main application file.

```python
# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Rectified Point Flow: Generic Point Cloud Pose Estimation Lab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Rectified Point Flow: Generic Point Cloud Pose Estimation Lab")
st.divider()
st.markdown("""
### Welcome to the Rectified Point Flow (RPF) Analyzer!

This interactive lab provides a platform to explore and compare different evaluation metrics for pairwise point cloud registration,
highlighting the performance of Rectified Point Flow (RPF) against various baseline methods.
Point cloud registration is a fundamental problem in 3D computer vision and robotics, aiming to find the rigid transformation (rotation and translation) that aligns two partially overlapping point clouds.

**Key Objectives of this Lab:**
*   **Understanding Evaluation Metrics**: Gain a clear understanding of common metrics like Rotation Error (RE), Translation Error (TE), Recall, Root Mean Square Error (RMSE), and Overlap Ratio (OR).
*   **Interactive Visualizations**: See how raw performance data can be transformed into interactive charts, allowing for dynamic exploration.
*   **Data Preprocessing & Exploration**: Observe concepts related to data preparation and analysis in the context of 3D alignment.
*   **Intuitive Interface**: Explore a user-friendly interface that explains the underlying concepts of pose estimation and rigidity preservation in point cloud registration.

**Target Audience:**
This lab is designed for students, researchers, and professionals in computer vision, robotics, and 3D geometry processing.

**Key Value Propositions:**
*   **Interactive Learning**: A dynamic environment to explore complex quantitative data.
*   **Comparative Analysis**: Directly compare Rectified Point Flow with established baseline methods.
*   **Conceptual Clarity**: Simplify the understanding of critical evaluation metrics through visualizations and explanations.
*   **Accessibility**: A web-based, easy-to-use interface, leveraging Streamlit.

Navigate through the sidebar to explore different aspects of the analysis.
""")

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Metric Comparison Dashboard", "Rigidity Preservation Analysis"])

# Dummy data for demonstration purposes as no real data is provided
# In a real application, this data would be loaded from a file or database.
# This data structure is designed to support the specified visualizations.
pairwise_data_df = pd.DataFrame({
    'Dataset': ['TUD-L', 'TUD-L', 'TUD-L', 'TUD-L', 'TUD-L', 'TUD-L', 'TUD-L', 'TUD-L',
                'ModelNet40', 'ModelNet40', 'ModelNet40', 'ModelNet40', 'ModelNet40', 'ModelNet40', 'ModelNet40', 'ModelNet40'],
    'Method': ['RPF (Single)', 'RPF (Joint)', 'DCPNet', 'RPMNet', 'GeoTransformer', 'GARF', 'Diff-RPMNet', 'PointDSC',
               'RPF (Single)', 'RPF (Joint)', 'DCPNet', 'RPMNet', 'GeoTransformer', 'GARF', 'Diff-RPMNet', 'PointDSC'],
    'RE': [0.5, 0.4, 0.8, 0.7, 0.6, 0.9, 1.0, 1.2,
           0.3, 0.2, 0.7, 0.6, 0.5, 0.8, 0.9, 1.1], # Rotation Error (degrees)
    'TE': [0.01, 0.008, 0.02, 0.015, 0.012, 0.025, 0.03, 0.035,
           0.005, 0.004, 0.018, 0.013, 0.01, 0.02, 0.028, 0.032], # Translation Error (cm)
    'Recall@5°': [0.98, 0.99, 0.90, 0.92, 0.95, 0.88, 0.85, 0.80,
                  0.99, 0.995, 0.91, 0.93, 0.96, 0.89, 0.87, 0.82], # Recall at 5 degrees
    'Recall@1cm': [0.97, 0.98, 0.89, 0.91, 0.94, 0.87, 0.84, 0.79,
                   0.98, 0.99, 0.90, 0.92, 0.95, 0.88, 0.86, 0.81], # Recall at 1 cm
    'RMSE': [0.015, 0.012, 0.03, 0.025, 0.02, 0.035, 0.04, 0.045,
             0.01, 0.008, 0.028, 0.022, 0.018, 0.032, 0.038, 0.042], # Root Mean Square Error
    'Overlap_Ratio': [0.85, 0.88, 0.70, 0.75, 0.80, 0.65, 0.60, 0.55,
                      0.90, 0.92, 0.72, 0.78, 0.83, 0.68, 0.63, 0.58] # Overlap Ratio
})

if page == "Metric Comparison Dashboard":
    from application_pages.metric_comparison import run_metric_comparison_page
    run_metric_comparison_page(pairwise_data_df)
elif page == "Rigidity Preservation Analysis":
    from application_pages.rigidity_preservation import run_rigidity_preservation_page
    run_rigidity_preservation_page(pairwise_data_df)

# Your code ends
st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.")
```

## Understanding the Data Structure
Duration: 0:03:00

The core of this application's analysis is a dataset containing the performance metrics of various point cloud registration methods evaluated on different datasets.

In `app.py`, this data is hardcoded into a pandas DataFrame called `pairwise_data_df`.

```python
# Dummy data for demonstration purposes as no real data is provided
# In a real application, this data would be loaded from a file or database.
# This data structure is designed to support the specified visualizations.
pairwise_data_df = pd.DataFrame({
    'Dataset': ['TUD-L', 'TUD-L', 'TUD-L', 'TUD-L', 'TUD-L', 'TUD-L', 'TUD-L', 'TUD-L',
                'ModelNet40', 'ModelNet40', 'ModelNet40', 'ModelNet40', 'ModelNet40', 'ModelNet40', 'ModelNet40', 'ModelNet40'],
    'Method': ['RPF (Single)', 'RPF (Joint)', 'DCPNet', 'RPMNet', 'GeoTransformer', 'GARF', 'Diff-RPMNet', 'PointDSC',
               'RPF (Single)', 'RPF (Joint)', 'DCPNet', 'RPMNet', 'GeoTransformer', 'GARF', 'Diff-RPMNet', 'PointDSC'],
    'RE': [0.5, 0.4, 0.8, 0.7, 0.6, 0.9, 1.0, 1.2,
           0.3, 0.2, 0.7, 0.6, 0.5, 0.8, 0.9, 1.1], # Rotation Error (degrees)
    'TE': [0.01, 0.008, 0.02, 0.015, 0.012, 0.025, 0.03, 0.035,
           0.005, 0.004, 0.018, 0.013, 0.01, 0.02, 0.028, 0.032], # Translation Error (cm)
    'Recall@5°': [0.98, 0.99, 0.90, 0.92, 0.95, 0.88, 0.85, 0.80,
                  0.99, 0.995, 0.91, 0.93, 0.96, 0.89, 0.87, 0.82], # Recall at 5 degrees
    'Recall@1cm': [0.97, 0.98, 0.89, 0.91, 0.94, 0.87, 0.84, 0.79,
                   0.98, 0.99, 0.90, 0.92, 0.95, 0.88, 0.86, 0.81], # Recall at 1 cm
    'RMSE': [0.015, 0.012, 0.03, 0.025, 0.02, 0.035, 0.04, 0.045,
             0.01, 0.008, 0.028, 0.022, 0.018, 0.032, 0.038, 0.042], # Root Mean Square Error
    'Overlap_Ratio': [0.85, 0.88, 0.70, 0.75, 0.80, 0.65, 0.60, 0.55,
                      0.90, 0.92, 0.72, 0.78, 0.83, 0.68, 0.63, 0.58] # Overlap Ratio
})
```

This DataFrame has the following columns:
*   `Dataset`: The name of the dataset used for evaluation (e.g., 'TUD-L', 'ModelNet40').
*   `Method`: The name of the point cloud registration method being evaluated (e.g., 'RPF (Single)', 'DCPNet').
*   `RE`: Rotation Error, typically in degrees. Lower is better.
*   `TE`: Translation Error, typically in the unit of the point cloud (here stated as cm). Lower is better.
*   `Recall@5°`: The percentage of registration instances where RE is <= 5 degrees. Higher is better.
*   `Recall@1cm`: The percentage of registration instances where TE is <= 1 cm. Higher is better.
*   `RMSE`: Root Mean Square Error. Lower is better.
*   `Overlap_Ratio`: Measures the correspondence quality or point overlap after transformation. Higher is better.

<aside class="negative">
It's important to note that this data is **dummy data** generated for demonstration purposes. In a real-world application, this data would be loaded from actual evaluation results, typically stored in files (like CSV, JSON, etc.) or a database. The values presented here are illustrative and do not necessarily reflect the true performance of the methods listed.
</aside>

The rest of the application uses this DataFrame to generate visualizations.

## Navigating the Application
Duration: 0:02:00

The `app.py` file uses Streamlit's sidebar to create a simple navigation menu.

```python
# app.py (snippet)
page = st.sidebar.selectbox(label="Navigation", options=["Metric Comparison Dashboard", "Rigidity Preservation Analysis"])

if page == "Metric Comparison Dashboard":
    from application_pages.metric_comparison import run_metric_comparison_page
    run_metric_comparison_page(pairwise_data_df)
elif page == "Rigidity Preservation Analysis":
    from application_pages.rigidity_preservation import run_rigidity_preservation_page
    run_rigidity_preservation_page(pairwise_data_df)
```

*   `st.sidebar.selectbox` creates a dropdown menu in the sidebar with the specified options.
*   The variable `page` stores the currently selected option.
*   An `if/elif` block checks the value of `page` and imports and calls the corresponding page function from the `application_pages` directory.
*   Crucially, the `pairwise_data_df` is passed to each page function, making the data available for filtering and visualization on those pages.

This structure keeps the main `app.py` clean and delegates the logic for each specific view (or "page") to separate modules, which is a good practice for larger Streamlit applications.

## Exploring Metric Comparison
Duration: 0:08:00

The "Metric Comparison Dashboard" page is handled by the `application_pages/metric_comparison.py` file. This page focuses on standard pose estimation errors (Rotation and Translation Error) and Recall metrics, which indicate the success rate of registration.

Here's the code for this page:

```python
# application_pages/metric_comparison.py
import streamlit as st
import plotly.express as px
import pandas as pd

def run_metric_comparison_page(df):
    st.header("Metric Comparison Dashboard")
    st.markdown("""
    This dashboard allows you to compare the performance of different point cloud registration methods
    across various datasets and metrics. You can select the datasets and methods you are interested in,
    and the charts will update in real-time.
    """)

    st.subheader("Filter Options")
    col1, col2 = st.columns(2)

    with col1:
        selected_datasets = st.multiselect(
            "Select Dataset(s)",
            options=df['Dataset'].unique().tolist(),
            default=df['Dataset'].unique().tolist()
        )
    with col2:
        selected_methods = st.multiselect(
            "Select Method(s)",
            options=df['Method'].unique().tolist(),
            default=['RPF (Single)', 'RPF (Joint)', 'DCPNet', 'RPMNet'] # Default selection
        )

    if not selected_datasets or not selected_methods:
        st.warning("Please select at least one dataset and one method to display the charts.")
        return

    filtered_df = df[df['Dataset'].isin(selected_datasets) & df['Method'].isin(selected_methods)]

    if filtered_df.empty:
        st.warning("No data available for the selected combination of datasets and methods.")
        return

    st.subheader("Select Metrics to Display")
    metrics_to_display = st.multiselect(
        "Choose metrics to visualize (select one or more)",
        options=['RE', 'TE', 'Recall@5°', 'Recall@1cm'],
        default=['RE', 'TE']
    )

    if not metrics_to_display:
        st.info("Please select at least one metric to display its chart.")
        return

    st.divider()
    st.subheader("Performance Metrics Visualizations")

    for metric in metrics_to_display:
        st.markdown(f"#### {metric} Performance")
        if metric == 'RE':
            st.markdown(r"**Rotation Error (RE):** Angular difference in degrees between predicted and ground-truth rotations. A lower RE indicates higher accuracy. Formula: $RE =  rccos\left(rac{	ext{trace}(R_{pred}^T R_{gt}) - 1}{2}ight) 	imes rac{180}{\pi}$")
        elif metric == 'TE':
            st.markdown(r"**Translation Error (TE):** Euclidean distance in centimeters between predicted and ground-truth translations. A lower TE indicates higher accuracy. Formula: $TE = \| t_{pred} - t_{gt} \|_2$")
        elif metric == 'Recall@5°':
            st.markdown("**Recall@5°:** The percentage of successful registrations where the Rotation Error (RE) is below or equal to 5 degrees. A higher recall indicates better robustness.")
        elif metric == 'Recall@1cm':
            st.markdown("**Recall@1cm:** The percentage of successful registrations where the Translation Error (TE) is below or equal to 1 cm. A higher recall indicates better robustness.")

        fig = px.bar(
            filtered_df,
            x='Method',
            y=metric,
            color='Dataset',
            barmode='group',
            title=f'{metric} by Method and Dataset',
            labels={'value': metric, 'Method': 'Registration Method', 'Dataset': 'Dataset'},
            hover_data={'Method': True, 'Dataset': True, metric: ':.4f'}
        )
        fig.update_layout(xaxis_title="Method", yaxis_title=metric)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(f"") # Spacer for better separation

    st.markdown("""
    **Interpretation of Results:**
    *   **Lower is Better for Errors:** For metrics like Rotation Error (RE) and Translation Error (TE), lower values indicate more accurate registration.
    *   **Higher is Better for Recall:** For Recall metrics (e.g., Recall@5°, Recall@1cm), higher percentages indicate a greater proportion of successful registrations within the defined error thresholds.
    *   Observe how Rectified Point Flow (RPF) methods compare to other baselines across different datasets. Typically, RPF aims for "state-of-the-art performance" [3] in both accuracy and robustness.
    """)
    st.markdown("")
    st.markdown("""
    **References:**
    *   [3] (Placeholder for actual reference to RPF paper/section discussing state-of-the-art performance)
    *   Table 3 (Placeholder for reference to a specific table in the source document)
    """)
```

**Functionality Breakdown:**

1.  **Filters:**
    *   `st.multiselect` widgets allow the user to choose which 'Dataset' and 'Method' entries from the DataFrame should be included in the visualization.
    *   `df['Dataset'].unique().tolist()` extracts the unique dataset names to populate the options. Same for 'Method'.
    *   The `default` argument sets the initial selection (all datasets, a specific subset of methods).
    *   The DataFrame `df` is filtered based on these selections: `filtered_df = df[df['Dataset'].isin(selected_datasets) & df['Method'].isin(selected_methods)]`.

2.  **Metric Selection:**
    *   Another `st.multiselect` allows the user to choose which of the pose estimation metrics ('RE', 'TE', 'Recall@5°', 'Recall@1cm') they want to visualize.

3.  **Metric Definitions and Formulas:**
    *   Inside the loop that iterates through the `metrics_to_display`, `st.markdown` is used to provide a definition and, where applicable, a mathematical formula for the current metric.
    *   Mathematical formulas are correctly formatted using LaTeX syntax within `$...$` (inline) or `$$...$$` (display). The `r""` prefix is used for raw strings to handle backslashes in LaTeX formulas.

4.  **Visualization:**
    *   `plotly.express.bar` is used to create bar charts for each selected metric.
    *   `x='Method'` sets the methods as the x-axis categories.
    *   `y=metric` sets the value of the current metric as the y-axis value.
    *   `color='Dataset'` creates grouped bars, where different datasets for the same method are colored differently.
    *   `barmode='group'` ensures the bars for different datasets are grouped side-by-side for each method.
    *   `title`, `labels`, and `hover_data` are configured for clarity and interactivity.
    *   `st.plotly_chart(fig, use_container_width=True)` renders the interactive Plotly chart in the Streamlit app, making it fill the container width.

This page effectively demonstrates how to use Streamlit widgets to filter data and then use Plotly to create dynamic, comparative bar charts for quantitative evaluation metrics.

## Analyzing Rigidity Preservation
Duration: 0:10:00

The "Rigidity Preservation Analysis" page is handled by `application_pages/rigidity_preservation.py`. This page focuses on metrics that indicate how well the shape and structure of the point cloud are maintained after transformation, specifically RMSE and Overlap Ratio, and includes a conceptual 3D visualization.

Here's the code for this page:

```python
# application_pages/rigidity_preservation.py
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def run_rigidity_preservation_page(df):
    st.header("Rigidity Preservation Analysis")
    st.markdown("""
    This section focuses on evaluating how well different registration methods preserve the
    rigidity of the point clouds during transformation. Key metrics for this analysis include
    Root Mean Square Error (RMSE) and Overlap Ratio (OR).
    """)

    st.subheader("Filter Options")
    col1, col2 = st.columns(2)

    with col1:
        selected_datasets = st.multiselect(
            "Select Dataset(s)",
            options=df['Dataset'].unique().tolist(),
            default=df['Dataset'].unique().tolist()
        )
    with col2:
        selected_methods = st.multiselect(
            "Select Method(s)",
            options=df['Method'].unique().tolist(),
            default=['RPF (Single)', 'RPF (Joint)', 'DCPNet', 'RPMNet'] # Default selection
        )

    if not selected_datasets or not selected_methods:
        st.warning("Please select at least one dataset and one method to display the charts.")
        return

    filtered_df = df[df['Dataset'].isin(selected_datasets) & df['Method'].isin(selected_methods)]

    if filtered_df.empty:
        st.warning("No data available for the selected combination of datasets and methods.")
        return

    st.divider()
    st.subheader("Rigidity Preservation Metrics")

    st.markdown("#### Root Mean Square Error (RMSE)")
    st.markdown("""
    The Root Mean Square Error (RMSE) quantifies the average magnitude of the errors between
    predicted and ground-truth point positions after transformation. It is a critical metric
    for assessing alignment accuracy and rigidity preservation. A lower RMSE indicates a more accurate
    and rigid transformation.
    """)
    st.latex(r"\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \| \mathbf{p}_{i,transformed} - \mathbf{p}_{i,groundtruth} \|^2}")
    st.markdown("""
    Where:
    *   $N$ is the number of corresponding points.
    *   $\| \mathbf{p}_{i,transformed} - \mathbf{p}_{i,groundtruth} \|^2$ is the squared Euclidean distance between the $i$-th transformed point and its corresponding ground truth point.
    """)
    st.markdown("""
    *Note: The formula provided in the specifications was for a different context or mis-transcribed.
    The standard RMSE for point cloud registration refers to the error between transformed points and their ground truth positions,
    often after applying the estimated transformation.*
    """)


    fig_rmse = px.bar(
        filtered_df,
        x='Method',
        y='RMSE',
        color='Dataset',
        barmode='group',
        title='Root Mean Square Error (RMSE) by Method and Dataset',
        labels={'RMSE': 'RMSE Value', 'Method': 'Registration Method', 'Dataset': 'Dataset'},
        hover_data={'Method': True, 'Dataset': True, 'RMSE': ':.4f'}
    )
    fig_rmse.update_layout(xaxis_title="Method", yaxis_title="RMSE")
    st.plotly_chart(fig_rmse, use_container_width=True)


    st.markdown("#### Overlap Ratio (OR)")
    st.markdown("""
    The Overlap Ratio (OR) measures the proportion of points in one point cloud that overlap
    with points in another after registration, given a certain distance threshold (e.g., $\tau$).
    A higher overlap ratio indicates better coverage and alignment of the point clouds.
    """)

    fig_or = px.bar(
        filtered_df,
        x='Method',
        y='Overlap_Ratio',
        color='Dataset',
        barmode='group',
        title='Overlap Ratio by Method and Dataset',
        labels={'Overlap_Ratio': 'Overlap Ratio', 'Method': 'Registration Method', 'Dataset': 'Dataset'},
        hover_data={'Method': True, 'Dataset': True, 'Overlap_Ratio': ':.4f'}
    )
    fig_or.update_layout(xaxis_title="Method", yaxis_title="Overlap Ratio")
    st.plotly_chart(fig_or, use_container_width=True)

    st.subheader("Conceptual 3D Visualization of Point Clouds")
    st.markdown("""
    This section provides a conceptual visualization to help understand point cloud alignment.
    In a real-world scenario, you would load actual 3D point cloud data and visualize their
    transformation. Here, we simulate simple point clouds to illustrate the concept.
    """)

    # Simulate original and transformed point clouds for a conceptual visualization
    np.random.seed(42)
    num_points = 100

    # Original point cloud (a simple cube)
    original_points = np.random.rand(num_points, 3) * 10
    original_points_df = pd.DataFrame(original_points, columns=['x', 'y', 'z'])
    original_points_df['Type'] = 'Original'

    # Simulate a "ground truth" transformation (simple rotation and translation)
    angle = np.pi / 6 # 30 degrees
    rotation_matrix_gt = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    translation_gt = np.array([1, 2, 3])

    # Simulate transformed point cloud (ground truth aligned)
    ground_truth_transformed_points = (rotation_matrix_gt @ original_points.T).T + translation_gt
    ground_truth_transformed_points_df = pd.DataFrame(ground_truth_transformed_points, columns=['x', 'y', 'z'])
    ground_truth_transformed_points_df['Type'] = 'Ground Truth Transformed'

    # Simulate a "predicted" transformation (slightly different from ground truth)
    angle_pred = np.pi / 5.5 # Slightly different angle
    rotation_matrix_pred = np.array([
        [np.cos(angle_pred), -np.sin(angle_pred), 0],
        [np.sin(angle_pred), np.cos(angle_pred), 0],
        [0, 0, 1]
    ])
    translation_pred = np.array([1.1, 1.9, 3.2])

    predicted_transformed_points = (rotation_matrix_pred @ original_points.T).T + translation_pred
    predicted_transformed_points_df = pd.DataFrame(predicted_transformed_points, columns=['x', 'y', 'z'])
    predicted_transformed_points_df['Type'] = 'Predicted Transformed'

    # Combine for Plotly
    combined_points_df = pd.concat([original_points_df, ground_truth_transformed_points_df, predicted_transformed_points_df])

    fig_3d = go.Figure(data=[
        go.Scatter3d(
            x=combined_points_df[combined_points_df['Type'] == 'Original']['x'],
            y=combined_points_df[combined_points_df['Type'] == 'Original']['y'],
            z=combined_points_df[combined_points_df['Type'] == 'Original']['z'],
            mode='markers',
            marker=dict(size=3, color='blue'),
            name='Original Point Cloud'
        ),
        go.Scatter3d(
            x=combined_points_df[combined_points_df['Type'] == 'Ground Truth Transformed']['x'],
            y=combined_points_df[combined_points_df['Type'] == 'Ground Truth Transformed']['y'],
            z=combined_points_df[combined_points_df['Type'] == 'Ground Truth Transformed']['z'],
            mode='markers',
            marker=dict(size=3, color='green'),
            name='Ground Truth Aligned'
        ),
        go.Scatter3d(
            x=combined_points_df[combined_points_df['Type'] == 'Predicted Transformed']['x'],
            y=combined_points_df[combined_points_df['Type'] == 'Predicted Transformed']['y'],
            z=combined_points_df[combined_points_df['Type'] == 'Predicted Transformed']['z'],
            mode='markers',
            marker=dict(size=3, color='red'),
            name='Predicted Aligned'
        )
    ])

    fig_3d.update_layout(
        title='Conceptual 3D Point Cloud Alignment',
        scene=dict(
            xaxis_title='X-axis',
            yaxis_title='Y-axis',
            zaxis_title='Z-axis',
            aspectmode='cube' # Ensures equal scaling for axes
        ),
        legend=dict(x=0, y=1, bgcolor='rgba(255,255,255,0.7)', bordercolor='Black', borderwidth=1)
    )
    st.plotly_chart(fig_3d, use_container_width=True)

    st.markdown("""
    **Interpretation of Rigidity Preservation:**
    *   **Lower RMSE is Better**: A smaller RMSE value indicates that the transformed point cloud
        is closer to the ground truth, implying higher accuracy and better preservation of the
        original shape and distances within the cloud.
    *   **Higher Overlap Ratio is Better**: A higher OR signifies that a larger portion of the
        point clouds are successfully aligned and correspond to each other, which is crucial
        for tasks like 3D reconstruction and scene understanding.

    Rectified Point Flow (RPF) aims to achieve excellent rigidity preservation, minimizing
    deformation during registration, which is reflected in its competitive RMSE and OR scores [2].
    """)
    st.markdown("")
    st.markdown("""
    **References:**
    *   [2] (Placeholder for actual reference to RPF paper/section discussing rigidity preservation)
    *   Table 6 (Placeholder for reference to a specific table in the source document)
    """)
```

**Functionality Breakdown:**

1.  **Filters:**
    *   Similar to the metric comparison page, `st.multiselect` widgets are used to filter the data by 'Dataset' and 'Method'. The filtering logic is identical.

2.  **Metric Definitions and Formulas:**
    *   This page specifically details RMSE and Overlap Ratio.
    *   **RMSE:** The definition explains it as the average error in point positions after transformation. The standard formula $RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \| \mathbf{p}_{i,transformed} - \mathbf{p}_{i,groundtruth} \|^2}$ is provided using `st.latex`. A note clarifies this standard interpretation for point cloud alignment.
    *   **Overlap Ratio:** The definition explains it as the proportion of points that successfully overlap within a threshold.

3.  **Visualizations:**
    *   `plotly.express.bar` is again used to generate bar charts for 'RMSE' and 'Overlap_Ratio', showing values per Method, colored by Dataset, with grouped bars.

4.  **Conceptual 3D Visualization:**
    *   This is a unique part of this page, aiming to *conceptually* show what point cloud alignment means.
    *   It uses `numpy` to generate simple random points representing an "Original Point Cloud".
    *   It simulates a "Ground Truth" rigid transformation (rotation and translation) and applies it to the original points.
    *   It simulates a "Predicted" rigid transformation (slightly different) and applies it.
    *   These three sets of points ('Original', 'Ground Truth Transformed', 'Predicted Transformed') are combined into a single DataFrame.
    *   `plotly.graph_objects.Scatter3d` is used to create a 3D scatter plot. Each set of points is added as a separate trace with different colors and names.
    *   `fig_3d.update_layout` sets the title, axis labels, and `aspectmode='cube'` to ensure proper 3D scaling, preventing distortion.
    *   `st.plotly_chart` renders the interactive 3D plot.

<aside class="positive">
This conceptual visualization section is a great example of how to add illustrative content in a data analysis application. Even without real 3D data loading, simulating simple data helps users grasp the core concept of alignment and the difference between a perfect (ground truth) and an imperfect (predicted) transformation.
</aside>

This page effectively uses filters and bar charts for quantitative analysis (RMSE, OR) and complements it with a conceptual 3D visualization to build intuition about the problem being solved.

## Running and Interacting
Duration: 0:02:00

To run this Streamlit application locally, you need to have Python installed, along with the required libraries: `streamlit`, `pandas`, `plotly`, and `numpy`.

1.  **Save the code:** Save the provided code snippets into the correct file structure:
    *   `app.py`
    *   Create a directory `application_pages/`
    *   Inside `application_pages/`, save `metric_comparison.py` and `rigidity_preservation.py`.
    *   You can optionally create an empty `application_pages/__init__.py` file, although it's not strictly necessary for this simple structure with modern Python.

2.  **Install dependencies:** Open your terminal or command prompt and navigate to the directory containing `app.py`. Run:
    ```console
    pip install streamlit pandas plotly numpy
    ```

3.  **Run the application:** In the same terminal, run the Streamlit application:
    ```console
    streamlit run app.py
    ```

    This will open the application in your web browser (usually at `http://localhost:8501`).

**Interacting with the Application:**

*   Use the `Navigation` selectbox in the sidebar to switch between the "Metric Comparison Dashboard" and "Rigidity Preservation Analysis" pages.
*   On each page, use the `Select Dataset(s)` and `Select Method(s)` multiselect widgets to filter the data displayed in the charts.
*   On the "Metric Comparison Dashboard", use the `Choose metrics to visualize` multiselect to show or hide specific metric charts.
*   Hover over the bars in the charts to see the exact metric values (as configured by `hover_data` in `plotly.express`).
*   Interact with the 3D plot on the "Rigidity Preservation Analysis" page: click and drag to rotate, scroll to zoom.

Experiment with different selections to see how the performance metrics vary across datasets and methods.

## Conclusion
Duration: 0:01:00

This codelab has walked you through a Streamlit application designed to analyze point cloud registration performance. You've seen:

*   How to structure a multi-page Streamlit app.
*   How to load and filter data using pandas based on user input from Streamlit widgets.
*   How to use Plotly Express to create interactive bar charts for quantitative data comparison.
*   How to use Plotly Graph Objects to create conceptual 3D visualizations.
*   The common metrics used to evaluate point cloud registration accuracy and rigidity preservation.

While this application uses dummy data, the structure and techniques demonstrated are applicable to analyzing real evaluation results from your own point cloud registration experiments.

Feel free to modify the code, integrate your own data, or add new visualization types to further explore the concepts of 3D point cloud analysis!
