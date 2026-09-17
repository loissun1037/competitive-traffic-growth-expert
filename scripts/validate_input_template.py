#!/usr/bin/env python3
"""Validate the competitive-traffic-growth-expert input workbook schema.

Checks required worksheet names and row-5 machine headers. This script uses only
the Python standard library so it can run in lightweight skill environments.
"""

from __future__ import annotations

import argparse
import json
import posixpath
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


EXPECTED_HEADERS = {
    "批量任务": [
        "task_id",
        "enabled",
        "category",
        "business_goal",
        "own_product",
        "target_geo",
        "target_language",
        "period_start",
        "period_end",
        "device",
        "domain_scope",
        "include_sem",
        "data_mode",
        "input_files",
        "report_name",
    ],
    "竞品清单": [
        "task_id",
        "competitor_id",
        "product_name",
        "domain",
        "official_url",
        "positioning",
        "audience",
        "inclusion_reason",
    ],
    "来源口径": [
        "task_id",
        "source_id",
        "provider",
        "module",
        "reference",
        "locator",
        "retrieved_at",
        "geo_filter",
        "device",
        "domain_scope",
        "evidence_type",
        "notes",
    ],
    "月度流量": [
        "task_id",
        "domain",
        "period_start",
        "period_end",
        "visits",
        "unique_visitors",
        "source_id",
    ],
    "访问质量": [
        "task_id",
        "domain",
        "period_start",
        "period_end",
        "bounce_rate",
        "pages_per_visit",
        "avg_duration_seconds",
        "visits_per_unique_visitor",
        "source_id",
    ],
    "渠道流量": [
        "task_id",
        "domain",
        "period_start",
        "period_end",
        "channel",
        "visits",
        "share",
        "denominator",
        "source_id",
    ],
    "社交流量": [
        "task_id",
        "domain",
        "period_start",
        "period_end",
        "platform",
        "social_scope",
        "visits",
        "share",
        "denominator",
        "source_id",
    ],
    "国家流量": [
        "task_id",
        "domain",
        "period_start",
        "period_end",
        "country",
        "visits",
        "share",
        "denominator",
        "source_id",
    ],
    "公开观察": [
        "task_id",
        "competitor_id",
        "observed_at",
        "topic",
        "raw_description",
        "normalized_value",
        "currency",
        "pricing_unit",
        "source_id",
    ],
    "扩展指标": [
        "task_id",
        "entity_id",
        "competitor_id",
        "period_start",
        "period_end",
        "metric",
        "value",
        "unit",
        "denominator",
        "source_id",
    ],
    "关键词": [
        "task_id",
        "keyword",
        "country",
        "language",
        "period_start",
        "period_end",
        "intent",
        "avg_monthly_searches",
        "cpc",
        "bid_low",
        "bid_high",
        "currency",
        "ad_competition",
        "source_id",
    ],
    "广告与落地页": [
        "task_id",
        "domain",
        "observed_at",
        "country",
        "platform",
        "ad_text",
        "ad_url",
        "landing_url",
        "offer",
        "cta",
        "source_id",
    ],
    "我方投放与转化": [
        "task_id",
        "period_start",
        "period_end",
        "country",
        "campaign",
        "keyword",
        "impressions",
        "clicks",
        "spend",
        "currency",
        "conversion_event",
        "conversions",
        "attributed_revenue",
        "attribution_window",
        "source_id",
    ],
}

NS = {
    "a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def _column_index(cell_ref: str) -> int:
    letters = "".join(ch for ch in cell_ref if ch.isalpha())
    index = 0
    for ch in letters:
        index = index * 26 + ord(ch.upper()) - 64
    return index - 1


def _normalize_target(target: str) -> str:
    target = target.lstrip("/")
    if target.startswith("xl/"):
        return target
    return posixpath.normpath("xl/" + target)


def _shared_strings(zf: zipfile.ZipFile) -> list[str]:
    try:
        root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    values = []
    for item in root.findall("a:si", NS):
        values.append("".join(text.text or "" for text in item.findall(".//a:t", NS)))
    return values


def _sheet_paths(zf: zipfile.ZipFile) -> dict[str, str]:
    workbook = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    relmap = {rel.attrib["Id"]: _normalize_target(rel.attrib["Target"]) for rel in rels}
    paths = {}
    for sheet in workbook.findall("a:sheets/a:sheet", NS):
        rel_id = sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
        paths[sheet.attrib["name"]] = relmap[rel_id]
    return paths


def _row_values(zf: zipfile.ZipFile, sheet_path: str, row_number: int, strings: list[str]) -> list[str]:
    root = ET.fromstring(zf.read(sheet_path))
    row = root.find(f".//a:sheetData/a:row[@r='{row_number}']", NS)
    if row is None:
        return []
    cells = []
    for cell in row.findall("a:c", NS):
        value_node = cell.find("a:v", NS)
        if value_node is None:
            continue
        value = value_node.text or ""
        if cell.attrib.get("t") == "s":
            value = strings[int(value)]
        cells.append((_column_index(cell.attrib["r"]), value))
    if not cells:
        return []
    values = [""] * (max(index for index, _ in cells) + 1)
    for index, value in cells:
        values[index] = value
    return values


def validate(path: Path) -> dict:
    problems = []
    with zipfile.ZipFile(path) as zf:
        strings = _shared_strings(zf)
        sheet_paths = _sheet_paths(zf)
        missing_sheets = [sheet for sheet in EXPECTED_HEADERS if sheet not in sheet_paths]
        for sheet in missing_sheets:
            problems.append({"sheet": sheet, "problem": "missing_sheet"})
        for sheet, expected in EXPECTED_HEADERS.items():
            if sheet not in sheet_paths:
                continue
            actual = _row_values(zf, sheet_paths[sheet], 5, strings)
            if actual != expected:
                problems.append(
                    {
                        "sheet": sheet,
                        "problem": "header_mismatch",
                        "expected": expected,
                        "actual": actual,
                    }
                )
    return {
        "file": str(path),
        "sheets_checked": len(EXPECTED_HEADERS),
        "problem_count": len(problems),
        "problems": problems,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate competitive-traffic-growth-expert input workbook headers.")
    parser.add_argument("workbook", type=Path, help="Path to the input template or filled workbook.")
    args = parser.parse_args()
    result = validate(args.workbook)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["problem_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

