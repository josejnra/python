"""
 Pylab combina funcionalidades do pyplot com funcionalidades do Numpy
"""
from pylab import *

alpha = 0.7
phi_ext = 2 * np.pi * 0.5


def duas_figuras_no_grafico():
    x = linspace(0, 5, 100)
    y = x**2

    fig = plt.figure()

    axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # eixos da figura principal
    axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # eixos da figura secundária

    # Figura principal
    axes1.plot(x, y, "r")
    axes1.set_xlabel("x")
    axes1.set_ylabel("y")
    axes1.set_title("Figura Principal")

    # Figura secundária
    axes2.plot(y, x, "g")
    axes2.set_xlabel("y")
    axes2.set_ylabel("x")
    axes2.set_title("Figura Secundária")

    plt.show()


def graficos_em_paralelo():
    x = linspace(0, 5, 100)
    y = x**2
    fig, axes = plt.subplots(nrows=1, ncols=2)

    for ax in axes:
        ax.plot(x, y, "r")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Título")

    fig.tight_layout()

    plt.show()


def plots_diversos():
    _, ax = plt.subplots(2, 3)

    ax[0, 1].plot(np.random.randn(50), color="green", linestyle="-")
    ax[1, 0].hist(np.random.randn(50))
    ax[1, 2].scatter(np.arange(50), np.random.randn(50), color="red")
    plt.show()


def estilos_plots():
    x = linspace(0, 5, 10)

    xx = np.linspace(-0.75, 1.0, 100)
    n = np.array([0, 1, 2, 3, 4, 5])

    fig, axes = plt.subplots(1, 4, figsize=(12, 3))

    axes[0].scatter(xx, xx + 0.25 * np.random.randn(len(xx)))
    axes[0].set_title("scatter")

    axes[1].step(n, n**2, lw=2)
    axes[1].set_title("step")

    axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
    axes[2].set_title("bar")

    axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5)
    axes[3].set_title("fill_between")

    plt.show()


def histograma():
    n = np.random.randn(100000)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].hist(n)
    axes[0].set_title("Histograma Padrão")
    axes[0].set_xlim((min(n), max(n)))

    axes[1].hist(n, cumulative=True, bins=50)
    axes[1].set_title("Histograma Cumulativo")
    axes[1].set_xlim((min(n), max(n)))

    plt.show()


def ColorMap(phi_m, phi_p):
    return +alpha - 2 * np.cos(phi_p) * cos(phi_m) - alpha * np.cos(phi_ext - 2 * phi_p)


def mapa_de_calor():
    phi_m = np.linspace(0, 2 * np.pi, 100)
    phi_p = np.linspace(0, 2 * np.pi, 100)
    X, Y = np.meshgrid(phi_p, phi_m)
    Z = ColorMap(X, Y).T

    fig, ax = plt.subplots()

    p = ax.pcolor(
        X / (2 * np.pi),
        Y / (2 * np.pi),
        Z,
        cmap=cm.RdBu,
        vmin=abs(Z).min(),
        vmax=abs(Z).max(),
    )
    cb = fig.colorbar(p, ax=ax)

    plt.show()


def graficos_3d():
    phi_m = np.linspace(0, 2 * np.pi, 100)
    phi_p = np.linspace(0, 2 * np.pi, 100)
    X, Y = np.meshgrid(phi_p, phi_m)
    Z = ColorMap(X, Y).T

    fig = plt.figure(figsize=(14, 6))

    ax = fig.add_subplot(1, 2, 1, projection="3d")

    p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

    ax = fig.add_subplot(1, 2, 2, projection="3d")
    p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    cb = fig.colorbar(p, shrink=0.5)

    plt.show()


def wire_frame():
    phi_m = np.linspace(0, 2 * np.pi, 100)
    phi_p = np.linspace(0, 2 * np.pi, 100)
    X, Y = np.meshgrid(phi_p, phi_m)
    Z = ColorMap(X, Y).T

    fig = plt.figure(figsize=(8, 6))

    ax = fig.add_subplot(1, 1, 1, projection="3d")

    p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)

    plt.show()


def grafico_3dinterativo():
    # Countour Plot com projeção
    phi_m = np.linspace(0, 2 * np.pi, 100)
    phi_p = np.linspace(0, 2 * np.pi, 100)
    X, Y = np.meshgrid(phi_p, phi_m)
    Z = ColorMap(X, Y).T

    fig = plt.figure(figsize=(8, 6))

    ax = fig.add_subplot(1, 1, 1, projection="3d")

    ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
    cset = ax.contour(X, Y, Z, zdir="z", offset=-pi, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir="x", offset=-pi, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir="y", offset=3 * pi, cmap=cm.coolwarm)

    ax.set_xlim3d(-pi, 2 * pi)
    ax.set_ylim3d(0, 3 * pi)
    ax.set_zlim3d(-pi, 2 * pi)

    plt.show()


grafico_3dinterativo()
