#!/usr/bin/env python3
"""Validate complete Simplified Chinese keys, plural forms and printf arguments."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / 'composeApp/src/commonMain/composeResources'

def load(folder):
    nodes = list(ET.parse(ROOT / folder / 'strings.xml').getroot())
    keys = [node.attrib['name'] for node in nodes]
    assert len(keys) == len(set(keys)), f'Duplicate keys in {folder}'
    return dict(zip(keys, nodes))

base, zh = load('values'), load('values-zh-rCN')
assert base.keys() == zh.keys(), f'Missing: {base.keys() - zh.keys()}; stale: {zh.keys() - base.keys()}'
# Compose resources here use indexed arguments; ignore literal percentages in prose.
pattern = re.compile(r'%\d+\$[-+#0 ,]*(?:\d+)?(?:\.\d+)?[a-zA-Z]')
for name, source in base.items():
    target = zh[name]
    assert source.tag == target.tag, name
    a, b = ([source], [target]) if source.tag == 'string' else (list(source), list(target))
    assert [x.get('quantity') for x in a] == [x.get('quantity') for x in b], name
    for x, y in zip(a, b):
        assert (y.text or '').strip(), f'Empty: {name}'
        assert sorted(pattern.findall(x.text or '')) == sorted(pattern.findall(y.text or '')), name
        assert sorted(re.findall(r'\\[ntr]', x.text or '')) == sorted(re.findall(r'\\[ntr]', y.text or '')), f'Escapes: {name}'
print(f'PASS: {len(base)}/{len(base)} Simplified Chinese resource entries; plural forms, printf arguments and escaped whitespace match.')
