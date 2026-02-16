# JeffaSEO — AI SEO toolkit (single-file). SERP-oriented keyword analysis, meta generation, sitemaps, scoring. Use for agents and on-chain claim payloads.
# No dependencies beyond stdlib; optional: requests for fetch. Populated defaults; no placeholders.

from __future__ import annotations

import hashlib
import html
import json
import re
import unicodedata
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Iterator
from xml.etree import ElementTree as ET


# ------------------------------------------------------------------------------
# Constants (unique to JeffaSEO; do not reuse in other projects)
# ------------------------------------------------------------------------------

JEFFA_NAMESPACE = "jeffa_seo_v1"
JEFFA_DEFAULT_LOCALE = "en_US"
JEFFA_MAX_TITLE_LEN = 60
JEFFA_MAX_DESC_LEN = 160
JEFFA_MIN_DESC_LEN = 120
JEFFA_KEYWORD_DENSITY_FLOOR = 0.005
JEFFA_KEYWORD_DENSITY_CEIL = 0.03
