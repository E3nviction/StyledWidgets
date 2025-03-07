import fabric
from fabric import Application
from fabric.widgets.datetime import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.wayland import WaylandWindow as Window
from styledwidgets import Styled, style
from styledwidgets.agents import textsize, colors, paddings
from styledwidgets.types import rem

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