CREATE TABLE coordinates_dms (
    lat_degrees INTEGER,
    lat_minutes INTEGER,
    lat_seconds NUMERIC,
    lat_direction CHAR(1),
    lon_degrees INTEGER,
    lon_minutes INTEGER,
    lon_seconds NUMERIC,
    lon_direction CHAR(1)
);

INSERT INTO coordinates_dms (lat_degrees, lat_minutes, lat_seconds, lat_direction, lon_degrees, lon_minutes, lon_seconds, lon_direction)
VALUES
    (51, 15, 44, 'N', 179, 6, 31, 'W'),
    (71, 23, 25, 'N', 156, 28, 30, 'W');

SELECT
    dms_to_dd(lat_degrees, lat_minutes, lat_seconds, lat_direction) AS latitude_dd,
    dms_to_dd(lon_degrees, lon_minutes, lon_seconds, lon_direction) AS longitude_dd
FROM
    coordinates_dms;
