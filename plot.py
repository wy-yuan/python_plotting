from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as patches

def subplot_adjust_params(x, y):
    plt.figure(figsize=(88.9 / 25.4, 88.9 / 25.4 / 2))  # 88.9mm for width
    plt.rcParams['font.family'] = 'Times New Roman'

    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.tick_params(labelsize=8, pad=0.01, length=2)
        plt.plot(x, y, linewidth=0.6, color='b', label='y')
        plt.plot(x, y+1, linewidth=0.6, color='r', label='y+1')
        plt.xlabel('x', fontsize=8, labelpad=0.01)
        plt.ylabel('y', fontsize=8, labelpad=0.01)
        plt.ylim([-2, 2])
        plt.xlim([0, 100])
        plt.xticks([0, 50, 100])
        plt.yticks([-2, -1, 0, 1, 2])
        plt.legend(fontsize=6, frameon=False, loc='lower right', handlelength=1.2, ncol=2)  # ,loc='upper left',
        # plt.legend(fontsize=6, frameon=False, loc='upper right', ncol=2)

    plt.tight_layout()
    plt.subplots_adjust(wspace=0.35, hspace=0.3, bottom=0.15, left=0.08, right=0.95)
    plt.savefig(r"./figures_subplot_adjust_params.svg")
    plt.show()

def plot_two_axis(x, y):
    plt.figure(figsize=(88.9 / 25.4, 88.9 / 25.4/1.5))
    plt.rcParams['font.family'] = 'Times New Roman'
    fig, ax1 = plt.subplots(1, 1, figsize=(88.9 / 25.4, 88.9 / 25.4 / 1.5))

    plt.rcParams['font.family'] = 'Times New Roman'
    plt.tick_params(labelsize=8, pad=0.01, length=2)
    ax1.tick_params(labelsize=8, pad=0.01, length=2)

    # Plot the first data on the left y-axis
    ax1.plot(x, y, 'o-', color='blue', label='y', linewidth=0.8, markersize=1)
    ax1.set_xlabel('x', fontsize=8)
    ax1.set_ylabel('y', color='blue', fontsize=8, labelpad=0.01)
    ax1.tick_params('y', colors='blue', pad=0.01, length=2)
    ax1.set_ylim([0, 2])
    ax1.set_xticks([0, 50, 100])

    # Create a secondary y-axis on the right side
    ax2 = ax1.twinx()
    plt.rcParams['font.family'] = 'Times New Roman'
    ax2.tick_params(labelsize=8, pad=0.01, length=2)
    ax2.plot(x, y+2, 'X-', color='red', label='cos(x)', linewidth=0.8, markersize=2)
    ax2.set_ylabel('y+2', color='red', fontsize=8)
    ax2.tick_params('y', colors='red')
    ax2.set_ylim([0, 3])
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.35, hspace=0.3, bottom=0.15, left=0.15, right=0.85)
    plt.savefig("./figures_two_axis.svg")
    plt.show()

def plot_with_rectangle(x, y):
    plt.figure(figsize=(88.9 / 25.4, 88.9 / 25.4 / 1.3))
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.tick_params(labelsize=8)

    ax = plt.subplot(1, 1, 1)
    plt.tick_params(labelsize=8, pad=0.1)
    plt.plot(x, y, label='y')
    plt.plot(x, y+5, label='y+5')
    plt.plot(x, y-5, label='y-5')
    # plot rectangle
    rectangle = patches.Rectangle((50, -10), 30, 20, edgecolor='black', facecolor='none')
    ax.add_patch(rectangle)
    plt.legend(fontsize=6, frameon=False)

    plt.savefig("./figures_with_rectangle.svg")
    plt.show()

def subplot_adjust_hwRatios(x, y):
    gs_kw = dict(width_ratios=[1, 1], height_ratios=[1, 2])
    fig, axd = plt.subplot_mosaic([['up1', 'up2'], ['down', 'down']], gridspec_kw=gs_kw,
                                  figsize=(88.9 / 25.4, 88.9 / 25.4 * 1.2), layout="tight")
    plt.rcParams['font.family'] = 'Times New Roman'
    for k, ax in axd.items():
        print(k, ax)

    axd["up1"].tick_params(labelsize=8, pad=0.01, length=2)
    axd["up1"].plot(x, y)
    axd["up2"].tick_params(labelsize=8, pad=0.01, length=2)
    axd["up2"].plot(x, y)
    axd["down"].tick_params(labelsize=8, pad=0.01, length=2)
    axd["down"].plot(x, y)

    plt.tight_layout()
    plt.savefig("./figures_subplot_adjust_hwRatios.svg")
    plt.show()


if __name__ == '__main__':
    x = np.linspace(0, 100, 1000)
    y = np.sin(x)
    subplot_adjust_params(x, y)

    plot_two_axis(x, y)

    plot_with_rectangle(x, y)

    subplot_adjust_hwRatios(x[:100], y[:100])