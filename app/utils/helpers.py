
def argb_to_hex(a, r, g, b) -> str:
    """
    Convert ARGB values to a hexadecimal color string.

    :param a: Alpha component (0-255)
    :param r: Red component (0-255)
    :param g: Green component (0-255)
    :param b: Blue component (0-255)
    :return: Hexadecimal color string (e.g., '#AARRGGBB')
    """
    return f"#{a:02X}{r:02X}{g:02X}{b:02X}"

def lighten_color(hex_color, ratio) -> str:

    amount = int(255 * ratio)

    hex_int = int(hex_color.lstrip('#'), 16)
    amount = max(0, min(255, amount))
    
    # Extract the RGB components from the hex value
    red = (hex_int >> 16) & 0xFF
    green = (hex_int >> 8) & 0xFF
    blue = hex_int & 0xFF
    
    # Recombine the new alpha with the original RGB components back into a hex value
    new_hex = (amount << 24) | (red << 16) | (green << 8) | blue

    
    return f"#{hex(new_hex)[2:].upper().zfill(8)}"