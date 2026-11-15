"""Lesson 4 homework: baseline tasks (reference solution)."""
import json
from pathlib import Path


def count_selected(media_ids: list[str]) -> int:
    return len(set(media_ids))


def group_by_gallery(media: list[dict]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for item in media:
        groups.setdefault(item["gallery_id"], []).append(item["id"])
    return groups


def total_price(prices_minor: list[int | None]) -> int:
    return sum(p for p in prices_minor if p is not None)


def first_missing(required: list[str], present: list[str]) -> str | None:
    present_set = set(present)
    for item in required:
        if item not in present_set:
            return item
    return None


def load_events(path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)
