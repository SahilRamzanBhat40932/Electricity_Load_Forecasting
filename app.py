# ============================================================
# Electricity Load Forecasting Dashboard
# Developed by Sahil Ramzan Bhat
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# ============================================================
# Load Trained Model
# ============================================================

model = joblib.load("model.pkl")

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Electricity Load Forecasting",
    page_icon="⚡",
    layout="wide"
)

# ============================================================
# Premium Dark Theme
# ============================================================
st.markdown("""
<style>

/* ------------------------------------------------ */
/* Hide Streamlit Default Elements */
/* ------------------------------------------------ */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* ------------------------------------------------ */
/* Main Background */
/* ------------------------------------------------ */

.stApp{
    background:
    radial-gradient(circle at top left,#0F766E 0%,transparent 35%),
    radial-gradient(circle at bottom right,#7C3AED 0%,transparent 35%),
    #0F172A;
}

/* ------------------------------------------------ */
/* ALL TEXT */
/* ------------------------------------------------ */

html,
body,
p,
span,
label,
div,
h1,
h2,
h3,
h4,
h5,
h6{
    color:white !important;
}

/* ------------------------------------------------ */
/* Sidebar */
/* ------------------------------------------------ */

section[data-testid="stSidebar"]{
    background:#111827 !important;
    border-right:1px solid #374151;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* ------------------------------------------------ */
/* Metric Cards */
/* ------------------------------------------------ */

[data-testid="metric-container"]{
    background:#1E293B !important;
    border:1px solid #3B82F6 !important;
    border-radius:15px;
    padding:18px;
}

[data-testid="metric-container"] *{
    color:white !important;
}

/* ------------------------------------------------ */
/* Number Input */
/* ------------------------------------------------ */

.stNumberInput input{
    background:#111827 !important;
    color:white !important;
}

/* ------------------------------------------------ */
/* Selectbox */
/* ------------------------------------------------ */

div[data-baseweb="select"] *{
    background:#233423 !important;
    color:white !important;
}

div[data-baseweb="select"] span{
    color:white !important;
}

div[role="listbox"]{
    background:#111827 !important;
}

div[role="option"]{
    background:#111827 !important;
    color:white !important;
}

div[role="option"]:hover{
    background:#2563EB !important;
    color:white !important;
}

/* ------------------------------------------------ */
/* Download Button */
/* ------------------------------------------------ */

[data-testid="stDownloadButton"] > button{

    width:100%;
    height:55px;

    border:none;
    border-radius:15px;

    background:linear-gradient(90deg,#10B981,#059669) !important;

    color:red !important;
    font-size:18px;
    font-weight:bold;

}

[data-testid="stDownloadButton"] > button:hover{

    background:linear-gradient(90deg,#059669,#047857) !important;

    transform:scale(1.02);

}

/* ------------------------------------------------ */
/* Dataframe */
/* ------------------------------------------------ */

[data-testid="stDataFrame"] *{

    color:white !important;

}

/* ------------------------------------------------ */
/* Tabs */
/* ------------------------------------------------ */

button[data-baseweb="tab"]{

    color:white !important;

}

/* ------------------------------------------------ */
/* Expander */
/* ------------------------------------------------ */

details{

    background:#1E293B;
    border-radius:10px;

}

/* ------------------------------------------------ */
/* Success / Info */
/* ------------------------------------------------ */

[data-testid="stAlert"]{

    color:white !important;

}

/* ------------------------------------------------ */
/* Markdown */
/* ------------------------------------------------ */

.stMarkdown{

    color:white !important;

}

</style>
""", unsafe_allow_html=True)

# ============================================================
# Hero Banner
# ============================================================

st.markdown("""

<div style='
background:linear-gradient(90deg,#2563EB,#7C3AED);
padding:30px;
border-radius:20px;
text-align:center;
'>

<h1 style='color:white;'>

⚡ Electricity Load Forecasting

</h1>

<h3 style='color:white;'>

AI Powered Time Series Forecasting Dashboard

</h3>

</div>

""", unsafe_allow_html=True)

st.markdown("")

# ============================================================
# Sidebar
# ============================================================

st.sidebar.title("📊 Dashboard")

st.sidebar.markdown("---")

st.sidebar.success("Model Loaded Successfully")

st.sidebar.metric(
    "Best Model",
    "Gradient Boosting"
)

st.sidebar.metric(
    "R² Score",
    "94.79%"
)

st.sidebar.metric(
    "Forecast",
    "10 Minutes"
)

st.sidebar.metric(
    "Developer",
    "Sahil Ramzan Bhat"
)

st.sidebar.markdown("---")

st.sidebar.info("""

This application forecasts electricity load
using Gradient Boosting Regression trained
on historical electricity consumption.

""")

# ============================================================
# Dashboard Cards
# ============================================================

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "🤖 Model",
        "Gradient Boosting"
    )

with c2:

    st.metric(
        "📊 Type",
        "Regression"
    )

with c3:

    st.metric(
        "⏱ Horizon",
        "10 Min"
    )

with c4:

    st.metric(
        "🎯 Accuracy",
        "94.79%"
    )

st.markdown("---")


# ============================================================
# Forecast Input Form
# ============================================================

st.header("📥 Enter Forecast Details")

left, right = st.columns(2)

with left:

    year = st.number_input(
        "Year",
        min_value=2022,
        max_value=2035,
        value=2024
    )

    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=5
    )

    day = st.number_input(
        "Day",
        min_value=1,
        max_value=31,
        value=24
    )

    hour = st.number_input(
        "Hour",
        min_value=0,
        max_value=23,
        value=10
    )

    minute = st.selectbox(
        "Minute",
        [0,10,20,30,40,50]
    )

with right:
    
    lag1 = st.number_input(
        "Previous Load (10 min ago)",
        min_value=0.0,
        max_value=2340.0,
        value=90.0,
        step=0.1
    )

    lag2 = st.number_input(
        "Previous Load (20 min ago)",
        min_value=0.0,
        max_value=2340.0,
        value=88.0,
        step=0.1
    )
    
    lag3 = st.number_input(
        "Previous Load (30 min ago)",
        min_value=0.0,
        max_value=2340.0,
        value=86.0,
        step=0.1
    )

st.markdown("---")

# ============================================================
# Automatic Feature Engineering
# ============================================================

date = pd.Timestamp(
    year=int(year),
    month=int(month),
    day=int(day)
)

day_of_week = date.dayofweek

quarter = ((month - 1)//3)+1

weekend = 1 if day_of_week >= 5 else 0

rolling_mean = np.mean(
    [lag1, lag2, lag3]
)

rolling_std = np.std(
    [lag1, lag2, lag3]
)

# ============================================================
# Forecast Button
# ============================================================

forecast = st.button(
    "⚡ Forecast Electricity Load"
)

# ============================================================
# Prediction
# ============================================================

if forecast:

    sample = [[

        year,
        month,
        day,
        hour,
        minute,
        day_of_week,
        quarter,
        weekend,
        lag1,
        lag2,
        lag3,
        rolling_mean,
        rolling_std

    ]]

    prediction = model.predict(sample)

    predicted_load = prediction[0]

    st.markdown("---")

    st.markdown(
    f"""
    <div style="



    <h2 style="color:white;">

    ⚡ Forecasted Electricity Load

    </h2>

    <h1 style="font-size:60px;color:white;">

    {predicted_load:.2f}

    </h1>

    <h3 style="color:white;">

    Mega Watts (MW)

    </h3>

    </div>

    """,
    unsafe_allow_html=True
    )

    st.markdown("")

    # ========================================================
    # Prediction Information
    # ========================================================

    st.subheader("📋 Prediction Details")

    c1,c2 = st.columns(2)

    with c1:

        st.info(f"""

Date : {day}/{month}/{year}

Time : {hour}:{minute:02d}

Forecast Horizon : 10 Minutes

""")

    with c2:

        st.info(f"""

Previous Load 1 : {lag1:.2f}

Previous Load 2 : {lag2:.2f}

Previous Load 3 : {lag3:.2f}

""")
        


    # ============================================================
    # Feature Statistics
    # ============================================================

    st.markdown("---")

    st.subheader("📊 Feature Statistics")

    s1, s2, s3 = st.columns(3)

    with s1:
        st.metric(
            "Rolling Mean",
            f"{rolling_mean:.2f}"
        )

    with s2:
        st.metric(
            "Rolling Std",
            f"{rolling_std:.2f}"
        )

    with s3:
        st.metric(
            "Day Of Week",
            day_of_week
        )

    # ============================================================
    # Electricity Load Trend
    # ============================================================

    st.markdown("---")

    st.subheader("📈 Electricity Load Trend")

    trend_values = [
        lag3,
        lag2,
        lag1,
        predicted_load
    ]

    trend_labels = [
        "30 min Ago",
        "20 min Ago",
        "10 min Ago",
        "Forecast"
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=trend_labels,
            y=trend_values,
            mode="lines+markers",
            line=dict(
                width=4,
                color="#60A5FA"
            ),
            marker=dict(
                size=12,
                color="#2563EB"
            )
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        title="Electricity Load Forecast Trend",
        xaxis_title="Time",
        yaxis_title="Electricity Load (MW)",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ============================================================
    # Forecast Summary
    # ============================================================

    st.markdown("---")

    st.subheader("📄 Forecast Summary")

    st.success(f"""
Predicted Electricity Load : **{predicted_load:.2f} MW**

The prediction is generated using:

- Gradient Boosting Regressor
- Time Series Forecasting
- Lag Features
- Rolling Statistics
- Date & Time Features

Forecast Horizon:
**Next 10 Minutes**
""")

    # ============================================================
    # About Model
    # ============================================================

    with st.expander("ℹ About This Model"):

        st.write("""

### Model

Gradient Boosting Regressor

### Dataset

Electricity Load Time Series Dataset

### Features Used

- Year
- Month
- Day
- Hour
- Minute
- Day Of Week
- Quarter
- Weekend
- Lag 1
- Lag 2
- Lag 3
- Rolling Mean
- Rolling Standard Deviation

### Model Performance

- MAE : 1.5084
- RMSE : 3.3842
- R² Score : 0.9479

This model forecasts electricity demand for the next
10-minute interval using historical electricity load
patterns and engineered time-series features.

""")

    # ============================================================
    # Download Prediction
    # ============================================================

    prediction_df = pd.DataFrame({
        "Year":[year],
        "Month":[month],
        "Day":[day],
        "Hour":[hour],
        "Minute":[minute],
        "Forecast Load (MW)":[round(predicted_load,2)]
    })

    csv = prediction_df.to_csv(index=False)

    st.download_button(
        "📥 Download Prediction (CSV)",
        csv,
        file_name="forecast.csv",
        mime="text/csv"
    )


#============================================================
# Select city for Forecasting
#============================================================

city = st.selectbox(
    "Select City",
    [
        "Laayoune",
        "Boujdour",
        "Foum Eloued",
        "Marrakech"
    ]
)


# ============================================================
# Footer
# ============================================================

st.markdown("---")

st.markdown("""

<div style="text-align:center;color:gray;">

<h3>⚡ Electricity Load Forecasting Dashboard</h3>

Developed by <b>Sahil Ramzan Bhat</b>

Machine Learning • Time Series Forecasting • Streamlit

</div>

""", unsafe_allow_html=True)
