from collections.abc import Iterable
from math import cos, pi, sin
from hints.lite import lite


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


def _squared_distance(first: Point, second: Point) -> float:
    return (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2


def _is_internal_area_edge(
        start: Point,
        end: Point,
        city_index: int,
        points: list[Point],
        radii: list[float],
        area_keys: list[object]
) -> bool:
    midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    city_distance = _squared_distance(midpoint, points[city_index])

    for other_index, other_point in enumerate(points):
        if other_index == city_index or area_keys[other_index] != area_keys[city_index]:
            continue
        if _squared_distance(points[city_index], other_point) <= _EPSILON:
            continue

        other_distance = _squared_distance(midpoint, other_point)
        tolerance = max(1.0, city_distance, other_distance) * 1e-7

        if abs(city_distance - other_distance) > tolerance:
            continue

        other_radius_squared = radii[other_index] ** 2 + tolerance
        if (
                _squared_distance(start, other_point) <= other_radius_squared
                and _squared_distance(end, other_point) <= other_radius_squared
        ):
            return True

    return False


def build_visible_edges(
        cells: list[Polygon],
        points: list[Point],
        radii: list[float],
        area_keys: list[object]
) -> list[tuple[Point, Point, int]]:
    """Return boundary edges, excluding borders inside the same area."""
    visible_edges = []

    for city_index, cell in enumerate(cells):
        if len(cell) < 2:
            continue

        for start, end in zip(cell, cell[1:] + cell[:1]):
            if not _is_internal_area_edge(
                    start,
                    end,
                    city_index,
                    points,
                    radii,
                    area_keys
            ):
                visible_edges.append((start, end, city_index))

    return visible_edges


def build_internal_edges(
        cells: list[Polygon],
        points: list[Point],
        radii: list[float],
        area_keys: list[object]
) -> list[tuple[Point, Point, int]]:
    """Return shared edges that must blend into the fill of one area."""
    internal_edges = []

    for city_index, cell in enumerate(cells):
        if len(cell) < 2:
            continue

        for start, end in zip(cell, cell[1:] + cell[:1]):
            if _is_internal_area_edge(
                    start,
                    end,
                    city_index,
                    points,
                    radii,
                    area_keys
            ):
                internal_edges.append((start, end, city_index))

    return internal_edges


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
                seeds.append((city.location.x, city.location.y, city, area))

    points = [(x, y) for x, y, _city, _area in seeds]
    radii = [max_distance] * len(seeds)
    area_keys = [area.name for _x, _y, _city, area in seeds]
    fill_colors = [
        lite(area.color, -120)
        for _x, _y, _city, area in seeds
    ]

    cells = build_voronoi_cells(
        points,
        bounds,
        max_distance=max_distance
    )
    object_ids = []

    # Draw every fill first. Outlines are separate objects so shared borders
    # between cities in the same area can be omitted.
    for city_index, ((_x, _y, _city, _area), cell) in enumerate(zip(seeds, cells)):
        if len(cell) < 3:
            continue

        object_id = display.add_id()
        display.create_polygon(
            cell,
            color=fill_colors[city_index],
            outline="",
            tag=object_id
        )
        object_ids.append(object_id)

    for start, end, city_index in build_visible_edges(
            cells,
            points,
            radii,
            area_keys
    ):
        object_id = display.add_id()
        display.create_line(
            start[0],
            start[1],
            end[0],
            end[1],
            color=seeds[city_index][3].color,
            tag=object_id
        )
        object_ids.append(object_id)

    # A larger cell can have a longer bisector than its smaller neighbour.
    # Paint the genuinely shared part last so no internal outline remains.
    for start, end, city_index in build_internal_edges(
            cells,
            points,
            radii,
            area_keys
    ):
        object_id = display.add_id()
        display.create_line(
            start[0],
            start[1],
            end[0],
            end[1],
            color=fill_colors[city_index],
            tag=object_id
        )
        object_ids.append(object_id)

    return object_ids
