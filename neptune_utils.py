
import neptune.new as neptune
import pandas as pd
import os


class NeptuneViewer:
    @staticmethod
    def get_neptune_dataframe(account, project_name, api_token=None):
        if api_token == None:
            API_TOKEN = os.environ.get("NEPTUNE_API_TOKEN")

        project = neptune.get_project(name=os.path.join(account, project_name), api_token=API_TOKEN)

        df = project.fetch_runs_table().to_pandas()
        project.stop()

        index_list = []

        # optional
        for i in df.columns:
            index_list.append((i.split("/")[-1]).split("__")[-1])

        df.columns = pd.Index(index_list)
        return df

    @staticmethod
    def select_rows_by_exp_id(df, start, end):
        try:
            temp = df["id"].str.split("-", expand=True)[1].apply(pd.to_numeric)
        except:
            temp = df["sys/id"].str.split("-", expand=True)[1].apply(pd.to_numeric)
        idx = (temp >= start) & (temp <= end)
        return df[idx]

    @staticmethod
    def to_numeric(df, keys):
        for key in keys:
            df[key] = df[key].apply(pd.to_numeric)
        return df

    @staticmethod
    def find_id_by(df, kl_lamb, softplus_beta, weight_decay):
        return df.query(
            f"kl_lamb == {kl_lamb} and softplus_beta == {softplus_beta} and weight_decay == {weight_decay}"
        )["id"].item()
