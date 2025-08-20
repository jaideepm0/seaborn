# chart.py
# 📧 23f2001992@ds.study.iitm.ac.in
# Professional Seaborn Barplot for Business Insights

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ------------------------
# Generate synthetic data
# ------------------------
data = {
    "Product": ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"],
    "Quarter1": [120, 90, 75, 60, 110],
    "Quarter2": [140, 105, 80, 70, 125],
    "Quarter3": [160, 130, 95, 85, 135],
    "Quarter4": [180, 150, 100, 90, 145],
}

df = pd.DataFrame(data)

# Melt to long format for Seaborn
df_long = df.melt(id_vars="Product",
                  var_name="Quarter",
                  value_name="Sales")

# ------------------------
# Styling best practices
# ------------------------
sns.set_theme(style="whitegrid", context="talk")
palette = sns.color_palette("crest", n_colors=len(df_long["Quarter"].unique()))

# ------------------------
# Create barplot
# ------------------------
plt.figure(figsize=(8, 8))   # 512x512 at dpi=64

ax = sns.barplot(
    data=df_long,
    x="Product",
    y="Sales",
    hue="Quarter",
    palette=palette
)

# Titles and labels
ax.set_title("Quarterly Product Sales Performance", fontsize=18, pad=20)
ax.set_xlabel("Product", fontsize=14)
ax.set_ylabel("Sales (Units)", fontsize=14)

# Adjust legend
ax.legend(title="Quarter", loc="upper left", bbox_to_anchor=(1, 1))

# ------------------------
# Save chart
# ------------------------
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches="tight")  # 8in*64dpi = 512px
