from collections.abc import Iterable
from math import cos, pi, sin


Point = tuple[float, float]
Polygon = list[Point]
Bounds = tuple[float, float, float, float]

_EPSILON = 1e-9


def _circle(center: Point, radius: float, number_of_sides: int = 48) -> Polygon:
    return [
        (
            center[0] + cos(2 * pi * index / number_of_sides) * radius,
            center[1] + sin(2 * pi * index / number_of_sides) * radius
        )
        for index in range(number_of_sides)
    ]


def _clip_to_bounds(polygon: Polygon, bounds: Bounds) -> Polygon:
    x1, y1, x2, y2 = bounds

    for a, b, c in (
            (1, 0, x2),
            (-1, 0, -x1),
            (0, 1, y2),
            (0, -1, -y1)
    ):
        polygon = _clip_polygon(polygon, a, b, c)

    return polygon


def _blend_colors(foreground: str, background: str, opacity: float) -> str:
    """Pre-blend a colour because tkinter Canvas has no alpha channel."""
    foreground_rgb = [int(foreground[index:index + 2], 16) for index in (1, 3, 5)]
    background_rgb = [int(background[index:index + 2], 16) for index in (1, 3, 5)]
    blended = [
        round(front * opacity + back * (1 - opacity))
        for front, back in zip(foreground_rgb, background_rgb)
    ]
    return "#" + "".join(f"{component:02x}" for component in blended)


def _inside_half_plane(point: Point, a: float, b: float, c: float) -> bool:
    return a * point[0] + b * point[1] <= c + _EPSILON


def _line_intersection(
        start: Point,
        end: Point,
        a: float,
        b: float,
        c: float
) -> Point:
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    denominator = a * dx + b * dy

    if abs(denominator) <= _EPSILON:
        return start

    distance = (c - a * start[0] - b * start[1]) / denominator
    return start[0] + distance * dx, start[1] + distance * dy


def _clip_polygon(polygon: Polygon, a: float, b: float, c: float) -> Polygon:
    """Clip a polygon by the half-plane a*x + b*y <= c."""
    if not polygon:
        return []

    result = []
    previous = polygon[-1]
    previous_inside = _inside_half_plane(previous, a, b, c)

    for current in polygon:
        current_inside = _inside_half_plane(current, a, b, c)

        if current_inside != previous_inside:
            result.append(_line_intersection(previous, current, a, b, c))
        if current_inside:
            result.append(current)

        previous = current
        previous_inside = current_inside

    return result


def build_voronoi_cells(
        points: Iterable[Point],
        bounds: Bounds,
        max_distance: float | None = None
) -> list[Polygon]:
    """Build non-overlapping Voronoi cells, optionally limited around cities."""
    points = list(points)
    x1, y1, x2, y2 = bounds
    canvas = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
    cells = []

    if max_distance is not None and max_distance <= 0:
        raise ValueError("max_distance must be greater than zero")

    for point_index, point in enumerate(points):
        if max_distance is None:
            cell = canvas.copy()
        else:
            cell = _clip_to_bounds(_circle(point, max_distance), bounds)

        for other_index, other in enumerate(points):
            if point_index == other_index:
                continue

            dx = other[0] - point[0]
            dy = other[1] - point[1]

            # Two cities cannot own different territory from the same point.
            # Resolve an exact tie deterministically in favour of the first one.
            if abs(dx) <= _EPSILON and abs(dy) <= _EPSILON:
                if other_index < point_index:
                    cell = []
                    break
                continue

            # Points on this side of the perpendicular bisector are closer
            # to `point` than to `other`.
            a = dx
            b = dy
            c = (
                other[0] ** 2 + other[1] ** 2
                - point[0] ** 2 - point[1] ** 2
            ) / 2
            cell = _clip_polygon(cell, a, b, c)

            if not cell:
                break

        cells.append(cell)

    return cells


def create_area_backgrounds(
        display,
        countries,
        bounds: Bounds,
        max_distance: float,
        background_color: str
) -> list[str]:
    """Draw one Voronoi cell per city and colour it with its area's colour."""
    seeds = []

    for country in countries.values():
        for area in country.areas.values():
            for city in area.cities.values():
                seeds.append((city.location.x, city.location.y, area))

    cells = build_voronoi_cells(
        ((x, y) for x, y, _area in seeds),
        bounds,
        max_distance=max_distance
    )
    object_ids = []

    for (_x, _y, area), cell in zip(seeds, cells):
        if len(cell) < 3:
            continue

        object_id = display.add_id()
        display.create_polygon(
            cell,
            color=_blend_colors(area.color, background_color, opacity=0.24),
            tag=object_id
        )
        object_ids.append(object_id)

    return object_ids
