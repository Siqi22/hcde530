import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("clean_yrbs_2023.csv")

# Helper function
def outcome_rate_chart(data, group_col, outcome_cols, group_labels, title, filename):
    plot_data = []

    for outcome in outcome_cols:
        grouped = (
            data[[group_col, outcome]]
            .dropna()
            .groupby(group_col)[outcome]
            .mean()
            .reset_index()
        )
        grouped["percent"] = grouped[outcome] * 100
        grouped["group"] = grouped[group_col].map(group_labels)
        grouped["outcome"] = outcome

        plot_data.append(grouped[["group", "outcome", "percent"]])

    plot_df = pd.concat(plot_data)

    outcome_labels = {
        "NotGoodMentalHealth": "Poor mental health",
        "Hopelessness": "Sadness / hopelessness"
    }

    plot_df["outcome"] = plot_df["outcome"].map(outcome_labels)

    fig = px.bar(
        plot_df,
        x="group",
        y="percent",
        color="outcome",
        barmode="group",
        text=plot_df["percent"].round(1),
        title=title,
        labels={
            "group": "",
            "percent": "Percent of students (%)",
            "outcome": "Mental health outcome"
        }
    )

    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    fig.update_layout(yaxis_range=[0, max(plot_df["percent"]) + 10])

    fig.show()
    fig.write_image(filename)


# Chart 1: Social media use and mental health
outcome_rate_chart(
    df,
    group_col="SocialMedia",
    outcome_cols=["NotGoodMentalHealth", "Hopelessness"],
    group_labels={0: "Does not use social media", 1: "Uses social media"},
    title="Mental Health Outcomes by Social Media Use",
    filename="chart1_social_media_mental_health.png"
)


# Chart 2: Cyberbullying and mental health
outcome_rate_chart(
    df,
    group_col="CyberBullying",
    outcome_cols=["NotGoodMentalHealth", "Hopelessness"],
    group_labels={0: "Not cyberbullied", 1: "Cyberbullied"},
    title="Mental Health Outcomes by Cyberbullying Experience",
    filename="chart2_cyberbullying_mental_health.png"
)


# Chart 3: Sleep and mental health
outcome_rate_chart(
    df,
    group_col="EightOrMoreHoursSleep",
    outcome_cols=["NotGoodMentalHealth", "Hopelessness"],
    group_labels={0: "Less than 8 hours sleep", 1: "8+ hours sleep"},
    title="Mental Health Outcomes by Sleep Duration",
    filename="chart3_sleep_mental_health.png"
)