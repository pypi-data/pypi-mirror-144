# altair-grid

The Grid theme for Altair visualization library in Python

### Getting started

Install from PyPI.

```bash
$ pip install altair-grid
```

Import with Altair.

```python
import altair as alt
import altair_grid as altgrid
```

Register and enable the theme.

```python
alt.themes.register('grid', altgrid.theme)
alt.themes.enable('grid')
```

Make a chart.

```python
from vega_datasets import data
source = data.iowa_electricity()

alt.Chart(source, title="Iowa's renewable energy boom").mark_area().encode(
    x=alt.X(
        "year:T",
        title="Year"
    ),
    y=alt.Y(
        "net_generation:Q",
        stack="normalize",
        title="Share of net generation",
        axis=alt.Axis(format=".0%"),
    ),
    color=alt.Color(
        "source:N",
        legend=alt.Legend(title="Electricity source"),
    )
)
```

![example](./iowa.png)

### What else?

This library requires that you have both the "Roboto" and "Summit Sans" fonts installed. More examples can be found in [notebook.ipynb](./notebook.ipynb).
