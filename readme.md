# Proyecto de Cálculo del Índice de Masa Corporal (IMC)

Este proyecto es una aplicación que permite a los usuarios calcular su **Índice de Masa Corporal (IMC)** con base en su peso y altura. El IMC es un valor que permite determinar si una persona tiene un peso saludable en relación con su altura.

## Descripción

La aplicación de cálculo del IMC toma como entrada el peso en kilogramos y la altura en metros, y devuelve el valor del IMC junto con una interpretación del resultado en función de categorías estándar, tales como:
- Peso inferior al normal
- Peso normal
- Sobrepeso
- Obesidad

Este proyecto ha sido desarrollado en Python y utiliza una base de datos MySQL para almacenar el historial de cálculos realizados por los usuarios. El objetivo es proporcionar una herramienta sencilla y útil para monitorear la salud corporal.

### Fórmula del IMC

\[
\text{IMC} = \frac{\text{peso (kg)}}{\text{altura (m)}^2}
\]

### Imagenes del proyecto
- Menu

![Menu](/menu.png)
- Consultar Paciente
![bd](/consultarpaciente.png)
- Base de datos
![bd](/basedatos.png)




## Instalación

Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:
```bash
pip3 install mysql-connector-python
```

### Colaboradores

```markdown
- **Ruth Tomala** 
- **Sasha Sancan** 
- **Genesis Morante** 
- **Jenny Tenesaca** 