from fastapi import FastAPI, Response
import numpy as np
import matplotlib.pyplot as plt
import io

app = FastAPI()

plt.switch_backend('Agg')


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/sine-image")
def sine_image(start: float = 0.0, end: float = 2 * np.pi, num: int = 100):
    """
    Return a PNG image of the sine curve.
    - start: start angle (in radians)
    - end: end angle (in radians)
    - num: number of data points
    """
    x = np.linspace(start, end, num)
    y = np.sin(x)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, label="y = sin(x)")
    ax.set_title("Sine Curve")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()

    buf = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)

    return Response(content=buf.read(), media_type="image/png")