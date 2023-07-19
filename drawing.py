import os
import pandas as pd
import matplotlib.pyplot as plt

class PlotDrawer:

    def draw_plots(self, json_file):
        df = pd.read_json(json_file)

        os.makedirs("plots", exist_ok=True)

        paths_to_plots = []
        for column in df.columns:
            plt.figure()
            plt.plot(df[column])
            plt.xlabel("Rooms")
            plt.ylabel(column)
            plt.title(f"Comparison of {column}")
            plot_path = os.path.join("plots", f"{column}_plot.png")
            plt.savefig(plot_path)
            paths_to_plots.append(plot_path)
            plt.close()

        return paths_to_plots
