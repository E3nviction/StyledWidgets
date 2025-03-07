# StyledWidgets

StyledWidgets is a Python library designed to simplify the styling of widgets for [Fabric](https://github.com/Fabric-Development/fabric). It provides a set of utilities and classes to handle colors, dimensions, and styles in a consistent and easy-to-use manner.

## Features

- **Color Utilities**: Functions to handle color transformations and conversions.
- **Dimension Utilities**: Functions to handle various units like px, em, rem, etc.
- **Styled Classes**: Base classes to create styled widgets easily.
- **Agents**: Predefined styles for text sizes, colors, shadows, margins, and paddings.

## Installation

To use StyledWidgets, you need to have [Pip](https://pypi.org/project/pip/) installed.

```bash
pip install git+https://github.com/E3nviction/StyledWidgets.git
```

## Usage

### Example

Here is an example of how to create a simple status bar with a date-time widget:

```py
import fabric
from fabric import Application
from fabric.widgets.datetime import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.wayland import WaylandWindow as Window
from styledwidgets import Styled, style
from styledwidgets.agents import textsize, colors, paddings

class MyDateTime(Styled, DateTime):
    def __init__(self, **kwargs):
        super().__init__(
            style=style(
                color=colors.white,
                font_weight="bold",
                font_family="cantarell, sans-serif",
                font_size=textsize.normal,
                padding=paddings.small,
            ),
            **kwargs
        )

class StatusBar(Styled, Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="top",
            anchor="left top right",
            style=style(
                background_color=colors.black,
            ),
            exclusivity="auto",
            **kwargs
        )

        self.date_time = MyDateTime(formatters=["%d %b %H:%M"])
        self.children = CenterBox(center_children=self.date_time)

if __name__ == "__main__":
    bar = StatusBar()
    app = Application("bar-example", bar)
    app.run()
```

## Documentation

### Agents

#### Shared

This agent class provides predefined dimensions for various sizes, including micro, tiny, small, normal, big, large, macro, giganto, massive, huge, gigafantastico, and endless.

#### colors

This agent provides predefined colors, including blue, black, `gray`, `white`, `red`, `green`, `yellow`, `magenta`, `cyan`, `orange`, `gold`, and `transparent`. It also supports different levels of brightness for each color, these can be achieved by using the methods `one`, `two`, `three`, `four`, `five`, `six`, and `seven`.

#### shadows

This agent provides predefined shadows for various use cases, including none, sm, md, lg, xl, xxl, inner, intense, soft_glow, deep, light_hover, dark_hover, glow, neumorphism

#### margins

This agent provides predefined margins, see [Shared](#shared)

#### textsize

This agent provides predefined text sizes, see [Shared](#shared)

#### paddings

This agent provides predefined paddings, see [Shared](#shared)

### Color Utilities (color.py)

This module provides functions to handle color transformations and conversions.

### Types (types.py)

This module provides classes to handle various units like px, em, rem, etc.

All Units:
- px
- em
- rem
- percent
- vh
- vw
- vmin
- vmax
- deg
- rad
- turn
- ms
- s
- cm
- mm
- in_
- pc
- pt
- ch

## Styled (styled.py)

This module provides base classes to create styled widgets easily.

- class Styled
  - This class is the base class for all styled widgets.
- class StyleProvider
  - This class is used to create a style dictionary, with acss.
- style
  - This function is used to create a style dictionary on-the-go, with acss.
- compile_acss
  - This function is used to compile acss to css.

### What is acss?

```txt
acss–or Advanced CSS, is a CSS version more python friendly.

It converts the arguments from the style or StyleProvider into gtk
supportable css.

This is done by converting any argument from underscore_arguments to
dash-arguments.

And any hex color with alpha to alpha(hex, alpha), so #ffffffaa becomes
alpha(#ffffff, 0.67).
```

## Contributing

Contributions are welcome! Please open an issue or submit a PR.

## License

This project is licensed under the MIT License.  

This means you can use, modify, and distribute this project as you see fit.  
  
See the [LICENSE](LICENSE) file for more details.
