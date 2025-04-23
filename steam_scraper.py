#!/usr/bin/env python3

"""
Steam Reviews Scraper
---------------------
Downloads the first *N* reviews for a list of Steam app IDs and saves them
to a single CSV file.

Usage:
    python steam_scraper.py --apps 730 570 578080 --limit 4000 --outfile reviews.csv

Arguments:
    --apps      One or more Steam app IDs (integers).
    --limit     Total reviews per app ID to fetch (default 10_000).
    --outfile   Path of output CSV file (default steam_reviews.csv).

Notes:
    * The Steam store review endpoint is public and does not require an API key.
    * The script sleeps 0.4 s between requests to respect Steam’s rate limits.
    * Each request fetches up to 100 reviews; the `cursor` parameter is used
      for pagination.
"""

import requests
import time
import csv
import argparse
from typing import List, Tuple

STEAM_REVIEW_ENDPOINT = (
    "https://store.steampowered.com/appreviews/{app_id}"
)

def fetch_reviews(app_id: int, limit: int = 10000, rate_delay: float = 0.4) -> List[Tuple]:
    """Fetch up to *limit* reviews for a single Steam `app_id`.

    Returns a list of tuples:
        (recommendation_id, timestamp_created, voted_up, review_body)
    """
    reviews: List[Tuple] = []
    cursor = "*"
    while len(reviews) < limit:
        params = {
            "json": 1,
            "num_per_page": 100,
            "filter": "all",
            "cursor": cursor,
        }
        response = requests.get(
            STEAM_REVIEW_ENDPOINT.format(app_id=app_id),
            params=params,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        # If Steam returns an error or there are no more reviews, stop.
        if data.get("success") != 1 or not data.get("reviews"):
            break

        for r in data["reviews"]:
            reviews.append(
                (
                    r["recommendationid"],
                    r["timestamp_created"],
                    r["voted_up"],
                    r["review"].replace("\r", " ").replace("\n", " ").strip(),
                )
            )
            if len(reviews) >= limit:
                break

        cursor = data["cursor"]
        time.sleep(rate_delay)

    return reviews


def write_csv(rows: List[Tuple], outfile: str) -> None:
    header = ["id", "unix_time", "thumbs_up", "text"]
    with open(outfile, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Steam review scraper")
    parser.add_argument(
        "--apps",
        type=int,
        nargs="+",
        required=True,
        help="One or more Steam app IDs (e.g., 730 570)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10000,
        help="Maximum reviews per app (default 10000)",
    )
    parser.add_argument(
        "--outfile",
        type=str,
        default="steam_reviews.csv",
        help="Output CSV file path",
    )
    args = parser.parse_args()

    all_reviews: List[Tuple] = []
    for app in args.apps:
        print(f"Fetching up to {args.limit} reviews for app {app} …")
        app_reviews = fetch_reviews(app, limit=args.limit)
        print(f"  ↳ retrieved {len(app_reviews):,} rows")
        all_reviews.extend(app_reviews)

    write_csv(all_reviews, args.outfile)
    print(f"Done! Total rows written: {len(all_reviews):,}")
    print(f"CSV saved to: {args.outfile}")


if __name__ == "__main__":
    main()
