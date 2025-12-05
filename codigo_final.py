"""
DASHBOARD BEPENSA - VERSION COMPLETA
Sidebar ancho estilo Bootstrap United
Home con tarjetas clickeables
Multipágina: Inicio, Panel, Ingresos, Unidades, Demanda, Rutas
Dark mode completo
"""
# pip install dash-auth
# pip install dash-bootstrap-components
import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import base64
import plotly.express as px
import datetime as dt

# -------------------------------------------------------------------
#                       CONFIGURACIÓN GENERAL
# -------------------------------------------------------------------

# Cargar logo
image_filename = "bepensa_logo.png"
encoded_image = base64.b64encode(open(image_filename, "rb").read()).decode()

# Tema general
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.LUX, dbc.icons.BOOTSTRAP],
)
app.title = "Bepensa Logistics Dashboard"

COLOR_ORANGE = "#f57c3b"

# Datos de ejemplo
df = px.data.gapminder().query("year == 2007")
df2 = px.data.stocks()

# -------------------------------------------------------------------
#                              SIDEBAR
# -------------------------------------------------------------------

def sidebar():
    return html.Div(
        [
            # LOGO PRINCIPAL
            html.Img(
                src=f"data:image/png;base64,{encoded_image}",
                style={
                    "height": "60px",
                    "margin-bottom": "25px",
                    "object-fit": "contain",
                    "margin-left": "10px"
                },
            ),

            # NAV CON ICONOS
            dbc.Nav(
                [
                    dbc.NavLink(
                        html.Img(src="/assets/icon_home.png",
                                style={"height": "32px", "marginBottom": "14px"}),
                        href="/",
                        active="exact",
                        className="sidebar-icon-link",
                    ),

                    dbc.NavLink(
                        html.Img(src="/assets/icon_panel.png",
                                style={"height": "32px", "marginBottom": "14px"}),
                        href="/panel",
                        active="exact",
                        className="sidebar-icon-link",
                    ),

                    dbc.NavLink(
                        html.Img(src="/assets/icon_ingresos.png",
                                style={"height": "32px", "marginBottom": "14px"}),
                        href="/ingresos",
                        active="exact",
                        className="sidebar-icon-link",
                    ),

                    dbc.NavLink(
                        html.Img(src="/assets/icon_unidades.png",
                                style={"height": "32px", "marginBottom": "14px"}),
                        href="/unidades",
                        active="exact",
                        className="sidebar-icon-link",
                    ),

                    dbc.NavLink(
                        html.Img(src="/assets/icon_demanda.png",
                                style={"height": "32px", "marginBottom": "14px"}),
                        href="/demanda",
                        active="exact",
                        className="sidebar-icon-link",
                    ),

                    dbc.NavLink(
                        html.Img(src="/assets/icon_rutas.png",
                                style={"height": "32px", "marginBottom": "14px"}),
                        href="/rutas",
                        active="exact",
                        className="sidebar-icon-link",
                    ),
                ],
                vertical=True,
                pills=True,
                style={"marginTop": "5px"},
            ),

            html.Hr(),

            # DARK MODE SWITCH
            html.Div(
                [
                    html.Span("Modo oscuro", style={"fontSize": "13px"}),
                    dbc.Switch(id="theme-switch", value=False, class_name="ms-2"),
                ],
                style={"marginTop": "20px"},
            ),
        ],

        id="sidebar",
        style={
            "position": "fixed",
            "top": 0,
            "left": 0,
            "bottom": 0,
            "width": "8rem",
            "padding": "1rem",
            "background-color": "#ffffff",
            "overflow-x": "hidden",
            "transition": "all 0.3s",
            "box-shadow": "2px 0 6px rgba(0,0,0,0.1)",
            "textAlign": "center",
        },
    )


# -------------------------------------------------------------------
#                 COMPONENTES REUTILIZABLES
# -------------------------------------------------------------------

def page_header(title, subtitle="Bepensa Logistics"):
    return dbc.Row(
        [
            dbc.Col(
                [
                    html.H2(title),
                    html.H6(subtitle),
                ]
            ),
            dbc.Col(
                html.Div(id="clock", className="clock-box"),
                width=3,
            ),
        ],
        style={"marginBottom": "20px"},
        align="center",
    )

def section_card(icon, title, subtitle, href):
    return dcc.Link(
        dbc.Card(
            dbc.CardBody(
                [
                    html.I(className=f"{icon}", style={"fontSize": "28px", "color": COLOR_ORANGE}),
                    html.H4(title, style={"marginTop": "10px"}),
                    html.P(subtitle, style={"fontSize": "13px", "color": "#555"}),
                ]
            ),
            style={
                "borderRadius": "16px",
                "border": "none",
                "borderTop": f"6px solid {COLOR_ORANGE}",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.15)",
                "height": "170px",
                "transition": "0.2s",
                "textAlign": "center",
            },
            className="mb-4 section-card",
        ),
        href=href,
        style={"textDecoration": "none", "color": "black"},
    )


# -------------------------------------------------------------------
#                      LAYOUTS DE CADA PÁGINA
# -------------------------------------------------------------------

def layout_inicio():
    return html.Div(
        [
            page_header("Dashboard de Control Logístico"),

            html.H4("Secciones", style={"marginBottom": "20px"}),

            dbc.Row(
                [
                    dbc.Col(section_card("bi bi-cash-coin", "Ingresos",
                                        "Detalle de ingresos y costos", "/ingresos"), md=4),
                    dbc.Col(section_card("bi bi-truck", "Unidades",
                                        "Flota y operación", "/unidades"), md=4),
                    dbc.Col(section_card("bi bi-graph-up-arrow", "Demanda",
                                        "Comportamiento de la demanda", "/demanda"), md=4),
                ]
            ),

            dbc.Row(
                [
                    dbc.Col(section_card("bi bi-signpost-split", "Rutas",
                                        "Corredores logísticos", "/rutas"), md=4),
                    dbc.Col(section_card("bi bi-layout-text-sidebar", "Panel de Control",
                                        "Resumen ejecutivo", "/panel"), md=4),
                ],
                style={"marginTop": "10px"},
            ),
        ],
        style={"padding": "20px"},
    )


def layout_panel():
    fig1 = px.bar(df, x="country", y="gdpPercap", title="Meta Mensual (dummy)")
    fig2 = px.line(df2, x="date", y=["GOOG"], title="Demanda (dummy)")

    return html.Div(
        [
            page_header("Panel de Control"),
            dbc.Row(
                [
                    dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(figure=fig1))), md=6),
                    dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(figure=fig2))), md=6),
                ]
            ),
        ],
        style={"padding": "20px"},
    )


def layout_ingresos():
    fig = px.histogram(df, x="gdpPercap", nbins=10, title="Ingresos dummy")
    return html.Div(
        [
            page_header("Ingresos"),
            dbc.Row([dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(figure=fig))), md=12)])
        ],
        style={"padding": "20px"},
    )


def layout_unidades():
    fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="continent")
    return html.Div(
        [
            page_header("Unidades"),
            dbc.Row([dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(figure=fig))), md=12)])
        ],
        style={"padding": "20px"},
    )


def layout_demanda():
    fig = px.line(df2, x="date", y="AAPL", title="Demanda dummy")
    return html.Div(
        [
            page_header("Demanda"),
            dbc.Row([dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(figure=fig))), md=12)])
        ],
        style={"padding": "20px"},
    )


def layout_rutas():
    fig = px.choropleth(df, locations="iso_alpha", color="continent", title="Mapa dummy")
    return html.Div(
        [
            page_header("Rutas"),
            dbc.Row([dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(figure=fig))), md=12)])
        ],
        style={"padding": "20px"},
    )

# -------------------------------------------------------------------
#                          LAYOUT GENERAL
# -------------------------------------------------------------------

# -------------------------------------------------------------------
#                          LAYOUT GENERAL
# -------------------------------------------------------------------

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dcc.Interval(id="clock-interval", interval=1000, n_intervals=0),

        sidebar(),

        html.Div(
            id="page-content",
            style={
                "marginLeft": "8rem",
                "padding": "2rem",
                "transition": "0.3s",
            },
        ),
    ],
    id="app-root",
    className="light-theme",

    # Imagen de fondo desde assets
    style={
        "backgroundImage": "url('/assets/bepensa_logos.png')",
        "backgroundPosition": "top right",
        "backgroundSize": "1300px",
        "backgroundRepeat": "no-repeat",
        "backgroundAttachment": "fixed"
    }
)


# -------------------------------------------------------------------
#                             CALLBACKS
# -------------------------------------------------------------------

@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/panel":
        return layout_panel()
    elif pathname == "/ingresos":
        return layout_ingresos()
    elif pathname == "/unidades":
        return layout_unidades()
    elif pathname == "/demanda":
        return layout_demanda()
    elif pathname == "/rutas":
        return layout_rutas()
    else:
        return layout_inicio()


@app.callback(Output("clock", "children"), Input("clock-interval", "n_intervals"))
def update_clock(n):
    now = dt.datetime.now()
    return now.strftime("%d de %B de %Y — %I:%M %p")


@app.callback(Output("app-root", "className"), Input("theme-switch", "value"))
def toggle_theme(dark):
    return "dark-theme" if dark else "light-theme"


# -------------------------------------------------------------------
# RUN
# -------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8053, debug=True)
# ngrok config add-authtoken 36OIzBTUaQ16Eh3Ko6BIM6kPAf3_62CAuBtD7F1LWMBqcDv2y