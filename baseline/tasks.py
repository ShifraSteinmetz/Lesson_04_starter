"""Lesson 4 homework: baseline tasks (reference solution)."""
import json
from pathlib import Path


import json


def count_selected(media_ids: list[str]) -> int:
    """Return the number of DIFFERENT media ids."""
    return len(set(media_ids))


def group_by_gallery(media: list[dict]) -> dict[str, list[str]]:
    """Group media items {"gallery_id": ..., "id": ...} by gallery.
    Return a dict: gallery id -> list of media ids, in input order.
    """
<<<<<<< HEAD
    groups: dict[str, list[str]] = {}
    for item in media:
        groups.setdefault(item["gallery_id"], []).append(item["id"])
    return groups
=======
    result = {}

    for med in media:
        gallery_id = med["gallery_id"]
        if gallery_id not in result:
            result[gallery_id] = []

        result[gallery_id].append(med["id"])

    return result    
>>>>>>> Lesson_04


def total_price(prices_minor: list[int | None]) -> int:
    """Return the sum of the prices (in agorot), ignoring None."""
<<<<<<< HEAD
    return sum(p for p in prices_minor if p is not None)
=======
    total = 0

    for price in prices_minor:
        if price != None:
            total = total + price

    return total
>>>>>>> Lesson_04


def first_missing(required: list[str], present: list[str]) -> str | None:
    """Return the first item of `required` that is not in `present`, or None."""
<<<<<<< HEAD
    present_set = set(present)
    for item in required:
        if item not in present_set:
            return item
=======
    for item in required:
        if item not in present:
            return item

>>>>>>> Lesson_04
    return None


def load_events(path) -> list[dict]:
    """Read a JSON file encoded in UTF-8 and return its content (a list of events)."""
<<<<<<< HEAD
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)
=======
    with open(path, "r", encoding="utf-8") as file:
        events = json.load(file)

    return events
>>>>>>> Lesson_04
