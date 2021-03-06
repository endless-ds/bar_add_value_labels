def bar_add_value_labels(ax, spacing=5):
    # Add labels to the end of each bar in a bar chart.

    # Arguments:
    #     ax (matplotlib.axes.Axes): The matplotlib object containing the axes
    #         of the plot to annotate.
    #     spacing (int): The distance between the labels and the bars.

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            spacing *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, spacing),        # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.

# How to create the histogram:
# fig, ax = matplotlib.pyplot.subplots()
# ax.hist()

# To call the function:
# bar_add_value_labels(ax)

# To call the function w/ different spacing (example):
# bar_add_value_labels(ax,spacing=3)




