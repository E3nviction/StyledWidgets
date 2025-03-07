from .color import rgba

def compile_acss(style):
	if isinstance(style, Styled):
		style = style.__dict__
	style_new = style
	for key, value in style.items():
		if isinstance(value, str):
			value = value.strip()
			if value.startswith("#"):
				match len(value):
					case 4:
						style_new[key] = value
					case 7:
						style_new[key] = value
					case 9:
						style_new[key] = rgba(*[int(value[i:i+2], 16) for i in (1, 3, 5, 7)])
					case 5:
						style_new[key] = rgba(*[int(value[i:i+2], 16) for i in (1, 2, 3, 4)])
					case _:
						raise ValueError(f"Invalid hex color: {value}")

	return style_new
class Styled:
	def __init__(self, advanced_css: bool=True, use_gtk: bool=False, **kwargs):
		rules = {
			"classes": "style_classes",
		}
		for key, value in rules.items():
			if key in kwargs:
				kwargs[value] = kwargs.pop(key)
		if "style" in kwargs:
			style = {}
			if not use_gtk:
				# We use update, so the order of the styles stays the same, if we were to just __set_item__ it would make everything unset
				style.update({"all": "unset"})
			style.update(kwargs.pop("style"))
			if advanced_css:
				style = compile_acss(style)
			style_string = ""
			style_string = style_string + "".join([f"{k}: {v};" for k, v in style.items()])
			kwargs["style"] = style_string
		super().__init__(**kwargs)
class StyleProvider:
	def __init__(self, **kwargs):
		self.__dict__.update(style(**kwargs))

	@property
	def build(self):
		return self.__dict__
def style(**dict):
	# convert style_name to style-name
	new_dict = dict.copy()
	for key, value in dict.items():
		if "_" in key:
			new_key = key.replace("_", "-")
			new_dict.pop(key)
			new_dict[new_key] = value
	return new_dict
