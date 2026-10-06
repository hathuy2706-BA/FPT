import os
import glob
import re

dot_files = glob.glob('bpmn_*.dot')

for f in dot_files:
    with open(f, 'r') as file:
        content = file.read()

    # Customer lane
    content = re.sub(r'color="#CBD5E1";\s*fillcolor="#F0F4F8"', 'color="#1f4e78"; fillcolor="#eef3fb"', content)
    content = re.sub(r'fillcolor="#28547B",\s*color="#28547B"', 'fillcolor="#1f4e78", color="#1f4e78"', content)

    # Frontend lane
    content = re.sub(r'color="#CBD5E1";\s*fillcolor="#E6F2FF"', 'color="#2e75b6"; fillcolor="#eef7fd"', content)
    content = re.sub(r'fillcolor="#4682B4",\s*color="#4682B4"', 'fillcolor="#2e75b6", color="#2e75b6"', content)

    # Backend lane
    content = re.sub(r'color="#CBD5E1";\s*fillcolor="#F8F0F8"', 'color="#7030a0"; fillcolor="#f6f0fb"', content)
    content = re.sub(r'fillcolor="#8B008B",\s*color="#8B008B"', 'fillcolor="#7030a0", color="#7030a0"', content)

    # Edges
    content = re.sub(r'edge\s*\[(.*?)color="#555555"(.*?)\]', r'edge [\1color="#444444"\2]', content)

    # Start event
    content = re.sub(r'fillcolor="white",\s*color="#22C55E",\s*fontcolor="#16A34A"', 'fillcolor="#e8f5e9", color="#2e7d32", fontcolor="#1b5e20"', content)

    # End event
    content = re.sub(r'fillcolor="white",\s*color="#EF4444",\s*fontcolor="#DC2626"', 'fillcolor="#ffebee", color="#c62828", fontcolor="#b71c1c"', content)

    # Gateways (if any diamond)
    content = re.sub(r'shape=diamond,\s*style="filled",\s*fillcolor="white",\s*color="#F59E0B",\s*fontcolor="#B45309"', 'shape=diamond, style="filled", fillcolor="#fff2cc", color="#bf8f00", fontcolor="#5b4500"', content)

    # Task nodes in backend
    content = re.sub(r'color="#8B008B"', 'color="#7030a0"', content)
    
    with open(f, 'w') as file:
        file.write(content)
        
    os.system(f"dot -Tpng {f} -o {f.replace('.dot', '.png')}")
    os.system(f"dot -Tsvg {f} -o {f.replace('.dot', '.svg')}")

print("Done fixing dot files")
