import asyncio
from datetime import date

import numpy as np

from shiny import *

app_ui = ui.page_fluid(
    ui.download_link("downloadData", "Download"),
)

# For more examples of different types of download handlers, see:
# https://github.com/rstudio/py-shiny/blob/68ffc27/examples/download/app.py#L90
def server(input: Inputs, output: Outputs, session: Session):
    @session.download(
        filename=lambda: f"新型-{date.today().isoformat()}-{np.random.randint(100,999)}.csv"
    )
    async def downloadData():
        await asyncio.sleep(0.25)
        yield "one,two,three\n"
        yield "新,1,2\n"
        yield "型,4,5\n"


app = App(app_ui, server)
