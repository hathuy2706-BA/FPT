figma.showUI(__html__, { width: 460, height: 380 });

figma.ui.onmessage = async function(msg) {
  if (msg.type === 'get-info') {
    figma.ui.postMessage({ type: 'info', editorType: figma.editorType });
    return;
  }

  if (msg.type !== 'insert') return;

  var selected = msg.selected; // array of { label, svg }
  if (!selected || selected.length === 0) {
    figma.ui.postMessage({ type: 'error', message: 'Chưa chọn sơ đồ nào.' });
    return;
  }

  try {
    await figma.loadFontAsync({ family: 'Inter', style: 'Bold' });
  } catch(e) {
    // font optional
  }

  var GAP = 200;
  var LABEL_H = 50;
  var vpCenter = figma.viewport.center;

  // Measure total width first pass (default 800 per diagram)
  var totalW = selected.length * (800 + GAP) - GAP;
  var startX = Math.round(vpCenter.x - totalW / 2);
  var startY = Math.round(vpCenter.y - 400);

  var allNodes = [];
  var errors = [];
  var curX = startX;

  for (var i = 0; i < selected.length; i++) {
    var d = selected[i];
    try {
      // createNodeFromSvg returns a FrameNode — fully editable native vectors
      var svgNode = figma.createNodeFromSvg(d.svg);
      svgNode.name = d.label;
      svgNode.x = curX;
      svgNode.y = startY + LABEL_H + 8;

      figma.currentPage.appendChild(svgNode);

      // Title label above
      var title = figma.createText();
      try {
        title.fontName = { family: 'Inter', style: 'Bold' };
        title.fontSize = 20;
      } catch(e) {
        title.fontSize = 18;
      }
      title.characters = d.label;
      title.fills = [{ type: 'SOLID', color: { r: 0.1, g: 0.2, b: 0.55 } }];
      title.x = curX;
      title.y = startY;
      title.resize(svgNode.width, LABEL_H);
      title.textAlignHorizontal = 'LEFT';

      figma.currentPage.appendChild(title);

      allNodes.push(svgNode);
      allNodes.push(title);

      curX += svgNode.width + GAP;

    } catch(e) {
      errors.push(d.label + ': ' + e.toString());
    }
  }

  if (allNodes.length > 0) {
    figma.viewport.scrollAndZoomIntoView(allNodes);
  }

  figma.ui.postMessage({
    type: 'done',
    created: allNodes.filter(function(n){ return n.type !== 'TEXT'; }).length,
    errors: errors
  });
};
