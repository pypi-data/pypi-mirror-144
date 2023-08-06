from __future__ import annotations

import itertools
import logging
import math
from collections import defaultdict
from typing import Dict, List, Set, Tuple

from . import query

logger = logging.getLogger(__name__)


def cluster(
    matches, cluster_size: int = 3, cluster_dist: float = 20
) -> Tuple[List[query.Cluster], List[query.Cluster]]:
    logger.info("Clustering matches...")
    logger.debug(f"cluster_dist: {cluster_dist} samples")
    clusters = set()
    votes = ght(matches, cluster_dist)
    for source, bins in votes.items():
        for bin, cluster in bins.items():
            if len(cluster) >= cluster_size:
                clusters.add(frozenset(cluster))
    clusters = [query.Cluster(list(c)) for c in clusters]
    total_clusters = [query.Cluster(list(c)) for bins in votes.values() for c in bins.values()]
    return clusters, total_clusters


def ght(matches: List[query.Match], cluster_dist: float = 20) -> Dict[str, Dict[Tuple[float, float], Set[query.Match]]]:
    votes = defaultdict(lambda: defaultdict(set))
    try:
        dim = max(m.neighbors[0].keypoint.scale for m in matches)
    except:
        dim = 2
    for match in matches:
        ds = round_to(match.keypoint.scale / match.neighbors[0].keypoint.scale, 2)
        d_theta = round_to(match.keypoint.orientation - match.neighbors[0].keypoint.orientation, 0.4)
        dx = round_to(match.keypoint.x - match.neighbors[0].keypoint.x, 1.5 * dim)
        dy = round_to(match.keypoint.y - match.neighbors[0].keypoint.y, 1.5 * dim)
        bins = itertools.product(*(dx, dy))
        for bin in bins:
            train_kps = [tuple(m.neighbors[0].keypoint.kp[:2]) for m in votes[match.neighbors[0].source_id][bin]]
            x = [m.neighbors[0].keypoint.x for m in votes[match.neighbors[0].source_id][bin]]
            try:
                min_x = min(x)
                max_x = max(x)
            except:
                min_x = max_x = match.neighbors[0].keypoint.x
            if tuple(match.neighbors[0].keypoint.kp[:2]) not in train_kps:
                if min_x - cluster_dist < match.neighbors[0].keypoint.x < max_x + cluster_dist:
                    votes[match.neighbors[0].source_id][bin].add(match)
    return votes


def round_to(x: float, base: float = 1, n: float = 2) -> Tuple[float, float]:
    lo = base * math.floor(float(x) / base)
    hi = base * math.ceil(float(x) / base)
    return (lo, hi)
