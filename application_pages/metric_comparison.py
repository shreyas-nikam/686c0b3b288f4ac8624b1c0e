
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
            st.markdown(r"**Rotation Error (RE):** Angular difference in degrees between predicted and ground-truth rotations. A lower RE indicates higher accuracy. Formula: $RE = rccos\left(rac{	ext{trace}(R_{pred}^T R_{gt}) - 1}{2}ight) 	imes rac{180}{\pi}$")
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
    st.markdown("---")
    st.markdown("""
    **References:**
    *   [3] (Placeholder for actual reference to RPF paper/section discussing state-of-the-art performance)
    *   Table 3 (Placeholder for reference to a specific table in the source document)
    """)
