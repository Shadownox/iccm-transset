import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the data
result_df = pd.read_csv("ccobra_eval/results.csv")
subj_df = result_df.groupby(
    ['model', 'id'], as_index=False)['hit'].agg('mean')

# Compute model order based on mean accuracies
order_df = subj_df.groupby(['model'], as_index=False)['hit'].agg('mean')
order = order_df.sort_values('hit')['model']

# Plot model accuracies
sns.set(style="whitegrid")
plt.figure(figsize=(15, 5))
point = [0.3, 0.6, 0.8]
box = [0.3, 0.6, 0.8, 0.5]

sns.swarmplot(x="model", y="hit", data=subj_df, order=order,dodge=True, linewidth=0.5, size=5,
              edgecolor=[0.3,0.3,0.3], color=point, zorder=1)
sns.boxplot(x="model", y="hit", data=subj_df, order=order, showcaps=False,
            boxprops={'facecolor': box, "zorder": 10}, showfliers=False,whiskerprops={"zorder":10},
            linewidth=1, color="black", zorder=10)

plt.ylim(0, 1)
plt.xticks(rotation=65)
plt.xlabel('')
plt.ylabel('Predictive Accuracy')
plt.tight_layout()

plt.savefig('swarmplot.pdf')
plt.show()
