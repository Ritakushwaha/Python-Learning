# Function to convert coordinates from degrees, minutes, seconds to decimal degrees
def dms_to_dd(degrees, minutes, seconds, direction):
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    if direction in ['W', 'S']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

coords_dms = [
    (51, 15, 44, 'N', 179, 6, 31, 'W'),
    (71, 23, 25, 'N', 156, 28, 30, 'W')
]

coords_dd = [(dms_to_dd(lat_deg, lat_min, lat_sec, lat_dir), dms_to_dd(lon_deg, lon_min, lon_sec, lon_dir))
             for lat_deg, lat_min, lat_sec, lat_dir, lon_deg, lon_min, lon_sec, lon_dir in coords_dms]

print(coords_dd)
