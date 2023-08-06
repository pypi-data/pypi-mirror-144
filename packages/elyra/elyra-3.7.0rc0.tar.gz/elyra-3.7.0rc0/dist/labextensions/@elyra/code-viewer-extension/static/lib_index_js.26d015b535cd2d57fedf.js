"use strict";
(self["webpackChunk_elyra_code_viewer_extension"] = self["webpackChunk_elyra_code_viewer_extension"] || []).push([["lib_index_js"],{

/***/ "./lib/CodeViewerWidget.js":
/*!*********************************!*\
  !*** ./lib/CodeViewerWidget.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


/*
 * Copyright 2018-2022 Elyra Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CodeViewerWidget = void 0;
const codeeditor_1 = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor");
const widgets_1 = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
class CodeViewerWidget extends widgets_1.Widget {
    /**
     * Construct a new text viewer widget.
     */
    constructor(options) {
        super();
        this.model = new codeeditor_1.CodeEditor.Model({
            value: options.content,
            mimeType: options.mimeType
        });
        const editorWidget = (this.editorWidget = new codeeditor_1.CodeEditorWrapper({
            factory: options.factory,
            model: this.model
        }));
        this.editor = editorWidget.editor;
        this.editor.setOption('readOnly', true);
        const layout = (this.layout = new widgets_1.StackedLayout());
        layout.addWidget(editorWidget);
    }
}
exports.CodeViewerWidget = CodeViewerWidget;
//# sourceMappingURL=CodeViewerWidget.js.map

/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


/*
 * Copyright 2018-2022 Elyra Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
Object.defineProperty(exports, "__esModule", ({ value: true }));
const apputils_1 = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
const codeeditor_1 = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor");
const ui_components_1 = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
const algorithm_1 = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm");
const CodeViewerWidget_1 = __webpack_require__(/*! ./CodeViewerWidget */ "./lib/CodeViewerWidget.js");
const ELYRA_CODE_VIEWER_NAMESPACE = 'elyra-code-viewer-extension';
/**
 * The command IDs used by the code-viewer plugin.
 */
const CommandIDs = {
    openViewer: 'elyra-code-viewer:open'
};
/**
 * Initialization data for the code-viewer extension.
 */
const extension = {
    id: ELYRA_CODE_VIEWER_NAMESPACE,
    autoStart: true,
    requires: [codeeditor_1.IEditorServices],
    activate: (app, editorServices) => {
        console.log('Elyra - code-viewer extension is activated!');
        const openCodeViewer = (args) => {
            var _a;
            const func = editorServices.factoryService.newDocumentEditor;
            const factory = options => {
                return func(options);
            };
            // Derive mimetype from extension
            let mimetype = args.mimeType;
            if (!mimetype && args.extension) {
                mimetype = editorServices.mimeTypeService.getMimeTypeByFilePath(`temp.${args.extension.replace(/\\.$/, '')}`);
            }
            const widget = new CodeViewerWidget_1.CodeViewerWidget({
                factory,
                content: args.content,
                mimeType: mimetype
            });
            widget.title.label = args.label || 'Code Viewer';
            widget.title.caption = widget.title.label;
            // Get the fileType based on the mimetype to determine the icon
            const fileType = algorithm_1.toArray(app.docRegistry.fileTypes()).find(fileType => {
                return mimetype ? fileType.mimeTypes.includes(mimetype) : undefined;
            });
            widget.title.icon = (_a = fileType === null || fileType === void 0 ? void 0 : fileType.icon) !== null && _a !== void 0 ? _a : ui_components_1.textEditorIcon;
            const main = new apputils_1.MainAreaWidget({ content: widget });
            app.shell.add(main, 'main');
        };
        app.commands.addCommand(CommandIDs.openViewer, {
            execute: (args) => {
                openCodeViewer(args);
            }
        });
    }
};
exports["default"] = extension;
//# sourceMappingURL=index.js.map

/***/ })

}]);
//# sourceMappingURL=lib_index_js.26d015b535cd2d57fedf.js.map