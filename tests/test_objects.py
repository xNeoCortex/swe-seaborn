import seaborn as sns
import seaborn.objects as so


import seaborn.objects
from seaborn._core.plot import Plot
from seaborn._core.moves import Move
from seaborn._core.scales import Scale
from seaborn._marks.base import Mark
from seaborn._stats.base import Stat


def test_objects_namespace():
def test_plot_nominal_integer():
    p = (
        so.Plot(x=[1, 2, 3], y=[1, 2, 3], color=[1, 2, 3])
        .add(so.Dot())
        .add(so.Dot(), x=[1], y=[1], color=[1])
        .scale(color=so.Nominal())
    )
    p._repr_svg_()



    for name in dir(seaborn.objects):
        if not name.startswith("__"):
            obj = getattr(seaborn.objects, name)
            assert issubclass(obj, (Plot, Mark, Stat, Move, Scale))
