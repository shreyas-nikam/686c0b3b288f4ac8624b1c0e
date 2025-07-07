
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
    st.markdown("---")
    st.markdown("""
    **References:**
    *   [2] (Placeholder for actual reference to RPF paper/section discussing rigidity preservation)
    *   Table 6 (Placeholder for reference to a specific table in the source document)
    """)
