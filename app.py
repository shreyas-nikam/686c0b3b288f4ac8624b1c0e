
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
