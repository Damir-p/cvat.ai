from plot_drawer import GraphDrawer

graph_drawer = GraphDrawer()

plots_paths = graph_drawer.draw_plots("json_file.json")

print("Созданные графики:")
for plot_path in plots_paths:
    print(plot_path)
