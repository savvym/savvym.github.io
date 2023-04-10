---
title: "Car detection with YOLO"
date: 2023-04-10
summary: "Convolutional Neural Networks Programming Assignments YOLO"
categories:
- Paper Read
tags:
# hidemeta: true
markup: HTML
---
<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Autonomous_driving_application_Car_detection</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>




<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>



<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/*
 * Webkit scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-corner {
  background: var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-thumb {
  background: rgb(var(--jp-scrollbar-thumb-color));
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-right: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-bottom: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar */

[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-corner,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-corner {
  background-color: transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-thumb,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid transparent;
  border-right: var(--jp-scrollbar-endpad) solid transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid transparent;
  border-bottom: var(--jp-scrollbar-endpad) solid transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0px solid transparent;
  border-right: 0px solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0px solid transparent;
  border-bottom: 0px solid transparent;
}

/*
 * Phosphor
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Widget, /* </DEPRECATED> */
.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}


/* <DEPRECATED> */ .p-Widget.p-mod-hidden, /* </DEPRECATED> */
.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-CommandPalette, /* </DEPRECATED> */
.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-CommandPalette-search, /* </DEPRECATED> */
.lm-CommandPalette-search {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-content, /* </DEPRECATED> */
.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-CommandPalette-header, /* </DEPRECATED> */
.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}


/* <DEPRECATED> */ .p-CommandPalette-item, /* </DEPRECATED> */
.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}


/* <DEPRECATED> */ .p-CommandPalette-itemIcon, /* </DEPRECATED> */
.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemContent, /* </DEPRECATED> */
.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}


/* <DEPRECATED> */ .p-CommandPalette-itemShortcut, /* </DEPRECATED> */
.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemLabel, /* </DEPRECATED> */
.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
	border:1px solid transparent;
  background-color: transparent;
  position: absolute;
	z-index:1;
	right:3%;
	top: 0;
	bottom: 0;
	margin: auto;
	padding: 7px 0;
	display: none;
	vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
	content: "X";
	display: block;
	width: 15px;
	height: 15px;
	text-align: center;
	color:#000;
	font-weight: normal;
	font-size: 12px;
	cursor: pointer;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-DockPanel, /* </DEPRECATED> */
.lm-DockPanel {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-widget, /* </DEPRECATED> */
.lm-DockPanel-widget {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-tabBar, /* </DEPRECATED> */
.lm-DockPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-DockPanel-handle, /* </DEPRECATED> */
.lm-DockPanel-handle {
  z-index: 2;
}


/* <DEPRECATED> */ .p-DockPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-DockPanel-handle:after, /* </DEPRECATED> */
.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}


/* <DEPRECATED> */ .p-DockPanel-overlay, /* </DEPRECATED> */
.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}


/* <DEPRECATED> */ .p-DockPanel-overlay.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Menu, /* </DEPRECATED> */
.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-Menu-content, /* </DEPRECATED> */
.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-Menu-item, /* </DEPRECATED> */
.lm-Menu-item {
  display: table-row;
}


/* <DEPRECATED> */
.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed,
/* </DEPRECATED> */
.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}


/* <DEPRECATED> */
.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon,
/* </DEPRECATED> */
.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}


/* <DEPRECATED> */ .p-Menu-itemLabel, /* </DEPRECATED> */
.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}


/* <DEPRECATED> */ .p-Menu-itemShortcut, /* </DEPRECATED> */
.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-MenuBar, /* </DEPRECATED> */
.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-MenuBar-content, /* </DEPRECATED> */
.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}


/* <DEPRECATED> */ .p--MenuBar-item, /* </DEPRECATED> */
.lm-MenuBar-item {
  box-sizing: border-box;
}


/* <DEPRECATED> */
.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel,
/* </DEPRECATED> */
.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-ScrollBar, /* </DEPRECATED> */
.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-ScrollBar-button, /* </DEPRECATED> */
.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-track, /* </DEPRECATED> */
.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-thumb, /* </DEPRECATED> */
.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-SplitPanel-child, /* </DEPRECATED> */
.lm-SplitPanel-child {
  z-index: 0;
}


/* <DEPRECATED> */ .p-SplitPanel-handle, /* </DEPRECATED> */
.lm-SplitPanel-handle {
  z-index: 1;
}


/* <DEPRECATED> */ .p-SplitPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-SplitPanel-handle:after, /* </DEPRECATED> */
.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabBar, /* </DEPRECATED> */
.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='horizontal'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='vertical'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}


/* <DEPRECATED> */ .p-TabBar-content, /* </DEPRECATED> */
.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='vertical'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


/* <DEPRECATED> */
.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon,
/* </DEPRECATED> */
.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-TabBar-tabLabel, /* </DEPRECATED> */
.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing : border-box;
}


/* <DEPRECATED> */ .p-TabBar-tab.p-mod-hidden, /* </DEPRECATED> */
.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}


.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-TabBar.p-mod-dragging .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing : border-box;
  background: inherit;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabPanel-tabBar, /* </DEPRECATED> */
.lm-TabPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-TabPanel-stackedPanel, /* </DEPRECATED> */
.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

@charset "UTF-8";
html{
  -webkit-box-sizing:border-box;
          box-sizing:border-box; }

*,
*::before,
*::after{
  -webkit-box-sizing:inherit;
          box-sizing:inherit; }

body{
  font-size:14px;
  font-weight:400;
  letter-spacing:0;
  line-height:1.28581;
  text-transform:none;
  color:#182026;
  font-family:-apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", "Icons16", sans-serif; }

p{
  margin-bottom:10px;
  margin-top:0; }

small{
  font-size:12px; }

strong{
  font-weight:600; }

::-moz-selection{
  background:rgba(125, 188, 255, 0.6); }

::selection{
  background:rgba(125, 188, 255, 0.6); }
.bp3-heading{
  color:#182026;
  font-weight:600;
  margin:0 0 10px;
  padding:0; }
  .bp3-dark .bp3-heading{
    color:#f5f8fa; }

h1.bp3-heading, .bp3-running-text h1{
  font-size:36px;
  line-height:40px; }

h2.bp3-heading, .bp3-running-text h2{
  font-size:28px;
  line-height:32px; }

h3.bp3-heading, .bp3-running-text h3{
  font-size:22px;
  line-height:25px; }

h4.bp3-heading, .bp3-running-text h4{
  font-size:18px;
  line-height:21px; }

h5.bp3-heading, .bp3-running-text h5{
  font-size:16px;
  line-height:19px; }

h6.bp3-heading, .bp3-running-text h6{
  font-size:14px;
  line-height:16px; }
.bp3-ui-text{
  font-size:14px;
  font-weight:400;
  letter-spacing:0;
  line-height:1.28581;
  text-transform:none; }

.bp3-monospace-text{
  font-family:monospace;
  text-transform:none; }

.bp3-text-muted{
  color:#5c7080; }
  .bp3-dark .bp3-text-muted{
    color:#a7b6c2; }

.bp3-text-disabled{
  color:rgba(92, 112, 128, 0.6); }
  .bp3-dark .bp3-text-disabled{
    color:rgba(167, 182, 194, 0.6); }

.bp3-text-overflow-ellipsis{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal; }
.bp3-running-text{
  font-size:14px;
  line-height:1.5; }
  .bp3-running-text h1{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h1{
      color:#f5f8fa; }
  .bp3-running-text h2{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h2{
      color:#f5f8fa; }
  .bp3-running-text h3{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h3{
      color:#f5f8fa; }
  .bp3-running-text h4{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h4{
      color:#f5f8fa; }
  .bp3-running-text h5{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h5{
      color:#f5f8fa; }
  .bp3-running-text h6{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h6{
      color:#f5f8fa; }
  .bp3-running-text hr{
    border:none;
    border-bottom:1px solid rgba(16, 22, 26, 0.15);
    margin:20px 0; }
    .bp3-dark .bp3-running-text hr{
      border-color:rgba(255, 255, 255, 0.15); }
  .bp3-running-text p{
    margin:0 0 10px;
    padding:0; }

.bp3-text-large{
  font-size:16px; }

.bp3-text-small{
  font-size:12px; }
a{
  color:#106ba3;
  text-decoration:none; }
  a:hover{
    color:#106ba3;
    cursor:pointer;
    text-decoration:underline; }
  a .bp3-icon, a .bp3-icon-standard, a .bp3-icon-large{
    color:inherit; }
  a code,
  .bp3-dark a code{
    color:inherit; }
  .bp3-dark a,
  .bp3-dark a:hover{
    color:#48aff0; }
    .bp3-dark a .bp3-icon, .bp3-dark a .bp3-icon-standard, .bp3-dark a .bp3-icon-large,
    .bp3-dark a:hover .bp3-icon,
    .bp3-dark a:hover .bp3-icon-standard,
    .bp3-dark a:hover .bp3-icon-large{
      color:inherit; }
.bp3-running-text code, .bp3-code{
  font-family:monospace;
  text-transform:none;
  background:rgba(255, 255, 255, 0.7);
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
  color:#5c7080;
  font-size:smaller;
  padding:2px 5px; }
  .bp3-dark .bp3-running-text code, .bp3-running-text .bp3-dark code, .bp3-dark .bp3-code{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#a7b6c2; }
  .bp3-running-text a > code, a > .bp3-code{
    color:#137cbd; }
    .bp3-dark .bp3-running-text a > code, .bp3-running-text .bp3-dark a > code, .bp3-dark a > .bp3-code{
      color:inherit; }

.bp3-running-text pre, .bp3-code-block{
  font-family:monospace;
  text-transform:none;
  background:rgba(255, 255, 255, 0.7);
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
  color:#182026;
  display:block;
  font-size:13px;
  line-height:1.4;
  margin:10px 0;
  padding:13px 15px 12px;
  word-break:break-all;
  word-wrap:break-word; }
  .bp3-dark .bp3-running-text pre, .bp3-running-text .bp3-dark pre, .bp3-dark .bp3-code-block{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
  .bp3-running-text pre > code, .bp3-code-block > code{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:inherit;
    font-size:inherit;
    padding:0; }

.bp3-running-text kbd, .bp3-key{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#5c7080;
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  font-family:inherit;
  font-size:12px;
  height:24px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  line-height:24px;
  min-width:24px;
  padding:3px 6px;
  vertical-align:middle; }
  .bp3-running-text kbd .bp3-icon, .bp3-key .bp3-icon, .bp3-running-text kbd .bp3-icon-standard, .bp3-key .bp3-icon-standard, .bp3-running-text kbd .bp3-icon-large, .bp3-key .bp3-icon-large{
    margin-right:5px; }
  .bp3-dark .bp3-running-text kbd, .bp3-running-text .bp3-dark kbd, .bp3-dark .bp3-key{
    background:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#a7b6c2; }
.bp3-running-text blockquote, .bp3-blockquote{
  border-left:solid 4px rgba(167, 182, 194, 0.5);
  margin:0 0 10px;
  padding:0 20px; }
  .bp3-dark .bp3-running-text blockquote, .bp3-running-text .bp3-dark blockquote, .bp3-dark .bp3-blockquote{
    border-color:rgba(115, 134, 148, 0.5); }
.bp3-running-text ul,
.bp3-running-text ol, .bp3-list{
  margin:10px 0;
  padding-left:30px; }
  .bp3-running-text ul li:not(:last-child), .bp3-running-text ol li:not(:last-child), .bp3-list li:not(:last-child){
    margin-bottom:5px; }
  .bp3-running-text ul ol, .bp3-running-text ol ol, .bp3-list ol,
  .bp3-running-text ul ul,
  .bp3-running-text ol ul,
  .bp3-list ul{
    margin-top:5px; }

.bp3-list-unstyled{
  list-style:none;
  margin:0;
  padding:0; }
  .bp3-list-unstyled li{
    padding:0; }
.bp3-rtl{
  text-align:right; }

.bp3-dark{
  color:#f5f8fa; }

:focus{
  outline:rgba(19, 124, 189, 0.6) auto 2px;
  outline-offset:2px;
  -moz-outline-radius:6px; }

.bp3-focus-disabled :focus{
  outline:none !important; }
  .bp3-focus-disabled :focus ~ .bp3-control-indicator{
    outline:none !important; }

.bp3-alert{
  max-width:400px;
  padding:20px; }

.bp3-alert-body{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-alert-body .bp3-icon{
    font-size:40px;
    margin-right:20px;
    margin-top:0; }

.bp3-alert-contents{
  word-break:break-word; }

.bp3-alert-footer{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:reverse;
      -ms-flex-direction:row-reverse;
          flex-direction:row-reverse;
  margin-top:10px; }
  .bp3-alert-footer .bp3-button{
    margin-left:10px; }
.bp3-breadcrumbs{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  cursor:default;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:wrap;
      flex-wrap:wrap;
  height:30px;
  list-style:none;
  margin:0;
  padding:0; }
  .bp3-breadcrumbs > li{
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex; }
    .bp3-breadcrumbs > li::after{
      background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M10.71 7.29l-4-4a1.003 1.003 0 00-1.42 1.42L8.59 8 5.3 11.29c-.19.18-.3.43-.3.71a1.003 1.003 0 001.71.71l4-4c.18-.18.29-.43.29-.71 0-.28-.11-.53-.29-.71z' fill='%235C7080'/%3e%3c/svg%3e");
      content:"";
      display:block;
      height:16px;
      margin:0 5px;
      width:16px; }
    .bp3-breadcrumbs > li:last-of-type::after{
      display:none; }

.bp3-breadcrumb,
.bp3-breadcrumb-current,
.bp3-breadcrumbs-collapsed{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  font-size:16px; }

.bp3-breadcrumb,
.bp3-breadcrumbs-collapsed{
  color:#5c7080; }

.bp3-breadcrumb:hover{
  text-decoration:none; }

.bp3-breadcrumb.bp3-disabled{
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-breadcrumb .bp3-icon{
  margin-right:5px; }

.bp3-breadcrumb-current{
  color:inherit;
  font-weight:600; }
  .bp3-breadcrumb-current .bp3-input{
    font-size:inherit;
    font-weight:inherit;
    vertical-align:baseline; }

.bp3-breadcrumbs-collapsed{
  background:#ced9e0;
  border:none;
  border-radius:3px;
  cursor:pointer;
  margin-right:2px;
  padding:1px 5px;
  vertical-align:text-bottom; }
  .bp3-breadcrumbs-collapsed::before{
    background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cg fill='%235C7080'%3e%3ccircle cx='2' cy='8.03' r='2'/%3e%3ccircle cx='14' cy='8.03' r='2'/%3e%3ccircle cx='8' cy='8.03' r='2'/%3e%3c/g%3e%3c/svg%3e") center no-repeat;
    content:"";
    display:block;
    height:16px;
    width:16px; }
  .bp3-breadcrumbs-collapsed:hover{
    background:#bfccd6;
    color:#182026;
    text-decoration:none; }

.bp3-dark .bp3-breadcrumb,
.bp3-dark .bp3-breadcrumbs-collapsed{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumbs > li::after{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumb.bp3-disabled{
  color:rgba(167, 182, 194, 0.6); }

.bp3-dark .bp3-breadcrumb-current{
  color:#f5f8fa; }

.bp3-dark .bp3-breadcrumbs-collapsed{
  background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-breadcrumbs-collapsed:hover{
    background:rgba(16, 22, 26, 0.6);
    color:#f5f8fa; }
.bp3-button{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  font-size:14px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  padding:5px 10px;
  text-align:left;
  vertical-align:middle;
  min-height:30px;
  min-width:30px; }
  .bp3-button > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-button > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-button::before,
  .bp3-button > *{
    margin-right:7px; }
  .bp3-button:empty::before,
  .bp3-button > :last-child{
    margin-right:0; }
  .bp3-button:empty{
    padding:0 !important; }
  .bp3-button:disabled, .bp3-button.bp3-disabled{
    cursor:not-allowed; }
  .bp3-button.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button.bp3-align-right,
  .bp3-align-right .bp3-button{
    text-align:right; }
  .bp3-button.bp3-align-left,
  .bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-button:not([class*="bp3-intent-"]){
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    color:#182026; }
    .bp3-button:not([class*="bp3-intent-"]):hover{
      background-clip:padding-box;
      background-color:#ebf1f5;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
    .bp3-button:not([class*="bp3-intent-"]):active, .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      background-color:#d8e1e8;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      outline:none; }
      .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active:hover, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-button.bp3-intent-primary{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover, .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover{
      background-color:#106ba3;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      background-color:#0e5a8a;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-primary:disabled, .bp3-button.bp3-intent-primary.bp3-disabled{
      background-color:rgba(19, 124, 189, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-success{
    background-color:#0f9960;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-success:hover, .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-success:hover{
      background-color:#0d8050;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      background-color:#0a6640;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-success:disabled, .bp3-button.bp3-intent-success.bp3-disabled{
      background-color:rgba(15, 153, 96, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-warning{
    background-color:#d9822b;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover, .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover{
      background-color:#bf7326;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      background-color:#a66321;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-warning:disabled, .bp3-button.bp3-intent-warning.bp3-disabled{
      background-color:rgba(217, 130, 43, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-danger{
    background-color:#db3737;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover, .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover{
      background-color:#c23030;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      background-color:#a82a2a;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-danger:disabled, .bp3-button.bp3-intent-danger.bp3-disabled{
      background-color:rgba(219, 55, 55, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
    stroke:#ffffff; }
  .bp3-button.bp3-large,
  .bp3-large .bp3-button{
    min-height:40px;
    min-width:40px;
    font-size:16px;
    padding:5px 15px; }
    .bp3-button.bp3-large::before,
    .bp3-button.bp3-large > *,
    .bp3-large .bp3-button::before,
    .bp3-large .bp3-button > *{
      margin-right:10px; }
    .bp3-button.bp3-large:empty::before,
    .bp3-button.bp3-large > :last-child,
    .bp3-large .bp3-button:empty::before,
    .bp3-large .bp3-button > :last-child{
      margin-right:0; }
  .bp3-button.bp3-small,
  .bp3-small .bp3-button{
    min-height:24px;
    min-width:24px;
    padding:0 7px; }
  .bp3-button.bp3-loading{
    position:relative; }
    .bp3-button.bp3-loading[class*="bp3-icon-"]::before{
      visibility:hidden; }
    .bp3-button.bp3-loading .bp3-button-spinner{
      margin:0;
      position:absolute; }
    .bp3-button.bp3-loading > :not(.bp3-button-spinner){
      visibility:hidden; }
  .bp3-button[class*="bp3-icon-"]::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    color:#5c7080; }
  .bp3-button .bp3-icon, .bp3-button .bp3-icon-standard, .bp3-button .bp3-icon-large{
    color:#5c7080; }
    .bp3-button .bp3-icon.bp3-align-right, .bp3-button .bp3-icon-standard.bp3-align-right, .bp3-button .bp3-icon-large.bp3-align-right{
      margin-left:7px; }
  .bp3-button .bp3-icon:first-child:last-child,
  .bp3-button .bp3-spinner + .bp3-icon:last-child{
    margin:0 -7px; }
  .bp3-dark .bp3-button:not([class*="bp3-intent-"]){
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover, .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"])[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-large{
      color:#a7b6c2; }
  .bp3-dark .bp3-button[class*="bp3-intent-"]{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:hover{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:active, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-active{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:disabled, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-disabled{
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.3); }
    .bp3-dark .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
      stroke:#8a9ba8; }
  .bp3-button:disabled::before,
  .bp3-button:disabled .bp3-icon, .bp3-button:disabled .bp3-icon-standard, .bp3-button:disabled .bp3-icon-large, .bp3-button.bp3-disabled::before,
  .bp3-button.bp3-disabled .bp3-icon, .bp3-button.bp3-disabled .bp3-icon-standard, .bp3-button.bp3-disabled .bp3-icon-large, .bp3-button[class*="bp3-intent-"]::before,
  .bp3-button[class*="bp3-intent-"] .bp3-icon, .bp3-button[class*="bp3-intent-"] .bp3-icon-standard, .bp3-button[class*="bp3-intent-"] .bp3-icon-large{
    color:inherit !important; }
  .bp3-button.bp3-minimal{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-button.bp3-minimal:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button.bp3-minimal:active, .bp3-button.bp3-minimal.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button.bp3-minimal:disabled, .bp3-button.bp3-minimal:disabled:hover, .bp3-button.bp3-minimal.bp3-disabled, .bp3-button.bp3-minimal.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-minimal{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-minimal:hover, .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button.bp3-minimal:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-minimal:disabled, .bp3-dark .bp3-button.bp3-minimal:disabled:hover, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover, .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover, .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover, .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover, .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button.bp3-outlined{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    border:1px solid rgba(24, 32, 38, 0.2);
    -webkit-box-sizing:border-box;
            box-sizing:border-box; }
    .bp3-button.bp3-outlined:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button.bp3-outlined:active, .bp3-button.bp3-outlined.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button.bp3-outlined:disabled, .bp3-button.bp3-outlined:disabled:hover, .bp3-button.bp3-outlined.bp3-disabled, .bp3-button.bp3-outlined.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button.bp3-outlined:disabled.bp3-active, .bp3-button.bp3-outlined:disabled:hover.bp3-active, .bp3-button.bp3-outlined.bp3-disabled.bp3-active, .bp3-button.bp3-outlined.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-outlined{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-outlined:hover, .bp3-dark .bp3-button.bp3-outlined:active, .bp3-dark .bp3-button.bp3-outlined.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button.bp3-outlined:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-outlined:active, .bp3-dark .bp3-button.bp3-outlined.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-outlined:disabled, .bp3-dark .bp3-button.bp3-outlined:disabled:hover, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button.bp3-outlined:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:hover, .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:hover, .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:hover, .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:hover, .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
    .bp3-button.bp3-outlined:disabled, .bp3-button.bp3-outlined.bp3-disabled, .bp3-button.bp3-outlined:disabled:hover, .bp3-button.bp3-outlined.bp3-disabled:hover{
      border-color:rgba(92, 112, 128, 0.1); }
    .bp3-dark .bp3-button.bp3-outlined{
      border-color:rgba(255, 255, 255, 0.4); }
      .bp3-dark .bp3-button.bp3-outlined:disabled, .bp3-dark .bp3-button.bp3-outlined:disabled:hover, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover{
        border-color:rgba(255, 255, 255, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-primary{
      border-color:rgba(16, 107, 163, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
        border-color:rgba(16, 107, 163, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary{
        border-color:rgba(72, 175, 240, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
          border-color:rgba(72, 175, 240, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-success{
      border-color:rgba(13, 128, 80, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
        border-color:rgba(13, 128, 80, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success{
        border-color:rgba(61, 204, 145, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
          border-color:rgba(61, 204, 145, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-warning{
      border-color:rgba(191, 115, 38, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
        border-color:rgba(191, 115, 38, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning{
        border-color:rgba(255, 179, 102, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
          border-color:rgba(255, 179, 102, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-danger{
      border-color:rgba(194, 48, 48, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
        border-color:rgba(194, 48, 48, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger{
        border-color:rgba(255, 115, 115, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
          border-color:rgba(255, 115, 115, 0.2); }

a.bp3-button{
  text-align:center;
  text-decoration:none;
  -webkit-transition:none;
  transition:none; }
  a.bp3-button, a.bp3-button:hover, a.bp3-button:active{
    color:#182026; }
  a.bp3-button.bp3-disabled{
    color:rgba(92, 112, 128, 0.6); }

.bp3-button-text{
  -webkit-box-flex:0;
      -ms-flex:0 1 auto;
          flex:0 1 auto; }

.bp3-button.bp3-align-left .bp3-button-text, .bp3-button.bp3-align-right .bp3-button-text,
.bp3-button-group.bp3-align-left .bp3-button-text,
.bp3-button-group.bp3-align-right .bp3-button-text{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto; }
.bp3-button-group{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex; }
  .bp3-button-group .bp3-button{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    position:relative;
    z-index:4; }
    .bp3-button-group .bp3-button:focus{
      z-index:5; }
    .bp3-button-group .bp3-button:hover{
      z-index:6; }
    .bp3-button-group .bp3-button:active, .bp3-button-group .bp3-button.bp3-active{
      z-index:7; }
    .bp3-button-group .bp3-button:disabled, .bp3-button-group .bp3-button.bp3-disabled{
      z-index:3; }
    .bp3-button-group .bp3-button[class*="bp3-intent-"]{
      z-index:9; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:focus{
        z-index:10; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:hover{
        z-index:11; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:active, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-active{
        z-index:12; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:disabled, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-disabled{
        z-index:8; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:first-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:first-child){
    border-bottom-left-radius:0;
    border-top-left-radius:0; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    border-bottom-right-radius:0;
    border-top-right-radius:0;
    margin-right:-1px; }
  .bp3-button-group.bp3-minimal .bp3-button{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-button-group.bp3-minimal .bp3-button:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button-group.bp3-minimal .bp3-button{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
      color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
      color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button-group .bp3-popover-wrapper,
  .bp3-button-group .bp3-popover-target{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button-group .bp3-button.bp3-fill,
  .bp3-button-group.bp3-fill .bp3-button:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-vertical{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column;
    vertical-align:top; }
    .bp3-button-group.bp3-vertical.bp3-fill{
      height:100%;
      width:unset; }
    .bp3-button-group.bp3-vertical .bp3-button{
      margin-right:0 !important;
      width:100%; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:first-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:first-child{
      border-radius:3px 3px 0 0; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:last-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:last-child{
      border-radius:0 0 3px 3px; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:not(:last-child){
      margin-bottom:-1px; }
  .bp3-button-group.bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    margin-right:1px; }
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-button:not(:last-child){
    margin-bottom:1px; }
.bp3-callout{
  font-size:14px;
  line-height:1.5;
  background-color:rgba(138, 155, 168, 0.15);
  border-radius:3px;
  padding:10px 12px 9px;
  position:relative;
  width:100%; }
  .bp3-callout[class*="bp3-icon-"]{
    padding-left:40px; }
    .bp3-callout[class*="bp3-icon-"]::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      color:#5c7080;
      left:10px;
      position:absolute;
      top:10px; }
  .bp3-callout.bp3-callout-icon{
    padding-left:40px; }
    .bp3-callout.bp3-callout-icon > .bp3-icon:first-child{
      color:#5c7080;
      left:10px;
      position:absolute;
      top:10px; }
  .bp3-callout .bp3-heading{
    line-height:20px;
    margin-bottom:5px;
    margin-top:0; }
    .bp3-callout .bp3-heading:last-child{
      margin-bottom:0; }
  .bp3-dark .bp3-callout{
    background-color:rgba(138, 155, 168, 0.2); }
    .bp3-dark .bp3-callout[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
  .bp3-callout.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15); }
    .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-primary .bp3-heading{
      color:#106ba3; }
    .bp3-dark .bp3-callout.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-primary .bp3-heading{
        color:#48aff0; }
  .bp3-callout.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15); }
    .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-success .bp3-heading{
      color:#0d8050; }
    .bp3-dark .bp3-callout.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-success .bp3-heading{
        color:#3dcc91; }
  .bp3-callout.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15); }
    .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-warning .bp3-heading{
      color:#bf7326; }
    .bp3-dark .bp3-callout.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-warning .bp3-heading{
        color:#ffb366; }
  .bp3-callout.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15); }
    .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-danger .bp3-heading{
      color:#c23030; }
    .bp3-dark .bp3-callout.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-danger .bp3-heading{
        color:#ff7373; }
  .bp3-running-text .bp3-callout{
    margin:20px 0; }
.bp3-card{
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
  padding:20px;
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-card.bp3-dark,
  .bp3-dark .bp3-card{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-0{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }
  .bp3-elevation-0.bp3-dark,
  .bp3-dark .bp3-elevation-0{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-1{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-1.bp3-dark,
  .bp3-dark .bp3-elevation-1{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-elevation-2{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-2.bp3-dark,
  .bp3-dark .bp3-elevation-2{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4); }

.bp3-elevation-3{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-3.bp3-dark,
  .bp3-dark .bp3-elevation-3{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-elevation-4{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-4.bp3-dark,
  .bp3-dark .bp3-elevation-4{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:hover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  cursor:pointer; }
  .bp3-card.bp3-interactive:hover.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:hover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:active{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  opacity:0.9;
  -webkit-transition-duration:0;
          transition-duration:0; }
  .bp3-card.bp3-interactive:active.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:active{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-collapse{
  height:0;
  overflow-y:hidden;
  -webkit-transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-collapse .bp3-collapse-body{
    -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-collapse .bp3-collapse-body[aria-hidden="true"]{
      display:none; }

.bp3-context-menu .bp3-popover-target{
  display:block; }

.bp3-context-menu-popover-target{
  position:fixed; }

.bp3-divider{
  border-bottom:1px solid rgba(16, 22, 26, 0.15);
  border-right:1px solid rgba(16, 22, 26, 0.15);
  margin:5px; }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-dialog-container{
  opacity:1;
  -webkit-transform:scale(1);
          transform:scale(1);
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  min-height:100%;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none;
  width:100%; }
  .bp3-dialog-container.bp3-overlay-enter > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5); }
  .bp3-dialog-container.bp3-overlay-enter-active > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear-active > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-dialog-container.bp3-overlay-exit > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-dialog-container.bp3-overlay-exit-active > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }

.bp3-dialog{
  background:#ebf1f5;
  border-radius:6px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:30px 0;
  padding-bottom:20px;
  pointer-events:all;
  -webkit-user-select:text;
     -moz-user-select:text;
      -ms-user-select:text;
          user-select:text;
  width:500px; }
  .bp3-dialog:focus{
    outline:0; }
  .bp3-dialog.bp3-dark,
  .bp3-dark .bp3-dialog{
    background:#293742;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }

.bp3-dialog-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background:#ffffff;
  border-radius:6px 6px 0 0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  min-height:40px;
  padding-left:20px;
  padding-right:5px;
  z-index:30; }
  .bp3-dialog-header .bp3-icon-large,
  .bp3-dialog-header .bp3-icon{
    color:#5c7080;
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px; }
  .bp3-dialog-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:inherit;
    margin:0; }
    .bp3-dialog-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-dialog-header{
    background:#30404d;
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-dialog-header .bp3-icon-large,
    .bp3-dark .bp3-dialog-header .bp3-icon{
      color:#a7b6c2; }

.bp3-dialog-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  line-height:18px;
  margin:20px; }

.bp3-dialog-footer{
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  margin:0 20px; }

.bp3-dialog-footer-actions{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:end;
      -ms-flex-pack:end;
          justify-content:flex-end; }
  .bp3-dialog-footer-actions .bp3-button{
    margin-left:10px; }
.bp3-multistep-dialog-panels{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }

.bp3-multistep-dialog-left-panel{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:1;
      -ms-flex:1;
          flex:1;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column; }
  .bp3-dark .bp3-multistep-dialog-left-panel{
    background:#202b33; }

.bp3-multistep-dialog-right-panel{
  background-color:#f5f8fa;
  border-left:1px solid rgba(16, 22, 26, 0.15);
  border-radius:0 0 6px 0;
  -webkit-box-flex:3;
      -ms-flex:3;
          flex:3;
  min-width:0; }
  .bp3-dark .bp3-multistep-dialog-right-panel{
    background-color:#293742;
    border-left:1px solid rgba(16, 22, 26, 0.4); }

.bp3-multistep-dialog-footer{
  background-color:#ffffff;
  border-radius:0 0 6px 0;
  border-top:1px solid rgba(16, 22, 26, 0.15);
  padding:10px; }
  .bp3-dark .bp3-multistep-dialog-footer{
    background:#30404d;
    border-top:1px solid rgba(16, 22, 26, 0.4); }

.bp3-dialog-step-container{
  background-color:#f5f8fa;
  border-bottom:1px solid rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-dialog-step-container{
    background:#293742;
    border-bottom:1px solid rgba(16, 22, 26, 0.4); }
  .bp3-dialog-step-container.bp3-dialog-step-viewed{
    background-color:#ffffff; }
    .bp3-dark .bp3-dialog-step-container.bp3-dialog-step-viewed{
      background:#30404d; }

.bp3-dialog-step{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:#f5f8fa;
  border-radius:6px;
  cursor:not-allowed;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin:4px;
  padding:6px 14px; }
  .bp3-dark .bp3-dialog-step{
    background:#293742; }
  .bp3-dialog-step-viewed .bp3-dialog-step{
    background-color:#ffffff;
    cursor:pointer; }
    .bp3-dark .bp3-dialog-step-viewed .bp3-dialog-step{
      background:#30404d; }
  .bp3-dialog-step:hover{
    background-color:#f5f8fa; }
    .bp3-dark .bp3-dialog-step:hover{
      background:#293742; }

.bp3-dialog-step-icon{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:rgba(92, 112, 128, 0.6);
  border-radius:50%;
  color:#ffffff;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:25px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  width:25px; }
  .bp3-dark .bp3-dialog-step-icon{
    background-color:rgba(167, 182, 194, 0.6); }
  .bp3-active.bp3-dialog-step-viewed .bp3-dialog-step-icon{
    background-color:#2b95d6; }
  .bp3-dialog-step-viewed .bp3-dialog-step-icon{
    background-color:#8a9ba8; }

.bp3-dialog-step-title{
  color:rgba(92, 112, 128, 0.6);
  -webkit-box-flex:1;
      -ms-flex:1;
          flex:1;
  padding-left:10px; }
  .bp3-dark .bp3-dialog-step-title{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-active.bp3-dialog-step-viewed .bp3-dialog-step-title{
    color:#2b95d6; }
  .bp3-dialog-step-viewed:not(.bp3-active) .bp3-dialog-step-title{
    color:#182026; }
    .bp3-dark .bp3-dialog-step-viewed:not(.bp3-active) .bp3-dialog-step-title{
      color:#f5f8fa; }
.bp3-drawer{
  background:#ffffff;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0;
  padding:0; }
  .bp3-drawer:focus{
    outline:0; }
  .bp3-drawer.bp3-position-top{
    height:50%;
    left:0;
    right:0;
    top:0; }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter, .bp3-drawer.bp3-position-top.bp3-overlay-appear{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%); }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter-active, .bp3-drawer.bp3-position-top.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit-active{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-bottom{
    bottom:0;
    height:50%;
    left:0;
    right:0; }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter-active, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-left{
    bottom:0;
    left:0;
    top:0;
    width:50%; }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter, .bp3-drawer.bp3-position-left.bp3-overlay-appear{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%); }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter-active, .bp3-drawer.bp3-position-left.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit-active{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-right{
    bottom:0;
    right:0;
    top:0;
    width:50%; }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter, .bp3-drawer.bp3-position-right.bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter-active, .bp3-drawer.bp3-position-right.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right):not(.bp3-vertical){
    bottom:0;
    right:0;
    top:0;
    width:50%; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right).bp3-vertical{
    bottom:0;
    height:50%;
    left:0;
    right:0; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-dark,
  .bp3-dark .bp3-drawer{
    background:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }

.bp3-drawer-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border-radius:0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  min-height:40px;
  padding:5px;
  padding-left:20px;
  position:relative; }
  .bp3-drawer-header .bp3-icon-large,
  .bp3-drawer-header .bp3-icon{
    color:#5c7080;
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px; }
  .bp3-drawer-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:inherit;
    margin:0; }
    .bp3-drawer-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-drawer-header{
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-drawer-header .bp3-icon-large,
    .bp3-dark .bp3-drawer-header .bp3-icon{
      color:#a7b6c2; }

.bp3-drawer-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  line-height:18px;
  overflow:auto; }

.bp3-drawer-footer{
  -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  padding:10px 20px;
  position:relative; }
  .bp3-dark .bp3-drawer-footer{
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4); }
.bp3-editable-text{
  cursor:text;
  display:inline-block;
  max-width:100%;
  position:relative;
  vertical-align:top;
  white-space:nowrap; }
  .bp3-editable-text::before{
    bottom:-3px;
    left:-3px;
    position:absolute;
    right:-3px;
    top:-3px;
    border-radius:3px;
    content:"";
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-editable-text.bp3-editable-text-editing::before{
    background-color:#ffffff;
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#137cbd; }
  .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4); }
  .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#0f9960; }
  .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4); }
  .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#d9822b; }
  .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4); }
  .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#db3737; }
  .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4); }
  .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15); }
  .bp3-dark .bp3-editable-text.bp3-editable-text-editing::before{
    background-color:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#48aff0; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4);
            box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#3dcc91; }
  .bp3-dark .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4);
            box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#ffb366; }
  .bp3-dark .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4);
            box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#ff7373; }
  .bp3-dark .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4);
            box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-editable-text-input,
.bp3-editable-text-content{
  color:inherit;
  display:inherit;
  font:inherit;
  letter-spacing:inherit;
  max-width:inherit;
  min-width:inherit;
  position:relative;
  resize:none;
  text-transform:inherit;
  vertical-align:top; }

.bp3-editable-text-input{
  background:none;
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0;
  white-space:pre-wrap;
  width:100%; }
  .bp3-editable-text-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input:focus{
    outline:none; }
  .bp3-editable-text-input::-ms-clear{
    display:none; }

.bp3-editable-text-content{
  overflow:hidden;
  padding-right:2px;
  text-overflow:ellipsis;
  white-space:pre; }
  .bp3-editable-text-editing > .bp3-editable-text-content{
    left:0;
    position:absolute;
    visibility:hidden; }
  .bp3-editable-text-placeholder > .bp3-editable-text-content{
    color:rgba(92, 112, 128, 0.6); }
    .bp3-dark .bp3-editable-text-placeholder > .bp3-editable-text-content{
      color:rgba(167, 182, 194, 0.6); }

.bp3-editable-text.bp3-multiline{
  display:block; }
  .bp3-editable-text.bp3-multiline .bp3-editable-text-content{
    overflow:auto;
    white-space:pre-wrap;
    word-wrap:break-word; }
.bp3-divider{
  border-bottom:1px solid rgba(16, 22, 26, 0.15);
  border-right:1px solid rgba(16, 22, 26, 0.15);
  margin:5px; }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-control-group{
  -webkit-transform:translateZ(0);
          transform:translateZ(0);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:stretch;
      -ms-flex-align:stretch;
          align-items:stretch; }
  .bp3-control-group > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select,
  .bp3-control-group .bp3-input,
  .bp3-control-group .bp3-select{
    position:relative; }
  .bp3-control-group .bp3-input{
    border-radius:inherit;
    z-index:2; }
    .bp3-control-group .bp3-input:focus{
      border-radius:3px;
      z-index:14; }
    .bp3-control-group .bp3-input[class*="bp3-intent"]{
      z-index:13; }
      .bp3-control-group .bp3-input[class*="bp3-intent"]:focus{
        z-index:15; }
    .bp3-control-group .bp3-input[readonly], .bp3-control-group .bp3-input:disabled, .bp3-control-group .bp3-input.bp3-disabled{
      z-index:1; }
  .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input{
    z-index:13; }
    .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input:focus{
      z-index:15; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select select,
  .bp3-control-group .bp3-select select{
    -webkit-transform:translateZ(0);
            transform:translateZ(0);
    border-radius:inherit;
    z-index:4; }
    .bp3-control-group .bp3-button:focus,
    .bp3-control-group .bp3-html-select select:focus,
    .bp3-control-group .bp3-select select:focus{
      z-index:5; }
    .bp3-control-group .bp3-button:hover,
    .bp3-control-group .bp3-html-select select:hover,
    .bp3-control-group .bp3-select select:hover{
      z-index:6; }
    .bp3-control-group .bp3-button:active,
    .bp3-control-group .bp3-html-select select:active,
    .bp3-control-group .bp3-select select:active{
      z-index:7; }
    .bp3-control-group .bp3-button[readonly], .bp3-control-group .bp3-button:disabled, .bp3-control-group .bp3-button.bp3-disabled,
    .bp3-control-group .bp3-html-select select[readonly],
    .bp3-control-group .bp3-html-select select:disabled,
    .bp3-control-group .bp3-html-select select.bp3-disabled,
    .bp3-control-group .bp3-select select[readonly],
    .bp3-control-group .bp3-select select:disabled,
    .bp3-control-group .bp3-select select.bp3-disabled{
      z-index:3; }
    .bp3-control-group .bp3-button[class*="bp3-intent"],
    .bp3-control-group .bp3-html-select select[class*="bp3-intent"],
    .bp3-control-group .bp3-select select[class*="bp3-intent"]{
      z-index:9; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:focus{
        z-index:10; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:hover{
        z-index:11; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:active{
        z-index:12; }
      .bp3-control-group .bp3-button[class*="bp3-intent"][readonly], .bp3-control-group .bp3-button[class*="bp3-intent"]:disabled, .bp3-control-group .bp3-button[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"].bp3-disabled{
        z-index:8; }
  .bp3-control-group .bp3-input-group > .bp3-icon,
  .bp3-control-group .bp3-input-group > .bp3-button,
  .bp3-control-group .bp3-input-group > .bp3-input-left-container,
  .bp3-control-group .bp3-input-group > .bp3-input-action{
    z-index:16; }
  .bp3-control-group .bp3-select::after,
  .bp3-control-group .bp3-html-select::after,
  .bp3-control-group .bp3-select > .bp3-icon,
  .bp3-control-group .bp3-html-select > .bp3-icon{
    z-index:17; }
  .bp3-control-group .bp3-select:focus-within{
    z-index:5; }
  .bp3-control-group:not(.bp3-vertical) > *:not(.bp3-divider){
    margin-right:-1px; }
  .bp3-control-group:not(.bp3-vertical) > .bp3-divider:not(:first-child){
    margin-left:6px; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > *:not(.bp3-divider){
    margin-right:0; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > .bp3-button + .bp3-button{
    margin-left:1px; }
  .bp3-control-group .bp3-popover-wrapper,
  .bp3-control-group .bp3-popover-target{
    border-radius:inherit; }
  .bp3-control-group > :first-child{
    border-radius:3px 0 0 3px; }
  .bp3-control-group > :last-child{
    border-radius:0 3px 3px 0;
    margin-right:0; }
  .bp3-control-group > :only-child{
    border-radius:3px;
    margin-right:0; }
  .bp3-control-group .bp3-input-group .bp3-button{
    border-radius:3px; }
  .bp3-control-group .bp3-numeric-input:not(:first-child) .bp3-input-group{
    border-bottom-left-radius:0;
    border-top-left-radius:0; }
  .bp3-control-group.bp3-fill{
    width:100%; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-fill > *:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-vertical{
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-control-group.bp3-vertical > *{
      margin-top:-1px; }
    .bp3-control-group.bp3-vertical > :first-child{
      border-radius:3px 3px 0 0;
      margin-top:0; }
    .bp3-control-group.bp3-vertical > :last-child{
      border-radius:0 0 3px 3px; }
.bp3-control{
  cursor:pointer;
  display:block;
  margin-bottom:10px;
  position:relative;
  text-transform:none; }
  .bp3-control input:checked ~ .bp3-control-indicator{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
  .bp3-control:hover input:checked ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
  .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    background:#0e5a8a;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-control input:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control:hover input:checked ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    background-color:#0e5a8a;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-control:not(.bp3-align-right){
    padding-left:26px; }
    .bp3-control:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-26px; }
  .bp3-control.bp3-align-right{
    padding-right:26px; }
    .bp3-control.bp3-align-right .bp3-control-indicator{
      margin-right:-26px; }
  .bp3-control.bp3-disabled{
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-control.bp3-inline{
    display:inline-block;
    margin-right:20px; }
  .bp3-control input{
    left:0;
    opacity:0;
    position:absolute;
    top:0;
    z-index:-1; }
  .bp3-control .bp3-control-indicator{
    background-clip:padding-box;
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    border:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    cursor:pointer;
    display:inline-block;
    font-size:16px;
    height:1em;
    margin-right:10px;
    margin-top:-3px;
    position:relative;
    -webkit-user-select:none;
       -moz-user-select:none;
        -ms-user-select:none;
            user-select:none;
    vertical-align:middle;
    width:1em; }
    .bp3-control .bp3-control-indicator::before{
      content:"";
      display:block;
      height:1em;
      width:1em; }
  .bp3-control:hover .bp3-control-indicator{
    background-color:#ebf1f5; }
  .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
    background:#d8e1e8;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    cursor:not-allowed; }
  .bp3-control input:focus ~ .bp3-control-indicator{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:2px;
    -moz-outline-radius:6px; }
  .bp3-control.bp3-align-right .bp3-control-indicator{
    float:right;
    margin-left:10px;
    margin-top:1px; }
  .bp3-control.bp3-large{
    font-size:16px; }
    .bp3-control.bp3-large:not(.bp3-align-right){
      padding-left:30px; }
      .bp3-control.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
        margin-left:-30px; }
    .bp3-control.bp3-large.bp3-align-right{
      padding-right:30px; }
      .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
        margin-right:-30px; }
    .bp3-control.bp3-large .bp3-control-indicator{
      font-size:20px; }
    .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-top:0; }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
  .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
  .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    background:#0e5a8a;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    background-color:#0e5a8a;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-control.bp3-checkbox .bp3-control-indicator{
    border-radius:3px; }
  .bp3-control.bp3-checkbox input:checked ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M12 5c-.28 0-.53.11-.71.29L7 9.59l-2.29-2.3a1.003 1.003 0 00-1.42 1.42l3 3c.18.18.43.29.71.29s.53-.11.71-.29l5-5A1.003 1.003 0 0012 5z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M11 7H5c-.55 0-1 .45-1 1s.45 1 1 1h6c.55 0 1-.45 1-1s-.45-1-1-1z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-radio .bp3-control-indicator{
    border-radius:50%; }
  .bp3-control.bp3-radio input:checked ~ .bp3-control-indicator::before{
    background-image:radial-gradient(#ffffff, #ffffff 28%, transparent 32%); }
  .bp3-control.bp3-radio input:checked:disabled ~ .bp3-control-indicator::before{
    opacity:0.5; }
  .bp3-control.bp3-radio input:focus ~ .bp3-control-indicator{
    -moz-outline-radius:16px; }
  .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(167, 182, 194, 0.5); }
  .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(115, 134, 148, 0.5); }
  .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(92, 112, 128, 0.5); }
  .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5); }
    .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5); }
    .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch:not(.bp3-align-right){
    padding-left:38px; }
    .bp3-control.bp3-switch:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-38px; }
  .bp3-control.bp3-switch.bp3-align-right{
    padding-right:38px; }
    .bp3-control.bp3-switch.bp3-align-right .bp3-control-indicator{
      margin-right:-38px; }
  .bp3-control.bp3-switch .bp3-control-indicator{
    border:none;
    border-radius:1.75em;
    -webkit-box-shadow:none !important;
            box-shadow:none !important;
    min-width:1.75em;
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    width:auto; }
    .bp3-control.bp3-switch .bp3-control-indicator::before{
      background:#ffffff;
      border-radius:50%;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
      height:calc(1em - 4px);
      left:0;
      margin:2px;
      position:absolute;
      -webkit-transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      width:calc(1em - 4px); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    left:calc(100% - 1em); }
  .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right){
    padding-left:45px; }
    .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-45px; }
  .bp3-control.bp3-switch.bp3-large.bp3-align-right{
    padding-right:45px; }
    .bp3-control.bp3-switch.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-right:-45px; }
  .bp3-dark .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.7); }
  .bp3-dark .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.9); }
  .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(57, 75, 89, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-dark .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-dark .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch .bp3-control-indicator::before{
    background:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-control.bp3-switch .bp3-switch-inner-text{
    font-size:0.7em;
    text-align:center; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:first-child{
    line-height:0;
    margin-left:0.5em;
    margin-right:1.2em;
    visibility:hidden; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:last-child{
    line-height:1em;
    margin-left:1.2em;
    margin-right:0.5em;
    visibility:visible; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:first-child{
    line-height:1em;
    visibility:visible; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:last-child{
    line-height:0;
    visibility:hidden; }
  .bp3-dark .bp3-control{
    color:#f5f8fa; }
    .bp3-dark .bp3-control.bp3-disabled{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-control .bp3-control-indicator{
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-control:hover .bp3-control-indicator{
      background-color:#30404d; }
    .bp3-dark .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
      background:#202b33;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-control input:disabled ~ .bp3-control-indicator{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      cursor:not-allowed; }
    .bp3-dark .bp3-control.bp3-checkbox input:disabled:checked ~ .bp3-control-indicator, .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
      color:rgba(167, 182, 194, 0.6); }
.bp3-file-input{
  cursor:pointer;
  display:inline-block;
  height:30px;
  position:relative; }
  .bp3-file-input input{
    margin:0;
    min-width:200px;
    opacity:0; }
    .bp3-file-input input:disabled + .bp3-file-upload-input,
    .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
      background:rgba(206, 217, 224, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      resize:none; }
      .bp3-file-input input:disabled + .bp3-file-upload-input::after,
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
        background-color:rgba(206, 217, 224, 0.5);
        background-image:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(92, 112, 128, 0.6);
        cursor:not-allowed;
        outline:none; }
        .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active:hover,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active:hover{
          background:rgba(206, 217, 224, 0.7); }
      .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input, .bp3-dark
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
        background:rgba(57, 75, 89, 0.5);
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after, .bp3-dark
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
          background-color:rgba(57, 75, 89, 0.5);
          background-image:none;
          -webkit-box-shadow:none;
                  box-shadow:none;
          color:rgba(167, 182, 194, 0.6); }
          .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-dark
          .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active{
            background:rgba(57, 75, 89, 0.7); }
  .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#182026; }
  .bp3-dark .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#f5f8fa; }
  .bp3-file-input.bp3-fill{
    width:100%; }
  .bp3-file-input.bp3-large,
  .bp3-large .bp3-file-input{
    height:40px; }
  .bp3-file-input .bp3-file-upload-input-custom-text::after{
    content:attr(bp3-button-text); }

.bp3-file-upload-input{
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  background:#ffffff;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#182026;
  font-size:14px;
  font-weight:400;
  height:30px;
  line-height:30px;
  outline:none;
  padding:0 10px;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  vertical-align:middle;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  color:rgba(92, 112, 128, 0.6);
  left:0;
  padding-right:80px;
  position:absolute;
  right:0;
  top:0;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-file-upload-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input:focus, .bp3-file-upload-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-file-upload-input[type="search"], .bp3-file-upload-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-file-upload-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-file-upload-input:disabled, .bp3-file-upload-input.bp3-disabled{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    resize:none; }
  .bp3-file-upload-input::after{
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    color:#182026;
    min-height:24px;
    min-width:24px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    border-radius:3px;
    content:"Browse";
    line-height:24px;
    margin:3px;
    position:absolute;
    right:0;
    text-align:center;
    top:0;
    width:70px; }
    .bp3-file-upload-input::after:hover{
      background-clip:padding-box;
      background-color:#ebf1f5;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
    .bp3-file-upload-input::after:active, .bp3-file-upload-input::after.bp3-active{
      background-color:#d8e1e8;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-file-upload-input::after:disabled, .bp3-file-upload-input::after.bp3-disabled{
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      outline:none; }
      .bp3-file-upload-input::after:disabled.bp3-active, .bp3-file-upload-input::after:disabled.bp3-active:hover, .bp3-file-upload-input::after.bp3-disabled.bp3-active, .bp3-file-upload-input::after.bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-file-upload-input:hover::after{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-file-upload-input:active::after{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-large .bp3-file-upload-input{
    font-size:16px;
    height:40px;
    line-height:40px;
    padding-right:95px; }
    .bp3-large .bp3-file-upload-input[type="search"], .bp3-large .bp3-file-upload-input.bp3-round{
      padding:0 15px; }
    .bp3-large .bp3-file-upload-input::after{
      min-height:30px;
      min-width:30px;
      line-height:30px;
      margin:5px;
      width:85px; }
  .bp3-dark .bp3-file-upload-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:disabled, .bp3-dark .bp3-file-upload-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::after{
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
      color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover, .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover{
        background-color:#30404d;
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        background-color:#202b33;
        background-image:none;
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
      .bp3-dark .bp3-file-upload-input::after:disabled, .bp3-dark .bp3-file-upload-input::after.bp3-disabled{
        background-color:rgba(57, 75, 89, 0.5);
        background-image:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-upload-input::after:disabled.bp3-active, .bp3-dark .bp3-file-upload-input::after.bp3-disabled.bp3-active{
          background:rgba(57, 75, 89, 0.7); }
      .bp3-dark .bp3-file-upload-input::after .bp3-button-spinner .bp3-spinner-head{
        background:rgba(16, 22, 26, 0.5);
        stroke:#8a9ba8; }
    .bp3-dark .bp3-file-upload-input:hover::after{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:active::after{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
.bp3-file-upload-input::after{
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
.bp3-form-group{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0 0 15px; }
  .bp3-form-group label.bp3-label{
    margin-bottom:5px; }
  .bp3-form-group .bp3-control{
    margin-top:7px; }
  .bp3-form-group .bp3-form-helper-text{
    color:#5c7080;
    font-size:12px;
    margin-top:5px; }
  .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#106ba3; }
  .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#0d8050; }
  .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#bf7326; }
  .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#c23030; }
  .bp3-form-group.bp3-inline{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row; }
    .bp3-form-group.bp3-inline.bp3-large label.bp3-label{
      line-height:40px;
      margin:0 10px 0 0; }
    .bp3-form-group.bp3-inline label.bp3-label{
      line-height:30px;
      margin:0 10px 0 0; }
  .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-dark .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#48aff0; }
  .bp3-dark .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#3dcc91; }
  .bp3-dark .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#ffb366; }
  .bp3-dark .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#ff7373; }
  .bp3-dark .bp3-form-group .bp3-form-helper-text{
    color:#a7b6c2; }
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(167, 182, 194, 0.6) !important; }
.bp3-input-group{
  display:block;
  position:relative; }
  .bp3-input-group .bp3-input{
    position:relative;
    width:100%; }
    .bp3-input-group .bp3-input:not(:first-child){
      padding-left:30px; }
    .bp3-input-group .bp3-input:not(:last-child){
      padding-right:30px; }
  .bp3-input-group .bp3-input-action,
  .bp3-input-group > .bp3-input-left-container,
  .bp3-input-group > .bp3-button,
  .bp3-input-group > .bp3-icon{
    position:absolute;
    top:0; }
    .bp3-input-group .bp3-input-action:first-child,
    .bp3-input-group > .bp3-input-left-container:first-child,
    .bp3-input-group > .bp3-button:first-child,
    .bp3-input-group > .bp3-icon:first-child{
      left:0; }
    .bp3-input-group .bp3-input-action:last-child,
    .bp3-input-group > .bp3-input-left-container:last-child,
    .bp3-input-group > .bp3-button:last-child,
    .bp3-input-group > .bp3-icon:last-child{
      right:0; }
  .bp3-input-group .bp3-button{
    min-height:24px;
    min-width:24px;
    margin:3px;
    padding:0 7px; }
    .bp3-input-group .bp3-button:empty{
      padding:0; }
  .bp3-input-group > .bp3-input-left-container,
  .bp3-input-group > .bp3-icon{
    z-index:1; }
  .bp3-input-group > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group > .bp3-icon{
    color:#5c7080; }
    .bp3-input-group > .bp3-input-left-container > .bp3-icon:empty,
    .bp3-input-group > .bp3-icon:empty{
      font-family:"Icons16", sans-serif;
      font-size:16px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased; }
  .bp3-input-group > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group > .bp3-icon,
  .bp3-input-group .bp3-input-action > .bp3-spinner{
    margin:7px; }
  .bp3-input-group .bp3-tag{
    margin:5px; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus),
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
    color:#5c7080; }
    .bp3-dark .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus), .bp3-dark
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
      color:#a7b6c2; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large{
      color:#5c7080; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled,
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled{
    color:rgba(92, 112, 128, 0.6) !important; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-large{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-input-group.bp3-disabled{
    cursor:not-allowed; }
    .bp3-input-group.bp3-disabled .bp3-icon{
      color:rgba(92, 112, 128, 0.6); }
  .bp3-input-group.bp3-large .bp3-button{
    min-height:30px;
    min-width:30px;
    margin:5px; }
  .bp3-input-group.bp3-large > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group.bp3-large > .bp3-icon,
  .bp3-input-group.bp3-large .bp3-input-action > .bp3-spinner{
    margin:12px; }
  .bp3-input-group.bp3-large .bp3-input{
    font-size:16px;
    height:40px;
    line-height:40px; }
    .bp3-input-group.bp3-large .bp3-input[type="search"], .bp3-input-group.bp3-large .bp3-input.bp3-round{
      padding:0 15px; }
    .bp3-input-group.bp3-large .bp3-input:not(:first-child){
      padding-left:40px; }
    .bp3-input-group.bp3-large .bp3-input:not(:last-child){
      padding-right:40px; }
  .bp3-input-group.bp3-small .bp3-button{
    min-height:20px;
    min-width:20px;
    margin:2px; }
  .bp3-input-group.bp3-small .bp3-tag{
    min-height:20px;
    min-width:20px;
    margin:2px; }
  .bp3-input-group.bp3-small > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group.bp3-small > .bp3-icon,
  .bp3-input-group.bp3-small .bp3-input-action > .bp3-spinner{
    margin:4px; }
  .bp3-input-group.bp3-small .bp3-input{
    font-size:12px;
    height:24px;
    line-height:24px;
    padding-left:8px;
    padding-right:8px; }
    .bp3-input-group.bp3-small .bp3-input[type="search"], .bp3-input-group.bp3-small .bp3-input.bp3-round{
      padding:0 12px; }
    .bp3-input-group.bp3-small .bp3-input:not(:first-child){
      padding-left:24px; }
    .bp3-input-group.bp3-small .bp3-input:not(:last-child){
      padding-right:24px; }
  .bp3-input-group.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-input-group.bp3-round .bp3-button,
  .bp3-input-group.bp3-round .bp3-input,
  .bp3-input-group.bp3-round .bp3-tag{
    border-radius:30px; }
  .bp3-dark .bp3-input-group .bp3-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-input-group.bp3-disabled .bp3-icon{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-input-group.bp3-intent-primary .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input-group.bp3-intent-primary .bp3-input:disabled, .bp3-input-group.bp3-intent-primary .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-primary > .bp3-icon{
    color:#106ba3; }
    .bp3-dark .bp3-input-group.bp3-intent-primary > .bp3-icon{
      color:#48aff0; }
  .bp3-input-group.bp3-intent-success .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input-group.bp3-intent-success .bp3-input:disabled, .bp3-input-group.bp3-intent-success .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-success > .bp3-icon{
    color:#0d8050; }
    .bp3-dark .bp3-input-group.bp3-intent-success > .bp3-icon{
      color:#3dcc91; }
  .bp3-input-group.bp3-intent-warning .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input-group.bp3-intent-warning .bp3-input:disabled, .bp3-input-group.bp3-intent-warning .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-warning > .bp3-icon{
    color:#bf7326; }
    .bp3-dark .bp3-input-group.bp3-intent-warning > .bp3-icon{
      color:#ffb366; }
  .bp3-input-group.bp3-intent-danger .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input-group.bp3-intent-danger .bp3-input:disabled, .bp3-input-group.bp3-intent-danger .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-danger > .bp3-icon{
    color:#c23030; }
    .bp3-dark .bp3-input-group.bp3-intent-danger > .bp3-icon{
      color:#ff7373; }
.bp3-input{
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  background:#ffffff;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#182026;
  font-size:14px;
  font-weight:400;
  height:30px;
  line-height:30px;
  outline:none;
  padding:0 10px;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  vertical-align:middle; }
  .bp3-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input:focus, .bp3-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-input[type="search"], .bp3-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-input:disabled, .bp3-input.bp3-disabled{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    resize:none; }
  .bp3-input.bp3-large{
    font-size:16px;
    height:40px;
    line-height:40px; }
    .bp3-input.bp3-large[type="search"], .bp3-input.bp3-large.bp3-round{
      padding:0 15px; }
  .bp3-input.bp3-small{
    font-size:12px;
    height:24px;
    line-height:24px;
    padding-left:8px;
    padding-right:8px; }
    .bp3-input.bp3-small[type="search"], .bp3-input.bp3-small.bp3-round{
      padding:0 12px; }
  .bp3-input.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-dark .bp3-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input:disabled, .bp3-dark .bp3-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-input.bp3-intent-primary{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input.bp3-intent-primary:disabled, .bp3-input.bp3-intent-primary.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary:focus{
        -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #137cbd;
                box-shadow:inset 0 0 0 1px #137cbd; }
      .bp3-dark .bp3-input.bp3-intent-primary:disabled, .bp3-dark .bp3-input.bp3-intent-primary.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-success{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input.bp3-intent-success:disabled, .bp3-input.bp3-intent-success.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-success{
      -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success:focus{
        -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #0f9960;
                box-shadow:inset 0 0 0 1px #0f9960; }
      .bp3-dark .bp3-input.bp3-intent-success:disabled, .bp3-dark .bp3-input.bp3-intent-success.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-warning{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input.bp3-intent-warning:disabled, .bp3-input.bp3-intent-warning.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning:focus{
        -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #d9822b;
                box-shadow:inset 0 0 0 1px #d9822b; }
      .bp3-dark .bp3-input.bp3-intent-warning:disabled, .bp3-dark .bp3-input.bp3-intent-warning.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-danger{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input.bp3-intent-danger:disabled, .bp3-input.bp3-intent-danger.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger:focus{
        -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #db3737;
                box-shadow:inset 0 0 0 1px #db3737; }
      .bp3-dark .bp3-input.bp3-intent-danger:disabled, .bp3-dark .bp3-input.bp3-intent-danger.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input::-ms-clear{
    display:none; }
textarea.bp3-input{
  max-width:100%;
  padding:10px; }
  textarea.bp3-input, textarea.bp3-input.bp3-large, textarea.bp3-input.bp3-small{
    height:auto;
    line-height:inherit; }
  textarea.bp3-input.bp3-small{
    padding:8px; }
  .bp3-dark textarea.bp3-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark textarea.bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input:disabled, .bp3-dark textarea.bp3-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
label.bp3-label{
  display:block;
  margin-bottom:15px;
  margin-top:0; }
  label.bp3-label .bp3-html-select,
  label.bp3-label .bp3-input,
  label.bp3-label .bp3-select,
  label.bp3-label .bp3-slider,
  label.bp3-label .bp3-popover-wrapper{
    display:block;
    margin-top:5px;
    text-transform:none; }
  label.bp3-label .bp3-button-group{
    margin-top:5px; }
  label.bp3-label .bp3-select select,
  label.bp3-label .bp3-html-select select{
    font-weight:400;
    vertical-align:top;
    width:100%; }
  label.bp3-label.bp3-disabled,
  label.bp3-label.bp3-disabled .bp3-text-muted{
    color:rgba(92, 112, 128, 0.6); }
  label.bp3-label.bp3-inline{
    line-height:30px; }
    label.bp3-label.bp3-inline .bp3-html-select,
    label.bp3-label.bp3-inline .bp3-input,
    label.bp3-label.bp3-inline .bp3-input-group,
    label.bp3-label.bp3-inline .bp3-select,
    label.bp3-label.bp3-inline .bp3-popover-wrapper{
      display:inline-block;
      margin:0 0 0 5px;
      vertical-align:top; }
    label.bp3-label.bp3-inline .bp3-button-group{
      margin:0 0 0 5px; }
    label.bp3-label.bp3-inline .bp3-input-group .bp3-input{
      margin-left:0; }
    label.bp3-label.bp3-inline.bp3-large{
      line-height:40px; }
  label.bp3-label:not(.bp3-inline) .bp3-popover-target{
    display:block; }
  .bp3-dark label.bp3-label{
    color:#f5f8fa; }
    .bp3-dark label.bp3-label.bp3-disabled,
    .bp3-dark label.bp3-label.bp3-disabled .bp3-text-muted{
      color:rgba(167, 182, 194, 0.6); }
.bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button{
  -webkit-box-flex:1;
      -ms-flex:1 1 14px;
          flex:1 1 14px;
  min-height:0;
  padding:0;
  width:30px; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:first-child{
    border-radius:0 3px 0 0; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:last-child{
    border-radius:0 0 3px 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:first-child{
  border-radius:3px 0 0 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:last-child{
  border-radius:0 0 0 3px; }

.bp3-numeric-input.bp3-large .bp3-button-group.bp3-vertical > .bp3-button{
  width:40px; }

form{
  display:block; }
.bp3-html-select select,
.bp3-select select{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  font-size:14px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  padding:5px 10px;
  text-align:left;
  vertical-align:middle;
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  color:#182026;
  -moz-appearance:none;
  -webkit-appearance:none;
  border-radius:3px;
  height:30px;
  padding:0 25px 0 10px;
  width:100%; }
  .bp3-html-select select > *, .bp3-select select > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-html-select select > .bp3-fill, .bp3-select select > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-html-select select::before,
  .bp3-select select::before, .bp3-html-select select > *, .bp3-select select > *{
    margin-right:7px; }
  .bp3-html-select select:empty::before,
  .bp3-select select:empty::before,
  .bp3-html-select select > :last-child,
  .bp3-select select > :last-child{
    margin-right:0; }
  .bp3-html-select select:hover,
  .bp3-select select:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-html-select select:active,
  .bp3-select select:active, .bp3-html-select select.bp3-active,
  .bp3-select select.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-html-select select:disabled,
  .bp3-select select:disabled, .bp3-html-select select.bp3-disabled,
  .bp3-select select.bp3-disabled{
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    outline:none; }
    .bp3-html-select select:disabled.bp3-active,
    .bp3-select select:disabled.bp3-active, .bp3-html-select select:disabled.bp3-active:hover,
    .bp3-select select:disabled.bp3-active:hover, .bp3-html-select select.bp3-disabled.bp3-active,
    .bp3-select select.bp3-disabled.bp3-active, .bp3-html-select select.bp3-disabled.bp3-active:hover,
    .bp3-select select.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }

.bp3-html-select.bp3-minimal select,
.bp3-select.bp3-minimal select{
  background:none;
  -webkit-box-shadow:none;
          box-shadow:none; }
  .bp3-html-select.bp3-minimal select:hover,
  .bp3-select.bp3-minimal select:hover{
    background:rgba(167, 182, 194, 0.3);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:#182026;
    text-decoration:none; }
  .bp3-html-select.bp3-minimal select:active,
  .bp3-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal select.bp3-active,
  .bp3-select.bp3-minimal select.bp3-active{
    background:rgba(115, 134, 148, 0.3);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:#182026; }
  .bp3-html-select.bp3-minimal select:disabled,
  .bp3-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal select:disabled:hover,
  .bp3-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal select.bp3-disabled,
  .bp3-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal select.bp3-disabled:hover,
  .bp3-select.bp3-minimal select.bp3-disabled:hover{
    background:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
    .bp3-html-select.bp3-minimal select:disabled.bp3-active,
    .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active{
      background:rgba(115, 134, 148, 0.3); }
  .bp3-dark .bp3-html-select.bp3-minimal select, .bp3-html-select.bp3-minimal .bp3-dark select,
  .bp3-dark .bp3-select.bp3-minimal select, .bp3-select.bp3-minimal .bp3-dark select{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:inherit; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover, .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover{
      background:rgba(138, 155, 168, 0.15); }
    .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:rgba(138, 155, 168, 0.3);
      color:#f5f8fa; }
    .bp3-dark .bp3-html-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal .bp3-dark select:disabled,
    .bp3-dark .bp3-select.bp3-minimal select:disabled, .bp3-select.bp3-minimal .bp3-dark select:disabled, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select:disabled:hover, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover{
      background:none;
      color:rgba(167, 182, 194, 0.6);
      cursor:not-allowed; }
      .bp3-dark .bp3-html-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active{
        background:rgba(138, 155, 168, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-primary,
  .bp3-select.bp3-minimal select.bp3-intent-primary{
    color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover{
      background:rgba(19, 124, 189, 0.15);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:rgba(19, 124, 189, 0.3);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled{
      background:none;
      color:rgba(16, 107, 163, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active{
        background:rgba(19, 124, 189, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
      stroke:#106ba3; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary{
      color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.2);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(72, 175, 240, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-success,
  .bp3-select.bp3-minimal select.bp3-intent-success{
    color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover{
      background:rgba(15, 153, 96, 0.15);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:rgba(15, 153, 96, 0.3);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled{
      background:none;
      color:rgba(13, 128, 80, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active{
        background:rgba(15, 153, 96, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
      stroke:#0d8050; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success{
      color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.2);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(61, 204, 145, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-warning,
  .bp3-select.bp3-minimal select.bp3-intent-warning{
    color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover{
      background:rgba(217, 130, 43, 0.15);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:rgba(217, 130, 43, 0.3);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled{
      background:none;
      color:rgba(191, 115, 38, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active{
        background:rgba(217, 130, 43, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
      stroke:#bf7326; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning{
      color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.2);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(255, 179, 102, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-danger,
  .bp3-select.bp3-minimal select.bp3-intent-danger{
    color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover{
      background:rgba(219, 55, 55, 0.15);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:rgba(219, 55, 55, 0.3);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled{
      background:none;
      color:rgba(194, 48, 48, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active{
        background:rgba(219, 55, 55, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
      stroke:#c23030; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger{
      color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.2);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(255, 115, 115, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }

.bp3-html-select.bp3-large select,
.bp3-select.bp3-large select{
  font-size:16px;
  height:40px;
  padding-right:35px; }

.bp3-dark .bp3-html-select select, .bp3-dark .bp3-select select{
  background-color:#394b59;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
  color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover, .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    background-color:#202b33;
    background-image:none;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-html-select select:disabled, .bp3-dark .bp3-select select:disabled, .bp3-dark .bp3-html-select select.bp3-disabled, .bp3-dark .bp3-select select.bp3-disabled{
    background-color:rgba(57, 75, 89, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-html-select select:disabled.bp3-active, .bp3-dark .bp3-select select:disabled.bp3-active, .bp3-dark .bp3-html-select select.bp3-disabled.bp3-active, .bp3-dark .bp3-select select.bp3-disabled.bp3-active{
      background:rgba(57, 75, 89, 0.7); }
  .bp3-dark .bp3-html-select select .bp3-button-spinner .bp3-spinner-head, .bp3-dark .bp3-select select .bp3-button-spinner .bp3-spinner-head{
    background:rgba(16, 22, 26, 0.5);
    stroke:#8a9ba8; }

.bp3-html-select select:disabled,
.bp3-select select:disabled{
  background-color:rgba(206, 217, 224, 0.5);
  -webkit-box-shadow:none;
          box-shadow:none;
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-html-select .bp3-icon,
.bp3-select .bp3-icon, .bp3-select::after{
  color:#5c7080;
  pointer-events:none;
  position:absolute;
  right:7px;
  top:7px; }
  .bp3-html-select .bp3-disabled.bp3-icon,
  .bp3-select .bp3-disabled.bp3-icon, .bp3-disabled.bp3-select::after{
    color:rgba(92, 112, 128, 0.6); }
.bp3-html-select,
.bp3-select{
  display:inline-block;
  letter-spacing:normal;
  position:relative;
  vertical-align:middle; }
  .bp3-html-select select::-ms-expand,
  .bp3-select select::-ms-expand{
    display:none; }
  .bp3-html-select .bp3-icon,
  .bp3-select .bp3-icon{
    color:#5c7080; }
    .bp3-html-select .bp3-icon:hover,
    .bp3-select .bp3-icon:hover{
      color:#182026; }
    .bp3-dark .bp3-html-select .bp3-icon, .bp3-dark
    .bp3-select .bp3-icon{
      color:#a7b6c2; }
      .bp3-dark .bp3-html-select .bp3-icon:hover, .bp3-dark
      .bp3-select .bp3-icon:hover{
        color:#f5f8fa; }
  .bp3-html-select.bp3-large::after,
  .bp3-html-select.bp3-large .bp3-icon,
  .bp3-select.bp3-large::after,
  .bp3-select.bp3-large .bp3-icon{
    right:12px;
    top:12px; }
  .bp3-html-select.bp3-fill,
  .bp3-html-select.bp3-fill select,
  .bp3-select.bp3-fill,
  .bp3-select.bp3-fill select{
    width:100%; }
  .bp3-dark .bp3-html-select option, .bp3-dark
  .bp3-select option{
    background-color:#30404d;
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select option:disabled, .bp3-dark
  .bp3-select option:disabled{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-html-select::after, .bp3-dark
  .bp3-select::after{
    color:#a7b6c2; }

.bp3-select::after{
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  content:""; }
.bp3-running-text table, table.bp3-html-table{
  border-spacing:0;
  font-size:14px; }
  .bp3-running-text table th, table.bp3-html-table th,
  .bp3-running-text table td,
  table.bp3-html-table td{
    padding:11px;
    text-align:left;
    vertical-align:top; }
  .bp3-running-text table th, table.bp3-html-table th{
    color:#182026;
    font-weight:600; }
  
  .bp3-running-text table td,
  table.bp3-html-table td{
    color:#182026; }
  .bp3-running-text table tbody tr:first-child th, table.bp3-html-table tbody tr:first-child th,
  .bp3-running-text table tbody tr:first-child td,
  table.bp3-html-table tbody tr:first-child td,
  .bp3-running-text table tfoot tr:first-child th,
  table.bp3-html-table tfoot tr:first-child th,
  .bp3-running-text table tfoot tr:first-child td,
  table.bp3-html-table tfoot tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-running-text table th, .bp3-running-text .bp3-dark table th, .bp3-dark table.bp3-html-table th{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table td, .bp3-running-text .bp3-dark table td, .bp3-dark table.bp3-html-table td{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table tbody tr:first-child th, .bp3-running-text .bp3-dark table tbody tr:first-child th, .bp3-dark table.bp3-html-table tbody tr:first-child th,
  .bp3-dark .bp3-running-text table tbody tr:first-child td,
  .bp3-running-text .bp3-dark table tbody tr:first-child td,
  .bp3-dark table.bp3-html-table tbody tr:first-child td,
  .bp3-dark .bp3-running-text table tfoot tr:first-child th,
  .bp3-running-text .bp3-dark table tfoot tr:first-child th,
  .bp3-dark table.bp3-html-table tfoot tr:first-child th,
  .bp3-dark .bp3-running-text table tfoot tr:first-child td,
  .bp3-running-text .bp3-dark table tfoot tr:first-child td,
  .bp3-dark table.bp3-html-table tfoot tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }

table.bp3-html-table.bp3-html-table-condensed th,
table.bp3-html-table.bp3-html-table-condensed td, table.bp3-html-table.bp3-small th,
table.bp3-html-table.bp3-small td{
  padding-bottom:6px;
  padding-top:6px; }

table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
  background:rgba(191, 204, 214, 0.15); }

table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
  -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered tbody tr td,
table.bp3-html-table.bp3-html-table-bordered tfoot tr td{
  -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child),
  table.bp3-html-table.bp3-html-table-bordered tfoot tr td:not(:first-child){
    -webkit-box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
  -webkit-box-shadow:none;
          box-shadow:none; }
  table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:not(:first-child){
    -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-interactive tbody tr:hover td{
  background-color:rgba(191, 204, 214, 0.3);
  cursor:pointer; }

table.bp3-html-table.bp3-interactive tbody tr:active td{
  background-color:rgba(191, 204, 214, 0.4); }

.bp3-dark table.bp3-html-table{ }
  .bp3-dark table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
    background:rgba(92, 112, 128, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
    -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td,
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered tfoot tr td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child),
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered tfoot tr td:not(:first-child){
      -webkit-box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15);
              box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
    -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:first-child{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-dark table.bp3-html-table.bp3-interactive tbody tr:hover td{
    background-color:rgba(92, 112, 128, 0.3);
    cursor:pointer; }
  .bp3-dark table.bp3-html-table.bp3-interactive tbody tr:active td{
    background-color:rgba(92, 112, 128, 0.4); }

.bp3-key-combo{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center; }
  .bp3-key-combo > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-key-combo > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-key-combo::before,
  .bp3-key-combo > *{
    margin-right:5px; }
  .bp3-key-combo:empty::before,
  .bp3-key-combo > :last-child{
    margin-right:0; }

.bp3-hotkey-dialog{
  padding-bottom:0;
  top:40px; }
  .bp3-hotkey-dialog .bp3-dialog-body{
    margin:0;
    padding:0; }
  .bp3-hotkey-dialog .bp3-hotkey-label{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1; }

.bp3-hotkey-column{
  margin:auto;
  max-height:80vh;
  overflow-y:auto;
  padding:30px; }
  .bp3-hotkey-column .bp3-heading{
    margin-bottom:20px; }
    .bp3-hotkey-column .bp3-heading:not(:first-child){
      margin-top:40px; }

.bp3-hotkey{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:justify;
      -ms-flex-pack:justify;
          justify-content:space-between;
  margin-left:0;
  margin-right:0; }
  .bp3-hotkey:not(:last-child){
    margin-bottom:10px; }
.bp3-icon{
  display:inline-block;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  vertical-align:text-bottom; }
  .bp3-icon:not(:empty)::before{
    content:"" !important;
    content:unset !important; }
  .bp3-icon > svg{
    display:block; }
    .bp3-icon > svg:not([fill]){
      fill:currentColor; }

.bp3-icon.bp3-intent-primary, .bp3-icon-standard.bp3-intent-primary, .bp3-icon-large.bp3-intent-primary{
  color:#106ba3; }
  .bp3-dark .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-icon-large.bp3-intent-primary{
    color:#48aff0; }

.bp3-icon.bp3-intent-success, .bp3-icon-standard.bp3-intent-success, .bp3-icon-large.bp3-intent-success{
  color:#0d8050; }
  .bp3-dark .bp3-icon.bp3-intent-success, .bp3-dark .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-icon-large.bp3-intent-success{
    color:#3dcc91; }

.bp3-icon.bp3-intent-warning, .bp3-icon-standard.bp3-intent-warning, .bp3-icon-large.bp3-intent-warning{
  color:#bf7326; }
  .bp3-dark .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-icon-large.bp3-intent-warning{
    color:#ffb366; }

.bp3-icon.bp3-intent-danger, .bp3-icon-standard.bp3-intent-danger, .bp3-icon-large.bp3-intent-danger{
  color:#c23030; }
  .bp3-dark .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-icon-large.bp3-intent-danger{
    color:#ff7373; }

span.bp3-icon-standard{
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon-large{
  font-family:"Icons20", sans-serif;
  font-size:20px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon:empty{
  font-family:"Icons20";
  font-size:inherit;
  font-style:normal;
  font-weight:400;
  line-height:1; }
  span.bp3-icon:empty::before{
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased; }

.bp3-icon-add::before{
  content:""; }

.bp3-icon-add-column-left::before{
  content:""; }

.bp3-icon-add-column-right::before{
  content:""; }

.bp3-icon-add-row-bottom::before{
  content:""; }

.bp3-icon-add-row-top::before{
  content:""; }

.bp3-icon-add-to-artifact::before{
  content:""; }

.bp3-icon-add-to-folder::before{
  content:""; }

.bp3-icon-airplane::before{
  content:""; }

.bp3-icon-align-center::before{
  content:""; }

.bp3-icon-align-justify::before{
  content:""; }

.bp3-icon-align-left::before{
  content:""; }

.bp3-icon-align-right::before{
  content:""; }

.bp3-icon-alignment-bottom::before{
  content:""; }

.bp3-icon-alignment-horizontal-center::before{
  content:""; }

.bp3-icon-alignment-left::before{
  content:""; }

.bp3-icon-alignment-right::before{
  content:""; }

.bp3-icon-alignment-top::before{
  content:""; }

.bp3-icon-alignment-vertical-center::before{
  content:""; }

.bp3-icon-annotation::before{
  content:""; }

.bp3-icon-application::before{
  content:""; }

.bp3-icon-applications::before{
  content:""; }

.bp3-icon-archive::before{
  content:""; }

.bp3-icon-arrow-bottom-left::before{
  content:"↙"; }

.bp3-icon-arrow-bottom-right::before{
  content:"↘"; }

.bp3-icon-arrow-down::before{
  content:"↓"; }

.bp3-icon-arrow-left::before{
  content:"←"; }

.bp3-icon-arrow-right::before{
  content:"→"; }

.bp3-icon-arrow-top-left::before{
  content:"↖"; }

.bp3-icon-arrow-top-right::before{
  content:"↗"; }

.bp3-icon-arrow-up::before{
  content:"↑"; }

.bp3-icon-arrows-horizontal::before{
  content:"↔"; }

.bp3-icon-arrows-vertical::before{
  content:"↕"; }

.bp3-icon-asterisk::before{
  content:"*"; }

.bp3-icon-automatic-updates::before{
  content:""; }

.bp3-icon-badge::before{
  content:""; }

.bp3-icon-ban-circle::before{
  content:""; }

.bp3-icon-bank-account::before{
  content:""; }

.bp3-icon-barcode::before{
  content:""; }

.bp3-icon-blank::before{
  content:""; }

.bp3-icon-blocked-person::before{
  content:""; }

.bp3-icon-bold::before{
  content:""; }

.bp3-icon-book::before{
  content:""; }

.bp3-icon-bookmark::before{
  content:""; }

.bp3-icon-box::before{
  content:""; }

.bp3-icon-briefcase::before{
  content:""; }

.bp3-icon-bring-data::before{
  content:""; }

.bp3-icon-build::before{
  content:""; }

.bp3-icon-calculator::before{
  content:""; }

.bp3-icon-calendar::before{
  content:""; }

.bp3-icon-camera::before{
  content:""; }

.bp3-icon-caret-down::before{
  content:"⌄"; }

.bp3-icon-caret-left::before{
  content:"〈"; }

.bp3-icon-caret-right::before{
  content:"〉"; }

.bp3-icon-caret-up::before{
  content:"⌃"; }

.bp3-icon-cell-tower::before{
  content:""; }

.bp3-icon-changes::before{
  content:""; }

.bp3-icon-chart::before{
  content:""; }

.bp3-icon-chat::before{
  content:""; }

.bp3-icon-chevron-backward::before{
  content:""; }

.bp3-icon-chevron-down::before{
  content:""; }

.bp3-icon-chevron-forward::before{
  content:""; }

.bp3-icon-chevron-left::before{
  content:""; }

.bp3-icon-chevron-right::before{
  content:""; }

.bp3-icon-chevron-up::before{
  content:""; }

.bp3-icon-circle::before{
  content:""; }

.bp3-icon-circle-arrow-down::before{
  content:""; }

.bp3-icon-circle-arrow-left::before{
  content:""; }

.bp3-icon-circle-arrow-right::before{
  content:""; }

.bp3-icon-circle-arrow-up::before{
  content:""; }

.bp3-icon-citation::before{
  content:""; }

.bp3-icon-clean::before{
  content:""; }

.bp3-icon-clipboard::before{
  content:""; }

.bp3-icon-cloud::before{
  content:"☁"; }

.bp3-icon-cloud-download::before{
  content:""; }

.bp3-icon-cloud-upload::before{
  content:""; }

.bp3-icon-code::before{
  content:""; }

.bp3-icon-code-block::before{
  content:""; }

.bp3-icon-cog::before{
  content:""; }

.bp3-icon-collapse-all::before{
  content:""; }

.bp3-icon-column-layout::before{
  content:""; }

.bp3-icon-comment::before{
  content:""; }

.bp3-icon-comparison::before{
  content:""; }

.bp3-icon-compass::before{
  content:""; }

.bp3-icon-compressed::before{
  content:""; }

.bp3-icon-confirm::before{
  content:""; }

.bp3-icon-console::before{
  content:""; }

.bp3-icon-contrast::before{
  content:""; }

.bp3-icon-control::before{
  content:""; }

.bp3-icon-credit-card::before{
  content:""; }

.bp3-icon-cross::before{
  content:"✗"; }

.bp3-icon-crown::before{
  content:""; }

.bp3-icon-cube::before{
  content:""; }

.bp3-icon-cube-add::before{
  content:""; }

.bp3-icon-cube-remove::before{
  content:""; }

.bp3-icon-curved-range-chart::before{
  content:""; }

.bp3-icon-cut::before{
  content:""; }

.bp3-icon-dashboard::before{
  content:""; }

.bp3-icon-data-lineage::before{
  content:""; }

.bp3-icon-database::before{
  content:""; }

.bp3-icon-delete::before{
  content:""; }

.bp3-icon-delta::before{
  content:"Δ"; }

.bp3-icon-derive-column::before{
  content:""; }

.bp3-icon-desktop::before{
  content:""; }

.bp3-icon-diagnosis::before{
  content:""; }

.bp3-icon-diagram-tree::before{
  content:""; }

.bp3-icon-direction-left::before{
  content:""; }

.bp3-icon-direction-right::before{
  content:""; }

.bp3-icon-disable::before{
  content:""; }

.bp3-icon-document::before{
  content:""; }

.bp3-icon-document-open::before{
  content:""; }

.bp3-icon-document-share::before{
  content:""; }

.bp3-icon-dollar::before{
  content:"$"; }

.bp3-icon-dot::before{
  content:"•"; }

.bp3-icon-double-caret-horizontal::before{
  content:""; }

.bp3-icon-double-caret-vertical::before{
  content:""; }

.bp3-icon-double-chevron-down::before{
  content:""; }

.bp3-icon-double-chevron-left::before{
  content:""; }

.bp3-icon-double-chevron-right::before{
  content:""; }

.bp3-icon-double-chevron-up::before{
  content:""; }

.bp3-icon-doughnut-chart::before{
  content:""; }

.bp3-icon-download::before{
  content:""; }

.bp3-icon-drag-handle-horizontal::before{
  content:""; }

.bp3-icon-drag-handle-vertical::before{
  content:""; }

.bp3-icon-draw::before{
  content:""; }

.bp3-icon-drive-time::before{
  content:""; }

.bp3-icon-duplicate::before{
  content:""; }

.bp3-icon-edit::before{
  content:"✎"; }

.bp3-icon-eject::before{
  content:"⏏"; }

.bp3-icon-endorsed::before{
  content:""; }

.bp3-icon-envelope::before{
  content:"✉"; }

.bp3-icon-equals::before{
  content:""; }

.bp3-icon-eraser::before{
  content:""; }

.bp3-icon-error::before{
  content:""; }

.bp3-icon-euro::before{
  content:"€"; }

.bp3-icon-exchange::before{
  content:""; }

.bp3-icon-exclude-row::before{
  content:""; }

.bp3-icon-expand-all::before{
  content:""; }

.bp3-icon-export::before{
  content:""; }

.bp3-icon-eye-off::before{
  content:""; }

.bp3-icon-eye-on::before{
  content:""; }

.bp3-icon-eye-open::before{
  content:""; }

.bp3-icon-fast-backward::before{
  content:""; }

.bp3-icon-fast-forward::before{
  content:""; }

.bp3-icon-feed::before{
  content:""; }

.bp3-icon-feed-subscribed::before{
  content:""; }

.bp3-icon-film::before{
  content:""; }

.bp3-icon-filter::before{
  content:""; }

.bp3-icon-filter-keep::before{
  content:""; }

.bp3-icon-filter-list::before{
  content:""; }

.bp3-icon-filter-open::before{
  content:""; }

.bp3-icon-filter-remove::before{
  content:""; }

.bp3-icon-flag::before{
  content:"⚑"; }

.bp3-icon-flame::before{
  content:""; }

.bp3-icon-flash::before{
  content:""; }

.bp3-icon-floppy-disk::before{
  content:""; }

.bp3-icon-flow-branch::before{
  content:""; }

.bp3-icon-flow-end::before{
  content:""; }

.bp3-icon-flow-linear::before{
  content:""; }

.bp3-icon-flow-review::before{
  content:""; }

.bp3-icon-flow-review-branch::before{
  content:""; }

.bp3-icon-flows::before{
  content:""; }

.bp3-icon-folder-close::before{
  content:""; }

.bp3-icon-folder-new::before{
  content:""; }

.bp3-icon-folder-open::before{
  content:""; }

.bp3-icon-folder-shared::before{
  content:""; }

.bp3-icon-folder-shared-open::before{
  content:""; }

.bp3-icon-follower::before{
  content:""; }

.bp3-icon-following::before{
  content:""; }

.bp3-icon-font::before{
  content:""; }

.bp3-icon-fork::before{
  content:""; }

.bp3-icon-form::before{
  content:""; }

.bp3-icon-full-circle::before{
  content:""; }

.bp3-icon-full-stacked-chart::before{
  content:""; }

.bp3-icon-fullscreen::before{
  content:""; }

.bp3-icon-function::before{
  content:""; }

.bp3-icon-gantt-chart::before{
  content:""; }

.bp3-icon-geolocation::before{
  content:""; }

.bp3-icon-geosearch::before{
  content:""; }

.bp3-icon-git-branch::before{
  content:""; }

.bp3-icon-git-commit::before{
  content:""; }

.bp3-icon-git-merge::before{
  content:""; }

.bp3-icon-git-new-branch::before{
  content:""; }

.bp3-icon-git-pull::before{
  content:""; }

.bp3-icon-git-push::before{
  content:""; }

.bp3-icon-git-repo::before{
  content:""; }

.bp3-icon-glass::before{
  content:""; }

.bp3-icon-globe::before{
  content:""; }

.bp3-icon-globe-network::before{
  content:""; }

.bp3-icon-graph::before{
  content:""; }

.bp3-icon-graph-remove::before{
  content:""; }

.bp3-icon-greater-than::before{
  content:""; }

.bp3-icon-greater-than-or-equal-to::before{
  content:""; }

.bp3-icon-grid::before{
  content:""; }

.bp3-icon-grid-view::before{
  content:""; }

.bp3-icon-group-objects::before{
  content:""; }

.bp3-icon-grouped-bar-chart::before{
  content:""; }

.bp3-icon-hand::before{
  content:""; }

.bp3-icon-hand-down::before{
  content:""; }

.bp3-icon-hand-left::before{
  content:""; }

.bp3-icon-hand-right::before{
  content:""; }

.bp3-icon-hand-up::before{
  content:""; }

.bp3-icon-header::before{
  content:""; }

.bp3-icon-header-one::before{
  content:""; }

.bp3-icon-header-two::before{
  content:""; }

.bp3-icon-headset::before{
  content:""; }

.bp3-icon-heart::before{
  content:"♥"; }

.bp3-icon-heart-broken::before{
  content:""; }

.bp3-icon-heat-grid::before{
  content:""; }

.bp3-icon-heatmap::before{
  content:""; }

.bp3-icon-help::before{
  content:"?"; }

.bp3-icon-helper-management::before{
  content:""; }

.bp3-icon-highlight::before{
  content:""; }

.bp3-icon-history::before{
  content:""; }

.bp3-icon-home::before{
  content:"⌂"; }

.bp3-icon-horizontal-bar-chart::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-asc::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-desc::before{
  content:""; }

.bp3-icon-horizontal-distribution::before{
  content:""; }

.bp3-icon-id-number::before{
  content:""; }

.bp3-icon-image-rotate-left::before{
  content:""; }

.bp3-icon-image-rotate-right::before{
  content:""; }

.bp3-icon-import::before{
  content:""; }

.bp3-icon-inbox::before{
  content:""; }

.bp3-icon-inbox-filtered::before{
  content:""; }

.bp3-icon-inbox-geo::before{
  content:""; }

.bp3-icon-inbox-search::before{
  content:""; }

.bp3-icon-inbox-update::before{
  content:""; }

.bp3-icon-info-sign::before{
  content:"ℹ"; }

.bp3-icon-inheritance::before{
  content:""; }

.bp3-icon-inner-join::before{
  content:""; }

.bp3-icon-insert::before{
  content:""; }

.bp3-icon-intersection::before{
  content:""; }

.bp3-icon-ip-address::before{
  content:""; }

.bp3-icon-issue::before{
  content:""; }

.bp3-icon-issue-closed::before{
  content:""; }

.bp3-icon-issue-new::before{
  content:""; }

.bp3-icon-italic::before{
  content:""; }

.bp3-icon-join-table::before{
  content:""; }

.bp3-icon-key::before{
  content:""; }

.bp3-icon-key-backspace::before{
  content:""; }

.bp3-icon-key-command::before{
  content:""; }

.bp3-icon-key-control::before{
  content:""; }

.bp3-icon-key-delete::before{
  content:""; }

.bp3-icon-key-enter::before{
  content:""; }

.bp3-icon-key-escape::before{
  content:""; }

.bp3-icon-key-option::before{
  content:""; }

.bp3-icon-key-shift::before{
  content:""; }

.bp3-icon-key-tab::before{
  content:""; }

.bp3-icon-known-vehicle::before{
  content:""; }

.bp3-icon-lab-test::before{
  content:""; }

.bp3-icon-label::before{
  content:""; }

.bp3-icon-layer::before{
  content:""; }

.bp3-icon-layers::before{
  content:""; }

.bp3-icon-layout::before{
  content:""; }

.bp3-icon-layout-auto::before{
  content:""; }

.bp3-icon-layout-balloon::before{
  content:""; }

.bp3-icon-layout-circle::before{
  content:""; }

.bp3-icon-layout-grid::before{
  content:""; }

.bp3-icon-layout-group-by::before{
  content:""; }

.bp3-icon-layout-hierarchy::before{
  content:""; }

.bp3-icon-layout-linear::before{
  content:""; }

.bp3-icon-layout-skew-grid::before{
  content:""; }

.bp3-icon-layout-sorted-clusters::before{
  content:""; }

.bp3-icon-learning::before{
  content:""; }

.bp3-icon-left-join::before{
  content:""; }

.bp3-icon-less-than::before{
  content:""; }

.bp3-icon-less-than-or-equal-to::before{
  content:""; }

.bp3-icon-lifesaver::before{
  content:""; }

.bp3-icon-lightbulb::before{
  content:""; }

.bp3-icon-link::before{
  content:""; }

.bp3-icon-list::before{
  content:"☰"; }

.bp3-icon-list-columns::before{
  content:""; }

.bp3-icon-list-detail-view::before{
  content:""; }

.bp3-icon-locate::before{
  content:""; }

.bp3-icon-lock::before{
  content:""; }

.bp3-icon-log-in::before{
  content:""; }

.bp3-icon-log-out::before{
  content:""; }

.bp3-icon-manual::before{
  content:""; }

.bp3-icon-manually-entered-data::before{
  content:""; }

.bp3-icon-map::before{
  content:""; }

.bp3-icon-map-create::before{
  content:""; }

.bp3-icon-map-marker::before{
  content:""; }

.bp3-icon-maximize::before{
  content:""; }

.bp3-icon-media::before{
  content:""; }

.bp3-icon-menu::before{
  content:""; }

.bp3-icon-menu-closed::before{
  content:""; }

.bp3-icon-menu-open::before{
  content:""; }

.bp3-icon-merge-columns::before{
  content:""; }

.bp3-icon-merge-links::before{
  content:""; }

.bp3-icon-minimize::before{
  content:""; }

.bp3-icon-minus::before{
  content:"−"; }

.bp3-icon-mobile-phone::before{
  content:""; }

.bp3-icon-mobile-video::before{
  content:""; }

.bp3-icon-moon::before{
  content:""; }

.bp3-icon-more::before{
  content:""; }

.bp3-icon-mountain::before{
  content:""; }

.bp3-icon-move::before{
  content:""; }

.bp3-icon-mugshot::before{
  content:""; }

.bp3-icon-multi-select::before{
  content:""; }

.bp3-icon-music::before{
  content:""; }

.bp3-icon-new-drawing::before{
  content:""; }

.bp3-icon-new-grid-item::before{
  content:""; }

.bp3-icon-new-layer::before{
  content:""; }

.bp3-icon-new-layers::before{
  content:""; }

.bp3-icon-new-link::before{
  content:""; }

.bp3-icon-new-object::before{
  content:""; }

.bp3-icon-new-person::before{
  content:""; }

.bp3-icon-new-prescription::before{
  content:""; }

.bp3-icon-new-text-box::before{
  content:""; }

.bp3-icon-ninja::before{
  content:""; }

.bp3-icon-not-equal-to::before{
  content:""; }

.bp3-icon-notifications::before{
  content:""; }

.bp3-icon-notifications-updated::before{
  content:""; }

.bp3-icon-numbered-list::before{
  content:""; }

.bp3-icon-numerical::before{
  content:""; }

.bp3-icon-office::before{
  content:""; }

.bp3-icon-offline::before{
  content:""; }

.bp3-icon-oil-field::before{
  content:""; }

.bp3-icon-one-column::before{
  content:""; }

.bp3-icon-outdated::before{
  content:""; }

.bp3-icon-page-layout::before{
  content:""; }

.bp3-icon-panel-stats::before{
  content:""; }

.bp3-icon-panel-table::before{
  content:""; }

.bp3-icon-paperclip::before{
  content:""; }

.bp3-icon-paragraph::before{
  content:""; }

.bp3-icon-path::before{
  content:""; }

.bp3-icon-path-search::before{
  content:""; }

.bp3-icon-pause::before{
  content:""; }

.bp3-icon-people::before{
  content:""; }

.bp3-icon-percentage::before{
  content:""; }

.bp3-icon-person::before{
  content:""; }

.bp3-icon-phone::before{
  content:"☎"; }

.bp3-icon-pie-chart::before{
  content:""; }

.bp3-icon-pin::before{
  content:""; }

.bp3-icon-pivot::before{
  content:""; }

.bp3-icon-pivot-table::before{
  content:""; }

.bp3-icon-play::before{
  content:""; }

.bp3-icon-plus::before{
  content:"+"; }

.bp3-icon-polygon-filter::before{
  content:""; }

.bp3-icon-power::before{
  content:""; }

.bp3-icon-predictive-analysis::before{
  content:""; }

.bp3-icon-prescription::before{
  content:""; }

.bp3-icon-presentation::before{
  content:""; }

.bp3-icon-print::before{
  content:"⎙"; }

.bp3-icon-projects::before{
  content:""; }

.bp3-icon-properties::before{
  content:""; }

.bp3-icon-property::before{
  content:""; }

.bp3-icon-publish-function::before{
  content:""; }

.bp3-icon-pulse::before{
  content:""; }

.bp3-icon-random::before{
  content:""; }

.bp3-icon-record::before{
  content:""; }

.bp3-icon-redo::before{
  content:""; }

.bp3-icon-refresh::before{
  content:""; }

.bp3-icon-regression-chart::before{
  content:""; }

.bp3-icon-remove::before{
  content:""; }

.bp3-icon-remove-column::before{
  content:""; }

.bp3-icon-remove-column-left::before{
  content:""; }

.bp3-icon-remove-column-right::before{
  content:""; }

.bp3-icon-remove-row-bottom::before{
  content:""; }

.bp3-icon-remove-row-top::before{
  content:""; }

.bp3-icon-repeat::before{
  content:""; }

.bp3-icon-reset::before{
  content:""; }

.bp3-icon-resolve::before{
  content:""; }

.bp3-icon-rig::before{
  content:""; }

.bp3-icon-right-join::before{
  content:""; }

.bp3-icon-ring::before{
  content:""; }

.bp3-icon-rotate-document::before{
  content:""; }

.bp3-icon-rotate-page::before{
  content:""; }

.bp3-icon-satellite::before{
  content:""; }

.bp3-icon-saved::before{
  content:""; }

.bp3-icon-scatter-plot::before{
  content:""; }

.bp3-icon-search::before{
  content:""; }

.bp3-icon-search-around::before{
  content:""; }

.bp3-icon-search-template::before{
  content:""; }

.bp3-icon-search-text::before{
  content:""; }

.bp3-icon-segmented-control::before{
  content:""; }

.bp3-icon-select::before{
  content:""; }

.bp3-icon-selection::before{
  content:"⦿"; }

.bp3-icon-send-to::before{
  content:""; }

.bp3-icon-send-to-graph::before{
  content:""; }

.bp3-icon-send-to-map::before{
  content:""; }

.bp3-icon-series-add::before{
  content:""; }

.bp3-icon-series-configuration::before{
  content:""; }

.bp3-icon-series-derived::before{
  content:""; }

.bp3-icon-series-filtered::before{
  content:""; }

.bp3-icon-series-search::before{
  content:""; }

.bp3-icon-settings::before{
  content:""; }

.bp3-icon-share::before{
  content:""; }

.bp3-icon-shield::before{
  content:""; }

.bp3-icon-shop::before{
  content:""; }

.bp3-icon-shopping-cart::before{
  content:""; }

.bp3-icon-signal-search::before{
  content:""; }

.bp3-icon-sim-card::before{
  content:""; }

.bp3-icon-slash::before{
  content:""; }

.bp3-icon-small-cross::before{
  content:""; }

.bp3-icon-small-minus::before{
  content:""; }

.bp3-icon-small-plus::before{
  content:""; }

.bp3-icon-small-tick::before{
  content:""; }

.bp3-icon-snowflake::before{
  content:""; }

.bp3-icon-social-media::before{
  content:""; }

.bp3-icon-sort::before{
  content:""; }

.bp3-icon-sort-alphabetical::before{
  content:""; }

.bp3-icon-sort-alphabetical-desc::before{
  content:""; }

.bp3-icon-sort-asc::before{
  content:""; }

.bp3-icon-sort-desc::before{
  content:""; }

.bp3-icon-sort-numerical::before{
  content:""; }

.bp3-icon-sort-numerical-desc::before{
  content:""; }

.bp3-icon-split-columns::before{
  content:""; }

.bp3-icon-square::before{
  content:""; }

.bp3-icon-stacked-chart::before{
  content:""; }

.bp3-icon-star::before{
  content:"★"; }

.bp3-icon-star-empty::before{
  content:"☆"; }

.bp3-icon-step-backward::before{
  content:""; }

.bp3-icon-step-chart::before{
  content:""; }

.bp3-icon-step-forward::before{
  content:""; }

.bp3-icon-stop::before{
  content:""; }

.bp3-icon-stopwatch::before{
  content:""; }

.bp3-icon-strikethrough::before{
  content:""; }

.bp3-icon-style::before{
  content:""; }

.bp3-icon-swap-horizontal::before{
  content:""; }

.bp3-icon-swap-vertical::before{
  content:""; }

.bp3-icon-symbol-circle::before{
  content:""; }

.bp3-icon-symbol-cross::before{
  content:""; }

.bp3-icon-symbol-diamond::before{
  content:""; }

.bp3-icon-symbol-square::before{
  content:""; }

.bp3-icon-symbol-triangle-down::before{
  content:""; }

.bp3-icon-symbol-triangle-up::before{
  content:""; }

.bp3-icon-tag::before{
  content:""; }

.bp3-icon-take-action::before{
  content:""; }

.bp3-icon-taxi::before{
  content:""; }

.bp3-icon-text-highlight::before{
  content:""; }

.bp3-icon-th::before{
  content:""; }

.bp3-icon-th-derived::before{
  content:""; }

.bp3-icon-th-disconnect::before{
  content:""; }

.bp3-icon-th-filtered::before{
  content:""; }

.bp3-icon-th-list::before{
  content:""; }

.bp3-icon-thumbs-down::before{
  content:""; }

.bp3-icon-thumbs-up::before{
  content:""; }

.bp3-icon-tick::before{
  content:"✓"; }

.bp3-icon-tick-circle::before{
  content:""; }

.bp3-icon-time::before{
  content:"⏲"; }

.bp3-icon-timeline-area-chart::before{
  content:""; }

.bp3-icon-timeline-bar-chart::before{
  content:""; }

.bp3-icon-timeline-events::before{
  content:""; }

.bp3-icon-timeline-line-chart::before{
  content:""; }

.bp3-icon-tint::before{
  content:""; }

.bp3-icon-torch::before{
  content:""; }

.bp3-icon-tractor::before{
  content:""; }

.bp3-icon-train::before{
  content:""; }

.bp3-icon-translate::before{
  content:""; }

.bp3-icon-trash::before{
  content:""; }

.bp3-icon-tree::before{
  content:""; }

.bp3-icon-trending-down::before{
  content:""; }

.bp3-icon-trending-up::before{
  content:""; }

.bp3-icon-truck::before{
  content:""; }

.bp3-icon-two-columns::before{
  content:""; }

.bp3-icon-unarchive::before{
  content:""; }

.bp3-icon-underline::before{
  content:"⎁"; }

.bp3-icon-undo::before{
  content:"⎌"; }

.bp3-icon-ungroup-objects::before{
  content:""; }

.bp3-icon-unknown-vehicle::before{
  content:""; }

.bp3-icon-unlock::before{
  content:""; }

.bp3-icon-unpin::before{
  content:""; }

.bp3-icon-unresolve::before{
  content:""; }

.bp3-icon-updated::before{
  content:""; }

.bp3-icon-upload::before{
  content:""; }

.bp3-icon-user::before{
  content:""; }

.bp3-icon-variable::before{
  content:""; }

.bp3-icon-vertical-bar-chart-asc::before{
  content:""; }

.bp3-icon-vertical-bar-chart-desc::before{
  content:""; }

.bp3-icon-vertical-distribution::before{
  content:""; }

.bp3-icon-video::before{
  content:""; }

.bp3-icon-volume-down::before{
  content:""; }

.bp3-icon-volume-off::before{
  content:""; }

.bp3-icon-volume-up::before{
  content:""; }

.bp3-icon-walk::before{
  content:""; }

.bp3-icon-warning-sign::before{
  content:""; }

.bp3-icon-waterfall-chart::before{
  content:""; }

.bp3-icon-widget::before{
  content:""; }

.bp3-icon-widget-button::before{
  content:""; }

.bp3-icon-widget-footer::before{
  content:""; }

.bp3-icon-widget-header::before{
  content:""; }

.bp3-icon-wrench::before{
  content:""; }

.bp3-icon-zoom-in::before{
  content:""; }

.bp3-icon-zoom-out::before{
  content:""; }

.bp3-icon-zoom-to-fit::before{
  content:""; }
.bp3-submenu > .bp3-popover-wrapper{
  display:block; }

.bp3-submenu .bp3-popover-target{
  display:block; }
  .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{ }

.bp3-submenu.bp3-popover{
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0 5px; }
  .bp3-submenu.bp3-popover > .bp3-popover-content{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-submenu.bp3-popover, .bp3-submenu.bp3-popover.bp3-dark{
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-dark .bp3-submenu.bp3-popover > .bp3-popover-content, .bp3-submenu.bp3-popover.bp3-dark > .bp3-popover-content{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
.bp3-menu{
  background:#ffffff;
  border-radius:3px;
  color:#182026;
  list-style:none;
  margin:0;
  min-width:180px;
  padding:5px;
  text-align:left; }

.bp3-menu-divider{
  border-top:1px solid rgba(16, 22, 26, 0.15);
  display:block;
  margin:5px; }
  .bp3-dark .bp3-menu-divider{
    border-top-color:rgba(255, 255, 255, 0.15); }

.bp3-menu-item{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  border-radius:2px;
  color:inherit;
  line-height:20px;
  padding:5px 7px;
  text-decoration:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-menu-item > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-menu-item > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-menu-item::before,
  .bp3-menu-item > *{
    margin-right:7px; }
  .bp3-menu-item:empty::before,
  .bp3-menu-item > :last-child{
    margin-right:0; }
  .bp3-menu-item > .bp3-fill{
    word-break:break-word; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    background-color:rgba(167, 182, 194, 0.3);
    cursor:pointer;
    text-decoration:none; }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-dark .bp3-menu-item{
    color:inherit; }
    .bp3-dark .bp3-menu-item:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
      background-color:rgba(138, 155, 168, 0.15);
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-disabled{
      background-color:inherit;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-menu-item.bp3-intent-primary{
    color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-primary::before, .bp3-menu-item.bp3-intent-primary::after,
    .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
      color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary.bp3-active{
      background-color:#137cbd; }
    .bp3-menu-item.bp3-intent-primary:active{
      background-color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary:active, .bp3-menu-item.bp3-intent-primary:active::before, .bp3-menu-item.bp3-intent-primary:active::after,
    .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-menu-item.bp3-intent-primary.bp3-active::after,
    .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-success{
    color:#0d8050; }
    .bp3-menu-item.bp3-intent-success .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-success::before, .bp3-menu-item.bp3-intent-success::after,
    .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
      color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success.bp3-active{
      background-color:#0f9960; }
    .bp3-menu-item.bp3-intent-success:active{
      background-color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-menu-item.bp3-intent-success:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success:active, .bp3-menu-item.bp3-intent-success:active::before, .bp3-menu-item.bp3-intent-success:active::after,
    .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-menu-item.bp3-intent-success.bp3-active::after,
    .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-warning{
    color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-warning::before, .bp3-menu-item.bp3-intent-warning::after,
    .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
      color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning.bp3-active{
      background-color:#d9822b; }
    .bp3-menu-item.bp3-intent-warning:active{
      background-color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning:active, .bp3-menu-item.bp3-intent-warning:active::before, .bp3-menu-item.bp3-intent-warning:active::after,
    .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-menu-item.bp3-intent-warning.bp3-active::after,
    .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-danger{
    color:#c23030; }
    .bp3-menu-item.bp3-intent-danger .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-danger::before, .bp3-menu-item.bp3-intent-danger::after,
    .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
      color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger.bp3-active{
      background-color:#db3737; }
    .bp3-menu-item.bp3-intent-danger:active{
      background-color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger:active, .bp3-menu-item.bp3-intent-danger:active::before, .bp3-menu-item.bp3-intent-danger:active::after,
    .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-menu-item.bp3-intent-danger.bp3-active::after,
    .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    margin-right:7px; }
  .bp3-menu-item::before,
  .bp3-menu-item > .bp3-icon{
    color:#5c7080;
    margin-top:2px; }
  .bp3-menu-item .bp3-menu-item-label{
    color:#5c7080; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    color:inherit; }
  .bp3-menu-item.bp3-active, .bp3-menu-item:active{
    background-color:rgba(115, 134, 148, 0.3); }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit !important;
    color:rgba(92, 112, 128, 0.6) !important;
    cursor:not-allowed !important;
    outline:none !important; }
    .bp3-menu-item.bp3-disabled::before,
    .bp3-menu-item.bp3-disabled > .bp3-icon,
    .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-large .bp3-menu-item{
    font-size:16px;
    line-height:22px;
    padding:9px 7px; }
    .bp3-large .bp3-menu-item .bp3-icon{
      margin-top:3px; }
    .bp3-large .bp3-menu-item::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      margin-right:10px;
      margin-top:1px; }

button.bp3-menu-item{
  background:none;
  border:none;
  text-align:left;
  width:100%; }
.bp3-menu-header{
  border-top:1px solid rgba(16, 22, 26, 0.15);
  display:block;
  margin:5px;
  cursor:default;
  padding-left:2px; }
  .bp3-dark .bp3-menu-header{
    border-top-color:rgba(255, 255, 255, 0.15); }
  .bp3-menu-header:first-of-type{
    border-top:none; }
  .bp3-menu-header > h6{
    color:#182026;
    font-weight:600;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    line-height:17px;
    margin:0;
    padding:10px 7px 0 1px; }
    .bp3-dark .bp3-menu-header > h6{
      color:#f5f8fa; }
  .bp3-menu-header:first-of-type > h6{
    padding-top:0; }
  .bp3-large .bp3-menu-header > h6{
    font-size:18px;
    padding-bottom:5px;
    padding-top:15px; }
  .bp3-large .bp3-menu-header:first-of-type > h6{
    padding-top:0; }

.bp3-dark .bp3-menu{
  background:#30404d;
  color:#f5f8fa; }

.bp3-dark .bp3-menu-item{ }
  .bp3-dark .bp3-menu-item.bp3-intent-primary{
    color:#48aff0; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary::before, .bp3-dark .bp3-menu-item.bp3-intent-primary::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
      color:#48aff0; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active{
      background-color:#137cbd; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:active{
      background-color:#106ba3; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary:active, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-success{
    color:#3dcc91; }
    .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-success::before, .bp3-dark .bp3-menu-item.bp3-intent-success::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
      color:#3dcc91; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active{
      background-color:#0f9960; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:active{
      background-color:#0d8050; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success:active, .bp3-dark .bp3-menu-item.bp3-intent-success:active::before, .bp3-dark .bp3-menu-item.bp3-intent-success:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning{
    color:#ffb366; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning::before, .bp3-dark .bp3-menu-item.bp3-intent-warning::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
      color:#ffb366; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active{
      background-color:#d9822b; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:active{
      background-color:#bf7326; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning:active, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger{
    color:#ff7373; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger::before, .bp3-dark .bp3-menu-item.bp3-intent-danger::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
      color:#ff7373; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active{
      background-color:#db3737; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:active{
      background-color:#c23030; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger:active, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item::before,
  .bp3-dark .bp3-menu-item > .bp3-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-menu-item .bp3-menu-item-label{
    color:#a7b6c2; }
  .bp3-dark .bp3-menu-item.bp3-active, .bp3-dark .bp3-menu-item:active{
    background-color:rgba(138, 155, 168, 0.3); }
  .bp3-dark .bp3-menu-item.bp3-disabled{
    color:rgba(167, 182, 194, 0.6) !important; }
    .bp3-dark .bp3-menu-item.bp3-disabled::before,
    .bp3-dark .bp3-menu-item.bp3-disabled > .bp3-icon,
    .bp3-dark .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
      color:rgba(167, 182, 194, 0.6) !important; }

.bp3-dark .bp3-menu-divider,
.bp3-dark .bp3-menu-header{
  border-color:rgba(255, 255, 255, 0.15); }

.bp3-dark .bp3-menu-header > h6{
  color:#f5f8fa; }

.bp3-label .bp3-menu{
  margin-top:5px; }
.bp3-navbar{
  background-color:#ffffff;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  height:50px;
  padding:0 15px;
  position:relative;
  width:100%;
  z-index:10; }
  .bp3-navbar.bp3-dark,
  .bp3-dark .bp3-navbar{
    background-color:#394b59; }
  .bp3-navbar.bp3-dark{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-navbar{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-navbar.bp3-fixed-top{
    left:0;
    position:fixed;
    right:0;
    top:0; }

.bp3-navbar-heading{
  font-size:16px;
  margin-right:15px; }

.bp3-navbar-group{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:50px; }
  .bp3-navbar-group.bp3-align-left{
    float:left; }
  .bp3-navbar-group.bp3-align-right{
    float:right; }

.bp3-navbar-divider{
  border-left:1px solid rgba(16, 22, 26, 0.15);
  height:20px;
  margin:0 10px; }
  .bp3-dark .bp3-navbar-divider{
    border-left-color:rgba(255, 255, 255, 0.15); }
.bp3-non-ideal-state{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  height:100%;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  text-align:center;
  width:100%; }
  .bp3-non-ideal-state > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-non-ideal-state > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-non-ideal-state::before,
  .bp3-non-ideal-state > *{
    margin-bottom:20px; }
  .bp3-non-ideal-state:empty::before,
  .bp3-non-ideal-state > :last-child{
    margin-bottom:0; }
  .bp3-non-ideal-state > *{
    max-width:400px; }

.bp3-non-ideal-state-visual{
  color:rgba(92, 112, 128, 0.6);
  font-size:60px; }
  .bp3-dark .bp3-non-ideal-state-visual{
    color:rgba(167, 182, 194, 0.6); }

.bp3-overflow-list{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:nowrap;
      flex-wrap:nowrap;
  min-width:0; }

.bp3-overflow-list-spacer{
  -ms-flex-negative:1;
      flex-shrink:1;
  width:1px; }

body.bp3-overlay-open{
  overflow:hidden; }

.bp3-overlay{
  bottom:0;
  left:0;
  position:static;
  right:0;
  top:0;
  z-index:20; }
  .bp3-overlay:not(.bp3-overlay-open){
    pointer-events:none; }
  .bp3-overlay.bp3-overlay-container{
    overflow:hidden;
    position:fixed; }
    .bp3-overlay.bp3-overlay-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-scroll-container{
    overflow:auto;
    position:fixed; }
    .bp3-overlay.bp3-overlay-scroll-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-inline{
    display:inline;
    overflow:visible; }

.bp3-overlay-content{
  position:fixed;
  z-index:20; }
  .bp3-overlay-inline .bp3-overlay-content,
  .bp3-overlay-scroll-container .bp3-overlay-content{
    position:absolute; }

.bp3-overlay-backdrop{
  bottom:0;
  left:0;
  position:fixed;
  right:0;
  top:0;
  opacity:1;
  background-color:rgba(16, 22, 26, 0.7);
  overflow:auto;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none;
  z-index:20; }
  .bp3-overlay-backdrop.bp3-overlay-enter, .bp3-overlay-backdrop.bp3-overlay-appear{
    opacity:0; }
  .bp3-overlay-backdrop.bp3-overlay-enter-active, .bp3-overlay-backdrop.bp3-overlay-appear-active{
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-overlay-backdrop.bp3-overlay-exit{
    opacity:1; }
  .bp3-overlay-backdrop.bp3-overlay-exit-active{
    opacity:0;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-overlay-backdrop:focus{
    outline:none; }
  .bp3-overlay-inline .bp3-overlay-backdrop{
    position:absolute; }
.bp3-panel-stack{
  overflow:hidden;
  position:relative; }

.bp3-panel-stack-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-shadow:0 1px rgba(16, 22, 26, 0.15);
          box-shadow:0 1px rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-negative:0;
      flex-shrink:0;
  height:30px;
  z-index:1; }
  .bp3-dark .bp3-panel-stack-header{
    -webkit-box-shadow:0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 1px rgba(255, 255, 255, 0.15); }
  .bp3-panel-stack-header > span{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1;
            flex:1; }
  .bp3-panel-stack-header .bp3-heading{
    margin:0 5px; }

.bp3-button.bp3-panel-stack-header-back{
  margin-left:5px;
  padding-left:0;
  white-space:nowrap; }
  .bp3-button.bp3-panel-stack-header-back .bp3-icon{
    margin:0 2px; }

.bp3-panel-stack-view{
  bottom:0;
  left:0;
  position:absolute;
  right:0;
  top:0;
  background-color:#ffffff;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin-right:-1px;
  overflow-y:auto;
  z-index:1; }
  .bp3-dark .bp3-panel-stack-view{
    background-color:#30404d; }
  .bp3-panel-stack-view:nth-last-child(n + 4){
    display:none; }

.bp3-panel-stack-push .bp3-panel-stack-enter, .bp3-panel-stack-push .bp3-panel-stack-appear{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0; }

.bp3-panel-stack-push .bp3-panel-stack-enter-active, .bp3-panel-stack-push .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-push .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-push .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-pop .bp3-panel-stack-enter, .bp3-panel-stack-pop .bp3-panel-stack-appear{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0; }

.bp3-panel-stack-pop .bp3-panel-stack-enter-active, .bp3-panel-stack-pop .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-pop .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-pop .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }
.bp3-panel-stack2{
  overflow:hidden;
  position:relative; }

.bp3-panel-stack2-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-shadow:0 1px rgba(16, 22, 26, 0.15);
          box-shadow:0 1px rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-negative:0;
      flex-shrink:0;
  height:30px;
  z-index:1; }
  .bp3-dark .bp3-panel-stack2-header{
    -webkit-box-shadow:0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 1px rgba(255, 255, 255, 0.15); }
  .bp3-panel-stack2-header > span{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1;
            flex:1; }
  .bp3-panel-stack2-header .bp3-heading{
    margin:0 5px; }

.bp3-button.bp3-panel-stack2-header-back{
  margin-left:5px;
  padding-left:0;
  white-space:nowrap; }
  .bp3-button.bp3-panel-stack2-header-back .bp3-icon{
    margin:0 2px; }

.bp3-panel-stack2-view{
  bottom:0;
  left:0;
  position:absolute;
  right:0;
  top:0;
  background-color:#ffffff;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin-right:-1px;
  overflow-y:auto;
  z-index:1; }
  .bp3-dark .bp3-panel-stack2-view{
    background-color:#30404d; }
  .bp3-panel-stack2-view:nth-last-child(n + 4){
    display:none; }

.bp3-panel-stack2-push .bp3-panel-stack2-enter, .bp3-panel-stack2-push .bp3-panel-stack2-appear{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0; }

.bp3-panel-stack2-push .bp3-panel-stack2-enter-active, .bp3-panel-stack2-push .bp3-panel-stack2-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-push .bp3-panel-stack2-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack2-push .bp3-panel-stack2-exit-active{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-pop .bp3-panel-stack2-enter, .bp3-panel-stack2-pop .bp3-panel-stack2-appear{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0; }

.bp3-panel-stack2-pop .bp3-panel-stack2-enter-active, .bp3-panel-stack2-pop .bp3-panel-stack2-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-pop .bp3-panel-stack2-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack2-pop .bp3-panel-stack2-exit-active{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }
.bp3-popover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1);
  border-radius:3px;
  display:inline-block;
  z-index:20; }
  .bp3-popover .bp3-popover-arrow{
    height:30px;
    position:absolute;
    width:30px; }
    .bp3-popover .bp3-popover-arrow::before{
      height:20px;
      margin:5px;
      width:20px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover{
    margin-bottom:17px;
    margin-top:-17px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
      bottom:-11px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover{
    margin-left:17px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
      left:-11px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover{
    margin-top:17px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
      top:-11px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover{
    margin-left:-17px;
    margin-right:17px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
      right:-11px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-popover > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-popover > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
    top:-0.3934px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
    right:-0.3934px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
    left:-0.3934px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
    bottom:-0.3934px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-popover .bp3-popover-content{
    background:#ffffff;
    color:inherit; }
  .bp3-popover .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-popover .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-popover .bp3-popover-arrow-fill{
    fill:#ffffff; }
  .bp3-popover-enter > .bp3-popover, .bp3-popover-appear > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3); }
  .bp3-popover-enter-active > .bp3-popover, .bp3-popover-appear-active > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-popover-exit > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-popover .bp3-popover-content{
    border-radius:3px;
    position:relative; }
  .bp3-popover.bp3-popover-content-sizing .bp3-popover-content{
    max-width:350px;
    padding:20px; }
  .bp3-popover-target + .bp3-overlay .bp3-popover.bp3-popover-content-sizing{
    width:350px; }
  .bp3-popover.bp3-minimal{
    margin:0 !important; }
    .bp3-popover.bp3-minimal .bp3-popover-arrow{
      display:none; }
    .bp3-popover.bp3-minimal.bp3-popover{
      -webkit-transform:scale(1);
              transform:scale(1); }
      .bp3-popover-enter > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-enter-active > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-delay:0;
                transition-delay:0;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
      .bp3-popover-exit > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-exit-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-delay:0;
                transition-delay:0;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-popover.bp3-dark,
  .bp3-dark .bp3-popover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-popover .bp3-popover-content{
      background:#30404d;
      color:inherit; }
    .bp3-popover.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-popover .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-popover .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-popover.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-popover .bp3-popover-arrow-fill{
      fill:#30404d; }

.bp3-popover-arrow::before{
  border-radius:2px;
  content:"";
  display:block;
  position:absolute;
  -webkit-transform:rotate(45deg);
          transform:rotate(45deg); }

.bp3-tether-pinned .bp3-popover-arrow{
  display:none; }

.bp3-popover-backdrop{
  background:rgba(255, 255, 255, 0); }

.bp3-transition-container{
  opacity:1;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  z-index:20; }
  .bp3-transition-container.bp3-popover-enter, .bp3-transition-container.bp3-popover-appear{
    opacity:0; }
  .bp3-transition-container.bp3-popover-enter-active, .bp3-transition-container.bp3-popover-appear-active{
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-transition-container.bp3-popover-exit{
    opacity:1; }
  .bp3-transition-container.bp3-popover-exit-active{
    opacity:0;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-transition-container:focus{
    outline:none; }
  .bp3-transition-container.bp3-popover-leave .bp3-popover-content{
    pointer-events:none; }
  .bp3-transition-container[data-x-out-of-boundaries]{
    display:none; }

span.bp3-popover-target{
  display:inline-block; }

.bp3-popover-wrapper.bp3-fill{
  width:100%; }

.bp3-portal{
  left:0;
  position:absolute;
  right:0;
  top:0; }
@-webkit-keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }
@keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }

.bp3-progress-bar{
  background:rgba(92, 112, 128, 0.2);
  border-radius:40px;
  display:block;
  height:8px;
  overflow:hidden;
  position:relative;
  width:100%; }
  .bp3-progress-bar .bp3-progress-meter{
    background:linear-gradient(-45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%);
    background-color:rgba(92, 112, 128, 0.8);
    background-size:30px 30px;
    border-radius:40px;
    height:100%;
    position:absolute;
    -webkit-transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    width:100%; }
  .bp3-progress-bar:not(.bp3-no-animation):not(.bp3-no-stripes) .bp3-progress-meter{
    animation:linear-progress-bar-stripes 300ms linear infinite reverse; }
  .bp3-progress-bar.bp3-no-stripes .bp3-progress-meter{
    background-image:none; }

.bp3-dark .bp3-progress-bar{
  background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-progress-bar .bp3-progress-meter{
    background-color:#8a9ba8; }

.bp3-progress-bar.bp3-intent-primary .bp3-progress-meter{
  background-color:#137cbd; }

.bp3-progress-bar.bp3-intent-success .bp3-progress-meter{
  background-color:#0f9960; }

.bp3-progress-bar.bp3-intent-warning .bp3-progress-meter{
  background-color:#d9822b; }

.bp3-progress-bar.bp3-intent-danger .bp3-progress-meter{
  background-color:#db3737; }
@-webkit-keyframes skeleton-glow{
  from{
    background:rgba(206, 217, 224, 0.2);
    border-color:rgba(206, 217, 224, 0.2); }
  to{
    background:rgba(92, 112, 128, 0.2);
    border-color:rgba(92, 112, 128, 0.2); } }
@keyframes skeleton-glow{
  from{
    background:rgba(206, 217, 224, 0.2);
    border-color:rgba(206, 217, 224, 0.2); }
  to{
    background:rgba(92, 112, 128, 0.2);
    border-color:rgba(92, 112, 128, 0.2); } }
.bp3-skeleton{
  -webkit-animation:1000ms linear infinite alternate skeleton-glow;
          animation:1000ms linear infinite alternate skeleton-glow;
  background:rgba(206, 217, 224, 0.2);
  background-clip:padding-box !important;
  border-color:rgba(206, 217, 224, 0.2) !important;
  border-radius:2px;
  -webkit-box-shadow:none !important;
          box-shadow:none !important;
  color:transparent !important;
  cursor:default;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-skeleton::before, .bp3-skeleton::after,
  .bp3-skeleton *{
    visibility:hidden !important; }
.bp3-slider{
  height:40px;
  min-width:150px;
  width:100%;
  cursor:default;
  outline:none;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-slider:hover{
    cursor:pointer; }
  .bp3-slider:active{
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-slider.bp3-disabled{
    cursor:not-allowed;
    opacity:0.5; }
  .bp3-slider.bp3-slider-unlabeled{
    height:16px; }

.bp3-slider-track,
.bp3-slider-progress{
  height:6px;
  left:0;
  right:0;
  top:5px;
  position:absolute; }

.bp3-slider-track{
  border-radius:3px;
  overflow:hidden; }

.bp3-slider-progress{
  background:rgba(92, 112, 128, 0.2); }
  .bp3-dark .bp3-slider-progress{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-slider-progress.bp3-intent-primary{
    background-color:#137cbd; }
  .bp3-slider-progress.bp3-intent-success{
    background-color:#0f9960; }
  .bp3-slider-progress.bp3-intent-warning{
    background-color:#d9822b; }
  .bp3-slider-progress.bp3-intent-danger{
    background-color:#db3737; }

.bp3-slider-handle{
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  color:#182026;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
  cursor:pointer;
  height:16px;
  left:0;
  position:absolute;
  top:0;
  width:16px; }
  .bp3-slider-handle:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-slider-handle:active, .bp3-slider-handle.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-slider-handle:disabled, .bp3-slider-handle.bp3-disabled{
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    outline:none; }
    .bp3-slider-handle:disabled.bp3-active, .bp3-slider-handle:disabled.bp3-active:hover, .bp3-slider-handle.bp3-disabled.bp3-active, .bp3-slider-handle.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }
  .bp3-slider-handle:focus{
    z-index:1; }
  .bp3-slider-handle:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
    cursor:-webkit-grab;
    cursor:grab;
    z-index:2; }
  .bp3-slider-handle.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-disabled .bp3-slider-handle{
    background:#bfccd6;
    -webkit-box-shadow:none;
            box-shadow:none;
    pointer-events:none; }
  .bp3-dark .bp3-slider-handle{
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover, .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-slider-handle:disabled, .bp3-dark .bp3-slider-handle.bp3-disabled{
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-slider-handle:disabled.bp3-active, .bp3-dark .bp3-slider-handle.bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-slider-handle .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-slider-handle, .bp3-dark .bp3-slider-handle:hover{
      background-color:#394b59; }
    .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#293742; }
  .bp3-dark .bp3-disabled .bp3-slider-handle{
    background:#5c7080;
    border-color:#5c7080;
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-slider-handle .bp3-slider-label{
    background:#394b59;
    border-radius:3px;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
    color:#f5f8fa;
    margin-left:8px; }
    .bp3-dark .bp3-slider-handle .bp3-slider-label{
      background:#e1e8ed;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
      color:#394b59; }
    .bp3-disabled .bp3-slider-handle .bp3-slider-label{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-slider-handle.bp3-start, .bp3-slider-handle.bp3-end{
    width:8px; }
  .bp3-slider-handle.bp3-start{
    border-bottom-right-radius:0;
    border-top-right-radius:0; }
  .bp3-slider-handle.bp3-end{
    border-bottom-left-radius:0;
    border-top-left-radius:0;
    margin-left:8px; }
    .bp3-slider-handle.bp3-end .bp3-slider-label{
      margin-left:0; }

.bp3-slider-label{
  -webkit-transform:translate(-50%, 20px);
          transform:translate(-50%, 20px);
  display:inline-block;
  font-size:12px;
  line-height:1;
  padding:2px 5px;
  position:absolute;
  vertical-align:top; }

.bp3-slider.bp3-vertical{
  height:150px;
  min-width:40px;
  width:40px; }
  .bp3-slider.bp3-vertical .bp3-slider-track,
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    bottom:0;
    height:auto;
    left:5px;
    top:0;
    width:6px; }
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    top:auto; }
  .bp3-slider.bp3-vertical .bp3-slider-label{
    -webkit-transform:translate(20px, 50%);
            transform:translate(20px, 50%); }
  .bp3-slider.bp3-vertical .bp3-slider-handle{
    top:auto; }
    .bp3-slider.bp3-vertical .bp3-slider-handle .bp3-slider-label{
      margin-left:0;
      margin-top:-8px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end, .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      height:8px;
      margin-left:0;
      width:16px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      border-bottom-right-radius:3px;
      border-top-left-radius:0; }
      .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start .bp3-slider-label{
        -webkit-transform:translate(20px);
                transform:translate(20px); }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end{
      border-bottom-left-radius:0;
      border-bottom-right-radius:0;
      border-top-left-radius:3px;
      margin-bottom:8px; }

@-webkit-keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

@keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

.bp3-spinner{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  overflow:visible;
  vertical-align:middle; }
  .bp3-spinner svg{
    display:block; }
  .bp3-spinner path{
    fill-opacity:0; }
  .bp3-spinner .bp3-spinner-head{
    stroke:rgba(92, 112, 128, 0.8);
    stroke-linecap:round;
    -webkit-transform-origin:center;
            transform-origin:center;
    -webkit-transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-spinner .bp3-spinner-track{
    stroke:rgba(92, 112, 128, 0.2); }

.bp3-spinner-animation{
  -webkit-animation:pt-spinner-animation 500ms linear infinite;
          animation:pt-spinner-animation 500ms linear infinite; }
  .bp3-no-spin > .bp3-spinner-animation{
    -webkit-animation:none;
            animation:none; }

.bp3-dark .bp3-spinner .bp3-spinner-head{
  stroke:#8a9ba8; }

.bp3-dark .bp3-spinner .bp3-spinner-track{
  stroke:rgba(16, 22, 26, 0.5); }

.bp3-spinner.bp3-intent-primary .bp3-spinner-head{
  stroke:#137cbd; }

.bp3-spinner.bp3-intent-success .bp3-spinner-head{
  stroke:#0f9960; }

.bp3-spinner.bp3-intent-warning .bp3-spinner-head{
  stroke:#d9822b; }

.bp3-spinner.bp3-intent-danger .bp3-spinner-head{
  stroke:#db3737; }
.bp3-tabs.bp3-vertical{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-tabs.bp3-vertical > .bp3-tab-list{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start;
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab{
      border-radius:3px;
      padding:0 10px;
      width:100%; }
      .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab[aria-selected="true"]{
        background-color:rgba(19, 124, 189, 0.2);
        -webkit-box-shadow:none;
                box-shadow:none; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab-indicator-wrapper .bp3-tab-indicator{
      background-color:rgba(19, 124, 189, 0.2);
      border-radius:3px;
      bottom:0;
      height:auto;
      left:0;
      right:0;
      top:0; }
  .bp3-tabs.bp3-vertical > .bp3-tab-panel{
    margin-top:0;
    padding-left:20px; }

.bp3-tab-list{
  -webkit-box-align:end;
      -ms-flex-align:end;
          align-items:flex-end;
  border:none;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  list-style:none;
  margin:0;
  padding:0;
  position:relative; }
  .bp3-tab-list > *:not(:last-child){
    margin-right:20px; }

.bp3-tab{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  color:#182026;
  cursor:pointer;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  font-size:14px;
  line-height:30px;
  max-width:100%;
  position:relative;
  vertical-align:top; }
  .bp3-tab a{
    color:inherit;
    display:block;
    text-decoration:none; }
  .bp3-tab-indicator-wrapper ~ .bp3-tab{
    background-color:transparent !important;
    -webkit-box-shadow:none !important;
            box-shadow:none !important; }
  .bp3-tab[aria-disabled="true"]{
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-tab[aria-selected="true"]{
    border-radius:0;
    -webkit-box-shadow:inset 0 -3px 0 #106ba3;
            box-shadow:inset 0 -3px 0 #106ba3; }
  .bp3-tab[aria-selected="true"], .bp3-tab:not([aria-disabled="true"]):hover{
    color:#106ba3; }
  .bp3-tab:focus{
    -moz-outline-radius:0; }
  .bp3-large > .bp3-tab{
    font-size:16px;
    line-height:40px; }

.bp3-tab-panel{
  margin-top:20px; }
  .bp3-tab-panel[aria-hidden="true"]{
    display:none; }

.bp3-tab-indicator-wrapper{
  left:0;
  pointer-events:none;
  position:absolute;
  top:0;
  -webkit-transform:translateX(0), translateY(0);
          transform:translateX(0), translateY(0);
  -webkit-transition:height, width, -webkit-transform;
  transition:height, width, -webkit-transform;
  transition:height, transform, width;
  transition:height, transform, width, -webkit-transform;
  -webkit-transition-duration:200ms;
          transition-duration:200ms;
  -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
          transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tab-indicator-wrapper .bp3-tab-indicator{
    background-color:#106ba3;
    bottom:0;
    height:3px;
    left:0;
    position:absolute;
    right:0; }
  .bp3-tab-indicator-wrapper.bp3-no-animation{
    -webkit-transition:none;
    transition:none; }

.bp3-dark .bp3-tab{
  color:#f5f8fa; }
  .bp3-dark .bp3-tab[aria-disabled="true"]{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tab[aria-selected="true"]{
    -webkit-box-shadow:inset 0 -3px 0 #48aff0;
            box-shadow:inset 0 -3px 0 #48aff0; }
  .bp3-dark .bp3-tab[aria-selected="true"], .bp3-dark .bp3-tab:not([aria-disabled="true"]):hover{
    color:#48aff0; }

.bp3-dark .bp3-tab-indicator{
  background-color:#48aff0; }

.bp3-flex-expander{
  -webkit-box-flex:1;
      -ms-flex:1 1;
          flex:1 1; }
.bp3-tag{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:#5c7080;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:none;
          box-shadow:none;
  color:#f5f8fa;
  font-size:12px;
  line-height:16px;
  max-width:100%;
  min-height:20px;
  min-width:20px;
  padding:2px 6px;
  position:relative; }
  .bp3-tag.bp3-interactive{
    cursor:pointer; }
    .bp3-tag.bp3-interactive:hover{
      background-color:rgba(92, 112, 128, 0.85); }
    .bp3-tag.bp3-interactive.bp3-active, .bp3-tag.bp3-interactive:active{
      background-color:rgba(92, 112, 128, 0.7); }
  .bp3-tag > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag::before,
  .bp3-tag > *{
    margin-right:4px; }
  .bp3-tag:empty::before,
  .bp3-tag > :last-child{
    margin-right:0; }
  .bp3-tag:focus{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:0;
    -moz-outline-radius:6px; }
  .bp3-tag.bp3-round{
    border-radius:30px;
    padding-left:8px;
    padding-right:8px; }
  .bp3-dark .bp3-tag{
    background-color:#bfccd6;
    color:#182026; }
    .bp3-dark .bp3-tag.bp3-interactive{
      cursor:pointer; }
      .bp3-dark .bp3-tag.bp3-interactive:hover{
        background-color:rgba(191, 204, 214, 0.85); }
      .bp3-dark .bp3-tag.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-interactive:active{
        background-color:rgba(191, 204, 214, 0.7); }
    .bp3-dark .bp3-tag > .bp3-icon, .bp3-dark .bp3-tag .bp3-icon-standard, .bp3-dark .bp3-tag .bp3-icon-large{
      fill:currentColor; }
  .bp3-tag > .bp3-icon, .bp3-tag .bp3-icon-standard, .bp3-tag .bp3-icon-large{
    fill:#ffffff; }
  .bp3-tag.bp3-large,
  .bp3-large .bp3-tag{
    font-size:14px;
    line-height:20px;
    min-height:30px;
    min-width:30px;
    padding:5px 10px; }
    .bp3-tag.bp3-large::before,
    .bp3-tag.bp3-large > *,
    .bp3-large .bp3-tag::before,
    .bp3-large .bp3-tag > *{
      margin-right:7px; }
    .bp3-tag.bp3-large:empty::before,
    .bp3-tag.bp3-large > :last-child,
    .bp3-large .bp3-tag:empty::before,
    .bp3-large .bp3-tag > :last-child{
      margin-right:0; }
    .bp3-tag.bp3-large.bp3-round,
    .bp3-large .bp3-tag.bp3-round{
      padding-left:12px;
      padding-right:12px; }
  .bp3-tag.bp3-intent-primary{
    background:#137cbd;
    color:#ffffff; }
    .bp3-tag.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.85); }
      .bp3-tag.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.7); }
  .bp3-tag.bp3-intent-success{
    background:#0f9960;
    color:#ffffff; }
    .bp3-tag.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.85); }
      .bp3-tag.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.7); }
  .bp3-tag.bp3-intent-warning{
    background:#d9822b;
    color:#ffffff; }
    .bp3-tag.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.85); }
      .bp3-tag.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.7); }
  .bp3-tag.bp3-intent-danger{
    background:#db3737;
    color:#ffffff; }
    .bp3-tag.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.85); }
      .bp3-tag.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.7); }
  .bp3-tag.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-tag.bp3-minimal > .bp3-icon, .bp3-tag.bp3-minimal .bp3-icon-standard, .bp3-tag.bp3-minimal .bp3-icon-large{
    fill:#5c7080; }
  .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
    background-color:rgba(138, 155, 168, 0.2);
    color:#182026; }
    .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
        background-color:rgba(92, 112, 128, 0.3); }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
        background-color:rgba(92, 112, 128, 0.4); }
    .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
      color:#f5f8fa; }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
          background-color:rgba(191, 204, 214, 0.3); }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
          background-color:rgba(191, 204, 214, 0.4); }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) > .bp3-icon, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-large{
        fill:#a7b6c2; }
  .bp3-tag.bp3-minimal.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15);
    color:#106ba3; }
    .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-primary > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-large{
      fill:#137cbd; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25);
      color:#48aff0; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
          background-color:rgba(19, 124, 189, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
          background-color:rgba(19, 124, 189, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15);
    color:#0d8050; }
    .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-success > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-large{
      fill:#0f9960; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25);
      color:#3dcc91; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
          background-color:rgba(15, 153, 96, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
          background-color:rgba(15, 153, 96, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15);
    color:#bf7326; }
    .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-warning > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-large{
      fill:#d9822b; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25);
      color:#ffb366; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
          background-color:rgba(217, 130, 43, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
          background-color:rgba(217, 130, 43, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15);
    color:#c23030; }
    .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-danger > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-large{
      fill:#db3737; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25);
      color:#ff7373; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
          background-color:rgba(219, 55, 55, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
          background-color:rgba(219, 55, 55, 0.45); }

.bp3-tag-remove{
  background:none;
  border:none;
  color:inherit;
  cursor:pointer;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin-bottom:-2px;
  margin-right:-6px !important;
  margin-top:-2px;
  opacity:0.5;
  padding:2px;
  padding-left:0; }
  .bp3-tag-remove:hover{
    background:none;
    opacity:0.8;
    text-decoration:none; }
  .bp3-tag-remove:active{
    opacity:1; }
  .bp3-tag-remove:empty::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    content:""; }
  .bp3-large .bp3-tag-remove{
    margin-right:-10px !important;
    padding:0 5px 0 0; }
    .bp3-large .bp3-tag-remove:empty::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1; }
.bp3-tag-input{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  cursor:text;
  height:auto;
  line-height:inherit;
  min-height:30px;
  padding-left:5px;
  padding-right:0; }
  .bp3-tag-input > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag-input > .bp3-tag-input-values{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag-input .bp3-tag-input-icon{
    color:#5c7080;
    margin-left:2px;
    margin-right:7px;
    margin-top:7px; }
  .bp3-tag-input .bp3-tag-input-values{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row;
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    -ms-flex-item-align:stretch;
        align-self:stretch;
    -ms-flex-wrap:wrap;
        flex-wrap:wrap;
    margin-right:7px;
    margin-top:5px;
    min-width:0; }
    .bp3-tag-input .bp3-tag-input-values > *{
      -webkit-box-flex:0;
          -ms-flex-positive:0;
              flex-grow:0;
      -ms-flex-negative:0;
          flex-shrink:0; }
    .bp3-tag-input .bp3-tag-input-values > .bp3-fill{
      -webkit-box-flex:1;
          -ms-flex-positive:1;
              flex-grow:1;
      -ms-flex-negative:1;
          flex-shrink:1; }
    .bp3-tag-input .bp3-tag-input-values::before,
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-right:5px; }
    .bp3-tag-input .bp3-tag-input-values:empty::before,
    .bp3-tag-input .bp3-tag-input-values > :last-child{
      margin-right:0; }
    .bp3-tag-input .bp3-tag-input-values:first-child .bp3-input-ghost:first-child{
      padding-left:5px; }
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-bottom:5px; }
  .bp3-tag-input .bp3-tag{
    overflow-wrap:break-word; }
    .bp3-tag-input .bp3-tag.bp3-active{
      outline:rgba(19, 124, 189, 0.6) auto 2px;
      outline-offset:0;
      -moz-outline-radius:6px; }
  .bp3-tag-input .bp3-input-ghost{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:20px;
    width:80px; }
    .bp3-tag-input .bp3-input-ghost:disabled, .bp3-tag-input .bp3-input-ghost.bp3-disabled{
      cursor:not-allowed; }
  .bp3-tag-input .bp3-button,
  .bp3-tag-input .bp3-spinner{
    margin:3px;
    margin-left:0; }
  .bp3-tag-input .bp3-button{
    min-height:24px;
    min-width:24px;
    padding:0 7px; }
  .bp3-tag-input.bp3-large{
    height:auto;
    min-height:40px; }
    .bp3-tag-input.bp3-large::before,
    .bp3-tag-input.bp3-large > *{
      margin-right:10px; }
    .bp3-tag-input.bp3-large:empty::before,
    .bp3-tag-input.bp3-large > :last-child{
      margin-right:0; }
    .bp3-tag-input.bp3-large .bp3-tag-input-icon{
      margin-left:5px;
      margin-top:10px; }
    .bp3-tag-input.bp3-large .bp3-input-ghost{
      line-height:30px; }
    .bp3-tag-input.bp3-large .bp3-button{
      min-height:30px;
      min-width:30px;
      padding:5px 10px;
      margin:5px;
      margin-left:0; }
    .bp3-tag-input.bp3-large .bp3-spinner{
      margin:8px;
      margin-left:0; }
  .bp3-tag-input.bp3-active{
    background-color:#ffffff;
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-tag-input .bp3-tag-input-icon, .bp3-tag-input.bp3-dark .bp3-tag-input-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-tag-input .bp3-input-ghost, .bp3-tag-input.bp3-dark .bp3-input-ghost{
    color:#f5f8fa; }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-webkit-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-moz-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost:-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::placeholder{
      color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tag-input.bp3-active, .bp3-tag-input.bp3-dark.bp3-active{
    background-color:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-primary, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-success, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-warning, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-danger, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-input-ghost{
  background:none;
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0; }
  .bp3-input-ghost::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost:focus{
    outline:none !important; }
.bp3-toast{
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin:20px 0 0;
  max-width:500px;
  min-width:300px;
  pointer-events:all;
  position:relative !important; }
  .bp3-toast.bp3-toast-enter, .bp3-toast.bp3-toast-appear{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active, .bp3-toast.bp3-toast-appear-active{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-toast.bp3-toast-enter ~ .bp3-toast, .bp3-toast.bp3-toast-appear ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active ~ .bp3-toast, .bp3-toast.bp3-toast-appear-active ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-toast.bp3-toast-exit{
    opacity:1;
    -webkit-filter:blur(0);
            filter:blur(0); }
  .bp3-toast.bp3-toast-exit-active{
    opacity:0;
    -webkit-filter:blur(10px);
            filter:blur(10px);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:opacity, filter;
    transition-property:opacity, filter, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-toast.bp3-toast-exit ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0); }
  .bp3-toast.bp3-toast-exit-active ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px);
    -webkit-transition-delay:50ms;
            transition-delay:50ms;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-toast .bp3-button-group{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    padding:5px;
    padding-left:0; }
  .bp3-toast > .bp3-icon{
    color:#5c7080;
    margin:12px;
    margin-right:0; }
  .bp3-toast.bp3-dark,
  .bp3-dark .bp3-toast{
    background-color:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-toast.bp3-dark > .bp3-icon,
    .bp3-dark .bp3-toast > .bp3-icon{
      color:#a7b6c2; }
  .bp3-toast[class*="bp3-intent-"] a{
    color:rgba(255, 255, 255, 0.7); }
    .bp3-toast[class*="bp3-intent-"] a:hover{
      color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] > .bp3-icon{
    color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button, .bp3-toast[class*="bp3-intent-"] .bp3-button::before,
  .bp3-toast[class*="bp3-intent-"] .bp3-button .bp3-icon, .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    color:rgba(255, 255, 255, 0.7) !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:focus{
    outline-color:rgba(255, 255, 255, 0.5); }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:hover{
    background-color:rgba(255, 255, 255, 0.15) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    background-color:rgba(255, 255, 255, 0.3) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button::after{
    background:rgba(255, 255, 255, 0.3) !important; }
  .bp3-toast.bp3-intent-primary{
    background-color:#137cbd;
    color:#ffffff; }
  .bp3-toast.bp3-intent-success{
    background-color:#0f9960;
    color:#ffffff; }
  .bp3-toast.bp3-intent-warning{
    background-color:#d9822b;
    color:#ffffff; }
  .bp3-toast.bp3-intent-danger{
    background-color:#db3737;
    color:#ffffff; }

.bp3-toast-message{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  padding:11px;
  word-break:break-word; }

.bp3-toast-container{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box !important;
  display:-ms-flexbox !important;
  display:flex !important;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  left:0;
  overflow:hidden;
  padding:0 20px 20px;
  pointer-events:none;
  right:0;
  z-index:40; }
  .bp3-toast-container.bp3-toast-container-in-portal{
    position:fixed; }
  .bp3-toast-container.bp3-toast-container-inline{
    position:absolute; }
  .bp3-toast-container.bp3-toast-container-top{
    top:0; }
  .bp3-toast-container.bp3-toast-container-bottom{
    bottom:0;
    -webkit-box-orient:vertical;
    -webkit-box-direction:reverse;
        -ms-flex-direction:column-reverse;
            flex-direction:column-reverse;
    top:auto; }
  .bp3-toast-container.bp3-toast-container-left{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start; }
  .bp3-toast-container.bp3-toast-container-right{
    -webkit-box-align:end;
        -ms-flex-align:end;
            align-items:flex-end; }

.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active) ~ .bp3-toast, .bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active) ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-exit-active ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-leave-active ~ .bp3-toast{
  -webkit-transform:translateY(60px);
          transform:translateY(60px); }
.bp3-tooltip{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1); }
  .bp3-tooltip .bp3-popover-arrow{
    height:22px;
    position:absolute;
    width:22px; }
    .bp3-tooltip .bp3-popover-arrow::before{
      height:14px;
      margin:4px;
      width:14px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip{
    margin-bottom:11px;
    margin-top:-11px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
      bottom:-8px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip{
    margin-left:11px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
      left:-8px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip{
    margin-top:11px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
      top:-8px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip{
    margin-left:-11px;
    margin-right:11px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
      right:-8px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-tooltip > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-tooltip > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
    top:-0.22183px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
    right:-0.22183px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
    left:-0.22183px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
    bottom:-0.22183px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-tooltip .bp3-popover-content{
    background:#394b59;
    color:#f5f8fa; }
  .bp3-tooltip .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-tooltip .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-tooltip .bp3-popover-arrow-fill{
    fill:#394b59; }
  .bp3-popover-enter > .bp3-tooltip, .bp3-popover-appear > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8); }
  .bp3-popover-enter-active > .bp3-tooltip, .bp3-popover-appear-active > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-popover-exit > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tooltip .bp3-popover-content{
    padding:10px 12px; }
  .bp3-tooltip.bp3-dark,
  .bp3-dark .bp3-tooltip{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-tooltip .bp3-popover-content{
      background:#e1e8ed;
      color:#394b59; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-fill{
      fill:#e1e8ed; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-content{
    background:#137cbd;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-arrow-fill{
    fill:#137cbd; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-content{
    background:#0f9960;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-arrow-fill{
    fill:#0f9960; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-content{
    background:#d9822b;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-arrow-fill{
    fill:#d9822b; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-content{
    background:#db3737;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-arrow-fill{
    fill:#db3737; }

.bp3-tooltip-indicator{
  border-bottom:dotted 1px;
  cursor:help; }
.bp3-tree .bp3-icon, .bp3-tree .bp3-icon-standard, .bp3-tree .bp3-icon-large{
  color:#5c7080; }
  .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-tree .bp3-icon.bp3-intent-success, .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-tree-node-list{
  list-style:none;
  margin:0;
  padding-left:0; }

.bp3-tree-root{
  background-color:transparent;
  cursor:default;
  padding-left:0;
  position:relative; }

.bp3-tree-node-content-0{
  padding-left:0px; }

.bp3-tree-node-content-1{
  padding-left:23px; }

.bp3-tree-node-content-2{
  padding-left:46px; }

.bp3-tree-node-content-3{
  padding-left:69px; }

.bp3-tree-node-content-4{
  padding-left:92px; }

.bp3-tree-node-content-5{
  padding-left:115px; }

.bp3-tree-node-content-6{
  padding-left:138px; }

.bp3-tree-node-content-7{
  padding-left:161px; }

.bp3-tree-node-content-8{
  padding-left:184px; }

.bp3-tree-node-content-9{
  padding-left:207px; }

.bp3-tree-node-content-10{
  padding-left:230px; }

.bp3-tree-node-content-11{
  padding-left:253px; }

.bp3-tree-node-content-12{
  padding-left:276px; }

.bp3-tree-node-content-13{
  padding-left:299px; }

.bp3-tree-node-content-14{
  padding-left:322px; }

.bp3-tree-node-content-15{
  padding-left:345px; }

.bp3-tree-node-content-16{
  padding-left:368px; }

.bp3-tree-node-content-17{
  padding-left:391px; }

.bp3-tree-node-content-18{
  padding-left:414px; }

.bp3-tree-node-content-19{
  padding-left:437px; }

.bp3-tree-node-content-20{
  padding-left:460px; }

.bp3-tree-node-content{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:30px;
  padding-right:5px;
  width:100%; }
  .bp3-tree-node-content:hover{
    background-color:rgba(191, 204, 214, 0.4); }

.bp3-tree-node-caret,
.bp3-tree-node-caret-none{
  min-width:30px; }

.bp3-tree-node-caret{
  color:#5c7080;
  cursor:pointer;
  padding:7px;
  -webkit-transform:rotate(0deg);
          transform:rotate(0deg);
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tree-node-caret:hover{
    color:#182026; }
  .bp3-dark .bp3-tree-node-caret{
    color:#a7b6c2; }
    .bp3-dark .bp3-tree-node-caret:hover{
      color:#f5f8fa; }
  .bp3-tree-node-caret.bp3-tree-node-caret-open{
    -webkit-transform:rotate(90deg);
            transform:rotate(90deg); }
  .bp3-tree-node-caret.bp3-icon-standard::before{
    content:""; }

.bp3-tree-node-icon{
  margin-right:7px;
  position:relative; }

.bp3-tree-node-label{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-label span{
    display:inline; }

.bp3-tree-node-secondary-label{
  padding:0 5px;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-secondary-label .bp3-popover-wrapper,
  .bp3-tree-node-secondary-label .bp3-popover-target{
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-content{
  background-color:inherit;
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-caret,
.bp3-tree-node.bp3-disabled .bp3-tree-node-icon{
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content,
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-standard, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-large{
    color:#ffffff; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret::before{
    color:rgba(255, 255, 255, 0.7); }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret:hover::before{
    color:#ffffff; }

.bp3-dark .bp3-tree-node-content:hover{
  background-color:rgba(92, 112, 128, 0.3); }

.bp3-dark .bp3-tree .bp3-icon, .bp3-dark .bp3-tree .bp3-icon-standard, .bp3-dark .bp3-tree .bp3-icon-large{
  color:#a7b6c2; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-dark .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
.bp3-omnibar{
  -webkit-filter:blur(0);
          filter:blur(0);
  opacity:1;
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  left:calc(50% - 250px);
  top:20vh;
  width:500px;
  z-index:21; }
  .bp3-omnibar.bp3-overlay-enter, .bp3-omnibar.bp3-overlay-appear{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2; }
  .bp3-omnibar.bp3-overlay-enter-active, .bp3-omnibar.bp3-overlay-appear-active{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-omnibar.bp3-overlay-exit{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1; }
  .bp3-omnibar.bp3-overlay-exit-active{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-omnibar .bp3-input{
    background-color:transparent;
    border-radius:0; }
    .bp3-omnibar .bp3-input, .bp3-omnibar .bp3-input:focus{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-omnibar .bp3-menu{
    background-color:transparent;
    border-radius:0;
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
    max-height:calc(60vh - 40px);
    overflow:auto; }
    .bp3-omnibar .bp3-menu:empty{
      display:none; }
  .bp3-dark .bp3-omnibar, .bp3-omnibar.bp3-dark{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-omnibar-overlay .bp3-overlay-backdrop{
  background-color:rgba(16, 22, 26, 0.2); }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }

.bp3-multi-select{
  min-width:150px; }

.bp3-multi-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto; }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1pY29uLWJyYW5kMSBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNmZmYiPgogICAgPHBhdGggZD0iTTEwNSAxMjcuM2g0MHYxMi44aC00MHpNNTEuMSA3N0w3NCA5OS45bC0yMy4zIDIzLjMgMTAuNSAxMC41IDIzLjMtMjMuM0w5NSA5OS45IDg0LjUgODkuNCA2MS42IDY2LjV6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMSBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNGOUE4MjUiPgogICAgPHBhdGggZD0iTTIwLjIgMTEuOGMtMS42IDAtMS43LjUtMS43IDEgMCAuNC4xLjkuMSAxLjMuMS41LjEuOS4xIDEuMyAwIDEuNy0xLjQgMi4zLTMuNSAyLjNoLS45di0xLjloLjVjMS4xIDAgMS40IDAgMS40LS44IDAtLjMgMC0uNi0uMS0xIDAtLjQtLjEtLjgtLjEtMS4yIDAtMS4zIDAtMS44IDEuMy0yLTEuMy0uMi0xLjMtLjctMS4zLTIgMC0uNC4xLS44LjEtMS4yLjEtLjQuMS0uNy4xLTEgMC0uOC0uNC0uNy0xLjQtLjhoLS41VjQuMWguOWMyLjIgMCAzLjUuNyAzLjUgMi4zIDAgLjQtLjEuOS0uMSAxLjMtLjEuNS0uMS45LS4xIDEuMyAwIC41LjIgMSAxLjcgMXYxLjh6TTEuOCAxMC4xYzEuNiAwIDEuNy0uNSAxLjctMSAwLS40LS4xLS45LS4xLTEuMy0uMS0uNS0uMS0uOS0uMS0xLjMgMC0xLjYgMS40LTIuMyAzLjUtMi4zaC45djEuOWgtLjVjLTEgMC0xLjQgMC0xLjQuOCAwIC4zIDAgLjYuMSAxIDAgLjIuMS42LjEgMSAwIDEuMyAwIDEuOC0xLjMgMkM2IDExLjIgNiAxMS43IDYgMTNjMCAuNC0uMS44LS4xIDEuMi0uMS4zLS4xLjctLjEgMSAwIC44LjMuOCAxLjQuOGguNXYxLjloLS45Yy0yLjEgMC0zLjUtLjYtMy41LTIuMyAwLS40LjEtLjkuMS0xLjMuMS0uNS4xLS45LjEtMS4zIDAtLjUtLjItMS0xLjctMXYtMS45eiIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSIxMy44IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY3g9IjExIiBjeT0iOC4yIiByPSIyLjEiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgPGcgY2xhc3M9ImpwLWljb24td2FybjAiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4=);
  --jp-icon-listings-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MC45NzggNTAuOTc4IiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1MC45NzggNTAuOTc4OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+Cgk8Zz4KCQk8cGF0aCBzdHlsZT0iZmlsbDojMDEwMDAyOyIgZD0iTTQzLjUyLDcuNDU4QzM4LjcxMSwyLjY0OCwzMi4zMDcsMCwyNS40ODksMEMxOC42NywwLDEyLjI2NiwyLjY0OCw3LjQ1OCw3LjQ1OAoJCQljLTkuOTQzLDkuOTQxLTkuOTQzLDI2LjExOSwwLDM2LjA2MmM0LjgwOSw0LjgwOSwxMS4yMTIsNy40NTYsMTguMDMxLDcuNDU4YzAsMCwwLjAwMSwwLDAuMDAyLDAKCQkJYzYuODE2LDAsMTMuMjIxLTIuNjQ4LDE4LjAyOS03LjQ1OGM0LjgwOS00LjgwOSw3LjQ1Ny0xMS4yMTIsNy40NTctMTguMDNDNTAuOTc3LDE4LjY3LDQ4LjMyOCwxMi4yNjYsNDMuNTIsNy40NTh6CgkJCSBNNDIuMTA2LDQyLjEwNWMtNC40MzIsNC40MzEtMTAuMzMyLDYuODcyLTE2LjYxNSw2Ljg3MmgtMC4wMDJjLTYuMjg1LTAuMDAxLTEyLjE4Ny0yLjQ0MS0xNi42MTctNi44NzIKCQkJYy05LjE2Mi05LjE2My05LjE2Mi0yNC4wNzEsMC0zMy4yMzNDMTMuMzAzLDQuNDQsMTkuMjA0LDIsMjUuNDg5LDJjNi4yODQsMCwxMi4xODYsMi40NCwxNi42MTcsNi44NzIKCQkJYzQuNDMxLDQuNDMxLDYuODcxLDEwLjMzMiw2Ljg3MSwxNi42MTdDNDguOTc3LDMxLjc3Miw0Ni41MzYsMzcuNjc1LDQyLjEwNiw0Mi4xMDV6Ii8+CgkJPHBhdGggc3R5bGU9ImZpbGw6IzAxMDAwMjsiIGQ9Ik0yMy41NzgsMzIuMjE4Yy0wLjAyMy0xLjczNCwwLjE0My0zLjA1OSwwLjQ5Ni0zLjk3MmMwLjM1My0wLjkxMywxLjExLTEuOTk3LDIuMjcyLTMuMjUzCgkJCWMwLjQ2OC0wLjUzNiwwLjkyMy0xLjA2MiwxLjM2Ny0xLjU3NWMwLjYyNi0wLjc1MywxLjEwNC0xLjQ3OCwxLjQzNi0yLjE3NWMwLjMzMS0wLjcwNywwLjQ5NS0xLjU0MSwwLjQ5NS0yLjUKCQkJYzAtMS4wOTYtMC4yNi0yLjA4OC0wLjc3OS0yLjk3OWMtMC41NjUtMC44NzktMS41MDEtMS4zMzYtMi44MDYtMS4zNjljLTEuODAyLDAuMDU3LTIuOTg1LDAuNjY3LTMuNTUsMS44MzIKCQkJYy0wLjMwMSwwLjUzNS0wLjUwMywxLjE0MS0wLjYwNywxLjgxNGMtMC4xMzksMC43MDctMC4yMDcsMS40MzItMC4yMDcsMi4xNzRoLTIuOTM3Yy0wLjA5MS0yLjIwOCwwLjQwNy00LjExNCwxLjQ5My01LjcxOQoJCQljMS4wNjItMS42NCwyLjg1NS0yLjQ4MSw1LjM3OC0yLjUyN2MyLjE2LDAuMDIzLDMuODc0LDAuNjA4LDUuMTQxLDEuNzU4YzEuMjc4LDEuMTYsMS45MjksMi43NjQsMS45NSw0LjgxMQoJCQljMCwxLjE0Mi0wLjEzNywyLjExMS0wLjQxLDIuOTExYy0wLjMwOSwwLjg0NS0wLjczMSwxLjU5My0xLjI2OCwyLjI0M2MtMC40OTIsMC42NS0xLjA2OCwxLjMxOC0xLjczLDIuMDAyCgkJCWMtMC42NSwwLjY5Ny0xLjMxMywxLjQ3OS0xLjk4NywyLjM0NmMtMC4yMzksMC4zNzctMC40MjksMC43NzctMC41NjUsMS4xOTljLTAuMTYsMC45NTktMC4yMTcsMS45NTEtMC4xNzEsMi45NzkKCQkJQzI2LjU4OSwzMi4yMTgsMjMuNTc4LDMyLjIxOCwyMy41NzgsMzIuMjE4eiBNMjMuNTc4LDM4LjIydi0zLjQ4NGgzLjA3NnYzLjQ4NEgyMy41Nzh6Ii8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMEQ0N0ExIj4KICAgIDxwYXRoIGQ9Ik0xMS4xIDYuOVY1LjhINi45YzAtLjUgMC0xLjMuMi0xLjYuNC0uNy44LTEuMSAxLjctMS40IDEuNy0uMyAyLjUtLjMgMy45LS4xIDEgLjEgMS45LjkgMS45IDEuOXY0LjJjMCAuNS0uOSAxLjYtMiAxLjZIOC44Yy0xLjUgMC0yLjQgMS40LTIuNCAyLjh2Mi4ySDQuN0MzLjUgMTUuMSAzIDE0IDMgMTMuMVY5Yy0uMS0xIC42LTIgMS44LTIgMS41LS4xIDYuMy0uMSA2LjMtLjF6Ii8+CiAgICA8cGF0aCBkPSJNMTAuOSAxNS4xdjEuMWg0LjJjMCAuNSAwIDEuMy0uMiAxLjYtLjQuNy0uOCAxLjEtMS43IDEuNC0xLjcuMy0yLjUuMy0zLjkuMS0xLS4xLTEuOS0uOS0xLjktMS45di00LjJjMC0uNS45LTEuNiAyLTEuNmgzLjhjMS41IDAgMi40LTEuNCAyLjQtMi44VjYuNmgxLjdDMTguNSA2LjkgMTkgOCAxOSA4LjlWMTNjMCAxLS43IDIuMS0xLjkgMi4xaC02LjJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4=);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMikiIGZpbGw9IiMzMzMzMzMiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uLWFjY2VudDIganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGQ9Ik01LjA1NjY0IDguNzYxNzJDNS4wNTY2NCA4LjU5NzY2IDUuMDMxMjUgOC40NTMxMiA0Ljk4MDQ3IDguMzI4MTJDNC45MzM1OSA4LjE5OTIyIDQuODU1NDcgOC4wODIwMyA0Ljc0NjA5IDcuOTc2NTZDNC42NDA2MiA3Ljg3MTA5IDQuNSA3Ljc3NTM5IDQuMzI0MjIgNy42ODk0NUM0LjE1MjM0IDcuNTk5NjEgMy45NDMzNiA3LjUxMTcyIDMuNjk3MjcgNy40MjU3OEMzLjMwMjczIDcuMjg1MTYgMi45NDMzNiA3LjEzNjcyIDIuNjE5MTQgNi45ODA0N0MyLjI5NDkyIDYuODI0MjIgMi4wMTc1OCA2LjY0MjU4IDEuNzg3MTEgNi40MzU1NUMxLjU2MDU1IDYuMjI4NTIgMS4zODQ3NyA1Ljk4ODI4IDEuMjU5NzcgNS43MTQ4NEMxLjEzNDc3IDUuNDM3NSAxLjA3MjI3IDUuMTA5MzggMS4wNzIyNyA0LjczMDQ3QzEuMDcyMjcgNC4zOTg0NCAxLjEyODkxIDQuMDk1NyAxLjI0MjE5IDMuODIyMjdDMS4zNTU0NyAzLjU0NDkyIDEuNTE1NjIgMy4zMDQ2OSAxLjcyMjY2IDMuMTAxNTZDMS45Mjk2OSAyLjg5ODQ0IDIuMTc5NjkgMi43MzQzNyAyLjQ3MjY2IDIuNjA5MzhDMi43NjU2MiAyLjQ4NDM4IDMuMDkxOCAyLjQwNDMgMy40NTExNyAyLjM2OTE0VjEuMTA5MzhINC4zODg2N1YyLjM4MDg2QzQuNzQwMjMgMi40Mjc3MyA1LjA1NjY0IDIuNTIzNDQgNS4zMzc4OSAyLjY2Nzk3QzUuNjE5MTQgMi44MTI1IDUuODU3NDIgMy4wMDE5NSA2LjA1MjczIDMuMjM2MzNDNi4yNTE5NSAzLjQ2NjggNi40MDQzIDMuNzQwMjMgNi41MDk3NyA0LjA1NjY0QzYuNjE5MTQgNC4zNjkxNCA2LjY3MzgzIDQuNzIwNyA2LjY3MzgzIDUuMTExMzNINS4wNDQ5MkM1LjA0NDkyIDQuNjM4NjcgNC45Mzc1IDQuMjgxMjUgNC43MjI2NiA0LjAzOTA2QzQuNTA3ODEgMy43OTI5NyA0LjIxNjggMy42Njk5MiAzLjg0OTYxIDMuNjY5OTJDMy42NTAzOSAzLjY2OTkyIDMuNDc2NTYgMy42OTcyNyAzLjMyODEyIDMuNzUxOTVDMy4xODM1OSAzLjgwMjczIDMuMDY0NDUgMy44NzY5NSAyLjk3MDcgMy45NzQ2MUMyLjg3Njk1IDQuMDY4MzYgMi44MDY2NCA0LjE3OTY5IDIuNzU5NzcgNC4zMDg1OUMyLjcxNjggNC40Mzc1IDIuNjk1MzEgNC41NzgxMiAyLjY5NTMxIDQuNzMwNDdDMi42OTUzMSA0Ljg4MjgxIDIuNzE2OCA1LjAxOTUzIDIuNzU5NzcgNS4xNDA2MkMyLjgwNjY0IDUuMjU3ODEgMi44ODI4MSA1LjM2NzE5IDIuOTg4MjggNS40Njg3NUMzLjA5NzY2IDUuNTcwMzEgMy4yNDAyMyA1LjY2Nzk3IDMuNDE2MDIgNS43NjE3MkMzLjU5MTggNS44NTE1NiAzLjgxMDU1IDUuOTQzMzYgNC4wNzIyNyA2LjAzNzExQzQuNDY2OCA2LjE4NTU1IDQuODI0MjIgNi4zMzk4NCA1LjE0NDUzIDYuNUM1LjQ2NDg0IDYuNjU2MjUgNS43MzgyOCA2LjgzOTg0IDUuOTY0ODQgNy4wNTA3OEM2LjE5NTMxIDcuMjU3ODEgNi4zNzEwOSA3LjUgNi40OTIxOSA3Ljc3NzM0QzYuNjE3MTkgOC4wNTA3OCA2LjY3OTY5IDguMzc1IDYuNjc5NjkgOC43NUM2LjY3OTY5IDkuMDkzNzUgNi42MjMwNSA5LjQwNDMgNi41MDk3NyA5LjY4MTY0QzYuMzk2NDggOS45NTUwOCA2LjIzNDM4IDEwLjE5MTQgNi4wMjM0NCAxMC4zOTA2QzUuODEyNSAxMC41ODk4IDUuNTU4NTkgMTAuNzUgNS4yNjE3MiAxMC44NzExQzQuOTY0ODQgMTAuOTg4MyA0LjYzMjgxIDExLjA2NDUgNC4yNjU2MiAxMS4wOTk2VjEyLjI0OEgzLjMzMzk4VjExLjA5OTZDMy4wMDE5NSAxMS4wNjg0IDIuNjc5NjkgMTAuOTk2MSAyLjM2NzE5IDEwLjg4MjhDMi4wNTQ2OSAxMC43NjU2IDEuNzc3MzQgMTAuNTk3NyAxLjUzNTE2IDEwLjM3ODlDMS4yOTY4OCAxMC4xNjAyIDEuMTA1NDcgOS44ODQ3NyAwLjk2MDkzOCA5LjU1MjczQzAuODE2NDA2IDkuMjE2OCAwLjc0NDE0MSA4LjgxNDQ1IDAuNzQ0MTQxIDguMzQ1N0gyLjM3ODkxQzIuMzc4OTEgOC42MjY5NSAyLjQxOTkyIDguODYzMjggMi41MDE5NSA5LjA1NDY5QzIuNTgzOTggOS4yNDIxOSAyLjY4OTQ1IDkuMzkyNTggMi44MTgzNiA5LjUwNTg2QzIuOTUxMTcgOS42MTUyMyAzLjEwMTU2IDkuNjkzMzYgMy4yNjk1MyA5Ljc0MDIzQzMuNDM3NSA5Ljc4NzExIDMuNjA5MzggOS44MTA1NSAzLjc4NTE2IDkuODEwNTVDNC4yMDMxMiA5LjgxMDU1IDQuNTE5NTMgOS43MTI4OSA0LjczNDM4IDkuNTE3NThDNC45NDkyMiA5LjMyMjI3IDUuMDU2NjQgOS4wNzAzMSA1LjA1NjY0IDguNzYxNzJaTTEzLjQxOCAxMi4yNzE1SDguMDc0MjJWMTFIMTMuNDE4VjEyLjI3MTVaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzLjk1MjY0IDYpIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTUgMTVIM3YyaDEydi0yem0wLThIM3YyaDEyVjd6TTMgMTNoMTh2LTJIM3Yyem0wIDhoMTh2LTJIM3Yyek0zIDN2MmgxOFYzSDN6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4=);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}
.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}
.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}
.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}
.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}
.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}
.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}
.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}
.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}
.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}
.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}
.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}
.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}
.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}
.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}
.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}
.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}
.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}
.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}
.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}
.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}
.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}
.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}
.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}
.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}
.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}
.jp-FileIcon {
  background-image: var(--jp-icon-file);
}
.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}
.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}
.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}
.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}
.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}
.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}
.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}
.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}
.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}
.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}
.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}
.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}
.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}
.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}
.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}
.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}
.jp-ListIcon {
  background-image: var(--jp-icon-list);
}
.jp-ListingsInfoIcon {
  background-image: var(--jp-icon-listings-info);
}
.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}
.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}
.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}
.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}
.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}
.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}
.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}
.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}
.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}
.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}
.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}
.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}
.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}
.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}
.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}
.jp-RunIcon {
  background-image: var(--jp-icon-run);
}
.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}
.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}
.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}
.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}
.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}
.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}
.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}
.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}
.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}
.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}
.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}
.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}
.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}
.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}
.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}
.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}
.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}
/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}
/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}
/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}
.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}
.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}
.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}
.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}
.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}
.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}
.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}
.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}
/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}
.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}
.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}
.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}
.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}
.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}
.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}
/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

/* CSS for icons in selected items in the settings editor */
#setting-editor .jp-PluginList .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
#setting-editor
  .jp-PluginList
  .jp-mod-selected
  .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected tabs in the sidebar tab manager */
#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable[fill] {
  fill: #fff;
}

#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable[fill] {
  fill: var(--jp-brand-color1);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable-inverse[fill] {
  fill: #fff;
}

/**
 * TODO: come up with non css-hack solution for showing the busy icon on top
 *  of the close icon
 * CSS for complex behavior of close icon of tabs in the sidebar tab manager
 */
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-dirty.jp-mod-active
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: #fff;
}

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) svg {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-border-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0px;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-warn-color0);
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

/* Override Blueprint's _reset.scss styles */
html {
  box-sizing: unset;
}

*,
*::before,
*::after {
  box-sizing: unset;
}

body {
  color: unset;
  font-family: var(--jp-ui-font-family);
}

p {
  margin-top: unset;
  margin-bottom: unset;
}

small {
  font-size: unset;
}

strong {
  font-weight: unset;
}

/* Override Blueprint's _typography.scss styles */
a {
  text-decoration: unset;
  color: unset;
}
a:hover {
  text-decoration: unset;
  color: unset;
}

/* Override Blueprint's _accessibility.scss styles */
:focus {
  outline: unset;
  outline-offset: unset;
  -moz-outline-radius: unset;
}

/* Styles for ui-components */
.jp-Button {
  border-radius: var(--jp-border-radius);
  padding: 0px 12px;
  font-size: var(--jp-ui-font-size1);
}

/* Use our own theme for hover styles */
button.jp-Button.bp3-button.bp3-minimal:hover {
  background-color: var(--jp-layout-color2);
}
.jp-Button.minimal {
  color: unset !important;
}

.jp-Button.jp-ToolbarButtonComponent {
  text-transform: none;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color3);
}

.jp-BPIcon {
  display: inline-block;
  vertical-align: middle;
  margin: auto;
}

/* Stop blueprint futzing with our icon fills */
.bp3-icon.jp-BPIcon > svg:not([fill]) {
  fill: var(--jp-inverse-layout-color3);
}

.jp-InputGroupAction {
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

/* Use our own theme for hover and option styles */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}
select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-top: 1px solid var(--jp-border-color2);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-Collapse-header {
  padding: 1px 12px;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size2);
}

.jp-Collapse-header:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Collapse-contents {
  padding: 0px 12px 0px 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0px;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0px 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px 5px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0px;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty:after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0px 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0px;
  left: 0px;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px;
  padding-bottom: 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0px;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0px 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

.jp-HoverBox.jp-mod-outofview {
  display: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;

  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;

  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #aa00ff;

  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;

  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;

  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;

  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;

  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;

  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;

  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;

  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;

  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;

  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ffff00;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;

  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;

  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;

  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;

  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;

  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eeeeee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;

  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent:before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent:after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0px 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FileDialog-Checkbox {
  margin-top: 35px;
  display: flex;
  flex-direction: row;
  align-items: end;
  width: 100%;
}

.jp-FileDialog-Checkbox > label {
  flex: 1 1 auto;
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  height: 28px;
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  background-color: var(--jp-layout-color1);
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0px 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  height: 32px;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 1;
  overflow-x: auto;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px;
  margin: 0px;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px 6px;
  margin: 0px;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent span {
  padding: 0px;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ body.p-mod-override-cursor *, /* </DEPRECATED> */
body.lm-mod-override-cursor * {
  cursor: inherit !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/* BASICS */

.CodeMirror {
  /* Set height, width, borders, and global font properties here */
  font-family: monospace;
  height: 300px;
  color: black;
  direction: ltr;
}

/* PADDING */

.CodeMirror-lines {
  padding: 4px 0; /* Vertical padding around content */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  padding: 0 4px; /* Horizontal padding of content */
}

.CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  background-color: white; /* The little square between H and V scrollbars */
}

/* GUTTER */

.CodeMirror-gutters {
  border-right: 1px solid #ddd;
  background-color: #f7f7f7;
  white-space: nowrap;
}
.CodeMirror-linenumbers {}
.CodeMirror-linenumber {
  padding: 0 3px 0 5px;
  min-width: 20px;
  text-align: right;
  color: #999;
  white-space: nowrap;
}

.CodeMirror-guttermarker { color: black; }
.CodeMirror-guttermarker-subtle { color: #999; }

/* CURSOR */

.CodeMirror-cursor {
  border-left: 1px solid black;
  border-right: none;
  width: 0;
}
/* Shown when moving in bi-directional text */
.CodeMirror div.CodeMirror-secondarycursor {
  border-left: 1px solid silver;
}
.cm-fat-cursor .CodeMirror-cursor {
  width: auto;
  border: 0 !important;
  background: #7e7;
}
.cm-fat-cursor div.CodeMirror-cursors {
  z-index: 1;
}
.cm-fat-cursor-mark {
  background-color: rgba(20, 255, 20, 0.5);
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
}
.cm-animate-fat-cursor {
  width: auto;
  border: 0;
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
  background-color: #7e7;
}
@-moz-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@-webkit-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}

/* Can style cursor different in overwrite (non-insert) mode */
.CodeMirror-overwrite .CodeMirror-cursor {}

.cm-tab { display: inline-block; text-decoration: inherit; }

.CodeMirror-rulers {
  position: absolute;
  left: 0; right: 0; top: -50px; bottom: 0;
  overflow: hidden;
}
.CodeMirror-ruler {
  border-left: 1px solid #ccc;
  top: 0; bottom: 0;
  position: absolute;
}

/* DEFAULT THEME */

.cm-s-default .cm-header {color: blue;}
.cm-s-default .cm-quote {color: #090;}
.cm-negative {color: #d44;}
.cm-positive {color: #292;}
.cm-header, .cm-strong {font-weight: bold;}
.cm-em {font-style: italic;}
.cm-link {text-decoration: underline;}
.cm-strikethrough {text-decoration: line-through;}

.cm-s-default .cm-keyword {color: #708;}
.cm-s-default .cm-atom {color: #219;}
.cm-s-default .cm-number {color: #164;}
.cm-s-default .cm-def {color: #00f;}
.cm-s-default .cm-variable,
.cm-s-default .cm-punctuation,
.cm-s-default .cm-property,
.cm-s-default .cm-operator {}
.cm-s-default .cm-variable-2 {color: #05a;}
.cm-s-default .cm-variable-3, .cm-s-default .cm-type {color: #085;}
.cm-s-default .cm-comment {color: #a50;}
.cm-s-default .cm-string {color: #a11;}
.cm-s-default .cm-string-2 {color: #f50;}
.cm-s-default .cm-meta {color: #555;}
.cm-s-default .cm-qualifier {color: #555;}
.cm-s-default .cm-builtin {color: #30a;}
.cm-s-default .cm-bracket {color: #997;}
.cm-s-default .cm-tag {color: #170;}
.cm-s-default .cm-attribute {color: #00c;}
.cm-s-default .cm-hr {color: #999;}
.cm-s-default .cm-link {color: #00c;}

.cm-s-default .cm-error {color: #f00;}
.cm-invalidchar {color: #f00;}

.CodeMirror-composing { border-bottom: 2px solid; }

/* Default styles for common addons */

div.CodeMirror span.CodeMirror-matchingbracket {color: #0b0;}
div.CodeMirror span.CodeMirror-nonmatchingbracket {color: #a22;}
.CodeMirror-matchingtag { background: rgba(255, 150, 0, .3); }
.CodeMirror-activeline-background {background: #e8f2ff;}

/* STOP */

/* The rest of this file contains styles related to the mechanics of
   the editor. You probably shouldn't touch them. */

.CodeMirror {
  position: relative;
  overflow: hidden;
  background: white;
}

.CodeMirror-scroll {
  overflow: scroll !important; /* Things will break if this is overridden */
  /* 50px is the magic margin used to hide the element's real scrollbars */
  /* See overflow: hidden in .CodeMirror */
  margin-bottom: -50px; margin-right: -50px;
  padding-bottom: 50px;
  height: 100%;
  outline: none; /* Prevent dragging from highlighting the element */
  position: relative;
}
.CodeMirror-sizer {
  position: relative;
  border-right: 50px solid transparent;
}

/* The fake, visible scrollbars. Used to force redraw during scrolling
   before actual scrolling happens, thus preventing shaking and
   flickering artifacts. */
.CodeMirror-vscrollbar, .CodeMirror-hscrollbar, .CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  position: absolute;
  z-index: 6;
  display: none;
  outline: none;
}
.CodeMirror-vscrollbar {
  right: 0; top: 0;
  overflow-x: hidden;
  overflow-y: scroll;
}
.CodeMirror-hscrollbar {
  bottom: 0; left: 0;
  overflow-y: hidden;
  overflow-x: scroll;
}
.CodeMirror-scrollbar-filler {
  right: 0; bottom: 0;
}
.CodeMirror-gutter-filler {
  left: 0; bottom: 0;
}

.CodeMirror-gutters {
  position: absolute; left: 0; top: 0;
  min-height: 100%;
  z-index: 3;
}
.CodeMirror-gutter {
  white-space: normal;
  height: 100%;
  display: inline-block;
  vertical-align: top;
  margin-bottom: -50px;
}
.CodeMirror-gutter-wrapper {
  position: absolute;
  z-index: 4;
  background: none !important;
  border: none !important;
}
.CodeMirror-gutter-background {
  position: absolute;
  top: 0; bottom: 0;
  z-index: 4;
}
.CodeMirror-gutter-elt {
  position: absolute;
  cursor: default;
  z-index: 4;
}
.CodeMirror-gutter-wrapper ::selection { background-color: transparent }
.CodeMirror-gutter-wrapper ::-moz-selection { background-color: transparent }

.CodeMirror-lines {
  cursor: text;
  min-height: 1px; /* prevents collapsing before first draw */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  /* Reset some styles that the rest of the page might have set */
  -moz-border-radius: 0; -webkit-border-radius: 0; border-radius: 0;
  border-width: 0;
  background: transparent;
  font-family: inherit;
  font-size: inherit;
  margin: 0;
  white-space: pre;
  word-wrap: normal;
  line-height: inherit;
  color: inherit;
  z-index: 2;
  position: relative;
  overflow: visible;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-variant-ligatures: contextual;
  font-variant-ligatures: contextual;
}
.CodeMirror-wrap pre.CodeMirror-line,
.CodeMirror-wrap pre.CodeMirror-line-like {
  word-wrap: break-word;
  white-space: pre-wrap;
  word-break: normal;
}

.CodeMirror-linebackground {
  position: absolute;
  left: 0; right: 0; top: 0; bottom: 0;
  z-index: 0;
}

.CodeMirror-linewidget {
  position: relative;
  z-index: 2;
  padding: 0.1px; /* Force widget margins to stay inside of the container */
}

.CodeMirror-widget {}

.CodeMirror-rtl pre { direction: rtl; }

.CodeMirror-code {
  outline: none;
}

/* Force content-box sizing for the elements where we expect it */
.CodeMirror-scroll,
.CodeMirror-sizer,
.CodeMirror-gutter,
.CodeMirror-gutters,
.CodeMirror-linenumber {
  -moz-box-sizing: content-box;
  box-sizing: content-box;
}

.CodeMirror-measure {
  position: absolute;
  width: 100%;
  height: 0;
  overflow: hidden;
  visibility: hidden;
}

.CodeMirror-cursor {
  position: absolute;
  pointer-events: none;
}
.CodeMirror-measure pre { position: static; }

div.CodeMirror-cursors {
  visibility: hidden;
  position: relative;
  z-index: 3;
}
div.CodeMirror-dragcursors {
  visibility: visible;
}

.CodeMirror-focused div.CodeMirror-cursors {
  visibility: visible;
}

.CodeMirror-selected { background: #d9d9d9; }
.CodeMirror-focused .CodeMirror-selected { background: #d7d4f0; }
.CodeMirror-crosshair { cursor: crosshair; }
.CodeMirror-line::selection, .CodeMirror-line > span::selection, .CodeMirror-line > span > span::selection { background: #d7d4f0; }
.CodeMirror-line::-moz-selection, .CodeMirror-line > span::-moz-selection, .CodeMirror-line > span > span::-moz-selection { background: #d7d4f0; }

.cm-searching {
  background-color: #ffa;
  background-color: rgba(255, 255, 0, .4);
}

/* Used to force a border model for a node */
.cm-force-border { padding-right: .1px; }

@media print {
  /* Hide the cursor when printing */
  .CodeMirror div.CodeMirror-cursors {
    visibility: hidden;
  }
}

/* See issue #2901 */
.cm-tab-wrap-hack:after { content: ''; }

/* Help users use markselection to safely style text background */
span.CodeMirror-selectedtext { background: none; }

.CodeMirror-dialog {
  position: absolute;
  left: 0; right: 0;
  background: inherit;
  z-index: 15;
  padding: .1em .8em;
  overflow: hidden;
  color: inherit;
}

.CodeMirror-dialog-top {
  border-bottom: 1px solid #eee;
  top: 0;
}

.CodeMirror-dialog-bottom {
  border-top: 1px solid #eee;
  bottom: 0;
}

.CodeMirror-dialog input {
  border: none;
  outline: none;
  background: transparent;
  width: 20em;
  color: inherit;
  font-family: monospace;
}

.CodeMirror-dialog button {
  font-size: 70%;
}

.CodeMirror-foldmarker {
  color: blue;
  text-shadow: #b9f 1px 1px 2px, #b9f -1px -1px 2px, #b9f 1px -1px 2px, #b9f -1px 1px 2px;
  font-family: arial;
  line-height: .3;
  cursor: pointer;
}
.CodeMirror-foldgutter {
  width: .7em;
}
.CodeMirror-foldgutter-open,
.CodeMirror-foldgutter-folded {
  cursor: pointer;
}
.CodeMirror-foldgutter-open:after {
  content: "\25BE";
}
.CodeMirror-foldgutter-folded:after {
  content: "\25B8";
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.CodeMirror {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;
  /* Changed to auto to autogrow */
}

.CodeMirror pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* This causes https://github.com/jupyter/jupyterlab/issues/522 */
/* May not cause it not because we changed it! */
.CodeMirror-lines {
  padding: var(--jp-code-padding) 0;
}

.CodeMirror-linenumber {
  padding: 0 8px;
}

.jp-CodeMirrorEditor {
  cursor: text;
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.CodeMirror.jp-mod-readOnly .CodeMirror-cursor {
  display: none;
}

.CodeMirror-gutters {
  border-right: 1px solid var(--jp-border-color2);
  background-color: var(--jp-layout-color0);
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.CodeMirror-selectedtext.cm-searching {
  background-color: var(--jp-search-selected-match-background-color) !important;
  color: var(--jp-search-selected-match-color) !important;
}

.cm-searching {
  background-color: var(
    --jp-search-unselected-match-background-color
  ) !important;
  color: var(--jp-search-unselected-match-color) !important;
}

.CodeMirror-focused .CodeMirror-selected {
  background-color: var(--jp-editor-selected-focused-background);
}

.CodeMirror-selected {
  background-color: var(--jp-editor-selected-background);
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/**
 * Here is our jupyter theme for CodeMirror syntax highlighting
 * This is used in our marked.js syntax highlighting and CodeMirror itself
 * The string "jupyter" is set in ../codemirror/widget.DEFAULT_CODEMIRROR_THEME
 * This came from the classic notebook, which came form highlight.js/GitHub
 */

/**
 * CodeMirror themes are handling the background/color in this way. This works
 * fine for CodeMirror editors outside the notebook, but the notebook styles
 * these things differently.
 */
.CodeMirror.cm-s-jupyter {
  background: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* In the notebook, we want this styling to be handled by its container */
.jp-CodeConsole .CodeMirror.cm-s-jupyter,
.jp-Notebook .CodeMirror.cm-s-jupyter {
  background: transparent;
}

.cm-s-jupyter .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}
.cm-s-jupyter span.cm-keyword {
  color: var(--jp-mirror-editor-keyword-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-atom {
  color: var(--jp-mirror-editor-atom-color);
}
.cm-s-jupyter span.cm-number {
  color: var(--jp-mirror-editor-number-color);
}
.cm-s-jupyter span.cm-def {
  color: var(--jp-mirror-editor-def-color);
}
.cm-s-jupyter span.cm-variable {
  color: var(--jp-mirror-editor-variable-color);
}
.cm-s-jupyter span.cm-variable-2 {
  color: var(--jp-mirror-editor-variable-2-color);
}
.cm-s-jupyter span.cm-variable-3 {
  color: var(--jp-mirror-editor-variable-3-color);
}
.cm-s-jupyter span.cm-punctuation {
  color: var(--jp-mirror-editor-punctuation-color);
}
.cm-s-jupyter span.cm-property {
  color: var(--jp-mirror-editor-property-color);
}
.cm-s-jupyter span.cm-operator {
  color: var(--jp-mirror-editor-operator-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-comment {
  color: var(--jp-mirror-editor-comment-color);
  font-style: italic;
}
.cm-s-jupyter span.cm-string {
  color: var(--jp-mirror-editor-string-color);
}
.cm-s-jupyter span.cm-string-2 {
  color: var(--jp-mirror-editor-string-2-color);
}
.cm-s-jupyter span.cm-meta {
  color: var(--jp-mirror-editor-meta-color);
}
.cm-s-jupyter span.cm-qualifier {
  color: var(--jp-mirror-editor-qualifier-color);
}
.cm-s-jupyter span.cm-builtin {
  color: var(--jp-mirror-editor-builtin-color);
}
.cm-s-jupyter span.cm-bracket {
  color: var(--jp-mirror-editor-bracket-color);
}
.cm-s-jupyter span.cm-tag {
  color: var(--jp-mirror-editor-tag-color);
}
.cm-s-jupyter span.cm-attribute {
  color: var(--jp-mirror-editor-attribute-color);
}
.cm-s-jupyter span.cm-header {
  color: var(--jp-mirror-editor-header-color);
}
.cm-s-jupyter span.cm-quote {
  color: var(--jp-mirror-editor-quote-color);
}
.cm-s-jupyter span.cm-link {
  color: var(--jp-mirror-editor-link-color);
}
.cm-s-jupyter span.cm-error {
  color: var(--jp-mirror-editor-error-color);
}
.cm-s-jupyter span.cm-hr {
  color: #999;
}

.cm-s-jupyter span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}

.cm-s-jupyter .CodeMirror-activeline-background,
.cm-s-jupyter .CodeMirror-gutter {
  background-color: var(--jp-layout-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .remote-caret {
  position: relative;
  border-left: 2px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .remote-caret > div {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -2px;
  font-size: 0.95em;
  background-color: rgb(250, 129, 0);
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 3;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .remote-caret.hide-name > div {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .remote-caret:hover > div {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0px;
  padding: 0px;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}
.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}
.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}
.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}
.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}
.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}
.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}
.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}
.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}
.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}
.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}
.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}
.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}
.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}
.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}
.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}
.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0em;
}

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: 12px;
  table-layout: fixed;
  margin-left: auto;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon table {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0px;
}

.jp-RenderedHTMLCommon p {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}
/* ...or leave it untouched if they don't */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-dark-background {
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-light-background {
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}
.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}
.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}
.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}
.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}
.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}
.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}
.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}
.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: 0.8em;
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser {
  display: flex;
  flex-direction: column;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  border-bottom: none;
  height: auto;
  margin: var(--jp-toolbar-header-margin);
  box-shadow: none;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0px 2px;
  padding: 0px 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0px;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar.jp-Toolbar {
  padding: 0px;
  margin: 8px 12px 0px 12px;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  justify-content: flex-start;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0px;
  padding-right: 2px;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-ToolbarButtonComponent {
  width: 40px;
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent {
  width: 72px;
  background: var(--jp-brand-color1);
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent:focus-visible {
  background-color: var(--jp-brand-color0);
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent
  .jp-icon3 {
  fill: white;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileBrowser-filterBox {
  padding: 0px;
  flex: 0 0 auto;
  margin: 8px 12px 0px 12px;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing:focus-visible {
  border: 1px solid var(--jp-brand-color1);
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px 12px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon:before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon:before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0px;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-DirListing-deadSpace {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
}

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: flex;
  flex-direction: row;
}

body[data-format='mobile'] .jp-OutputArea-child {
  flex-direction: column;
}

.jp-OutputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

body[data-format='mobile'] .jp-OutputPrompt {
  flex: 0 0 auto;
  text-align: left;
}

.jp-OutputArea-output {
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea-child .jp-OutputArea-output {
  flex-grow: 1;
  flex-shrink: 1;
}

body[data-format='mobile'] .jp-OutputArea-child .jp-OutputArea-output {
  margin-left: var(--jp-notebook-padding);
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0px;
  padding: 0px;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0px;
  flex: 1 1 auto;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-OutputArea-stdin {
  line-height: var(--jp-code-line-height);
  padding-top: var(--jp-code-padding);
  display: flex;
}

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;
  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0px;
  bottom: 0px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0px;
  width: 100%;
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: flex;
  flex-direction: row;
  overflow: hidden;
}

body[data-format='mobile'] .jp-InputArea {
  flex-direction: column;
}

.jp-InputArea-editor {
  flex: 1 1 auto;
  overflow: hidden;
}

.jp-InputArea-editor {
  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0px;
  background: var(--jp-cell-editor-background);
}

body[data-format='mobile'] .jp-InputArea-editor {
  margin-left: var(--jp-notebook-padding);
}

.jp-InputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

body[data-format='mobile'] .jp-InputPrompt {
  flex: 0 0 auto;
  text-align: left;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: flex;
  flex-direction: row;
  flex: 1 1 auto;
}

.jp-Placeholder-prompt {
  box-sizing: border-box;
}

.jp-Placeholder-content {
  flex: 1 1 auto;
  border: none;
  background: transparent;
  height: 20px;
  box-sizing: border-box;
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0px;
  margin: 0px;
  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 200px;
  box-shadow: inset 0 0 6px 2px rgba(0, 0, 0, 0.3);
  margin-left: var(--jp-private-cell-scrolling-output-offset);
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  flex: 0 0
    calc(
      var(--jp-cell-prompt-width) -
        var(--jp-private-cell-scrolling-output-offset)
    );
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  flex: 1 1 auto;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

.jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
}

.jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-collapseHeadingButton {
  display: none;
}

.jp-MarkdownCell:hover .jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: 2px;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook-render * {
  contain: none !important;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
  float: left;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt:before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0px;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-NotebookTools-tool {
  padding: 0px 12px 0 12px;
}

.jp-ActiveCellTool {
  padding: 12px;
  background-color: var(--jp-layout-color1);
  border-top: none !important;
}

.jp-ActiveCellTool .jp-InputArea-prompt {
  flex: 0 0 auto;
  padding-left: 0px;
}

.jp-ActiveCellTool .jp-InputArea-editor {
  flex: 1 1 auto;
  background: var(--jp-cell-editor-background);
  border-color: var(--jp-cell-editor-border-color);
}

.jp-ActiveCellTool .jp-InputArea-editor .CodeMirror {
  background: transparent;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0px 12px 0px;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body div {
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>

    <style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0px 2px 1px -1px var(--jp-shadow-umbra-color),
    0px 1px 1px 0px var(--jp-shadow-penumbra-color),
    0px 1px 3px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0px 3px 1px -2px var(--jp-shadow-umbra-color),
    0px 2px 2px 0px var(--jp-shadow-penumbra-color),
    0px 1px 5px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0px 2px 4px -1px var(--jp-shadow-umbra-color),
    0px 4px 5px 0px var(--jp-shadow-penumbra-color),
    0px 1px 10px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0px 3px 5px -1px var(--jp-shadow-umbra-color),
    0px 6px 10px 0px var(--jp-shadow-penumbra-color),
    0px 1px 18px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0px 5px 5px -3px var(--jp-shadow-umbra-color),
    0px 8px 10px 1px var(--jp-shadow-penumbra-color),
    0px 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0px 7px 8px -4px var(--jp-shadow-umbra-color),
    0px 12px 17px 2px var(--jp-shadow-penumbra-color),
    0px 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0px 8px 10px -5px var(--jp-shadow-umbra-color),
    0px 16px 24px 2px var(--jp-shadow-penumbra-color),
    0px 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0px 10px 13px -6px var(--jp-shadow-umbra-color),
    0px 20px 31px 3px var(--jp-shadow-penumbra-color),
    0px 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0px 11px 15px -7px var(--jp-shadow-umbra-color),
    0px 24px 38px 3px var(--jp-shadow-penumbra-color),
    0px 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;

  --jp-ui-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica,
    Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;

  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);

  --jp-content-link-color: var(--md-blue-700);

  --jp-content-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: Menlo, Consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);

  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);

  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);

  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);

  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;

  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;

  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);

  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0px;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0px 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-border-color1);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: #05a;
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #aa22ff;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #aa22ff;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);
}
</style>

<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

.highlight  {
  margin: 0.4em;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.CodeMirror pre {
  margin: 0;
  padding: 0;
}

/* Using table instead of flexbox so that we can use break-inside property */
/* CSS rules under this comment should not be required anymore after we move to the JupyterLab 4.0 CSS */


.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  min-width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-OutputArea-child {
  display: table;
  width: 100%;
}

.jp-OutputPrompt {
  display: table-cell;
  vertical-align: top;
  min-width: var(--jp-cell-prompt-width);
}

body[data-format='mobile'] .jp-OutputPrompt {
  display: table-row;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
}

body[data-format='mobile'] .jp-OutputArea-child .jp-OutputArea-output {
  display: table-row;
}

.jp-OutputArea-output.jp-OutputArea-executeResult {
  width: 100%;
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }

  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}
</style>

<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                CommonHTML: {
                    linebreaks: {
                    automatic: true
                    }
                }
            });

            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
    <!-- End of mathjax configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h1 id="Autonomous-Driving---Car-Detection">Autonomous Driving - Car Detection<a class="anchor-link" href="#Autonomous-Driving---Car-Detection">&#182;</a></h1><p>Welcome to the Week 3 programming assignment! In this notebook, you'll implement object detection using the very powerful YOLO model. Many of the ideas in this notebook are described in the two YOLO papers: <a href="https://arxiv.org/abs/1506.02640">Redmon et al., 2016</a> and <a href="https://arxiv.org/abs/1612.08242">Redmon and Farhadi, 2016</a>.</p>
<p><strong>By the end of this assignment, you'll be able to</strong>:</p>
<ul>
<li>Detect objects in a car detection dataset</li>
<li>Implement non-max suppression to increase accuracy</li>
<li>Implement intersection over union</li>
<li>Handle bounding boxes, a type of image annotation popular in deep learning</li>
</ul>
<h2 id="Important-Note-on-Submission-to-the-AutoGrader">Important Note on Submission to the AutoGrader<a class="anchor-link" href="#Important-Note-on-Submission-to-the-AutoGrader">&#182;</a></h2><p>Before submitting your assignment to the AutoGrader, please make sure you are not doing the following:</p>
<ol>
<li>You have not added any <em>extra</em> <code>print</code> statement(s) in the assignment.</li>
<li>You have not added any <em>extra</em> code cell(s) in the assignment.</li>
<li>You have not changed any of the function parameters.</li>
<li>You are not using any global variables inside your graded exercises. Unless specifically instructed to do so, please refrain from it and use the local variables instead.</li>
<li>You are not changing the assignment code where it is not required, like creating <em>extra</em> variables.</li>
</ol>
<p>If you do any of the following, you will get something like, <code>Grader not found</code> (or similarly unexpected) error upon submitting your assignment. Before asking for help/debugging the errors in your assignment, check for these first. If this is the case, and you don't remember the changes you have made, you can get a fresh copy of the assignment by following these <a href="https://www.coursera.org/learn/convolutional-neural-networks/supplement/DS4yP/h-ow-to-refresh-your-workspace">instructions</a>.</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Table-of-Contents">Table of Contents<a class="anchor-link" href="#Table-of-Contents">&#182;</a></h2><ul>
<li><a href="#0">Packages</a></li>
<li><a href="#1">1 - Problem Statement</a></li>
<li><a href="#2">2 - YOLO</a><ul>
<li><a href="#2-1">2.1 - Model Details</a></li>
<li><a href="#2-2">2.2 - Filtering with a Threshold on Class Scores</a><ul>
<li><a href="#ex-1">Exercise 1 - yolo_filter_boxes</a></li>
</ul>
</li>
<li><a href="#2-3">2.3 - Non-max Suppression</a><ul>
<li><a href="#ex-2">Exercise 2 - iou</a></li>
</ul>
</li>
<li><a href="#2-4">2.4 - YOLO Non-max Suppression</a><ul>
<li><a href="#ex-3">Exercise 3 - yolo_non_max_suppression</a></li>
</ul>
</li>
<li><a href="#2-5">2.5 - Wrapping Up the Filtering</a><ul>
<li><a href="#ex-4">Exercise 4 - yolo_eval</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#3">3 - Test YOLO Pre-trained Model on Images</a><ul>
<li><a href="#3-1">3.1 - Defining Classes, Anchors and Image Shape</a></li>
<li><a href="#3-2">3.2 - Loading a Pre-trained Model</a></li>
<li><a href="#3-3">3.3 - Convert Output of the Model to Usable Bounding Box Tensors</a></li>
<li><a href="#3-4">3.4 - Filtering Boxes</a></li>
<li><a href="#3-5">3.5 - Run the YOLO on an Image</a></li>
</ul>
</li>
<li><a href="#4">4 - Summary for YOLO</a></li>
<li><a href="#5">5 - References</a></li>
</ul>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='0'></a></p>
<h2 id="Packages">Packages<a class="anchor-link" href="#Packages">&#182;</a></h2><p>Run the following cell to load the packages and dependencies that will come in handy as you build the object detector!</p>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>
<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">matplotlib.pyplot</span> <span class="kn">import</span> <span class="n">imshow</span>
<span class="kn">import</span> <span class="nn">scipy.io</span>
<span class="kn">import</span> <span class="nn">scipy.misc</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">PIL</span>
<span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">ImageFont</span><span class="p">,</span> <span class="n">ImageDraw</span><span class="p">,</span> <span class="n">Image</span>
<span class="kn">import</span> <span class="nn">tensorflow</span> <span class="k">as</span> <span class="nn">tf</span>
<span class="kn">from</span> <span class="nn">tensorflow.python.framework.ops</span> <span class="kn">import</span> <span class="n">EagerTensor</span>

<span class="kn">from</span> <span class="nn">tensorflow.keras.models</span> <span class="kn">import</span> <span class="n">load_model</span>
<span class="kn">from</span> <span class="nn">yad2k.models.keras_yolo</span> <span class="kn">import</span> <span class="n">yolo_head</span>
<span class="kn">from</span> <span class="nn">yad2k.utils.utils</span> <span class="kn">import</span> <span class="n">draw_boxes</span><span class="p">,</span> <span class="n">get_colors_for_classes</span><span class="p">,</span> <span class="n">scale_boxes</span><span class="p">,</span> <span class="n">read_classes</span><span class="p">,</span> <span class="n">read_anchors</span><span class="p">,</span> <span class="n">preprocess_image</span>

<span class="o">%</span><span class="k">matplotlib</span> inline
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='1'></a></p>
<h2 id="1---Problem-Statement">1 - Problem Statement<a class="anchor-link" href="#1---Problem-Statement">&#182;</a></h2><p>You are working on a self-driving car. Go you! As a critical component of this project, you'd like to first build a car detection system. To collect data, you've mounted a camera to the hood (meaning the front) of the car, which takes pictures of the road ahead every few seconds as you drive around.</p>
<center>
</center><caption><center> Pictures taken from a car-mounted camera while driving around Silicon Valley. <br> Dataset provided by <a href="https://www.drive.ai/">drive.ai</a>.
</center></caption><p>You've gathered all these images into a folder and labelled them by drawing bounding boxes around every car you found. Here's an example of what your bounding boxes look like:</p>
<p><img src="/nb_images/box_label.png" style="width:500px;height:250;"></p>
<caption><center> <u><b>Figure 1</u></b>: Definition of a box<br> </center></caption><p>If there are 80 classes you want the object detector to recognize, you can represent the class label $c$ either as an integer from 1 to 80, or as an 80-dimensional vector (with 80 numbers) one component of which is 1, and the rest of which are 0. The video lectures used the latter representation; in this notebook, you'll use both representations, depending on which is more convenient for a particular step.</p>
<p>In this exercise, you'll discover how YOLO ("You Only Look Once") performs object detection, and then apply it to car detection. Because the YOLO model is very computationally expensive to train, the pre-trained weights are already loaded for you to use.</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='2'></a></p>
<h2 id="2---YOLO">2 - YOLO<a class="anchor-link" href="#2---YOLO">&#182;</a></h2>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>"You Only Look Once" (YOLO) is a popular algorithm because it achieves high accuracy while also being able to run in real time. This algorithm "only looks once" at the image in the sense that it requires only one forward propagation pass through the network to make predictions. After non-max suppression, it then outputs recognized objects together with the bounding boxes.</p>
<p><a name='2-1'></a></p>
<h3 id="2.1---Model-Details">2.1 - Model Details<a class="anchor-link" href="#2.1---Model-Details">&#182;</a></h3><h4 id="Inputs-and-outputs">Inputs and outputs<a class="anchor-link" href="#Inputs-and-outputs">&#182;</a></h4><ul>
<li>The <strong>input</strong> is a batch of images, and each image has the shape (608, 608, 3)</li>
<li>The <strong>output</strong> is a list of bounding boxes along with the recognized classes. Each bounding box is represented by 6 numbers $(p_c, b_x, b_y, b_h, b_w, c)$ as explained above. If you expand $c$ into an 80-dimensional vector, each bounding box is then represented by 85 numbers. </li>
</ul>
<h4 id="Anchor-Boxes">Anchor Boxes<a class="anchor-link" href="#Anchor-Boxes">&#182;</a></h4><ul>
<li>Anchor boxes are chosen by exploring the training data to choose reasonable height/width ratios that represent the different classes.  For this assignment, 5 anchor boxes were chosen for you (to cover the 80 classes), and stored in the file './model_data/yolo_anchors.txt'</li>
<li>The dimension of the encoding tensor of the second to last dimension based on the anchor boxes is $(m, n_H,n_W,anchors,classes)$.</li>
<li>The YOLO architecture is: IMAGE (m, 608, 608, 3) -&gt; DEEP CNN -&gt; ENCODING (m, 19, 19, 5, 85).  </li>
</ul>
<h4 id="Encoding">Encoding<a class="anchor-link" href="#Encoding">&#182;</a></h4><p>Let's look in greater detail at what this encoding represents.</p>
<p><img src="/nb_images/architecture.png" style="width:700px;height:400;"></p>
<caption><center> <u><b> Figure 2 </u></b>: Encoding architecture for YOLO<br> </center></caption><p>If the center/midpoint of an object falls into a grid cell, that grid cell is responsible for detecting that object.</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Since you're using 5 anchor boxes, each of the 19 x19 cells thus encodes information about 5 boxes. Anchor boxes are defined only by their width and height.</p>
<p>For simplicity, you'll flatten the last two dimensions of the shape (19, 19, 5, 85) encoding, so the output of the Deep CNN is (19, 19, 425).</p>
<p><img src="/nb_images/flatten.png" style="width:700px;height:400;"></p>
<caption><center> <u><b> Figure 3 </u></b>: Flattening the last two last dimensions<br> </center></caption>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h4 id="Class-score">Class score<a class="anchor-link" href="#Class-score">&#182;</a></h4><p>Now, for each box (of each cell) you'll compute the following element-wise product and extract a probability that the box contains a certain class.<br>
The class score is $score_{c,i} = p_{c} \times c_{i}$: the probability that there is an object $p_{c}$ times the probability that the object is a certain class $c_{i}$.</p>
<p><img src="/nb_images/probability_extraction.png" style="width:700px;height:400;"></p>
<caption><center> <u><b>Figure 4</u></b>: Find the class detected by each box<br> </center></caption><h5 id="Example-of-figure-4">Example of figure 4<a class="anchor-link" href="#Example-of-figure-4">&#182;</a></h5><ul>
<li>In figure 4, let's say for box 1 (cell 1), the probability that an object exists is $p_{1}=0.60$.  So there's a 60% chance that an object exists in box 1 (cell 1).  </li>
<li>The probability that the object is the class "category 3 (a car)" is $c_{3}=0.73$.  </li>
<li>The score for box 1 and for category "3" is $score_{1,3}=0.60 \times 0.73 = 0.44$.  </li>
<li>Let's say you calculate the score for all 80 classes in box 1, and find that the score for the car class (class 3) is the maximum.  So you'll assign the score 0.44 and class "3" to this box "1".</li>
</ul>
<h4 id="Visualizing-classes">Visualizing classes<a class="anchor-link" href="#Visualizing-classes">&#182;</a></h4><p>Here's one way to visualize what YOLO is predicting on an image:</p>
<ul>
<li>For each of the 19x19 grid cells, find the maximum of the probability scores (taking a max across the 80 classes, one maximum for each of the 5 anchor boxes).</li>
<li>Color that grid cell according to what object that grid cell considers the most likely.</li>
</ul>
<p>Doing this results in this picture:</p>
<p><img src="/nb_images/proba_map.png" style="width:300px;height:300;"></p>
<caption><center> <u><b>Figure 5</u></b>: Each one of the 19x19 grid cells is colored according to which class has the largest predicted probability in that cell.<br> </center></caption><p>Note that this visualization isn't a core part of the YOLO algorithm itself for making predictions; it's just a nice way of visualizing an intermediate result of the algorithm.</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h4 id="Visualizing-bounding-boxes">Visualizing bounding boxes<a class="anchor-link" href="#Visualizing-bounding-boxes">&#182;</a></h4><p>Another way to visualize YOLO's output is to plot the bounding boxes that it outputs. Doing that results in a visualization like this:</p>
<p><img src="/nb_images/anchor_map.png" style="width:200px;height:200;"></p>
<caption><center> <u><b>Figure 6</u></b>: Each cell gives you 5 boxes. In total, the model predicts: 19x19x5 = 1805 boxes just by looking once at the image (one forward pass through the network)! Different colors denote different classes. <br> </center></caption><h4 id="Non-Max-suppression">Non-Max suppression<a class="anchor-link" href="#Non-Max-suppression">&#182;</a></h4><p>In the figure above, the only boxes plotted are ones for which the model had assigned a high probability, but this is still too many boxes. You'd like to reduce the algorithm's output to a much smaller number of detected objects.</p>
<p>To do so, you'll use <strong>non-max suppression</strong>. Specifically, you'll carry out these steps:</p>
<ul>
<li>Get rid of boxes with a low score. Meaning, the box is not very confident about detecting a class, either due to the low probability of any object, or low probability of this particular class.</li>
<li>Select only one box when several boxes overlap with each other and detect the same object.</li>
</ul>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='2-2'></a></p>
<h3 id="2.2---Filtering-with-a-Threshold-on-Class-Scores">2.2 - Filtering with a Threshold on Class Scores<a class="anchor-link" href="#2.2---Filtering-with-a-Threshold-on-Class-Scores">&#182;</a></h3><p>You're going to first apply a filter by thresholding, meaning you'll get rid of any box for which the class "score" is less than a chosen threshold.</p>
<p>The model gives you a total of 19x19x5x85 numbers, with each box described by 85 numbers. It's convenient to rearrange the (19,19,5,85) (or (19,19,425)) dimensional tensor into the following variables:</p>
<ul>
<li><code>box_confidence</code>: tensor of shape $(19, 19, 5, 1)$ containing $p_c$ (confidence probability that there's some object) for each of the 5 boxes predicted in each of the 19x19 cells.</li>
<li><code>boxes</code>: tensor of shape $(19, 19, 5, 4)$ containing the midpoint and dimensions $(b_x, b_y, b_h, b_w)$ for each of the 5 boxes in each cell.</li>
<li><code>box_class_probs</code>: tensor of shape $(19, 19, 5, 80)$ containing the "class probabilities" $(c_1, c_2, ... c_{80})$ for each of the 80 classes for each of the 5 boxes per cell.</li>
</ul>
<p><a name='ex-1'></a></p>
<h3 id="Exercise-1---yolo_filter_boxes">Exercise 1 - yolo_filter_boxes<a class="anchor-link" href="#Exercise-1---yolo_filter_boxes">&#182;</a></h3><p>Implement <code>yolo_filter_boxes()</code>.</p>
<ol>
<li><p>Compute box scores by doing the elementwise product as described in Figure 4 ($p \times c$).<br>
The following code may help you choose the right operator:</p>
<div class="highlight"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">19</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">b</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">19</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">80</span><span class="p">)</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">a</span> <span class="o">*</span> <span class="n">b</span> <span class="c1"># shape of c will be (19, 19, 5, 80)</span>
</pre></div>
<p>This is an example of <strong>broadcasting</strong> (multiplying vectors of different sizes).</p>
</li>
<li><p>For each box, find:</p>
<ul>
<li>the index of the class with the maximum box score</li>
<li><p>the corresponding box score</p>
<p><strong>Useful References</strong></p>
<ul>
<li><a href="https://www.tensorflow.org/api_docs/python/tf/math/argmax">tf.math.argmax</a></li>
<li><a href="https://www.tensorflow.org/api_docs/python/tf/math/reduce_max">tf.math.reduce_max</a></li>
</ul>
<p><strong>Helpful Hints</strong></p>
<ul>
<li>For the <code>axis</code> parameter of <code>argmax</code> and <code>reduce_max</code>, if you want to select the <strong>last</strong> axis, one way to do so is to set <code>axis=-1</code>.  This is similar to Python array indexing, where you can select the last position of an array using <code>arrayname[-1]</code>.</li>
<li>Applying <code>reduce_max</code> normally collapses the axis for which the maximum is applied.  <code>keepdims=False</code> is the default option, and allows that dimension to be removed.  You don't need to keep the last dimension after applying the maximum here.</li>
</ul>
</li>
</ul>
</li>
</ol>
<ol>
<li><p>Create a mask by using a threshold. As a reminder: <code>([0.9, 0.3, 0.4, 0.5, 0.1] &lt; 0.4)</code> returns: <code>[False, True, False, False, True]</code>. The mask should be <code>True</code> for the boxes you want to keep.</p>
</li>
<li><p>Use TensorFlow to apply the mask to <code>box_class_scores</code>, <code>boxes</code> and <code>box_classes</code> to filter out the boxes you don't want. You should be left with just the subset of boxes you want to keep.</p>
<p><strong>One more useful reference</strong>:</p>
<ul>
<li><a href="https://www.tensorflow.org/api_docs/python/tf/boolean_mask">tf.boolean mask</a>  </li>
</ul>
<p><strong>And one more helpful hint</strong>: :)</p>
<ul>
<li>For the <code>tf.boolean_mask</code>, you can keep the default <code>axis=None</code>.</li>
</ul>
</li>
</ol>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[6]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># UNQ_C1 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)</span>
<span class="c1"># GRADED FUNCTION: yolo_filter_boxes</span>

<span class="k">def</span> <span class="nf">yolo_filter_boxes</span><span class="p">(</span><span class="n">boxes</span><span class="p">,</span> <span class="n">box_confidence</span><span class="p">,</span> <span class="n">box_class_probs</span><span class="p">,</span> <span class="n">threshold</span> <span class="o">=</span> <span class="mf">.6</span><span class="p">):</span>
    <span class="sd">"""Filters YOLO boxes by thresholding on object and class confidence.</span>
<span class="sd">    </span>
<span class="sd">    Arguments:</span>
<span class="sd">        boxes -- tensor of shape (19, 19, 5, 4)</span>
<span class="sd">        box_confidence -- tensor of shape (19, 19, 5, 1)</span>
<span class="sd">        box_class_probs -- tensor of shape (19, 19, 5, 80)</span>
<span class="sd">        threshold -- real value, if [ highest class probability score &lt; threshold],</span>
<span class="sd">                     then get rid of the corresponding box</span>

<span class="sd">    Returns:</span>
<span class="sd">        scores -- tensor of shape (None,), containing the class probability score for selected boxes</span>
<span class="sd">        boxes -- tensor of shape (None, 4), containing (b_x, b_y, b_h, b_w) coordinates of selected boxes</span>
<span class="sd">        classes -- tensor of shape (None,), containing the index of the class detected by the selected boxes</span>

<span class="sd">    Note: "None" is here because you don't know the exact number of selected boxes, as it depends on the threshold. </span>
<span class="sd">    For example, the actual output size of scores would be (10,) if there are 10 boxes.</span>
<span class="sd">    """</span>
    
    <span class="c1">### START CODE HERE</span>
    <span class="c1"># Step 1: Compute box scores</span>
    <span class="c1">##(≈ 1 line)</span>
    <span class="n">box_scores</span> <span class="o">=</span> <span class="n">box_confidence</span> <span class="o">*</span> <span class="n">box_class_probs</span>

    <span class="c1"># Step 2: Find the box_classes using the max box_scores, keep track of the corresponding score</span>
    <span class="c1">##(≈ 2 lines)</span>
    <span class="c1"># IMPORTANT: set axis to -1</span>
    <span class="n">box_classes</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">math</span><span class="o">.</span><span class="n">argmax</span><span class="p">(</span><span class="n">box_scores</span><span class="p">,</span> <span class="n">axis</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">box_class_scores</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">math</span><span class="o">.</span><span class="n">reduce_max</span><span class="p">(</span><span class="n">box_scores</span><span class="p">,</span> <span class="n">axis</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>
    
    <span class="c1"># Step 3: Create a filtering mask based on "box_class_scores" by using "threshold". The mask should have the</span>
    <span class="c1"># same dimension as box_class_scores, and be True for the boxes you want to keep (with probability &gt;= threshold)</span>
    <span class="c1">## (≈ 1 line)</span>
    <span class="n">filtering_mask</span> <span class="o">=</span> <span class="n">box_class_scores</span> <span class="o">&gt;=</span> <span class="n">threshold</span>
    
    <span class="c1"># Step 4: Apply the mask to box_class_scores, boxes and box_classes</span>
    <span class="c1">## (≈ 3 lines)</span>
    <span class="n">scores</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">boolean_mask</span><span class="p">(</span><span class="n">box_class_scores</span><span class="p">,</span> <span class="n">filtering_mask</span><span class="p">)</span>
    <span class="n">boxes</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">boolean_mask</span><span class="p">(</span><span class="n">boxes</span><span class="p">,</span> <span class="n">filtering_mask</span><span class="p">)</span>
    <span class="n">classes</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">boolean_mask</span><span class="p">(</span><span class="n">box_classes</span><span class="p">,</span> <span class="n">filtering_mask</span><span class="p">)</span>
    <span class="c1">### END CODE HERE</span>
    
    <span class="k">return</span> <span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[7]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># BEGIN UNIT TEST</span>
<span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">set_seed</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="n">box_confidence</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">([</span><span class="mi">19</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">mean</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">stddev</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">boxes</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">([</span><span class="mi">19</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">4</span><span class="p">],</span> <span class="n">mean</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">stddev</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">box_class_probs</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">([</span><span class="mi">19</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">80</span><span class="p">],</span> <span class="n">mean</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">stddev</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span> <span class="o">=</span> <span class="n">yolo_filter_boxes</span><span class="p">(</span><span class="n">boxes</span><span class="p">,</span> <span class="n">box_confidence</span><span class="p">,</span> <span class="n">box_class_probs</span><span class="p">,</span> <span class="n">threshold</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"scores[2] = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">scores</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"boxes[2] = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">boxes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"classes[2] = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">classes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"scores.shape = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">scores</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"boxes.shape = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">boxes</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"classes.shape = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">classes</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>

<span class="k">assert</span> <span class="nb">type</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span> <span class="o">==</span> <span class="n">EagerTensor</span><span class="p">,</span> <span class="s2">"Use tensorflow functions"</span>
<span class="k">assert</span> <span class="nb">type</span><span class="p">(</span><span class="n">boxes</span><span class="p">)</span> <span class="o">==</span> <span class="n">EagerTensor</span><span class="p">,</span> <span class="s2">"Use tensorflow functions"</span>
<span class="k">assert</span> <span class="nb">type</span><span class="p">(</span><span class="n">classes</span><span class="p">)</span> <span class="o">==</span> <span class="n">EagerTensor</span><span class="p">,</span> <span class="s2">"Use tensorflow functions"</span>

<span class="k">assert</span> <span class="n">scores</span><span class="o">.</span><span class="n">shape</span> <span class="o">==</span> <span class="p">(</span><span class="mi">1789</span><span class="p">,),</span> <span class="s2">"Wrong shape in scores"</span>
<span class="k">assert</span> <span class="n">boxes</span><span class="o">.</span><span class="n">shape</span> <span class="o">==</span> <span class="p">(</span><span class="mi">1789</span><span class="p">,</span> <span class="mi">4</span><span class="p">),</span> <span class="s2">"Wrong shape in boxes"</span>
<span class="k">assert</span> <span class="n">classes</span><span class="o">.</span><span class="n">shape</span> <span class="o">==</span> <span class="p">(</span><span class="mi">1789</span><span class="p">,),</span> <span class="s2">"Wrong shape in classes"</span>

<span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">scores</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">(),</span> <span class="mf">9.270486</span><span class="p">),</span> <span class="s2">"Values are wrong on scores"</span>
<span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">allclose</span><span class="p">(</span><span class="n">boxes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">(),</span> <span class="p">[</span><span class="mf">4.6399336</span><span class="p">,</span> <span class="mf">3.2303846</span><span class="p">,</span> <span class="mf">4.431282</span><span class="p">,</span> <span class="o">-</span><span class="mf">2.202031</span><span class="p">]),</span> <span class="s2">"Values are wrong on boxes"</span>
<span class="k">assert</span> <span class="n">classes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span> <span class="o">==</span> <span class="mi">8</span><span class="p">,</span> <span class="s2">"Values are wrong on classes"</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\033</span><span class="s2">[92m All tests passed!"</span><span class="p">)</span>
<span class="c1"># END UNIT TEST</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>scores[2] = 9.270486
boxes[2] = [ 4.6399336  3.2303846  4.431282  -2.202031 ]
classes[2] = 8
scores.shape = (1789,)
boxes.shape = (1789, 4)
classes.shape = (1789,)
<span class="ansi-green-intense-fg"> All tests passed!
</span></pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Expected Output</strong>:</p>
<table>
    <tr>
        <td>
            <b>scores[2]</b>
        </td>
        <td>
           9.270486
        </td>
    </tr>
    <tr>
        <td>
            <b>boxes[2]</b>
        </td>
        <td>
           [ 4.6399336  3.2303846  4.431282  -2.202031 ]
        </td>
    </tr>
    <tr>
        <td>
            <b>classes[2]</b>
        </td>
        <td>
           8
        </td>
    </tr>
        <tr>
        <td>
            <b>scores.shape</b>
        </td>
        <td>
           (1789,)
        </td>
    </tr>
    <tr>
        <td>
            <b>boxes.shape</b>
        </td>
        <td>
           (1789, 4)
        </td>
    </tr>
    <tr>
        <td>
            <b>classes.shape</b>
        </td>
        <td>
           (1789,)
        </td>
    </tr>

</table>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Note</strong> In the test for <code>yolo_filter_boxes</code>, you're using random numbers to test the function.  In real data, the <code>box_class_probs</code> would contain non-zero values between 0 and 1 for the probabilities.  The box coordinates in <code>boxes</code> would also be chosen so that lengths and heights are non-negative.</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='2-3'></a></p>
<h3 id="2.3---Non-max-Suppression">2.3 - Non-max Suppression<a class="anchor-link" href="#2.3---Non-max-Suppression">&#182;</a></h3><p>Even after filtering by thresholding over the class scores, you still end up with a lot of overlapping boxes. A second filter for selecting the right boxes is called non-maximum suppression (NMS).</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><img src="/nb_images/non-max-suppression.png" style="width:500px;height:400;"></p>
<caption><center> <u> <b>Figure 7</b> </u>: In this example, the model has predicted 3 cars, but it's actually 3 predictions of the same car. Running non-max suppression (NMS) will select only the most accurate (highest probability) of the 3 boxes. <br> </center></caption>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Non-max suppression uses the very important function called <strong>"Intersection over Union"</strong>, or IoU.
<img src="/nb_images/iou.png" style="width:500px;height:400;"></p>
<caption><center> <u> <b>Figure 8</b> </u>: Definition of "Intersection over Union". <br> </center></caption><p><a name='ex-2'></a></p>
<h3 id="Exercise-2---iou">Exercise 2 - iou<a class="anchor-link" href="#Exercise-2---iou">&#182;</a></h3><p>Implement <code>iou()</code></p>
<p>Some hints:</p>
<ul>
<li>This code uses the convention that (0,0) is the top-left corner of an image, (1,0) is the upper-right corner, and (1,1) is the lower-right corner. In other words, the (0,0) origin starts at the top left corner of the image. As x increases, you move to the right.  As y increases, you move down.</li>
<li>For this exercise, a box is defined using its two corners: upper left $(x_1, y_1)$ and lower right $(x_2,y_2)$, instead of using the midpoint, height and width. This makes it a bit easier to calculate the intersection.</li>
<li>To calculate the area of a rectangle, multiply its height $(y_2 - y_1)$ by its width $(x_2 - x_1)$. Since $(x_1,y_1)$ is the top left and $x_2,y_2$ are the bottom right, these differences should be non-negative.</li>
<li>To find the <strong>intersection</strong> of the two boxes $(xi_{1}, yi_{1}, xi_{2}, yi_{2})$: <ul>
<li>Feel free to draw some examples on paper to clarify this conceptually.</li>
<li>The top left corner of the intersection $(xi_{1}, yi_{1})$ is found by comparing the top left corners $(x_1, y_1)$ of the two boxes and finding a vertex that has an x-coordinate that is closer to the right, and y-coordinate that is closer to the bottom.</li>
<li>The bottom right corner of the intersection $(xi_{2}, yi_{2})$ is found by comparing the bottom right corners $(x_2,y_2)$ of the two boxes and finding a vertex whose x-coordinate is closer to the left, and the y-coordinate that is closer to the top.</li>
<li>The two boxes <strong>may have no intersection</strong>.  You can detect this if the intersection coordinates you calculate end up being the top right and/or bottom left corners of an intersection box.  Another way to think of this is if you calculate the height $(y_2 - y_1)$ or width $(x_2 - x_1)$ and find that at least one of these lengths is negative, then there is no intersection (intersection area is zero).  </li>
<li>The two boxes may intersect at the <strong>edges or vertices</strong>, in which case the intersection area is still zero.  This happens when either the height or width (or both) of the calculated intersection is zero.</li>
</ul>
</li>
</ul>
<p><strong>Additional Hints</strong></p>
<ul>
<li><code>xi1</code> = <strong>max</strong>imum of the x1 coordinates of the two boxes</li>
<li><code>yi1</code> = <strong>max</strong>imum of the y1 coordinates of the two boxes</li>
<li><code>xi2</code> = <strong>min</strong>imum of the x2 coordinates of the two boxes</li>
<li><code>yi2</code> = <strong>min</strong>imum of the y2 coordinates of the two boxes</li>
<li><code>inter_area</code> = You can use <code>max(height, 0)</code> and <code>max(width, 0)</code></li>
</ul>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[20]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># UNQ_C2 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)</span>
<span class="c1"># GRADED FUNCTION: iou</span>

<span class="k">def</span> <span class="nf">iou</span><span class="p">(</span><span class="n">box1</span><span class="p">,</span> <span class="n">box2</span><span class="p">):</span>
    <span class="sd">"""Implement the intersection over union (IoU) between box1 and box2</span>
<span class="sd">    </span>
<span class="sd">    Arguments:</span>
<span class="sd">    box1 -- first box, list object with coordinates (box1_x1, box1_y1, box1_x2, box_1_y2)</span>
<span class="sd">    box2 -- second box, list object with coordinates (box2_x1, box2_y1, box2_x2, box2_y2)</span>
<span class="sd">    """</span>


    <span class="p">(</span><span class="n">box1_x1</span><span class="p">,</span> <span class="n">box1_y1</span><span class="p">,</span> <span class="n">box1_x2</span><span class="p">,</span> <span class="n">box1_y2</span><span class="p">)</span> <span class="o">=</span> <span class="n">box1</span>
    <span class="p">(</span><span class="n">box2_x1</span><span class="p">,</span> <span class="n">box2_y1</span><span class="p">,</span> <span class="n">box2_x2</span><span class="p">,</span> <span class="n">box2_y2</span><span class="p">)</span> <span class="o">=</span> <span class="n">box2</span>

    <span class="c1">### START CODE HERE</span>
    <span class="c1"># Calculate the (yi1, xi1, yi2, xi2) coordinates of the intersection of box1 and box2. Calculate its Area.</span>
    <span class="c1">##(≈ 7 lines)</span>
    <span class="n">xi1</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">box1_x1</span><span class="p">,</span> <span class="n">box2_x1</span><span class="p">)</span>
    <span class="n">yi1</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">box1_y1</span><span class="p">,</span> <span class="n">box2_y1</span><span class="p">)</span>
    <span class="n">xi2</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">box1_x2</span><span class="p">,</span> <span class="n">box2_x2</span><span class="p">)</span>
    <span class="n">yi2</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">box1_y2</span><span class="p">,</span> <span class="n">box2_y2</span><span class="p">)</span>
    <span class="n">inter_width</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">xi2</span> <span class="o">-</span> <span class="n">xi1</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
    <span class="n">inter_height</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">yi2</span> <span class="o">-</span> <span class="n">yi1</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
    <span class="n">inter_area</span> <span class="o">=</span> <span class="n">inter_width</span> <span class="o">*</span> <span class="n">inter_height</span>
    
    <span class="c1"># Calculate the Union area by using Formula: Union(A,B) = A + B - Inter(A,B)</span>
    <span class="c1">## (≈ 3 lines)</span>
    <span class="n">box1_area</span> <span class="o">=</span> <span class="p">(</span><span class="n">box1_x2</span> <span class="o">-</span> <span class="n">box1_x1</span><span class="p">)</span> <span class="o">*</span> <span class="p">(</span><span class="n">box1_y2</span> <span class="o">-</span> <span class="n">box1_y1</span><span class="p">)</span>
    <span class="n">box2_area</span> <span class="o">=</span> <span class="p">(</span><span class="n">box2_x2</span> <span class="o">-</span> <span class="n">box2_x1</span><span class="p">)</span> <span class="o">*</span> <span class="p">(</span><span class="n">box2_y2</span> <span class="o">-</span> <span class="n">box2_y1</span><span class="p">)</span>
    <span class="n">union_area</span> <span class="o">=</span> <span class="p">(</span><span class="n">box1_area</span> <span class="o">+</span> <span class="n">box2_area</span><span class="p">)</span> <span class="o">-</span> <span class="n">inter_area</span>
    
    <span class="c1"># compute the IoU</span>
    <span class="n">iou</span> <span class="o">=</span> <span class="n">inter_area</span> <span class="o">/</span> <span class="n">union_area</span>
    <span class="c1">### END CODE HERE</span>
    
    <span class="k">return</span> <span class="n">iou</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[21]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># BEGIN UNIT TEST</span>
<span class="c1">## Test case 1: boxes intersect</span>
<span class="n">box1</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="n">box2</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"iou for intersecting boxes = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">iou</span><span class="p">(</span><span class="n">box1</span><span class="p">,</span> <span class="n">box2</span><span class="p">)))</span>
<span class="k">assert</span> <span class="n">iou</span><span class="p">(</span><span class="n">box1</span><span class="p">,</span> <span class="n">box2</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">"The intersection area must be always smaller or equal than the union area."</span>
<span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">iou</span><span class="p">(</span><span class="n">box1</span><span class="p">,</span> <span class="n">box2</span><span class="p">),</span> <span class="mf">0.14285714</span><span class="p">),</span> <span class="s2">"Wrong value. Check your implementation. Problem with intersecting boxes"</span>

<span class="c1">## Test case 2: boxes do not intersect</span>
<span class="n">box1</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">)</span>
<span class="n">box2</span> <span class="o">=</span> <span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">,</span><span class="mi">7</span><span class="p">,</span><span class="mi">8</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"iou for non-intersecting boxes = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">iou</span><span class="p">(</span><span class="n">box1</span><span class="p">,</span><span class="n">box2</span><span class="p">)))</span>
<span class="k">assert</span> <span class="n">iou</span><span class="p">(</span><span class="n">box1</span><span class="p">,</span> <span class="n">box2</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">"Intersection must be 0"</span>

<span class="c1">## Test case 3: boxes intersect at vertices only</span>
<span class="n">box1</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span>
<span class="n">box2</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"iou for boxes that only touch at vertices = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">iou</span><span class="p">(</span><span class="n">box1</span><span class="p">,</span><span class="n">box2</span><span class="p">)))</span>
<span class="k">assert</span> <span class="n">iou</span><span class="p">(</span><span class="n">box1</span><span class="p">,</span> <span class="n">box2</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">"Intersection at vertices must be 0"</span>

<span class="c1">## Test case 4: boxes intersect at edge only</span>
<span class="n">box1</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span>
<span class="n">box2</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"iou for boxes that only touch at edges = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">iou</span><span class="p">(</span><span class="n">box1</span><span class="p">,</span><span class="n">box2</span><span class="p">)))</span>
<span class="k">assert</span> <span class="n">iou</span><span class="p">(</span><span class="n">box1</span><span class="p">,</span> <span class="n">box2</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">"Intersection at edges must be 0"</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\033</span><span class="s2">[92m All tests passed!"</span><span class="p">)</span>
<span class="c1"># END UNIT TEST</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>iou for intersecting boxes = 0.14285714285714285
iou for non-intersecting boxes = 0.0
iou for boxes that only touch at vertices = 0.0
iou for boxes that only touch at edges = 0.0
<span class="ansi-green-intense-fg"> All tests passed!
</span></pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Expected Output</strong>:</p>

<pre><code>iou for intersecting boxes = 0.14285714285714285
iou for non-intersecting boxes = 0.0
iou for boxes that only touch at vertices = 0.0
iou for boxes that only touch at edges = 0.0</code></pre>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='2-4'></a></p>
<h3 id="2.4---YOLO-Non-max-Suppression">2.4 - YOLO Non-max Suppression<a class="anchor-link" href="#2.4---YOLO-Non-max-Suppression">&#182;</a></h3><p>You are now ready to implement non-max suppression. The key steps are:</p>
<ol>
<li>Select the box that has the highest score.</li>
<li>Compute the overlap of this box with all other boxes, and remove boxes that overlap significantly (iou &gt;= <code>iou_threshold</code>).</li>
<li>Go back to step 1 and iterate until there are no more boxes with a lower score than the currently selected box.</li>
</ol>
<p>This will remove all boxes that have a large overlap with the selected boxes. Only the "best" boxes remain.</p>
<p><a name='ex-3'></a></p>
<h3 id="Exercise-3---yolo_non_max_suppression">Exercise 3 - yolo_non_max_suppression<a class="anchor-link" href="#Exercise-3---yolo_non_max_suppression">&#182;</a></h3><p>Implement <code>yolo_non_max_suppression()</code> using TensorFlow. TensorFlow has two built-in functions that are used to implement non-max suppression (so you don't actually need to use your <code>iou()</code> implementation):</p>
<p><strong>Reference documentation</strong>:</p>
<ul>
<li><p><a href="https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression">tf.image.non_max_suppression()</a></p>

<pre><code>tf.image.non_max_suppression(
  boxes,
  scores,
  max_output_size,
  iou_threshold=0.5,
  name=None
)</code></pre>
<p>Note that in the version of TensorFlow used here, there is no parameter <code>score_threshold</code> (it's shown in the documentation for the latest version) so trying to set this value will result in an error message: <em>got an unexpected keyword argument <code>score_threshold</code>.</em></p>
</li>
<li><p><a href="https://www.tensorflow.org/api_docs/python/tf/gather">tf.gather()</a></p>

<pre><code>keras.gather(
  reference,
  indices
)</code></pre>
</li>
</ul>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[22]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># UNQ_C3 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)</span>
<span class="c1"># GRADED FUNCTION: yolo_non_max_suppression</span>

<span class="k">def</span> <span class="nf">yolo_non_max_suppression</span><span class="p">(</span><span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span><span class="p">,</span> <span class="n">max_boxes</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span> <span class="n">iou_threshold</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">    Applies Non-max suppression (NMS) to set of boxes</span>
<span class="sd">    </span>
<span class="sd">    Arguments:</span>
<span class="sd">    scores -- tensor of shape (None,), output of yolo_filter_boxes()</span>
<span class="sd">    boxes -- tensor of shape (None, 4), output of yolo_filter_boxes() that have been scaled to the image size (see later)</span>
<span class="sd">    classes -- tensor of shape (None,), output of yolo_filter_boxes()</span>
<span class="sd">    max_boxes -- integer, maximum number of predicted boxes you'd like</span>
<span class="sd">    iou_threshold -- real value, "intersection over union" threshold used for NMS filtering</span>
<span class="sd">    </span>
<span class="sd">    Returns:</span>
<span class="sd">    scores -- tensor of shape (None, ), predicted score for each box</span>
<span class="sd">    boxes -- tensor of shape (None, 4), predicted box coordinates</span>
<span class="sd">    classes -- tensor of shape (None, ), predicted class for each box</span>
<span class="sd">    </span>
<span class="sd">    Note: The "None" dimension of the output tensors has obviously to be less than max_boxes. Note also that this</span>
<span class="sd">    function will transpose the shapes of scores, boxes, classes. This is made for convenience.</span>
<span class="sd">    """</span>
    
    <span class="n">max_boxes_tensor</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">max_boxes</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="s1">'int32'</span><span class="p">)</span>     <span class="c1"># tensor to be used in tf.image.non_max_suppression()</span>

    <span class="c1">### START CODE HERE</span>
    <span class="c1"># Use tf.image.non_max_suppression() to get the list of indices corresponding to boxes you keep</span>
    <span class="c1">##(≈ 1 line)</span>
    <span class="n">nms_indices</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">image</span><span class="o">.</span><span class="n">non_max_suppression</span><span class="p">(</span><span class="n">boxes</span><span class="p">,</span> <span class="n">scores</span><span class="p">,</span> <span class="n">max_boxes</span><span class="p">,</span> <span class="n">iou_threshold</span><span class="p">)</span>
    
    <span class="c1"># Use tf.gather() to select only nms_indices from scores, boxes and classes</span>
    <span class="c1">##(≈ 3 lines)</span>
    <span class="n">scores</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="n">scores</span><span class="p">,</span> <span class="n">nms_indices</span><span class="p">)</span>
    <span class="n">boxes</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="n">boxes</span><span class="p">,</span> <span class="n">nms_indices</span><span class="p">)</span>
    <span class="n">classes</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="n">classes</span><span class="p">,</span> <span class="n">nms_indices</span><span class="p">)</span>
    <span class="c1">### END CODE HERE</span>

    
    <span class="k">return</span> <span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[23]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># BEGIN UNIT TEST</span>
<span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">set_seed</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="n">scores</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">([</span><span class="mi">54</span><span class="p">,],</span> <span class="n">mean</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">stddev</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">boxes</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">([</span><span class="mi">54</span><span class="p">,</span> <span class="mi">4</span><span class="p">],</span> <span class="n">mean</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">stddev</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">classes</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">([</span><span class="mi">54</span><span class="p">,],</span> <span class="n">mean</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">stddev</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span> <span class="o">=</span> <span class="n">yolo_non_max_suppression</span><span class="p">(</span><span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span><span class="p">)</span>

<span class="k">assert</span> <span class="nb">type</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span> <span class="o">==</span> <span class="n">EagerTensor</span><span class="p">,</span> <span class="s2">"Use tensoflow functions"</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"scores[2] = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">scores</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"boxes[2] = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">boxes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"classes[2] = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">classes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"scores.shape = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">scores</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"boxes.shape = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">boxes</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"classes.shape = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">classes</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>

<span class="k">assert</span> <span class="nb">type</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span> <span class="o">==</span> <span class="n">EagerTensor</span><span class="p">,</span> <span class="s2">"Use tensoflow functions"</span>
<span class="k">assert</span> <span class="nb">type</span><span class="p">(</span><span class="n">boxes</span><span class="p">)</span> <span class="o">==</span> <span class="n">EagerTensor</span><span class="p">,</span> <span class="s2">"Use tensoflow functions"</span>
<span class="k">assert</span> <span class="nb">type</span><span class="p">(</span><span class="n">classes</span><span class="p">)</span> <span class="o">==</span> <span class="n">EagerTensor</span><span class="p">,</span> <span class="s2">"Use tensoflow functions"</span>

<span class="k">assert</span> <span class="n">scores</span><span class="o">.</span><span class="n">shape</span> <span class="o">==</span> <span class="p">(</span><span class="mi">10</span><span class="p">,),</span> <span class="s2">"Wrong shape"</span>
<span class="k">assert</span> <span class="n">boxes</span><span class="o">.</span><span class="n">shape</span> <span class="o">==</span> <span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">4</span><span class="p">),</span> <span class="s2">"Wrong shape"</span>
<span class="k">assert</span> <span class="n">classes</span><span class="o">.</span><span class="n">shape</span> <span class="o">==</span> <span class="p">(</span><span class="mi">10</span><span class="p">,),</span> <span class="s2">"Wrong shape"</span>

<span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">scores</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">(),</span> <span class="mf">8.147684</span><span class="p">),</span> <span class="s2">"Wrong value on scores"</span>
<span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">allclose</span><span class="p">(</span><span class="n">boxes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">(),</span> <span class="p">[</span> <span class="mf">6.0797963</span><span class="p">,</span> <span class="mf">3.743308</span><span class="p">,</span> <span class="mf">1.3914018</span><span class="p">,</span> <span class="o">-</span><span class="mf">0.34089637</span><span class="p">]),</span> <span class="s2">"Wrong value on boxes"</span>
<span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">classes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">(),</span> <span class="mf">1.7079165</span><span class="p">),</span> <span class="s2">"Wrong value on classes"</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\033</span><span class="s2">[92m All tests passed!"</span><span class="p">)</span>
<span class="c1"># END UNIT TEST</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>scores[2] = 8.147684
boxes[2] = [ 6.0797963   3.743308    1.3914018  -0.34089637]
classes[2] = 1.7079165
scores.shape = (10,)
boxes.shape = (10, 4)
classes.shape = (10,)
<span class="ansi-green-intense-fg"> All tests passed!
</span></pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Expected Output</strong>:</p>
<table>
    <tr>
        <td>
            <b>scores[2]</b>
        </td>
        <td>
           8.147684
        </td>
    </tr>
    <tr>
        <td>
            <b>boxes[2]</b>
        </td>
        <td>
           [ 6.0797963   3.743308    1.3914018  -0.34089637]
        </td>
    </tr>
    <tr>
        <td>
            <b>classes[2]</b>
        </td>
        <td>
           1.7079165
        </td>
    </tr>
        <tr>
        <td>
            <b>scores.shape</b>
        </td>
        <td>
           (10,)
        </td>
    </tr>
    <tr>
        <td>
            <b>boxes.shape</b>
        </td>
        <td>
           (10, 4)
        </td>
    </tr>
    <tr>
        <td>
            <b>classes.shape</b>
        </td>
        <td>
           (10,)
        </td>
    </tr>

</table>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='2-5'></a></p>
<h3 id="2.5---Wrapping-Up-the-Filtering">2.5 - Wrapping Up the Filtering<a class="anchor-link" href="#2.5---Wrapping-Up-the-Filtering">&#182;</a></h3><p>It's time to implement a function taking the output of the deep CNN (the 19x19x5x85 dimensional encoding) and filtering through all the boxes using the functions you've just implemented.</p>
<p><a name='ex-4'></a></p>
<h3 id="Exercise-4---yolo_eval">Exercise 4 - yolo_eval<a class="anchor-link" href="#Exercise-4---yolo_eval">&#182;</a></h3><p>Implement <code>yolo_eval()</code> which takes the output of the YOLO encoding and filters the boxes using score threshold and NMS. There's just one last implementational detail you have to know. There're a few ways of representing boxes, such as via their corners or via their midpoint and height/width. YOLO converts between a few such formats at different times, using the following functions (which are provided):</p>
<div class="highlight"><pre><span></span><span class="n">boxes</span> <span class="o">=</span> <span class="n">yolo_boxes_to_corners</span><span class="p">(</span><span class="n">box_xy</span><span class="p">,</span> <span class="n">box_wh</span><span class="p">)</span>
</pre></div>
<p>which converts the yolo box coordinates (x,y,w,h) to box corners' coordinates (x1, y1, x2, y2) to fit the input of <code>yolo_filter_boxes</code></p>
<div class="highlight"><pre><span></span><span class="n">boxes</span> <span class="o">=</span> <span class="n">scale_boxes</span><span class="p">(</span><span class="n">boxes</span><span class="p">,</span> <span class="n">image_shape</span><span class="p">)</span>
</pre></div>
<p>YOLO's network was trained to run on 608x608 images. If you are testing this data on a different size image -- for example, the car detection dataset had 720x1280 images -- this step rescales the boxes so that they can be plotted on top of the original 720x1280 image.</p>
<p>Don't worry about these two functions; you'll see where they need to be called below.</p>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[26]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">yolo_boxes_to_corners</span><span class="p">(</span><span class="n">box_xy</span><span class="p">,</span> <span class="n">box_wh</span><span class="p">):</span>
    <span class="sd">"""Convert YOLO box predictions to bounding box corners."""</span>
    <span class="n">box_mins</span> <span class="o">=</span> <span class="n">box_xy</span> <span class="o">-</span> <span class="p">(</span><span class="n">box_wh</span> <span class="o">/</span> <span class="mf">2.</span><span class="p">)</span>
    <span class="n">box_maxes</span> <span class="o">=</span> <span class="n">box_xy</span> <span class="o">+</span> <span class="p">(</span><span class="n">box_wh</span> <span class="o">/</span> <span class="mf">2.</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">tf</span><span class="o">.</span><span class="n">keras</span><span class="o">.</span><span class="n">backend</span><span class="o">.</span><span class="n">concatenate</span><span class="p">([</span>
        <span class="n">box_mins</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="mi">1</span><span class="p">:</span><span class="mi">2</span><span class="p">],</span>  <span class="c1"># y_min</span>
        <span class="n">box_mins</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="mi">0</span><span class="p">:</span><span class="mi">1</span><span class="p">],</span>  <span class="c1"># x_min</span>
        <span class="n">box_maxes</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="mi">1</span><span class="p">:</span><span class="mi">2</span><span class="p">],</span>  <span class="c1"># y_max</span>
        <span class="n">box_maxes</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="mi">0</span><span class="p">:</span><span class="mi">1</span><span class="p">]</span>  <span class="c1"># x_max</span>
    <span class="p">])</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[27]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># UNQ_C4 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)</span>
<span class="c1"># GRADED FUNCTION: yolo_eval</span>

<span class="k">def</span> <span class="nf">yolo_eval</span><span class="p">(</span><span class="n">yolo_outputs</span><span class="p">,</span> <span class="n">image_shape</span> <span class="o">=</span> <span class="p">(</span><span class="mi">720</span><span class="p">,</span> <span class="mi">1280</span><span class="p">),</span> <span class="n">max_boxes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">score_threshold</span><span class="o">=</span><span class="mf">.6</span><span class="p">,</span> <span class="n">iou_threshold</span><span class="o">=</span><span class="mf">.5</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">    Converts the output of YOLO encoding (a lot of boxes) to your predicted boxes along with their scores, box coordinates and classes.</span>
<span class="sd">    </span>
<span class="sd">    Arguments:</span>
<span class="sd">    yolo_outputs -- output of the encoding model (for image_shape of (608, 608, 3)), contains 4 tensors:</span>
<span class="sd">                    box_xy: tensor of shape (None, 19, 19, 5, 2)</span>
<span class="sd">                    box_wh: tensor of shape (None, 19, 19, 5, 2)</span>
<span class="sd">                    box_confidence: tensor of shape (None, 19, 19, 5, 1)</span>
<span class="sd">                    box_class_probs: tensor of shape (None, 19, 19, 5, 80)</span>
<span class="sd">    image_shape -- tensor of shape (2,) containing the input shape, in this notebook we use (608., 608.) (has to be float32 dtype)</span>
<span class="sd">    max_boxes -- integer, maximum number of predicted boxes you'd like</span>
<span class="sd">    score_threshold -- real value, if [ highest class probability score &lt; threshold], then get rid of the corresponding box</span>
<span class="sd">    iou_threshold -- real value, "intersection over union" threshold used for NMS filtering</span>
<span class="sd">    </span>
<span class="sd">    Returns:</span>
<span class="sd">    scores -- tensor of shape (None, ), predicted score for each box</span>
<span class="sd">    boxes -- tensor of shape (None, 4), predicted box coordinates</span>
<span class="sd">    classes -- tensor of shape (None,), predicted class for each box</span>
<span class="sd">    """</span>
    
    <span class="c1">### START CODE HERE</span>
    <span class="c1"># Retrieve outputs of the YOLO model (≈1 line)</span>
    <span class="n">box_xy</span><span class="p">,</span> <span class="n">box_wh</span><span class="p">,</span> <span class="n">box_confidence</span><span class="p">,</span> <span class="n">box_class_probs</span> <span class="o">=</span> <span class="n">yolo_outputs</span>
    
    <span class="c1"># Convert boxes to be ready for filtering functions (convert boxes box_xy and box_wh to corner coordinates)</span>
    <span class="n">boxes</span> <span class="o">=</span> <span class="n">yolo_boxes_to_corners</span><span class="p">(</span><span class="n">box_xy</span><span class="p">,</span> <span class="n">box_wh</span><span class="p">)</span>
    
    <span class="c1"># Use one of the functions you've implemented to perform Score-filtering with a threshold of score_threshold (≈1 line)</span>
    <span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span> <span class="o">=</span> <span class="n">yolo_filter_boxes</span><span class="p">(</span><span class="n">boxes</span><span class="p">,</span> <span class="n">box_confidence</span><span class="p">,</span> <span class="n">box_class_probs</span><span class="p">,</span> <span class="n">score_threshold</span><span class="p">)</span>
    
    <span class="c1"># Scale boxes back to original image shape.</span>
    <span class="n">boxes</span> <span class="o">=</span> <span class="n">scale_boxes</span><span class="p">(</span><span class="n">boxes</span><span class="p">,</span> <span class="n">image_shape</span><span class="p">)</span>
    
    <span class="c1"># Use one of the functions you've implemented to perform Non-max suppression with </span>
    <span class="c1"># maximum number of boxes set to max_boxes and a threshold of iou_threshold (≈1 line)</span>
    <span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span> <span class="o">=</span> <span class="n">yolo_non_max_suppression</span><span class="p">(</span><span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span><span class="p">,</span> <span class="n">max_boxes</span><span class="p">,</span> <span class="n">iou_threshold</span><span class="p">)</span>
    <span class="c1">### END CODE HERE</span>
    
    <span class="k">return</span> <span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[28]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># BEGIN UNIT TEST</span>
<span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">set_seed</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="n">yolo_outputs</span> <span class="o">=</span> <span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">([</span><span class="mi">19</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">2</span><span class="p">],</span> <span class="n">mean</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">stddev</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span> <span class="o">=</span> <span class="mi">1</span><span class="p">),</span>
                <span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">([</span><span class="mi">19</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">2</span><span class="p">],</span> <span class="n">mean</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">stddev</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span> <span class="o">=</span> <span class="mi">1</span><span class="p">),</span>
                <span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">([</span><span class="mi">19</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">mean</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">stddev</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span> <span class="o">=</span> <span class="mi">1</span><span class="p">),</span>
                <span class="n">tf</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">([</span><span class="mi">19</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">80</span><span class="p">],</span> <span class="n">mean</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">stddev</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span> <span class="o">=</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">scores</span><span class="p">,</span> <span class="n">boxes</span><span class="p">,</span> <span class="n">classes</span> <span class="o">=</span> <span class="n">yolo_eval</span><span class="p">(</span><span class="n">yolo_outputs</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"scores[2] = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">scores</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"boxes[2] = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">boxes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"classes[2] = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">classes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"scores.shape = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">scores</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"boxes.shape = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">boxes</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"classes.shape = "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">classes</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>

<span class="k">assert</span> <span class="nb">type</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span> <span class="o">==</span> <span class="n">EagerTensor</span><span class="p">,</span> <span class="s2">"Use tensoflow functions"</span>
<span class="k">assert</span> <span class="nb">type</span><span class="p">(</span><span class="n">boxes</span><span class="p">)</span> <span class="o">==</span> <span class="n">EagerTensor</span><span class="p">,</span> <span class="s2">"Use tensoflow functions"</span>
<span class="k">assert</span> <span class="nb">type</span><span class="p">(</span><span class="n">classes</span><span class="p">)</span> <span class="o">==</span> <span class="n">EagerTensor</span><span class="p">,</span> <span class="s2">"Use tensoflow functions"</span>

<span class="k">assert</span> <span class="n">scores</span><span class="o">.</span><span class="n">shape</span> <span class="o">==</span> <span class="p">(</span><span class="mi">10</span><span class="p">,),</span> <span class="s2">"Wrong shape"</span>
<span class="k">assert</span> <span class="n">boxes</span><span class="o">.</span><span class="n">shape</span> <span class="o">==</span> <span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">4</span><span class="p">),</span> <span class="s2">"Wrong shape"</span>
<span class="k">assert</span> <span class="n">classes</span><span class="o">.</span><span class="n">shape</span> <span class="o">==</span> <span class="p">(</span><span class="mi">10</span><span class="p">,),</span> <span class="s2">"Wrong shape"</span>
    
<span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">scores</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">(),</span> <span class="mf">171.60194</span><span class="p">),</span> <span class="s2">"Wrong value on scores"</span>
<span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">allclose</span><span class="p">(</span><span class="n">boxes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">(),</span> <span class="p">[</span><span class="o">-</span><span class="mf">1240.3483</span><span class="p">,</span> <span class="o">-</span><span class="mf">3212.5881</span><span class="p">,</span> <span class="o">-</span><span class="mf">645.78</span><span class="p">,</span> <span class="mf">2024.3052</span><span class="p">]),</span> <span class="s2">"Wrong value on boxes"</span>
<span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">classes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">(),</span> <span class="mi">16</span><span class="p">),</span> <span class="s2">"Wrong value on classes"</span>
    
<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\033</span><span class="s2">[92m All tests passed!"</span><span class="p">)</span>
<span class="c1"># END UNIT TEST</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>scores[2] = 171.60194
boxes[2] = [-1240.3483 -3212.5881  -645.78    2024.3052]
classes[2] = 16
scores.shape = (10,)
boxes.shape = (10, 4)
classes.shape = (10,)
<span class="ansi-green-intense-fg"> All tests passed!
</span></pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Expected Output</strong>:</p>
<table>
    <tr>
        <td>
            <b>scores[2]</b>
        </td>
        <td>
           171.60194
        </td>
    </tr>
    <tr>
        <td>
            <b>boxes[2]</b>
        </td>
        <td>
           [-1240.3483 -3212.5881  -645.78    2024.3052]
        </td>
    </tr>
    <tr>
        <td>
            <b>classes[2]</b>
        </td>
        <td>
           16
        </td>
    </tr> 
        <tr>
        <td>
            <b>scores.shape</b>
        </td>
        <td>
           (10,)
        </td>
    </tr>
    <tr>
        <td>
            <b>boxes.shape</b>
        </td>
        <td>
           (10, 4)
        </td>
    </tr>
    <tr>
        <td>
            <b>classes.shape</b>
        </td>
        <td>
           (10,)
        </td>
    </tr>

</table>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='3'></a></p>
<h2 id="3---Test-YOLO-Pre-trained-Model-on-Images">3 - Test YOLO Pre-trained Model on Images<a class="anchor-link" href="#3---Test-YOLO-Pre-trained-Model-on-Images">&#182;</a></h2><p>In this section, you are going to use a pre-trained model and test it on the car detection dataset.</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='3-1'></a></p>
<h3 id="3.1---Defining-Classes,-Anchors-and-Image-Shape">3.1 - Defining Classes, Anchors and Image Shape<a class="anchor-link" href="#3.1---Defining-Classes,-Anchors-and-Image-Shape">&#182;</a></h3><p>You're trying to detect 80 classes, and are using 5 anchor boxes. The information on the 80 classes and 5 boxes is gathered in two files: "coco_classes.txt" and "yolo_anchors.txt". You'll read class names and anchors from text files. The car detection dataset has 720x1280 images, which are pre-processed into 608x608 images.</p>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[29]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">class_names</span> <span class="o">=</span> <span class="n">read_classes</span><span class="p">(</span><span class="s2">"model_data/coco_classes.txt"</span><span class="p">)</span>
<span class="n">anchors</span> <span class="o">=</span> <span class="n">read_anchors</span><span class="p">(</span><span class="s2">"model_data/yolo_anchors.txt"</span><span class="p">)</span>
<span class="n">model_image_size</span> <span class="o">=</span> <span class="p">(</span><span class="mi">608</span><span class="p">,</span> <span class="mi">608</span><span class="p">)</span> <span class="c1"># Same as yolo_model input layer size</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='3-2'></a></p>
<h3 id="3.2---Loading-a-Pre-trained-Model">3.2 - Loading a Pre-trained Model<a class="anchor-link" href="#3.2---Loading-a-Pre-trained-Model">&#182;</a></h3><p>Training a YOLO model takes a very long time and requires a fairly large dataset of labelled bounding boxes for a large range of target classes. You are going to load an existing pre-trained Keras YOLO model stored in "yolo.h5". These weights come from the official YOLO website, and were converted using a function written by Allan Zelener. References are at the end of this notebook. Technically, these are the parameters from the "YOLOv2" model, but are simply referred to as "YOLO" in this notebook.</p>
<p>Run the cell below to load the model from this file.</p>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[30]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">yolo_model</span> <span class="o">=</span> <span class="n">load_model</span><span class="p">(</span><span class="s2">"model_data/"</span><span class="p">,</span> <span class="nb">compile</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>This loads the weights of a trained YOLO model. Here's a summary of the layers your model contains:</p>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[31]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">yolo_model</span><span class="o">.</span><span class="n">summary</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Model: &#34;functional_1&#34;
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            [(None, 608, 608, 3) 0                                            
__________________________________________________________________________________________________
conv2d (Conv2D)                 (None, 608, 608, 32) 864         input_1[0][0]                    
__________________________________________________________________________________________________
batch_normalization (BatchNorma (None, 608, 608, 32) 128         conv2d[0][0]                     
__________________________________________________________________________________________________
leaky_re_lu (LeakyReLU)         (None, 608, 608, 32) 0           batch_normalization[0][0]        
__________________________________________________________________________________________________
max_pooling2d (MaxPooling2D)    (None, 304, 304, 32) 0           leaky_re_lu[0][0]                
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 304, 304, 64) 18432       max_pooling2d[0][0]              
__________________________________________________________________________________________________
batch_normalization_1 (BatchNor (None, 304, 304, 64) 256         conv2d_1[0][0]                   
__________________________________________________________________________________________________
leaky_re_lu_1 (LeakyReLU)       (None, 304, 304, 64) 0           batch_normalization_1[0][0]      
__________________________________________________________________________________________________
max_pooling2d_1 (MaxPooling2D)  (None, 152, 152, 64) 0           leaky_re_lu_1[0][0]              
__________________________________________________________________________________________________
conv2d_2 (Conv2D)               (None, 152, 152, 128 73728       max_pooling2d_1[0][0]            
__________________________________________________________________________________________________
batch_normalization_2 (BatchNor (None, 152, 152, 128 512         conv2d_2[0][0]                   
__________________________________________________________________________________________________
leaky_re_lu_2 (LeakyReLU)       (None, 152, 152, 128 0           batch_normalization_2[0][0]      
__________________________________________________________________________________________________
conv2d_3 (Conv2D)               (None, 152, 152, 64) 8192        leaky_re_lu_2[0][0]              
__________________________________________________________________________________________________
batch_normalization_3 (BatchNor (None, 152, 152, 64) 256         conv2d_3[0][0]                   
__________________________________________________________________________________________________
leaky_re_lu_3 (LeakyReLU)       (None, 152, 152, 64) 0           batch_normalization_3[0][0]      
__________________________________________________________________________________________________
conv2d_4 (Conv2D)               (None, 152, 152, 128 73728       leaky_re_lu_3[0][0]              
__________________________________________________________________________________________________
batch_normalization_4 (BatchNor (None, 152, 152, 128 512         conv2d_4[0][0]                   
__________________________________________________________________________________________________
leaky_re_lu_4 (LeakyReLU)       (None, 152, 152, 128 0           batch_normalization_4[0][0]      
__________________________________________________________________________________________________
max_pooling2d_2 (MaxPooling2D)  (None, 76, 76, 128)  0           leaky_re_lu_4[0][0]              
__________________________________________________________________________________________________
conv2d_5 (Conv2D)               (None, 76, 76, 256)  294912      max_pooling2d_2[0][0]            
__________________________________________________________________________________________________
batch_normalization_5 (BatchNor (None, 76, 76, 256)  1024        conv2d_5[0][0]                   
__________________________________________________________________________________________________
leaky_re_lu_5 (LeakyReLU)       (None, 76, 76, 256)  0           batch_normalization_5[0][0]      
__________________________________________________________________________________________________
conv2d_6 (Conv2D)               (None, 76, 76, 128)  32768       leaky_re_lu_5[0][0]              
__________________________________________________________________________________________________
batch_normalization_6 (BatchNor (None, 76, 76, 128)  512         conv2d_6[0][0]                   
__________________________________________________________________________________________________
leaky_re_lu_6 (LeakyReLU)       (None, 76, 76, 128)  0           batch_normalization_6[0][0]      
__________________________________________________________________________________________________
conv2d_7 (Conv2D)               (None, 76, 76, 256)  294912      leaky_re_lu_6[0][0]              
__________________________________________________________________________________________________
batch_normalization_7 (BatchNor (None, 76, 76, 256)  1024        conv2d_7[0][0]                   
__________________________________________________________________________________________________
leaky_re_lu_7 (LeakyReLU)       (None, 76, 76, 256)  0           batch_normalization_7[0][0]      
__________________________________________________________________________________________________
max_pooling2d_3 (MaxPooling2D)  (None, 38, 38, 256)  0           leaky_re_lu_7[0][0]              
__________________________________________________________________________________________________
conv2d_8 (Conv2D)               (None, 38, 38, 512)  1179648     max_pooling2d_3[0][0]            
__________________________________________________________________________________________________
batch_normalization_8 (BatchNor (None, 38, 38, 512)  2048        conv2d_8[0][0]                   
__________________________________________________________________________________________________
leaky_re_lu_8 (LeakyReLU)       (None, 38, 38, 512)  0           batch_normalization_8[0][0]      
__________________________________________________________________________________________________
conv2d_9 (Conv2D)               (None, 38, 38, 256)  131072      leaky_re_lu_8[0][0]              
__________________________________________________________________________________________________
batch_normalization_9 (BatchNor (None, 38, 38, 256)  1024        conv2d_9[0][0]                   
__________________________________________________________________________________________________
leaky_re_lu_9 (LeakyReLU)       (None, 38, 38, 256)  0           batch_normalization_9[0][0]      
__________________________________________________________________________________________________
conv2d_10 (Conv2D)              (None, 38, 38, 512)  1179648     leaky_re_lu_9[0][0]              
__________________________________________________________________________________________________
batch_normalization_10 (BatchNo (None, 38, 38, 512)  2048        conv2d_10[0][0]                  
__________________________________________________________________________________________________
leaky_re_lu_10 (LeakyReLU)      (None, 38, 38, 512)  0           batch_normalization_10[0][0]     
__________________________________________________________________________________________________
conv2d_11 (Conv2D)              (None, 38, 38, 256)  131072      leaky_re_lu_10[0][0]             
__________________________________________________________________________________________________
batch_normalization_11 (BatchNo (None, 38, 38, 256)  1024        conv2d_11[0][0]                  
__________________________________________________________________________________________________
leaky_re_lu_11 (LeakyReLU)      (None, 38, 38, 256)  0           batch_normalization_11[0][0]     
__________________________________________________________________________________________________
conv2d_12 (Conv2D)              (None, 38, 38, 512)  1179648     leaky_re_lu_11[0][0]             
__________________________________________________________________________________________________
batch_normalization_12 (BatchNo (None, 38, 38, 512)  2048        conv2d_12[0][0]                  
__________________________________________________________________________________________________
leaky_re_lu_12 (LeakyReLU)      (None, 38, 38, 512)  0           batch_normalization_12[0][0]     
__________________________________________________________________________________________________
max_pooling2d_4 (MaxPooling2D)  (None, 19, 19, 512)  0           leaky_re_lu_12[0][0]             
__________________________________________________________________________________________________
conv2d_13 (Conv2D)              (None, 19, 19, 1024) 4718592     max_pooling2d_4[0][0]            
__________________________________________________________________________________________________
batch_normalization_13 (BatchNo (None, 19, 19, 1024) 4096        conv2d_13[0][0]                  
__________________________________________________________________________________________________
leaky_re_lu_13 (LeakyReLU)      (None, 19, 19, 1024) 0           batch_normalization_13[0][0]     
__________________________________________________________________________________________________
conv2d_14 (Conv2D)              (None, 19, 19, 512)  524288      leaky_re_lu_13[0][0]             
__________________________________________________________________________________________________
batch_normalization_14 (BatchNo (None, 19, 19, 512)  2048        conv2d_14[0][0]                  
__________________________________________________________________________________________________
leaky_re_lu_14 (LeakyReLU)      (None, 19, 19, 512)  0           batch_normalization_14[0][0]     
__________________________________________________________________________________________________
conv2d_15 (Conv2D)              (None, 19, 19, 1024) 4718592     leaky_re_lu_14[0][0]             
__________________________________________________________________________________________________
batch_normalization_15 (BatchNo (None, 19, 19, 1024) 4096        conv2d_15[0][0]                  
__________________________________________________________________________________________________
leaky_re_lu_15 (LeakyReLU)      (None, 19, 19, 1024) 0           batch_normalization_15[0][0]     
__________________________________________________________________________________________________
conv2d_16 (Conv2D)              (None, 19, 19, 512)  524288      leaky_re_lu_15[0][0]             
__________________________________________________________________________________________________
batch_normalization_16 (BatchNo (None, 19, 19, 512)  2048        conv2d_16[0][0]                  
__________________________________________________________________________________________________
leaky_re_lu_16 (LeakyReLU)      (None, 19, 19, 512)  0           batch_normalization_16[0][0]     
__________________________________________________________________________________________________
conv2d_17 (Conv2D)              (None, 19, 19, 1024) 4718592     leaky_re_lu_16[0][0]             
__________________________________________________________________________________________________
batch_normalization_17 (BatchNo (None, 19, 19, 1024) 4096        conv2d_17[0][0]                  
__________________________________________________________________________________________________
leaky_re_lu_17 (LeakyReLU)      (None, 19, 19, 1024) 0           batch_normalization_17[0][0]     
__________________________________________________________________________________________________
conv2d_18 (Conv2D)              (None, 19, 19, 1024) 9437184     leaky_re_lu_17[0][0]             
__________________________________________________________________________________________________
batch_normalization_18 (BatchNo (None, 19, 19, 1024) 4096        conv2d_18[0][0]                  
__________________________________________________________________________________________________
conv2d_20 (Conv2D)              (None, 38, 38, 64)   32768       leaky_re_lu_12[0][0]             
__________________________________________________________________________________________________
leaky_re_lu_18 (LeakyReLU)      (None, 19, 19, 1024) 0           batch_normalization_18[0][0]     
__________________________________________________________________________________________________
batch_normalization_20 (BatchNo (None, 38, 38, 64)   256         conv2d_20[0][0]                  
__________________________________________________________________________________________________
conv2d_19 (Conv2D)              (None, 19, 19, 1024) 9437184     leaky_re_lu_18[0][0]             
__________________________________________________________________________________________________
leaky_re_lu_20 (LeakyReLU)      (None, 38, 38, 64)   0           batch_normalization_20[0][0]     
__________________________________________________________________________________________________
batch_normalization_19 (BatchNo (None, 19, 19, 1024) 4096        conv2d_19[0][0]                  
__________________________________________________________________________________________________
space_to_depth_x2 (Lambda)      (None, 19, 19, 256)  0           leaky_re_lu_20[0][0]             
__________________________________________________________________________________________________
leaky_re_lu_19 (LeakyReLU)      (None, 19, 19, 1024) 0           batch_normalization_19[0][0]     
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 19, 19, 1280) 0           space_to_depth_x2[0][0]          
                                                                 leaky_re_lu_19[0][0]             
__________________________________________________________________________________________________
conv2d_21 (Conv2D)              (None, 19, 19, 1024) 11796480    concatenate[0][0]                
__________________________________________________________________________________________________
batch_normalization_21 (BatchNo (None, 19, 19, 1024) 4096        conv2d_21[0][0]                  
__________________________________________________________________________________________________
leaky_re_lu_21 (LeakyReLU)      (None, 19, 19, 1024) 0           batch_normalization_21[0][0]     
__________________________________________________________________________________________________
conv2d_22 (Conv2D)              (None, 19, 19, 425)  435625      leaky_re_lu_21[0][0]             
==================================================================================================
Total params: 50,983,561
Trainable params: 50,962,889
Non-trainable params: 20,672
__________________________________________________________________________________________________
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Note</strong>: On some computers, you may see a warning message from Keras. Don't worry about it if you do -- this is fine!</p>
<p><strong>Reminder</strong>: This model converts a preprocessed batch of input images (shape: (m, 608, 608, 3)) into a tensor of shape (m, 19, 19, 5, 85) as explained in Figure (2).</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='3-3'></a></p>
<h3 id="3.3---Convert-Output-of-the-Model-to-Usable-Bounding-Box-Tensors">3.3 - Convert Output of the Model to Usable Bounding Box Tensors<a class="anchor-link" href="#3.3---Convert-Output-of-the-Model-to-Usable-Bounding-Box-Tensors">&#182;</a></h3><p>The output of <code>yolo_model</code> is a (m, 19, 19, 5, 85) tensor that needs to pass through non-trivial processing and conversion. You will need to call <code>yolo_head</code> to format the encoding of the model you got from <code>yolo_model</code> into something decipherable:</p>
<p>yolo_model_outputs = yolo_model(image_data) 
yolo_outputs = yolo_head(yolo_model_outputs, anchors, len(class_names))
The variable <code>yolo_outputs</code> will be defined as a set of 4 tensors that you can then use as input by your yolo_eval function. If you are curious about how yolo_head is implemented, you can find the function definition in the file <code>keras_yolo.py</code>. The file is also located in your workspace in this path: <code>yad2k/models/keras_yolo.py</code>.</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='3-4'></a></p>
<h3 id="3.4---Filtering-Boxes">3.4 - Filtering Boxes<a class="anchor-link" href="#3.4---Filtering-Boxes">&#182;</a></h3><p><code>yolo_outputs</code> gave you all the predicted boxes of <code>yolo_model</code> in the correct format. To perform filtering and select only the best boxes, you will call <code>yolo_eval</code>, which you had previously implemented, to do so:</p>

<pre><code>out_scores, out_boxes, out_classes = yolo_eval(yolo_outputs, [image.size[1],  image.size[0]], 10, 0.3, 0.5)</code></pre>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='3-5'></a></p>
<h3 id="3.5---Run-the-YOLO-on-an-Image">3.5 - Run the YOLO on an Image<a class="anchor-link" href="#3.5---Run-the-YOLO-on-an-Image">&#182;</a></h3><p>Let the fun begin! You will create a graph that can be summarized as follows:</p>
<p><code>yolo_model.input</code> is given to <code>yolo_model</code>. The model is used to compute the output <code>yolo_model.output</code>
<code>yolo_model.output</code> is processed by <code>yolo_head</code>. It gives you <code>yolo_outputs</code>
<code>yolo_outputs</code> goes through a filtering function, <code>yolo_eval</code>. It outputs your predictions: <code>out_scores</code>, <code>out_boxes</code>, <code>out_classes</code>.</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Now, we have implemented for you the <code>predict(image_file)</code> function, which runs the graph to test YOLO on an image to compute <code>out_scores</code>, <code>out_boxes</code>, <code>out_classes</code>.</p>
<p>The code below also uses the following function:</p>

<pre><code>image, image_data = preprocess_image("images/" + image_file, model_image_size = (608, 608))
</code></pre>
<p>which opens the image file and scales, reshapes and normalizes the image. It returns the outputs:</p>

<pre><code>image: a python (PIL) representation of your image used for drawing boxes. You won't need to use it.
image_data: a numpy-array representing the image. This will be the input to the CNN.</code></pre>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[32]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">predict</span><span class="p">(</span><span class="n">image_file</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">    Runs the graph to predict boxes for "image_file". Prints and plots the predictions.</span>
<span class="sd">    </span>
<span class="sd">    Arguments:</span>
<span class="sd">    image_file -- name of an image stored in the "images" folder.</span>
<span class="sd">    </span>
<span class="sd">    Returns:</span>
<span class="sd">    out_scores -- tensor of shape (None, ), scores of the predicted boxes</span>
<span class="sd">    out_boxes -- tensor of shape (None, 4), coordinates of the predicted boxes</span>
<span class="sd">    out_classes -- tensor of shape (None, ), class index of the predicted boxes</span>
<span class="sd">    </span>
<span class="sd">    Note: "None" actually represents the number of predicted boxes, it varies between 0 and max_boxes. </span>
<span class="sd">    """</span>

    <span class="c1"># Preprocess your image</span>
    <span class="n">image</span><span class="p">,</span> <span class="n">image_data</span> <span class="o">=</span> <span class="n">preprocess_image</span><span class="p">(</span><span class="s2">"images/"</span> <span class="o">+</span> <span class="n">image_file</span><span class="p">,</span> <span class="n">model_image_size</span> <span class="o">=</span> <span class="p">(</span><span class="mi">608</span><span class="p">,</span> <span class="mi">608</span><span class="p">))</span>
    
    <span class="n">yolo_model_outputs</span> <span class="o">=</span> <span class="n">yolo_model</span><span class="p">(</span><span class="n">image_data</span><span class="p">)</span>
    <span class="n">yolo_outputs</span> <span class="o">=</span> <span class="n">yolo_head</span><span class="p">(</span><span class="n">yolo_model_outputs</span><span class="p">,</span> <span class="n">anchors</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">class_names</span><span class="p">))</span>
    
    <span class="n">out_scores</span><span class="p">,</span> <span class="n">out_boxes</span><span class="p">,</span> <span class="n">out_classes</span> <span class="o">=</span> <span class="n">yolo_eval</span><span class="p">(</span><span class="n">yolo_outputs</span><span class="p">,</span> <span class="p">[</span><span class="n">image</span><span class="o">.</span><span class="n">size</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>  <span class="n">image</span><span class="o">.</span><span class="n">size</span><span class="p">[</span><span class="mi">0</span><span class="p">]],</span> <span class="mi">10</span><span class="p">,</span> <span class="mf">0.3</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">)</span>

    <span class="c1"># Print predictions info</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">'Found </span><span class="si">{}</span><span class="s1"> boxes for </span><span class="si">{}</span><span class="s1">'</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">out_boxes</span><span class="p">),</span> <span class="s2">"images/"</span> <span class="o">+</span> <span class="n">image_file</span><span class="p">))</span>
    <span class="c1"># Generate colors for drawing bounding boxes.</span>
    <span class="n">colors</span> <span class="o">=</span> <span class="n">get_colors_for_classes</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">class_names</span><span class="p">))</span>
    <span class="c1"># Draw bounding boxes on the image file</span>
    <span class="c1">#draw_boxes2(image, out_scores, out_boxes, out_classes, class_names, colors, image_shape)</span>
    <span class="n">draw_boxes</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">out_boxes</span><span class="p">,</span> <span class="n">out_classes</span><span class="p">,</span> <span class="n">class_names</span><span class="p">,</span> <span class="n">out_scores</span><span class="p">)</span>
    <span class="c1"># Save the predicted bounding box on the image</span>
    <span class="n">image</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">"out"</span><span class="p">,</span> <span class="n">image_file</span><span class="p">),</span> <span class="n">quality</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
    <span class="c1"># Display the results in the notebook</span>
    <span class="n">output_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">"out"</span><span class="p">,</span> <span class="n">image_file</span><span class="p">))</span>
    <span class="n">imshow</span><span class="p">(</span><span class="n">output_image</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">out_scores</span><span class="p">,</span> <span class="n">out_boxes</span><span class="p">,</span> <span class="n">out_classes</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Run the following cell on the "test.jpg" image to verify that your function is correct.</p>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[33]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">out_scores</span><span class="p">,</span> <span class="n">out_boxes</span><span class="p">,</span> <span class="n">out_classes</span> <span class="o">=</span> <span class="n">predict</span><span class="p">(</span><span class="s2">"test.jpg"</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Found 10 boxes for images/test.jpg
car 0.89 (367, 300) (745, 648)
car 0.80 (761, 282) (942, 412)
car 0.74 (159, 303) (346, 440)
car 0.70 (947, 324) (1280, 705)
bus 0.67 (5, 266) (220, 407)
car 0.66 (706, 279) (786, 350)
car 0.60 (925, 285) (1045, 374)
car 0.44 (336, 296) (378, 335)
car 0.37 (965, 273) (1022, 292)
traffic light 0.36 (681, 195) (692, 214)
</pre>
</div>
</div>

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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
"
class="
jp-needs-light-background
"
>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Expected Output</strong>:</p>
<table>
    <tr>
        <td>
            <b>Found 10 boxes for images/test.jpg</b>
        </td>
    </tr>
    <tr>
        <td>
            <b>car</b>
        </td>
        <td>
           0.89 (367, 300) (745, 648)
        </td>
    </tr>
    <tr>
        <td>
            <b>car</b>
        </td>
        <td>
           0.80 (761, 282) (942, 412)
        </td>
    </tr>
    <tr>
        <td>
            <b>car</b>
        </td>
        <td>
           0.74 (159, 303) (346, 440)
        </td>
    </tr>
    <tr>
        <td>
            <b>car</b>
        </td>
        <td>
          0.70 (947, 324) (1280, 705)
        </td>
    </tr>
    <tr>
        <td>
            <b>bus</b>
        </td>
        <td>
           0.67 (5, 266) (220, 407)
        </td>
    </tr>
    <tr>
        <td>
            <b>car</b>
        </td>
        <td>
           0.66 (706, 279) (786, 350)
        </td>
    </tr>
    <tr>
        <td>
            <b>car</b>
        </td>
        <td>
           0.60 (925, 285) (1045, 374)
        </td>
    </tr>
        <tr>
        <td>
            <b>car</b>
        </td>
        <td>
           0.44 (336, 296) (378, 335)
        </td>
    </tr>
    <tr>
        <td>
            <b>car</b>
        </td>
        <td>
           0.37 (965, 273) (1022, 292)
        </td>
    </tr>
    <tr>
        <td>
            <b>traffic light</b>
        </td>
        <td>
           00.36 (681, 195) (692, 214)
        </td>
    </tr>
</table>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>The model you've just run is actually able to detect 80 different classes listed in "coco_classes.txt". To test the model on your own images:</p>

<pre><code>1. Click on "File" in the upper bar of this notebook, then click "Open" to go on your Coursera Hub.
2. Add your image to this Jupyter Notebook's directory, in the "images" folder
3. Write your image's name in the cell above code
4. Run the code and see the output of the algorithm!

</code></pre>
<p>If you were to run your session in a for loop over all your images. Here's what you would get:</p>
<caption><center> Predictions of the YOLO model on pictures taken from a camera while driving around the Silicon Valley <br> Thanks to <a href="https://www.drive.ai/">drive.ai</a> for providing this dataset! </center></caption>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='4'></a></p>
<h2 id="4---Summary-for-YOLO">4 - Summary for YOLO<a class="anchor-link" href="#4---Summary-for-YOLO">&#182;</a></h2><ul>
<li>Input image (608, 608, 3)</li>
<li>The input image goes through a CNN, resulting in a (19,19,5,85) dimensional output. </li>
<li>After flattening the last two dimensions, the output is a volume of shape (19, 19, 425):<ul>
<li>Each cell in a 19x19 grid over the input image gives 425 numbers. </li>
<li>425 = 5 x 85 because each cell contains predictions for 5 boxes, corresponding to 5 anchor boxes, as seen in lecture. </li>
<li>85 = 5 + 80 where 5 is because $(p_c, b_x, b_y, b_h, b_w)$ has 5 numbers, and 80 is the number of classes we'd like to detect</li>
</ul>
</li>
<li>You then select only few boxes based on:<ul>
<li>Score-thresholding: throw away boxes that have detected a class with a score less than the threshold</li>
<li>Non-max suppression: Compute the Intersection over Union and avoid selecting overlapping boxes</li>
</ul>
</li>
<li>This gives you YOLO's final output. </li>
</ul>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><font color='blue'></p>
<p><strong>What you should remember</strong>:</p>
<ul>
<li>YOLO is a state-of-the-art object detection model that is fast and accurate</li>
<li>It runs an input image through a CNN, which outputs a 19x19x5x85 dimensional volume. </li>
<li>The encoding can be seen as a grid where each of the 19x19 cells contains information about 5 boxes.</li>
<li>You filter through all the boxes using non-max suppression. Specifically: <ul>
<li>Score thresholding on the probability of detecting a class to keep only accurate (high probability) boxes</li>
<li>Intersection over Union (IoU) thresholding to eliminate overlapping boxes</li>
</ul>
</li>
<li>Because training a YOLO model from randomly initialized weights is non-trivial and requires a large dataset as well as lot of computation, previously trained model parameters were used in this exercise. If you wish, you can also try fine-tuning the YOLO model with your own dataset, though this would be a fairly non-trivial exercise. </li>
</ul>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Congratulations!</strong> You've come to the end of this assignment.</p>
<p>Here's a quick recap of all you've accomplished.</p>
<p>You've:</p>
<ul>
<li>Detected objects in a car detection dataset</li>
<li>Implemented non-max suppression to achieve better accuracy</li>
<li>Implemented intersection over union as a function of NMS</li>
<li>Created usable bounding box tensors from the model's predictions</li>
</ul>
<p>Amazing work! If you'd like to know more about the origins of these ideas, spend some time on the papers referenced below.</p>

</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><a name='5'></a></p>
<h2 id="5---References">5 - References<a class="anchor-link" href="#5---References">&#182;</a></h2><p>The ideas presented in this notebook came primarily from the two YOLO papers. The implementation here also took significant inspiration and used many components from Allan Zelener's GitHub repository. The pre-trained weights used in this exercise came from the official YOLO website.</p>
<ul>
<li>Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi - <a href="https://arxiv.org/abs/1506.02640">You Only Look Once: Unified, Real-Time Object Detection</a> (2015)</li>
<li>Joseph Redmon, Ali Farhadi - <a href="https://arxiv.org/abs/1612.08242">YOLO9000: Better, Faster, Stronger</a> (2016)</li>
<li>Allan Zelener - <a href="https://github.com/allanzelener/YAD2K">YAD2K: Yet Another Darknet 2 Keras</a></li>
<li>The official YOLO website (<a href="https://pjreddie.com/darknet/yolo/">https://pjreddie.com/darknet/yolo/</a>) </li>
</ul>
<h3 id="Car-detection-dataset">Car detection dataset<a class="anchor-link" href="#Car-detection-dataset">&#182;</a></h3><p><a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />&lt;span xmlns:dct="<a href="http://purl.org/dc/terms/">http://purl.org/dc/terms/</a>" property="dct:title"&gt;The Drive.ai Sample Dataset&lt;/span&gt; (provided by drive.ai) is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. Thanks to Brody Huval, Chih Hu and Rahul Patel for  providing this data.</p>

</div>
</div>
</div>
</div>
</body>







</html>

