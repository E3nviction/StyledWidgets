from typing import Any
from .color import get_rgba, rgba_to_hex, rgba_add

class Shared:
	def __init__(self, micro=None, tiny=None, small=None, normal=None, big=None, large=None, macro=None, giganto=None, massive=None, huge=None, gigafantastico=None, endless=None):
		self.micro          = "0.4rem" if micro          is None else micro
		self.tiny           = "0.6rem" if tiny           is None else tiny
		self.small          = "0.8rem" if small          is None else small
		self.normal         = "1rem"   if normal         is None else normal
		self.big            = "1.2rem" if big            is None else big
		self.large          = "1.4rem" if large          is None else large
		self.macro          = "1.6rem" if macro          is None else macro
		self.giganto        = "2rem"   if giganto        is None else giganto
		self.massive        = "2.4rem" if massive        is None else massive
		self.huge           = "2.8rem" if huge           is None else huge
		self.gigafantastico = "3rem"   if gigafantastico is None else gigafantastico
		self.endless        = "3.2rem" if endless        is None else endless
	def __call__(self, *args: Any, **kwds: Any) -> bool:
		return True

class Contrast:
	def __init__(self, val):
		self.rgba = get_rgba(val)
		self.val = val
		"""Normal"""
		self.one = self.val
		"""Normal"""
		self.two = rgba_to_hex(rgba_add(self.rgba, 20))
		"""Bright"""
		self.three = rgba_to_hex(rgba_add(self.rgba, 30))
		"""Brighter"""
		self.four = rgba_to_hex(rgba_add(self.rgba, 40))
		"""Brightest"""
		self.five = rgba_to_hex(rgba_add(self.rgba, -20))
		"""Dark"""
		self.six = rgba_to_hex(rgba_add(self.rgba, -30))
		"""Darker"""
		self.seven = rgba_to_hex(rgba_add(self.rgba, -40))
		"""Darkest"""

	def __call__(self, val):
		return rgba_to_hex(rgba_add(self.rgba, val))

	def __repr__(self):
		return self.val

	def __str__(self):
		return str(self.val)
class Colors:
	def __init__(self):
		self.transparent = "transparent"
		self.none        = "none"
		self.black   = Contrast("#000000")
		self.gray    = Contrast("#555555")
		self.white   = Contrast("#ffffff")
		self.red     = Contrast("#ff4444")
		self.green   = Contrast("#aaff88")
		self.blue    = Contrast("#007aff")
		self.yellow  = Contrast("#dddd66")
		self.magenta = Contrast("#ff66ff")
		self.cyan    = Contrast("#aadddd")
		self.orange  = Contrast("#ffaa55")
		self.gold    = Contrast("#ffaf33")
class Shadows:
    def __init__(self):
        self.none        = "0 0 transparent"
        self.sm          = "0px 1px 2px rgba(0, 0, 0, 0.1)"
        self.md          = "0px 4px 6px rgba(0, 0, 0, 0.1), 0px 2px 4px rgba(0, 0, 0, 0.06)"
        self.lg          = "0px 10px 15px rgba(0, 0, 0, 0.1), 0px 4px 6px rgba(0, 0, 0, 0.05)"
        self.xl          = "0px 20px 25px rgba(0, 0, 0, 0.1), 0px 10px 10px rgba(0, 0, 0, 0.04)"
        self.xxl         = "0px 25px 50px rgba(0, 0, 0, 0.25)"
        self.inner       = "inset 0px 2px 4px rgba(0, 0, 0, 0.06)"
        self.intense     = "0px 30px 60px rgba(0, 0, 0, 0.3), 0px 10px 20px rgba(0, 0, 0, 0.2)"
        self.soft_glow   = "0px 0px 10px rgba(255, 255, 255, 0.5)"
        self.deep        = "0px 35px 60px rgba(0, 0, 0, 0.3)"
        self.light_hover = "0px 4px 6px rgba(0, 0, 0, 0.15)"
        self.dark_hover  = "0px 8px 16px rgba(0, 0, 0, 0.3)"
        self.glow        = "0px 0px 8px rgba(0, 255, 255, 0.6)"
        self.neumorphism = "5px 5px 10px rgba(0, 0, 0, 0.2), -5px -5px 10px rgba(255, 255, 255, 0.8)"
class Margins(Shared):
	def __init__(self):
		super().__init__(normal=".5rem")
	def __call__(self, *args: Any, **kwds: Any) -> bool:
		return True
class TextSize(Shared):
	def __init__(self):
		super().__init__()
	def __call__(self, *args: Any, **kwds: Any) -> bool:
		return True
class Paddings(Shared):
	def __init__(self):
		super().__init__(normal=".25rem")
	def __call__(self, *args: Any, **kwds: Any) -> bool:
		return True

class Transitions:
	def __init__(self):
		self.none    = "none"
		self.ease = "ease"
		self.ease_in = "ease-in"
		self.ease_out = "ease-out"
		self.ease_in_out = "ease-in-out"
		self.ease_bouncy = "cubic-bezier(0.175, 0.885, 0.32, 1.275)"

		self.prop = "all"
		self.ease_function = self.ease_in_out
		self.ultra_slow = f"{self.prop} 2000ms {self.ease_function}"
		self.tea_time   = f"{self.prop} 1000ms {self.ease_function}"
		self.slowest    = f"{self.prop} 500ms {self.ease_function}"
		self.slower     = f"{self.prop} 400ms {self.ease_function}"
		self.medium     = f"{self.prop} 300ms {self.ease_function}"
		self.normal     = f"{self.prop} 200ms {self.ease_function}"
		self.fast       = f"{self.prop} 100ms {self.ease_function}"
		self.faster     = f"{self.prop} 50ms {self.ease_function}"
		self.fastest    = f"{self.prop} 20ms {self.ease_function}"
		self.sonic      = f"{self.prop} 10ms {self.ease_function}"

	def set_prop(self, prop):
		self.prop = prop
		return self

	def set_ease_function(self, function):
		self.ease_function = function
		return self
	def __call__(self, *args: Any, **kwds: Any) -> bool:
		return True

class BorderRadius(Shared):
	def __init__(self):
		super().__init__(
			micro = "0.3rem",
			tiny = "0.4rem",
			small = "0.5rem",
			normal = ".75rem",
			big = "1rem",
			large = "1.2rem",
			macro = "1.4rem",
			giganto = "1.6rem",
			massive = "1.8rem",
			huge = "2rem",
			gigafantastico = "3rem",
			endless = "50%"
		)
	def __call__(self, *args: Any, **kwds: Any) -> bool:
		return True

textsize = TextSize()
"""
	textsize.micro          = "0.4rem"
	textsize.tiny           = "0.6rem"
	textsize.small          = "0.8rem"
	textsize.normal         = "1rem"
	textsize.big            = "1.2rem"
	textsize.large          = "1.4rem"
	textsize.macro          = "1.6rem"
	textsize.giganto        = "2rem"
	textsize.massive        = "2.4rem"
	textsize.huge           = "2.8rem"
	textsize.gigafantastico = "3rem"
	textsize.endless        = "3.2rem"
"""
colors = Colors()
"""
	colors.any_color.one=Normal Color
	colors.any_color.two=Bright Color
	colors.any_color.three=Brighter Color
	colors.any_color.four=Brightest Color
	colors.any_color.five=Dark Color
	colors.any_color.six=Darker Color
	colors.any_color.seven=Darkest Color
"""
shadows = Shadows()

margins = Margins()
"""
	margins.micro          = "0.4rem"
	margins.tiny           = "0.6rem"
	margins.small          = "0.8rem"
	margins.normal         = "0.5rem"
	margins.big            = "1.2rem"
	margins.large          = "1.4rem"
	margins.macro          = "1.6rem"
	margins.giganto        = "2rem"
	margins.massive        = "2.4rem"
	margins.huge           = "2.8rem"
	margins.gigafantastico = "3rem"
	margins.endless        = "3.2rem"
"""
paddings = Paddings()
"""
	paddings.micro          = "0.4rem"
	paddings.tiny           = "0.6rem"
	paddings.small          = "0.8rem"
	paddings.normal         = "0.25rem"
	paddings.big            = "1.2rem"
	paddings.large          = "1.4rem"
	paddings.macro          = "1.6rem"
	paddings.giganto        = "2rem"
	paddings.massive        = "2.4rem"
	paddings.huge           = "2.8rem"
	paddings.gigafantastico = "3rem"
	paddings.endless        = "3.2rem"
"""

transitions = Transitions()
"""
	ultra_slow = "2000ms"
	tea_time   = "1000ms"
	slowest    = "500ms"
	slower     = "400ms"
	medium     = "300ms"
	normal     = "200ms"
	fast       = "100ms"
	faster     = "50ms"
	fastest    = "20ms"
	sonic      = "10ms"
"""

borderradius = BorderRadius()
"""
	micro = "0.3rem",
	tiny = "0.4rem",
	small = "0.5rem",
	normal = ".75rem",
	big = "1rem",
	large = "1.2rem",
	macro = "1.4rem",
	giganto = "1.6rem",
	massive = "1.8rem",
	huge = "2rem",
	gigafantastico = "3rem",
	endless = "50%"
"""