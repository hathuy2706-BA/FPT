#!/usr/bin/env python3
"""
Build Figma plugin UI by embedding SVG diagrams from diagrams/ folder.
Usage:
    python3 build_plugin.py
    python3 build_plugin.py --include cart_overview_bpmn cart_single_bpmn
    python3 build_plugin.py --dir /path/to/diagrams
"""
import argparse
import glob
import json
import os
import sys

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.join(SKILL_DIR, '..', '..', '..'))
PLUGIN_DIR = os.path.join(SKILL_DIR, 'plugin')
OUTPUT_HTML = os.path.join(PLUGIN_DIR, 'ui.html')


def load_svgs(diagrams_dir, include_filter=None):
    pattern = os.path.join(diagrams_dir, '*.svg')
    paths = sorted(glob.glob(pattern))
    if not paths:
        print(f'ERROR: No SVG files found in {diagrams_dir}')
        sys.exit(1)

    result = []
    for path in paths:
        stem = os.path.splitext(os.path.basename(path))[0]
        if include_filter and stem not in include_filter:
            continue
        with open(path, 'r', encoding='utf-8') as f:
            svg = f.read().strip()
        label = (stem
                 .replace('_bpmn', '')
                 .replace('camcart', 'Giỏ hàng — Camera')
                 .replace('fplcart', 'Giỏ hàng — FPT Play')
                 .replace('ulfcart', 'Giỏ hàng — Ultrafast')
                 .replace('cart_overview', 'Tổng quan — Giỏ hàng (BPMN)')
                 .replace('cart_single',   'Luồng GIỎ LẺ (thêm từng sản phẩm)')
                 .replace('cart_merge',    'Luồng GỘP GIỎ (đa sản phẩm)')
                 .replace('_', ' ')
                 .strip())
        if label == stem.replace('_bpmn', '').replace('_', ' ').strip():
            label = label.title()
        result.append({'stem': stem, 'label': label, 'svg': svg, 'path': path})

    return result


def build_js_array(diagrams):
    entries = []
    for d in diagrams:
        escaped = d['svg'].replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
        entries.append(f"  {{ label: {json.dumps(d['label'])}, svg: `{escaped}` }}")
    return 'var DIAGRAMS = [\n' + ',\n'.join(entries) + '\n];'


HTML_TEMPLATE = '''\
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; }}
body {{ font-family: Inter, sans-serif; margin: 0; padding: 16px; background: #f0f2ff; font-size: 13px; }}
h2 {{ color: #1a2b6b; font-size: 15px; margin: 0 0 12px; display: flex; align-items: center; gap: 8px; }}
h2 span {{ background: #1a3adb; color: #fff; border-radius: 4px; padding: 2px 8px; font-size: 11px; font-weight: 600; }}
.meta {{ color: #888; font-size: 11px; margin-bottom: 12px; }}
.actions {{ display: flex; gap: 8px; margin-bottom: 8px; }}
.actions a {{ font-size: 11px; color: #1a3adb; cursor: pointer; text-decoration: underline; }}
.list {{ display: flex; flex-direction: column; gap: 5px; margin-bottom: 14px; max-height: 200px; overflow-y: auto; }}
label {{ display: flex; align-items: center; gap: 9px; background: #fff; border: 1.5px solid #d0d8ff; border-radius: 7px; padding: 8px 12px; cursor: pointer; }}
label:hover {{ border-color: #1a3adb; }}
label input[type=checkbox] {{ width: 14px; height: 14px; accent-color: #1a3adb; flex-shrink: 0; }}
.lname {{ font-weight: 600; color: #1a2b6b; font-size: 13px; }}
.lstem {{ color: #999; font-size: 10px; font-family: monospace; }}
button {{ background: #1a3adb; color: #fff; border: none; border-radius: 8px; padding: 11px 0; font-size: 14px; font-weight: 700; cursor: pointer; width: 100%; }}
button:hover:not(:disabled) {{ background: #2d46e0; }}
button:disabled {{ background: #aaa; cursor: not-allowed; }}
#status {{ margin-top: 10px; font-size: 12px; min-height: 18px; text-align: center; }}
.ok {{ color: #2e7d32; font-weight: 700; }}
.err {{ color: #c62828; }}
</style>
</head>
<body>
<h2>BPMN → Figma Exporter <span id="etag">FIGJAM</span></h2>
<div class="meta">Diagrams dir: <code>{diagrams_dir}</code> · {count} sơ đồ · Build: {build_date}</div>

<div class="actions">
  <a onclick="selectAll(true)">Chọn tất cả</a> &nbsp;·&nbsp;
  <a onclick="selectAll(false)">Bỏ chọn</a>
</div>

<div class="list" id="list"></div>

<button id="btn" onclick="run()">Thêm vào Figma Board</button>
<div id="status"></div>

<script>
{diagrams_js}

function buildList() {{
  var el = document.getElementById('list');
  DIAGRAMS.forEach(function(d, i) {{
    var row = document.createElement('label');
    row.innerHTML =
      '<input type="checkbox" id="chk_' + i + '" checked>' +
      '<div><div class="lname">' + d.label + '</div>' +
      '<div class="lstem">' + (d.stem || '') + '.svg</div></div>';
    el.appendChild(row);
  }});
}}

function selectAll(v) {{
  DIAGRAMS.forEach(function(_, i) {{
    document.getElementById('chk_' + i).checked = v;
  }});
}}

function run() {{
  var btn = document.getElementById('btn');
  var status = document.getElementById('status');
  var sel = DIAGRAMS.filter(function(_, i) {{
    return document.getElementById('chk_' + i).checked;
  }});
  if (!sel.length) {{ status.innerHTML = '<span class="err">Chọn ít nhất 1 sơ đồ.</span>'; return; }}
  btn.disabled = true;
  btn.textContent = 'Đang tạo ' + sel.length + ' sơ đồ...';
  status.textContent = 'Đang convert SVG → Figma vectors...';
  parent.postMessage({{ pluginMessage: {{ type: 'insert', selected: sel }} }}, '*');
}}

window.onmessage = function(e) {{
  var msg = e.data.pluginMessage;
  if (!msg) return;
  var btn = document.getElementById('btn');
  var status = document.getElementById('status');
  if (msg.type === 'info') {{
    document.getElementById('etag').textContent = msg.editorType.toUpperCase();
  }}
  if (msg.type === 'done') {{
    btn.disabled = false;
    btn.textContent = 'Thêm vào Figma Board';
    var errPart = msg.errors && msg.errors.length ? ' | ' + msg.errors.length + ' lỗi' : '';
    status.innerHTML = msg.created > 0
      ? '<span class="ok">✓ Đã tạo ' + msg.created + ' sơ đồ editable' + errPart + '</span>'
      : '<span class="err">Không tạo được node: ' + (msg.errors || []).join('; ') + '</span>';
  }}
  if (msg.type === 'error') {{
    btn.disabled = false;
    btn.textContent = 'Thêm vào Figma Board';
    status.innerHTML = '<span class="err">' + msg.message + '</span>';
  }}
}};

buildList();
setTimeout(function() {{
  parent.postMessage({{ pluginMessage: {{ type: 'get-info' }} }}, '*');
}}, 100);
</script>
</body>
</html>'''


def main():
    parser = argparse.ArgumentParser(description='Build Figma plugin UI with embedded SVGs')
    parser.add_argument('--dir', default=os.path.join(PROJECT_ROOT, 'diagrams'),
                        help='Path to diagrams directory (default: <project>/diagrams)')
    parser.add_argument('--include', nargs='+', metavar='STEM',
                        help='Only include these SVG stems (without .svg extension)')
    args = parser.parse_args()

    diagrams_dir = os.path.abspath(args.dir)
    diagrams = load_svgs(diagrams_dir, set(args.include) if args.include else None)

    if not diagrams:
        print(f'ERROR: No SVG files matched. Available: {[os.path.basename(p) for p in glob.glob(os.path.join(diagrams_dir, "*.svg"))]}')
        sys.exit(1)

    print(f'Found {len(diagrams)} SVG files:')
    for d in diagrams:
        size_kb = len(d["svg"]) // 1024
        print(f'  [{size_kb:3d} KB]  {d["stem"]}.svg  →  "{d["label"]}"')

    # Add stem to each diagram for display in UI
    for d in diagrams:
        pass  # stem already in dict

    js = build_js_array(diagrams)

    from datetime import datetime
    build_date = datetime.now().strftime('%Y-%m-%d %H:%M')

    html = HTML_TEMPLATE.format(
        diagrams_dir=os.path.relpath(diagrams_dir, PROJECT_ROOT),
        count=len(diagrams),
        build_date=build_date,
        diagrams_js=js,
    )

    os.makedirs(PLUGIN_DIR, exist_ok=True)
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'\nBuilt: {OUTPUT_HTML}')
    print(f'Size:  {len(html) // 1024} KB')
    print()
    print('Next steps:')
    print('  1. Figma Desktop → Plugins → Development → Import plugin from manifest...')
    print(f'     → Select: {os.path.join(PLUGIN_DIR, "manifest.json")}')
    print('  2. Plugins → Development → BPMN → Figma Exporter')
    print('  3. Chọn sơ đồ → Click "Thêm vào Figma Board"')


if __name__ == '__main__':
    main()
