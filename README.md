Bepensa Logistics – Dashboard Interactivo de Utilización y Demanda

Equipo: 
Gustavo Saúl Santana Schwarz | A01710339
Oscar Méndez Sánchez | A01368480
Héctor Esteban Pérez Bonifant | A01710834
Eduardo Montiel Martínez | A01705615


Archivo principal de la aplicación: app.ipynb
Dataset procesado: bepensa_eda_procesado.pkl


Descripción del Proyecto
Este proyecto corresponde a la Evidencia 4 – Aplicación Web, cuyo objetivo es construir un dashboard interactivo que integre:
- Exploración de datos (EDA)
- Modelos predictivos de rendimiento
- Visualizaciones ejecutivas




Justificación de Tecnologías Usadas
- Dash (Framework principal de la aplicación)
- Se eligió Dash por su capacidad de integrar visualizaciones interactivas y componentes web sin necesidad de utilizar HTML o JavaScript directamente. 




Dash permite:
- Integración nativa con Plotly
- Creación de layouts profesionales
- Callbacks para interactividad avanzada
- Personalización visual para mantener línea corporativa
- Es adecuado para visualisaciones que se requiere claridad, rendimiento y escalabilidad.




Plotly (Visualizaciones)
- Plotly fue seleccionado debido a que:
- Ofrece visualizaciones limpias y profesionales
- Permite interacción nativa (hover, zoom, filtros)
- Se integra directamente con Dash
- Facilita la creación de gráficos ejecutivos, ideales para análisis corporativo




Pandas (Procesamiento de datos)
- Pandas se utilizó para manipulación, limpieza y transformación de los datos. Es la herramienta estándar en proyectos de analítica y machine learning, permitiendo:
- Agrupar información de flota
- Calcular KPIs operativos
- Preparar los datos para modelos predictivos




Scikit-Learn, XGBoost y ANOVA (Modelado predictivo y pruebas estadísticas)
- El modelo predictivo fue desarrollado en evidencias anteriores y en esta aplicación únicamente se carga el modelo ya entrenado. Se utilizaron modelos como XGBoost y regresión debido a su capacidad para manejar:
- Relaciones complejas entre variables
- Variabilidad operacional
- Escenarios comparativos entre capacidad y demanda
- ANOVA se utilizó para validar estadísticamente diferencias entre escenarios operativos, especialmente entre capacidad base y capacidad con buffer del 5 por ciento.




COMO CORRER EL CODIGO PRINCIPAL:
- Para poder visualisar el dashboard con las graficas necesitas simplente abrir el archivo de "app.ipynb".
- Despues darle en correr todos los codigos y ya te va a funcionar.
- No es tan complicado ya que todo ya esta dentro del repositorio asi que solo es correr el codigo principal.
- Solo recuerda que debes de tener la carpeta de "assets" para que este funcione.
- Y simplemente disfruta de la obra maestra