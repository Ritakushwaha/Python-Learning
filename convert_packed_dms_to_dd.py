def dms_to_decimal(degree, minute, second, direction):
    decimal = degree + minute / 60 + second / 3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

def convert_packed_dms(packed_dms):
    # Split coordinates from direction
    directions = packed_dms[-1]
    coordinates = packed_dms[:-1]
    
    # Extract degrees, minutes, and seconds
    degrees = int(coordinates[:2])
    minutes = int(coordinates[2:4])
    seconds = float(coordinates[4:])
    
    return dms_to_decimal(degrees, minutes, seconds, directions)

# List of coordinates in packed DMS format
packed_dms_coords = [
    "352215.78N", "0041448.71E",
    "352351.58N", "0041637.08E",
    "324554.53N", "0883049.65W",
    "324016.54N", "0883153.19W",
    "374733.00S", "1450640.30E",
    "374606.50S", "1445054.20E"
]

# Convert each packed DMS to decimal degrees
decimal_coords = [[coord,convert_packed_dms(coord)] for coord in packed_dms_coords]

# Print the converted coordinates
for coord in decimal_coords:
    print(coord)
