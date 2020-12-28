import matplotlib.pylab as plt


def show_cart(x, y, title="", x_label="", y_label=""):
    graph = plt.figure().gca()
    graph.plot(x, y)
    graph.set_title(title)
    graph.set_xlabel(x_label)
    graph.set_ylabel(y_label)
    plt.show()
