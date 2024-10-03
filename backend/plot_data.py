import matplotlib.pyplot as plt
import numpy as np


def data_plotting(plot_type: str, settings: dict):
    data = settings['data']
    var_data = []
    for i in range(1, len(data) + 1):
        var_data.append(np.array(data[str(i)].split(","), dtype=float))

    fig, ax = plt.subplots()

    for k in range(1, len(var_data)):
        if plot_type == "scatter":
            s_plot = ax.scatter(var_data[0], var_data[k], marker=settings['marker'])
            if settings['size'] != 0:
                s_plot.set_sizes([settings['size']])
            if settings['point_color'] != "Choose":
                s_plot.set_color(settings['point_color'])
            if settings['edge_color'] != "Choose":
                s_plot.set_edgecolor(settings['edge_color'])
            if settings['line_width']:
                s_plot.set_linewidth(settings['line_width'])
            if settings['cmap'] != "Choose":
                s_plot.set_cmap(settings['cmap'])
            if settings['legend']:
                s_plot.set_label(settings['legend_labels'][k - 1])
            if settings['color_bar']:
                fig.colorbar(s_plot, ax=ax)

        elif plot_type == "line":
            l_plot, = ax.plot(var_data[0], var_data[k])
            if settings['marker'] is not None:
                l_plot.set_marker(settings['marker'])
            if settings['line_colors'][k - 1] != "Choose":
                l_plot.set_color(settings['line_colors'][k - 1])
            if settings['line_styles'][k - 1] != "Choose":
                if settings['line_styles'][k - 1] == "dashed line":
                    line_style = '--'
                elif settings['line_styles'][k - 1] == "dotted line":
                    line_style = ':'
                elif settings['line_styles'][k - 1] == "dash dot line":
                    line_style = '-.'
                l_plot.set_linestyle(line_style)
            if settings['line_width'] != 0:
                l_plot.set_linewidth(settings['line_width'])
            if settings['cmap']:
                l_plot.set_cmap(settings['cmap'])
            if settings['legend']:
                l_plot.set_label(settings['legend_labels'][k - 1])
            if settings['color_bar']:
                fig.colorbar(l_plot, ax=ax)

    if settings['x_label']:
        ax.set_xlabel(settings['x_label'])
    if settings['y_label']:
        ax.set_ylabel(settings['y_label'])
    if settings['title']:
        ax.set_title(settings['title'])
    if settings['grid']:
        ax.grid(True)
    if settings['legend']:
        ax.legend()

    return fig
