import streamlit as st
import requests

st.header("Welcome to FAI")

st.sidebar.image("logos/github-dp.PNG")

st.markdown("## Plotting Data")
plot_type = st.selectbox(
    "select the plot type",
    ("None", "scatter", "line", "bar chart", "Histogram", "pie chart"),
)

if plot_type == "None":
    st.header("Plot your data")
    st.write("Select an option from above")
elif plot_type == "bar chart" or plot_type == "Histogram" or plot_type == "pie chart":
    st.header("Not Implemented yet")
else:
    settings = {}
    col1, col2, col3 = st.columns(3)
    col1.markdown("#### Variables")
    num_var = col1.slider("number of variable", 2, 5, 2)
    variables_data = []
    var_txt = {}
    for i in range(1, num_var + 1):
        var_txt[str(i)] = col1.text_input(
            "add variable " + str(i) + " data seperated with commas"
        )
    settings['data'] = var_txt

    col2.markdown("#### Titles")
    settings["title"] = col2.text_input("Enter title")
    settings["x_label"] = col2.text_input("Enter x axis label")
    settings["y_label"] = col2.text_input("Enter y axis label")
    settings["grid"] = col2.checkbox("Apply Grid")
    settings["legend"] = col2.checkbox("Add Legend")
    legend_labels = []
    if settings["legend"]:
        for j in range(2, num_var + 1):
            legend_labels.append(col2.text_input(f"Enter legend label for variable {j}"))
    settings["legend_labels"] = legend_labels

    col3.markdown("#### Setting")

    if plot_type == "scatter":
        settings["size"] = int(col3.number_input("Enter size of points", 0))
        settings["edge_color"] = col3.selectbox("color of edge", ("Choose", "black", "red", "green"))
        settings["point_color"] = col3.selectbox("color of points", ("Choose", "black", "red", "green"))
        settings["marker"] = col3.selectbox("marker type", (".", "o", "x"))
        settings["line_width"] = int(col3.number_input("Enter line width of edge", 0))
        settings["cmap"] = col2.selectbox("cmap", ("Choose", "viridis", "plasma", "Grays"))
        settings["color_bar"] = col2.checkbox("you want to add a color bar")
    elif plot_type == "line":
        line_colors = []
        line_styles = []
        for j in range(2, num_var + 1):
            line_colors.append(col3.selectbox(f"color of line for variable {j}",
                                              ("Choose", "black", "red", "green", "yellow", "magenta")))
            line_styles.append(col3.selectbox(f"line style for variable {j}",
                                              ("Choose", "dashed line", "dotted line", "dash dot line")))
        settings["line_colors"] = line_colors
        settings["line_styles"] = line_styles
        settings["marker"] = col3.selectbox("marker type", (None, "o", "X"))
        settings["line_width"] = int(col3.number_input("Enter line width", 0))

    # settings = [settings]
    if col1.button("Plot Data"):
        # st.write(settings)
        res = requests.post(f"http://0.0.0.0:8080/{plot_type}", json=settings)
        img_path = res.json()
        st.image(img_path['name'])
