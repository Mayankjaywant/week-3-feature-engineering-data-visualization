import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sample_digital_services.csv")

# Feature engineering
df["resolution_rate_pct"] = (
    df["resolved_requests"] / df["requests"].clip(lower=1)
) * 100

df["requests_per_staff"] = (
    df["requests"] / df["staff_count"].clip(lower=1)
)

df["service_efficiency_score"] = (
    df["resolution_rate_pct"]
    * df["citizen_satisfaction"]
    * df["digital_adoption_pct"]
) / (df["avg_processing_days"] * 100)

# Keep values readable
df["resolution_rate_pct"] = df["resolution_rate_pct"].round(2)
df["requests_per_staff"] = df["requests_per_staff"].round(2)
df["service_efficiency_score"] = df["service_efficiency_score"].round(2)

# 1. Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["avg_processing_days"], bins=10)
plt.title("Distribution of Average Processing Days")
plt.xlabel("Average Processing Days")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("visualizations/processing_days_distribution.png", dpi=160)
plt.close()

# 2. Relationship
plt.figure(figsize=(8, 5))
plt.scatter(df["digital_adoption_pct"], df["citizen_satisfaction"], alpha=0.75)
plt.title("Digital Adoption vs Citizen Satisfaction")
plt.xlabel("Digital Adoption (%)")
plt.ylabel("Citizen Satisfaction (1–5)")
plt.tight_layout()
plt.savefig("visualizations/digital_adoption_vs_satisfaction.png", dpi=160)
plt.close()

# 3. Service comparison
summary = (
    df.groupby("service")["resolution_rate_pct"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(9, 5))
plt.barh(summary.index, summary.values)
plt.title("Average Resolution Rate by Digital Service")
plt.xlabel("Average Resolution Rate (%)")
plt.ylabel("Service")
plt.tight_layout()
plt.savefig("visualizations/resolution_rate_by_service.png", dpi=160)
plt.close()

# Save engineered data
df.to_csv("engineered_digital_services.csv", index=False)
print("Feature engineering and visualizations completed successfully.")
