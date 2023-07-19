import pandas as pd
import matplotlib.pyplot as plt
import os

class GraphDrawer:
    def draw_plots(self, json_file):
        df = pd.read_json(json_file)

        if not os.path.exists("plots"):
            os.makedirs("plots")

        plots_paths = []
        for column in df.columns:
            plt.figure()
            plt.ylabel(column)
            plt.title(f"Comparison between Ground Truth Corners and {column}")
            plot_path = f"plots/{column}_plot.png"
            plt.savefig(plot_path)
            plots_paths.append(plot_path)

        return plots_paths
