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
	def __init__(self, advanced_css: bool=True, use_gtk: bool=False, enable_classes: bool=True, **kwargs):
		rules = {
			"classes": "style_classes",
		}
		for key, value in rules.items():
			if key in kwargs:
				kwargs[value] = kwargs.pop(key)
		if "style" in kwargs:
			kwargs["style"] = styler(advanced_css=advanced_css, use_gtk=use_gtk, enable_classes=enable_classes, **kwargs["style"])
		super().__init__(**kwargs)
class StyleProvider:
	def __init__(self, **kwargs):
		self.__dict__.update(style(**kwargs))

	@property
	def build(self):
		return self.__dict__

def style_dict(**dict):
	# convert style_name to style-name
	new_dict = dict.copy()
	for key, value in dict.items():
		if "_" in key:
			new_key = key.replace("_", "-")
			new_dict.pop(key)
			new_dict[new_key] = value
	return new_dict

def styler(*args, advanced_css: bool=True, use_gtk: bool=False, enable_classes: bool | None = None, **dict):
	if dict in [None, {}]:
		if len(args) == 0:
			raise ValueError("No arguments given")
		dict = args[0]
	new_dict = style_dict(**dict)
	enable_classes = True if enable_classes is not None else [key for key in new_dict.keys()][0][0] in ["*", ".", "#"]
	if enable_classes:
		style_string = ""
		for key, value in new_dict.items():
			style = {}
			if key == "default":
				key = "*"
			if not use_gtk and key == "*":
				# We use update, so the order of the styles stays the same, if we were to just __set_item__ it would make everything unset
				style.update({"all": "unset"})
			style.update(value)
			if advanced_css: style = compile_acss(style)
			style_string = style_string + f" {key} {"{"}" + "".join([f"{k}: {v};" for k, v in style.items()]) + f"{"}"}"
		return style_string
	else:
		style = {}
		if not use_gtk:
			# We use update, so the order of the styles stays the same, if we were to just __set_item__ it would make everything unset
			style.update({"all": "unset"})
		style.update(new_dict)
		if advanced_css: style = compile_acss(style)
		style_string = ""
		style_string = style_string + "".join([f"{k}: {v};" for k, v in style.items()])
		return style_string

def on_class(class_):
	return f".{class_}"
def class_(class_): return on_class(class_)

def on_id(id_):
	return f"#{id_}"
def id_(id_): return on_id(id_)

def on_tag(tag):
	return f"{tag}"
def tag(tag): return on_tag(tag)

def on_hover_(): return ":hover"
def on_active_(): return ":active"
def on_focus_(): return ":focus"

on_hover = on_hover_()
on_active = on_active_()
on_focus = on_focus_()