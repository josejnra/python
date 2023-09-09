import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
(line,) = ax.plot(x, y, color="k")

for n in range(len(x)):
    line.set_data(x[:n], y[:n])
    # ax.axis([0, 10, 0, 1])
    fig.canvas.draw()
    # dpi denota a qualidade da imagem (dots per inch)
    plt.savefig("Frame%03d.png" % n, dpi=180)

    # then generate a video with:
    # ffmpeg -framerate 10 -i Frame%03d.png nombre-video.mp4
