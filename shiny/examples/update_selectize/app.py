from shiny import *

app_ui = ui.page_fluid(
    ui.input_selectize("x", "Server side selectize", choices=None, multiple=True),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.Effect()
    def _():
        ui.update_selectize(
            "x",
            choices=[f"Foo {i}" for i in range(100000)],
            # selected=["Foo 0", "Foo 1"],
            server=True,
        )


app = App(app_ui, server, debug=True)