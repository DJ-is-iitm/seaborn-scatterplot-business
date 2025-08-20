import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic marketing campaign data
np.random.seed(42)
n = 150

data = pd.DataFrame({
    "Marketing_Spend": np.random.normal(50, 15, n).clip(10, 100),
    "Engagement_Score": np.random.normal(60, 20, n).clip(0, 100),
    "Campaign_Type": np.random.choice(["Email", "Social Media", "Paid Ads"], n, p=[0.3, 0.4, 0.3])
})

# Create figure with size for 512x512 output
plt.figure(figsize=(8, 8))

# Create scatterplot
sns.scatterplot(
    data=data,
    x="Marketing_Spend",
    y="Engagement_Score",
    hue="Campaign_Type",
    palette="Set2",
    s=80,
    edgecolor="black"
)

# Add titles and labels
plt.title("Marketing Spend vs. Engagement", fontsize=18, weight="bold")
plt.xlabel("Marketing Spend (in $1000s)", fontsize=14)
plt.ylabel("Customer Engagement Score", fontsize=14)

# Save exactly 512x512 image
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
