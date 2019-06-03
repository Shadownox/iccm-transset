import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ccobra


def extract_answer(syllog, df):
    """ Extracts a response from a syllogistic response table.

    Parameters
    ----------
    syllog : str
        Syllogistic problem identifier (e.g., "AA1").

    df : pd.DataFrame
        Prediction table of a syllogistic model.

    Returns
    -------
    list(str)
        List of model predictions.

    """

    return df[df["Syllogism"] == syllog]["Prediction"].values[0].split(";")

def plot(result_df, metric, y_axis):
    """ Plot data according to metric of choice.

    Parameters
    ----------
    result_df : pd.DataFrame
        Plot data, i.e., model accuracies.

    metric : str
        Either "accuracy" for MFA accuracy (discounting for multiple responses), or "contained"
        (not discounting for multiple responses).

    y_axis : str
        Y axis label.

    """

    agg_df = result_df.groupby(['model', 'Dataset'], as_index=False)[metric].agg('mean')
    order_df = result_df.groupby(['model'], as_index=False)[metric].agg('mean')
    order = order_df.sort_values(metric)['model']

    color1 = [0.2, 0.6, 0.9]
    color2 = [0.1, 0.4, 0.6]

    sns.set(style="whitegrid", palette='colorblind')
    plt.figure(figsize=(7, 4))
    sns.barplot(x='model', y=metric, hue="Dataset", data=agg_df, ci=None, order=order,
                palette=[color1, color2])
    plt.xticks(rotation=65)
    plt.xlabel('')
    plt.ylabel(y_axis)
    plt.ylim(0, 1)
    sns.despine()

    plt.tight_layout()
    plt.savefig('mfa_{}.pdf'.format(metric))
    plt.show()

# Define the MFA files
mfa_files = {
    "Ragni2016" : "mfa_tables/mfa_ragni_2016.csv",
    "Khemlani2012" : "mfa_tables/mfa_khemlani_2012.csv"
}

# Define the list of models
models = {
    "Atmosphere" : "models/Atmosphere.csv",
    "Conversion" : "models/Conversion.csv",
    "Matching" : "models/Matching.csv",
    "MentalModels" : "models/MMT.csv",
    "PHM" : "models/PHM.csv",
    "PSYCOP" : "models/PSYCOP.csv",
    "Transset" : "models/TransSet.csv",
    "VerbalModels" : "models/VerbalModels.csv"
}

# Obtain model prediction scores
result = []
for mfa_name, mfa_file in mfa_files.items():
    mfa_df = pd.read_csv(mfa_file)
    for model, model_path in models.items():
        model_df = pd.read_csv(model_path)
        model_containment_hits = 0
        model_accuracy = 0

        for syllog in ccobra.syllogistic.SYLLOGISMS:
            mfa_response = extract_answer(syllog, mfa_df)
            model_response = extract_answer(syllog, model_df)

            containment = set(mfa_response).issubset(set(model_response))
            accuracy = int(containment) / len(model_response)

            model_accuracy += accuracy
            if containment:
                model_containment_hits += 1

            result.append({
                "model" : model,
                "syllog" : syllog,
                "contained" : containment,
                "accuracy" : accuracy,
                "Dataset" : mfa_name
            })

        model_accuracy = round(model_accuracy / 64.0, 3)
        model_containment_hits = round(model_containment_hits / 64.0, 3)

# Fix model names
result_df = pd.DataFrame(result)
result_df['model'] = result_df['model'].replace({
    'Transset': 'TransSet',
    'VerbalModels': 'Verbal Models',
    'MentalModels': 'Mental Models'
})

# Plot the results
plot(result_df, "accuracy", "MFA Accuracy")
plot(result_df, "contained", "MFA Coverage")
