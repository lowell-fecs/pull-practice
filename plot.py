import matplotlib.pyplot as plt
import numpy as np

def rgb_int(r, g, b, a=255):

    # adjust integer values to float values to plug in
    return (r / 255.0, g / 255.0, b / 255.0, a / 255.0)


# =====================================================================
# Edit the colors below and submit a Pull Request
# Valid formats:
#   - Integer RGB/RGBA: rgb_int(255, 99, 71) or rgb_int(255, 99, 71, a=80)
#   - Hex strings:      "#282C34"
#   - Named colors:     "coral", "skyblue", "gold", "mediumseagreen"
# =====================================================================
THEME = {
    "background": "#1E222A",                  # Window & chart background (Hex)
    "wave":       rgb_int(97, 175, 239),      # Sine wave line color (0-255 RGB)
    "fill":       rgb_int(97, 175, 239, 60),  # Shaded area under curve (RGB + Alpha)
    "text":       "red",                    # Title, labels, and grid (Named color)
}
# =====================================================================

def make_plot():
    t = np.linspace(0.0, 2.0, 200) #start, stop, step for the graph
    y = np.sin(2 * np.pi * t) # graph of y = sin(2pi * x)
    
    #creates both the canvas (fig) and a single axes (ax) inside it
    fig, ax = plt.subplots(figsize=(8, 4), facecolor=THEME["background"])
    
    #apply background color
    ax.set_facecolor(THEME["background"])

    # plot the wave and shaded fill
    ax.plot(t, y, color=THEME["wave"], linewidth=3)

    
    ax.set_title("Sine wave", color=THEME["text"], fontsize=14, fontweight="bold")
    ax.set_xlabel("Time (s)", color=THEME["text"])
    ax.set_ylabel("Amplitude", color=THEME["text"])
    ax.tick_params(colors=THEME["text"])
    ax.grid(True, linestyle=":", alpha=0.3, color=THEME["text"])
    
    plt.show()

# this runs only when the file is executed
if __name__ == "__main__":
    make_plot()
