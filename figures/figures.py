import plotly.io as pio

# Panel
fig_panel_cpk_recorrido = pio.read_json("fig_panel_cpk_recorrido.json")
fig_panel_ingresosfacmes = pio.read_json("fig_panel_ingresosfacmes.json")
fig_panel_rutasngreprom = pio.read_json("fig_panel_rutasngreprom.json")
fig_panel_utilizacion_vs_distancia = pio.read_json("fig_panel_utilizacion_vs_distancia.json")

# Ingresos
fig_ingresos_importxcliente = pio.read_json("fig_ingresos_importxcliente.json")
fig_ingresos_rentxruta = pio.read_json("fig_ingresos_rentxruta.json")

# Rutas
fig_rutas_rendipromestado = pio.read_json("fig_rutas_rendipromestado.json")
fig_rutas_riesgopredi = pio.read_json("fig_rutas_riesgopredi.json")

# Unidades
fig_unidades_totalincidentes = pio.read_json("fig_unidades_totalincidentes.json")
fig_unidades_unicnomaskm = pio.read_json("fig_unicnomaskm.json")
fig_unidades_unimasrendi = pio.read_json("fig_unidades_unimasrendi.json")

# Demanda
fig_demanda_evoviajecliente = pio.read_json("fig_demanda_evoviajecliente.json")
fig_demanda_viajexmes = pio.read_json("fig_demanda_viajexmes.json")
