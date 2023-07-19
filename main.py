from drawing import PlotDrawer

def main():
    json_file = "deviation.json"

    plot_drawer = PlotDrawer()

    paths_to_plots = plot_drawer.draw_plots(json_file)

    print("Plots created and saved successfully.")
    print("Paths to plots:")
    for path in paths_to_plots:
        print(path)

if __name__ == "__main__":
    main()
