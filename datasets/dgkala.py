import json
from typing import Any, Dict, List, TypedDict

import requests


# Type definitions
class Reactions(TypedDict):
    likes: int
    dislikes: int


class Comment(TypedDict):
    id: int
    title: str
    body: str
    created_at: str
    rate: int
    reactions: Reactions
    is_buyer: bool
    user_name: str
    is_anonymous: bool


def save_comments_to_json(
    comments: List[Comment],
    filename: str = "comments.json",
) -> None:
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(comments, f, indent=4)


def get_comments(
    sess: requests.Session,
    product_id: int,
    page: int = 1,
) -> List[Comment]:
    r = sess.get(
        f"https://api.digikala.com/v1/product/{product_id}/comments/?page={page}"
    )
    if r.ok:
        return r.json()["data"]["comments"]
    return []


if __name__ == "__main__":
    c = get_comments(requests.Session(), 3493882)
    save_comments_to_json(c)
