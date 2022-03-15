import pandas as pd
from sklearn.linear_model import LinearRegression, RidgeCV

from datetime import *

supply_words = ["pan", "rasp", "kom"]

import pandas as pd


def getRecipesDF():
    df = pd.read_csv("data/lunch_recipes.csv")  # Read lunch recipes dataframe.
    for wrd in supply_words:

        def hulp_clean(text):
            # This function cleans text by seperating all the words and removing punctuation
            #
            # text:str

            str_list = ["".join(O for O in str if O.isalnum()) for str in text.split()]
            str_list = [str.lower() for str in str_list]
            return str_list

        df[f"{wrd}"] = df.recipe.apply(
            lambda text: hulp_clean(text).count(wrd) > 0
        )  ## count the amount of times a word occurs in the recipe.
        df[f"{wrd}"] = df[f"{wrd}"].apply(lambda x: x is True)
    df = df.drop("servings", axis=1)
    df = df.drop("recipe", axis=1)
    df["date"] = df.date.apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
    df = df.drop("url", axis=1)
    df = df.drop("dish", axis=1)

    return df


def attendance_sheet_uitlezen():
    df = pd.read_csv("../clean_code/data/key_tag_logs.csv")
    df["timestamp2"] = df.timestamp.apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    )
    df["date"] = df.timestamp.apply(lambda x: datetime.strptime(x[:10], "%Y-%m-%d"))
    df["time"] = df.timestamp2.apply(lambda x: x.time())
    df["timestamp"] = df["timestamp2"]
    df = df.drop("timestamp2", axis=1)
    import numpy as np

    result = pd.DataFrame(np.array(df.date), columns=["date"]).drop_duplicates()

    # print(df.name.unique())
    for name in df.name.unique():
        lunchdates = []
        for datum in df.date.unique():
            df2 = df[df.name == name]
            df2 = df2[df2.date == datum]

            dataframe_check_in = df2[df2.event == "check in"]
            dataframe_check_in = dataframe_check_in[
                dataframe_check_in.time < time(12, 0, 0)
            ]

            df_check_out = df2[df2.event == "check out"]
            df_check_out = df_check_out[df_check_out.time > time(12, 0, 0)]
            if df_check_out.shape[0] > 0 and dataframe_check_in.shape[0] > 0:
                lunchdates.append(datum)

        result[f"{name}"] = result.date.apply(
            lambda x: 1 if x in list(lunchdates) else 0
        )

    result["date"] = result["date"]  # .apply(str)
    return result


def train_model(alpha=0.1):
    recipes = getRecipesDF()
    attendance = attendance_sheet_uitlezen()
    l = pd.read_csv("data/dishwasher_log.csv")
    l["date"] = l.date.apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))

    df = recipes.merge(attendance, on="date", how="outer").merge(l).fillna(0)
    reg = LinearRegression(fit_intercept=False, positive=True).fit(
        df.drop(["dishwashers", "date"], axis=1), df["dishwashers"]
    )
    return dict(zip(reg.feature_names_in_, [round(c, 3) for c in reg.coef_]))


if __name__ == "__main__":

    print(train_model())
