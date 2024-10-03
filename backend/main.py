import json
from xmlrpc.client import Boolean
from typing import Any, Dict, Optional
import numpy as np
import uvicorn
import uuid
from fastapi import File, FastAPI, Request, Body
from plot_data import data_plotting
from pydantic import BaseModel


class DataModel(BaseModel):
    data: Dict[str, Any]
    title: str
    x_label: str
    y_label: str
    grid: bool
    legend: bool
    legend_labels: list
    marker: str | None
    line_width: int
    color_bar: Optional[bool] = False
    cmap: Optional[str] = None
    size: Optional[int] = 0
    edge_color: Optional[str] = None
    point_color: Optional[str] = None
    line_colors: Optional[list] = []
    line_styles: Optional[list] = []


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome from the backend server"}


@app.post("/{plot}")
async def get_plot(plot: str, settings: DataModel):
    settings = settings.dict()
    fig = data_plotting(plot, settings)
    img_name = str(uuid.uuid4())
    name = f"../storage/{img_name}.jpg"
    fig.savefig(name)
    name = f"storage/{img_name}.jpg"
    return {"name": name}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
