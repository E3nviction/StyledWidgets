from .utils import constrain

def get_alpha(alpha: int) -> float:
	"""Turns a value between 0 and 255 into a value between 0 and 1"""
	alpha = constrain(alpha, 0, 255)
	return alpha / 255

def alpha(color, alpha: float) -> str:
	"""Sets the alpha value of a color"""
	alpha = constrain(alpha)
	return f" alpha({color}, {alpha:.2f}) "

def rgb(r: int, g: int, b: int) -> str:
	"""Sets the rgb value of a color"""
	r,g,b = constrain(r,0,255), constrain(g,0,255), constrain(b,0,255)
	return f" rgb({r}, {g}, {b}) "

def rgba(r: int, g: int, b: int, a: int):
	"""Sets the rgba value of a color"""
	r,g,b,a = constrain(r,0,255), constrain(g,0,255), constrain(b,0,255), constrain(a,0,255)
	return f" alpha(rgb({r}, {g}, {b}), {get_alpha(a):.2f}) "

def hsl(h: int, s: int, l: int) -> str:
	"""Sets the hsl value of a color"""
	h, s, l = constrain(h, 0, 360), constrain(s, 0, 100), constrain(l, 0, 100)
	return f" hsl({h}, {s}%, {l}%) "

def hsla(h: int, s: int, l: int, a: float) -> str:
	"""Sets the hsla value of a color"""
	h, s, l, a = constrain(h, 0, 360), constrain(s, 0, 100), constrain(l, 0, 100), constrain(a, 0, 1)
	return f" alpha(hsl({h}, {s}%, {l}%), {a:.2f}) "

def hex(color: str) -> str:
	"""Sets the hex value of a color"""
	if len(color) > 6:
		raise ValueError(f"Invalid hex color: {color}")
	return f" #{color} "

def hexa(color, a: float):
	"""Sets the hexa value of a color"""
	a = constrain(a, 0, 1)
	return alpha(hex(color), a)

def color(color: str) -> str:
    if len(color) == 4:  # #rgb -> #rrggbb
        r, g, b = [int(color[i] * 2, 16) for i in (1, 2, 3)]
        return rgb(r, g, b)

    if len(color) == 5:  # #rgba -> #rrggbbaa
        r, g, b, a = [int(color[i] * 2, 16) for i in (1, 2, 3, 4)]
        return rgba(r, g, b, a)

    if len(color) == 7:  # #rrggbb
        r, g, b = [int(color[i:i+2], 16) for i in (1, 3, 5)]
        return rgb(r, g, b)

    if len(color) == 9:  # #rrggbbaa
        r, g, b, a = [int(color[i:i+2], 16) for i in (1, 3, 5, 7)]
        return rgba(r, g, b, a)

    raise ValueError("Invalid color format")

def get_rgba(color):
    if len(color) == 4:  # #rgb -> #rrggbb
        r, g, b = [int(color[i] * 2, 16) for i in (1, 2, 3)]
        r, g, b = constrain(r, 0, 255), constrain(g, 0, 255), constrain(b, 0, 255)
        return r, g, b, 255

    if len(color) == 5:  # #rgba -> #rrggbbaa
        r, g, b, a = [int(color[i] * 2, 16) for i in (1, 2, 3, 4)]
        r, g, b, a = constrain(r, 0, 255), constrain(g, 0, 255), constrain(b, 0, 255), constrain(a, 0, 255)
        return r, g, b, a

    if len(color) == 7:  # #rrggbb
        r, g, b = [int(color[i:i+2], 16) for i in (1, 3, 5)]
        r, g, b = constrain(r, 0, 255), constrain(g, 0, 255), constrain(b, 0, 255)
        return r, g, b, 255

    if len(color) == 9:  # #rrggbbaa
        r, g, b, a = [int(color[i:i+2], 16) for i in (1, 3, 5, 7)]
        r, g, b, a = constrain(r, 0, 255), constrain(g, 0, 255), constrain(b, 0, 255), constrain(a, 0, 255)
        return r, g, b, a

    raise ValueError("Invalid color format")

def hex_to_rgba(color):
    r, g, b, a = get_rgba(color)
    return rgba(r, g, b, a)

def rgba_to_hex(rgba):
    r, g, b, a = constrain(rgba[0], 0, 255), constrain(rgba[1], 0, 255), constrain(rgba[2], 0, 255), constrain(rgba[3], 0, 1)
    return hexa(f"{r:02x}{g:02x}{b:02x}", a)

def rgba_add(rgba, add, add_alpha: bool=False):
    r, g, b, a = rgba
    r, g, b, a = constrain(r, 0, 255), constrain(g, 0, 255), constrain(b, 0, 255), constrain(a, 0, 255)
    if add_alpha:
        a = constrain(a + add, 0, 255)
    else:
        r = constrain(r + add, 0, 255)
        g = constrain(g + add, 0, 255)
        b = constrain(b + add, 0, 255)
    return r, g, b, a