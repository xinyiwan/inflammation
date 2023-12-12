"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
import numpy as np

def visualize(data_dict):
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()

    plt.show()

def visualize_text(data_dict):
    """Display the textual presentation of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    
    """
    # num_text = len(data_dict)
    # fig = plt.figure(figsize=((3 * num_text) + 1, 3.0))
    cell_text = []
    rowlabel = []
    for i, (name, data) in enumerate(data_dict.items()):
        rowlabel.append(name)
        cell_text.append([f'{x:.1f}' for x in data])
    
    print(rowlabel)
    print(cell_text)
    the_table = plt.table(cellText=cell_text,
                      rowLabels=rowlabel,
                      loc='upper center')
    

    # fig.tight_layout()
    plt.axis('off')
    plt.title('Textual Presentation')
    plt.show()
