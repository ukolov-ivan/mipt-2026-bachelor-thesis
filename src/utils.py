# pylint: disable=import-outside-toplevel,protected-access
import packaging.version


def compatability():
    '''
    Should be called before tikzplotlib/matplotlib2tikz import
    '''

    import matplotlib
    # pylint: disable-next=line-too-long
    # See https://github.com/matplotlib/matplotlib/blob/42b88d01fdd93846d925b1097167d36ea31c7733/doc/api/prev_api_changes/api_changes_3.9.0/removals.rst?plain=1#L147
    if packaging.version.parse(
            matplotlib.__version__) >= packaging.version.parse("3.9.0"):
        setattr(matplotlib.legend.Legend, "legendHandles",
                property(lambda self: self.legend_handles))
    # See https://github.com/nschloe/tikzplotlib/issues/582
    if packaging.version.parse(matplotlib.__version__) >= packaging.version.parse("3.6.0"):
        import matplotlib.legend
        setattr(matplotlib.legend.Legend, "_ncol",
                property(lambda self: self._ncols))

        import matplotlib.backends.backend_pgf
        # See https://github.com/nschloe/tikzplotlib/issues/559
        setattr(matplotlib.backends.backend_pgf, "common_texification",
                matplotlib.backends.backend_pgf._tex_escape)

        import matplotlib.lines

        # See https://github.com/nschloe/tikzplotlib/issues/580#issuecomment-1628841511
        setattr(matplotlib.lines.Line2D, "_us_dashOffset", property(
            lambda self: self._unscaled_dash_pattern[0]))
        setattr(matplotlib.lines.Line2D, "_us_dashSeq", property(
            lambda self: self._unscaled_dash_pattern[1]))

    import numpy as np
    if packaging.version.parse(
            np.__version__) >= packaging.version.parse("2.0.0"):
        setattr(np, "float_", np.float64)
        setattr(np, "NaN", np.nan)

# TODO: add patches for tikzplotlib
