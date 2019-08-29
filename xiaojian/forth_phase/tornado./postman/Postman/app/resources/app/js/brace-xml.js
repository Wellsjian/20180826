webpackJsonp([8],{

/***/ 3698:
/***/ (function(module, exports, __webpack_require__) {

ace.define("ace/mode/xml_highlight_rules",["require","exports","module","ace/lib/oop","ace/mode/text_highlight_rules"], function(acequire, exports, module) {
"use strict";

var oop = acequire("../lib/oop");
var TextHighlightRules = acequire("./text_highlight_rules").TextHighlightRules;

var XmlHighlightRules = function(normalize) {
    var tagRegex = "[_:a-zA-Z\xc0-\uffff][-_:.a-zA-Z0-9\xc0-\uffff]*";

    this.$rules = {
        start : [
            {token : "string.cdata.xml", regex : "<\\!\\[CDATA\\[", next : "cdata"},
            {
                token : ["punctuation.xml-decl.xml", "keyword.xml-decl.xml"],
                regex : "(<\\?)(xml)(?=[\\s])", next : "xml_decl", caseInsensitive: true
            },
            {
                token : ["punctuation.instruction.xml", "keyword.instruction.xml"],
                regex : "(<\\?)(" + tagRegex + ")", next : "processing_instruction"
            },
            {token : "comment.xml", regex : "<\\!--", next : "comment"},
            {
                token : ["xml-pe.doctype.xml", "xml-pe.doctype.xml"],
                regex : "(<\\!)(DOCTYPE)(?=[\\s])", next : "doctype", caseInsensitive: true
            },
            {include : "tag"},
            {token : "text.end-tag-open.xml", regex: "</"},
            {token : "text.tag-open.xml", regex: "<"},
            {include : "reference"},
            {defaultToken : "text.xml"}
        ],

        xml_decl : [{
            token : "entity.other.attribute-name.decl-attribute-name.xml",
            regex : "(?:" + tagRegex + ":)?" + tagRegex + ""
        }, {
            token : "keyword.operator.decl-attribute-equals.xml",
            regex : "="
        }, {
            include: "whitespace"
        }, {
            include: "string"
        }, {
            token : "punctuation.xml-decl.xml",
            regex : "\\?>",
            next : "start"
        }],

        processing_instruction : [
            {token : "punctuation.instruction.xml", regex : "\\?>", next : "start"},
            {defaultToken : "instruction.xml"}
        ],

        doctype : [
            {include : "whitespace"},
            {include : "string"},
            {token : "xml-pe.doctype.xml", regex : ">", next : "start"},
            {token : "xml-pe.xml", regex : "[-_a-zA-Z0-9:]+"},
            {token : "punctuation.int-subset", regex : "\\[", push : "int_subset"}
        ],

        int_subset : [{
            token : "text.xml",
            regex : "\\s+"
        }, {
            token: "punctuation.int-subset.xml",
            regex: "]",
            next: "pop"
        }, {
            token : ["punctuation.markup-decl.xml", "keyword.markup-decl.xml"],
            regex : "(<\\!)(" + tagRegex + ")",
            push : [{
                token : "text",
                regex : "\\s+"
            },
            {
                token : "punctuation.markup-decl.xml",
                regex : ">",
                next : "pop"
            },
            {include : "string"}]
        }],

        cdata : [
            {token : "string.cdata.xml", regex : "\\]\\]>", next : "start"},
            {token : "text.xml", regex : "\\s+"},
            {token : "text.xml", regex : "(?:[^\\]]|\\](?!\\]>))+"}
        ],

        comment : [
            {token : "comment.xml", regex : "-->", next : "start"},
            {defaultToken : "comment.xml"}
        ],

        reference : [{
            token : "constant.language.escape.reference.xml",
            regex : "(?:&#[0-9]+;)|(?:&#x[0-9a-fA-F]+;)|(?:&[a-zA-Z0-9_:\\.-]+;)"
        }],

        attr_reference : [{
            token : "constant.language.escape.reference.attribute-value.xml",
            regex : "(?:&#[0-9]+;)|(?:&#x[0-9a-fA-F]+;)|(?:&[a-zA-Z0-9_:\\.-]+;)"
        }],

        tag : [{
            token : ["meta.tag.punctuation.tag-open.xml", "meta.tag.punctuation.end-tag-open.xml", "meta.tag.tag-name.xml"],
            regex : "(?:(<)|(</))((?:" + tagRegex + ":)?" + tagRegex + ")",
            next: [
                {include : "attributes"},
                {token : "meta.tag.punctuation.tag-close.xml", regex : "/?>", next : "start"}
            ]
        }],

        tag_whitespace : [
            {token : "text.tag-whitespace.xml", regex : "\\s+"}
        ],
        whitespace : [
            {token : "text.whitespace.xml", regex : "\\s+"}
        ],
        string: [{
            token : "string.xml",
            regex : "'",
            push : [
                {token : "string.xml", regex: "'", next: "pop"},
                {defaultToken : "string.xml"}
            ]
        }, {
            token : "string.xml",
            regex : '"',
            push : [
                {token : "string.xml", regex: '"', next: "pop"},
                {defaultToken : "string.xml"}
            ]
        }],

        attributes: [{
            token : "entity.other.attribute-name.xml",
            regex : "(?:" + tagRegex + ":)?" + tagRegex + ""
        }, {
            token : "keyword.operator.attribute-equals.xml",
            regex : "="
        }, {
            include: "tag_whitespace"
        }, {
            include: "attribute_value"
        }],

        attribute_value: [{
            token : "string.attribute-value.xml",
            regex : "'",
            push : [
                {token : "string.attribute-value.xml", regex: "'", next: "pop"},
                {include : "attr_reference"},
                {defaultToken : "string.attribute-value.xml"}
            ]
        }, {
            token : "string.attribute-value.xml",
            regex : '"',
            push : [
                {token : "string.attribute-value.xml", regex: '"', next: "pop"},
                {include : "attr_reference"},
                {defaultToken : "string.attribute-value.xml"}
            ]
        }]
    };

    if (this.constructor === XmlHighlightRules)
        this.normalizeRules();
};


(function() {

    this.embedTagRules = function(HighlightRules, prefix, tag){
        this.$rules.tag.unshift({
            token : ["meta.tag.punctuation.tag-open.xml", "meta.tag." + tag + ".tag-name.xml"],
            regex : "(<)(" + tag + "(?=\\s|>|$))",
            next: [
                {include : "attributes"},
                {token : "meta.tag.punctuation.tag-close.xml", regex : "/?>", next : prefix + "start"}
            ]
        });

        this.$rules[tag + "-end"] = [
            {include : "attributes"},
            {token : "meta.tag.punctuation.tag-close.xml", regex : "/?>",  next: "start",
                onMatch : function(value, currentState, stack) {
                    stack.splice(0);
                    return this.token;
            }}
        ]

        this.embedRules(HighlightRules, prefix, [{
            token: ["meta.tag.punctuation.end-tag-open.xml", "meta.tag." + tag + ".tag-name.xml"],
            regex : "(</)(" + tag + "(?=\\s|>|$))",
            next: tag + "-end"
        }, {
            token: "string.cdata.xml",
            regex : "<\\!\\[CDATA\\["
        }, {
            token: "string.cdata.xml",
            regex : "\\]\\]>"
        }]);
    };

}).call(TextHighlightRules.prototype);

oop.inherits(XmlHighlightRules, TextHighlightRules);

exports.XmlHighlightRules = XmlHighlightRules;
});

ace.define("ace/mode/behaviour/xml",["require","exports","module","ace/lib/oop","ace/mode/behaviour","ace/token_iterator","ace/lib/lang"], function(acequire, exports, module) {
"use strict";

var oop = acequire("../../lib/oop");
var Behaviour = acequire("../behaviour").Behaviour;
var TokenIterator = acequire("../../token_iterator").TokenIterator;
var lang = acequire("../../lib/lang");

function is(token, type) {
    return token.type.lastIndexOf(type + ".xml") > -1;
}

var XmlBehaviour = function () {

    this.add("string_dquotes", "insertion", function (state, action, editor, session, text) {
        if (text == '"' || text == "'") {
            var quote = text;
            var selected = session.doc.getTextRange(editor.getSelectionRange());
            if (selected !== "" && selected !== "'" && selected != '"' && editor.getWrapBehavioursEnabled()) {
                return {
                    text: quote + selected + quote,
                    selection: false
                };
            }

            var cursor = editor.getCursorPosition();
            var line = session.doc.getLine(cursor.row);
            var rightChar = line.substring(cursor.column, cursor.column + 1);
            var iterator = new TokenIterator(session, cursor.row, cursor.column);
            var token = iterator.getCurrentToken();

            if (rightChar == quote && (is(token, "attribute-value") || is(token, "string"))) {
                return {
                    text: "",
                    selection: [1, 1]
                };
            }

            if (!token)
                token = iterator.stepBackward();

            if (!token)
                return;

            while (is(token, "tag-whitespace") || is(token, "whitespace")) {
                token = iterator.stepBackward();
            }
            var rightSpace = !rightChar || rightChar.match(/\s/);
            if (is(token, "attribute-equals") && (rightSpace || rightChar == '>') || (is(token, "decl-attribute-equals") && (rightSpace || rightChar == '?'))) {
                return {
                    text: quote + quote,
                    selection: [1, 1]
                };
            }
        }
    });

    this.add("string_dquotes", "deletion", function(state, action, editor, session, range) {
        var selected = session.doc.getTextRange(range);
        if (!range.isMultiLine() && (selected == '"' || selected == "'")) {
            var line = session.doc.getLine(range.start.row);
            var rightChar = line.substring(range.start.column + 1, range.start.column + 2);
            if (rightChar == selected) {
                range.end.column++;
                return range;
            }
        }
    });

    this.add("autoclosing", "insertion", function (state, action, editor, session, text) {
        if (text == '>') {
            var position = editor.getSelectionRange().start;
            var iterator = new TokenIterator(session, position.row, position.column);
            var token = iterator.getCurrentToken() || iterator.stepBackward();
            if (!token || !(is(token, "tag-name") || is(token, "tag-whitespace") || is(token, "attribute-name") || is(token, "attribute-equals") || is(token, "attribute-value")))
                return;
            if (is(token, "reference.attribute-value"))
                return;
            if (is(token, "attribute-value")) {
                var firstChar = token.value.charAt(0);
                if (firstChar == '"' || firstChar == "'") {
                    var lastChar = token.value.charAt(token.value.length - 1);
                    var tokenEnd = iterator.getCurrentTokenColumn() + token.value.length;
                    if (tokenEnd > position.column || tokenEnd == position.column && firstChar != lastChar)
                        return;
                }
            }
            while (!is(token, "tag-name")) {
                token = iterator.stepBackward();
                if (token.value == "<") {
                    token = iterator.stepForward();
                    break;
                }
            }

            var tokenRow = iterator.getCurrentTokenRow();
            var tokenColumn = iterator.getCurrentTokenColumn();
            if (is(iterator.stepBackward(), "end-tag-open"))
                return;

            var element = token.value;
            if (tokenRow == position.row)
                element = element.substring(0, position.column - tokenColumn);

            if (this.voidElements.hasOwnProperty(element.toLowerCase()))
                 return;

            return {
               text: ">" + "</" + element + ">",
               selection: [1, 1]
            };
        }
    });

    this.add("autoindent", "insertion", function (state, action, editor, session, text) {
        if (text == "\n") {
            var cursor = editor.getCursorPosition();
            var line = session.getLine(cursor.row);
            var iterator = new TokenIterator(session, cursor.row, cursor.column);
            var token = iterator.getCurrentToken();

            if (token && token.type.indexOf("tag-close") !== -1) {
                if (token.value == "/>")
                    return;
                while (token && token.type.indexOf("tag-name") === -1) {
                    token = iterator.stepBackward();
                }

                if (!token) {
                    return;
                }

                var tag = token.value;
                var row = iterator.getCurrentTokenRow();
                token = iterator.stepBackward();
                if (!token || token.type.indexOf("end-tag") !== -1) {
                    return;
                }

                if (this.voidElements && !this.voidElements[tag]) {
                    var nextToken = session.getTokenAt(cursor.row, cursor.column+1);
                    var line = session.getLine(row);
                    var nextIndent = this.$getIndent(line);
                    var indent = nextIndent + session.getTabString();

                    if (nextToken && nextToken.value === "</") {
                        return {
                            text: "\n" + indent + "\n" + nextIndent,
                            selection: [1, indent.length, 1, indent.length]
                        };
                    } else {
                        return {
                            text: "\n" + indent
                        };
                    }
                }
            }
        }
    });

};

oop.inherits(XmlBehaviour, Behaviour);

exports.XmlBehaviour = XmlBehaviour;
});

ace.define("ace/mode/folding/xml",["require","exports","module","ace/lib/oop","ace/lib/lang","ace/range","ace/mode/folding/fold_mode","ace/token_iterator"], function(acequire, exports, module) {
"use strict";

var oop = acequire("../../lib/oop");
var lang = acequire("../../lib/lang");
var Range = acequire("../../range").Range;
var BaseFoldMode = acequire("./fold_mode").FoldMode;
var TokenIterator = acequire("../../token_iterator").TokenIterator;

var FoldMode = exports.FoldMode = function(voidElements, optionalEndTags) {
    BaseFoldMode.call(this);
    this.voidElements = voidElements || {};
    this.optionalEndTags = oop.mixin({}, this.voidElements);
    if (optionalEndTags)
        oop.mixin(this.optionalEndTags, optionalEndTags);
    
};
oop.inherits(FoldMode, BaseFoldMode);

var Tag = function() {
    this.tagName = "";
    this.closing = false;
    this.selfClosing = false;
    this.start = {row: 0, column: 0};
    this.end = {row: 0, column: 0};
};

function is(token, type) {
    return token.type.lastIndexOf(type + ".xml") > -1;
}

(function() {

    this.getFoldWidget = function(session, foldStyle, row) {
        var tag = this._getFirstTagInLine(session, row);

        if (!tag)
            return "";

        if (tag.closing || (!tag.tagName && tag.selfClosing))
            return foldStyle == "markbeginend" ? "end" : "";

        if (!tag.tagName || tag.selfClosing || this.voidElements.hasOwnProperty(tag.tagName.toLowerCase()))
            return "";

        if (this._findEndTagInLine(session, row, tag.tagName, tag.end.column))
            return "";

        return "start";
    };
    this._getFirstTagInLine = function(session, row) {
        var tokens = session.getTokens(row);
        var tag = new Tag();

        for (var i = 0; i < tokens.length; i++) {
            var token = tokens[i];
            if (is(token, "tag-open")) {
                tag.end.column = tag.start.column + token.value.length;
                tag.closing = is(token, "end-tag-open");
                token = tokens[++i];
                if (!token)
                    return null;
                tag.tagName = token.value;
                tag.end.column += token.value.length;
                for (i++; i < tokens.length; i++) {
                    token = tokens[i];
                    tag.end.column += token.value.length;
                    if (is(token, "tag-close")) {
                        tag.selfClosing = token.value == '/>';
                        break;
                    }
                }
                return tag;
            } else if (is(token, "tag-close")) {
                tag.selfClosing = token.value == '/>';
                return tag;
            }
            tag.start.column += token.value.length;
        }

        return null;
    };

    this._findEndTagInLine = function(session, row, tagName, startColumn) {
        var tokens = session.getTokens(row);
        var column = 0;
        for (var i = 0; i < tokens.length; i++) {
            var token = tokens[i];
            column += token.value.length;
            if (column < startColumn)
                continue;
            if (is(token, "end-tag-open")) {
                token = tokens[i + 1];
                if (token && token.value == tagName)
                    return true;
            }
        }
        return false;
    };
    this._readTagForward = function(iterator) {
        var token = iterator.getCurrentToken();
        if (!token)
            return null;

        var tag = new Tag();
        do {
            if (is(token, "tag-open")) {
                tag.closing = is(token, "end-tag-open");
                tag.start.row = iterator.getCurrentTokenRow();
                tag.start.column = iterator.getCurrentTokenColumn();
            } else if (is(token, "tag-name")) {
                tag.tagName = token.value;
            } else if (is(token, "tag-close")) {
                tag.selfClosing = token.value == "/>";
                tag.end.row = iterator.getCurrentTokenRow();
                tag.end.column = iterator.getCurrentTokenColumn() + token.value.length;
                iterator.stepForward();
                return tag;
            }
        } while(token = iterator.stepForward());

        return null;
    };
    
    this._readTagBackward = function(iterator) {
        var token = iterator.getCurrentToken();
        if (!token)
            return null;

        var tag = new Tag();
        do {
            if (is(token, "tag-open")) {
                tag.closing = is(token, "end-tag-open");
                tag.start.row = iterator.getCurrentTokenRow();
                tag.start.column = iterator.getCurrentTokenColumn();
                iterator.stepBackward();
                return tag;
            } else if (is(token, "tag-name")) {
                tag.tagName = token.value;
            } else if (is(token, "tag-close")) {
                tag.selfClosing = token.value == "/>";
                tag.end.row = iterator.getCurrentTokenRow();
                tag.end.column = iterator.getCurrentTokenColumn() + token.value.length;
            }
        } while(token = iterator.stepBackward());

        return null;
    };
    
    this._pop = function(stack, tag) {
        while (stack.length) {
            
            var top = stack[stack.length-1];
            if (!tag || top.tagName == tag.tagName) {
                return stack.pop();
            }
            else if (this.optionalEndTags.hasOwnProperty(top.tagName)) {
                stack.pop();
                continue;
            } else {
                return null;
            }
        }
    };
    
    this.getFoldWidgetRange = function(session, foldStyle, row) {
        var firstTag = this._getFirstTagInLine(session, row);
        
        if (!firstTag)
            return null;
        
        var isBackward = firstTag.closing || firstTag.selfClosing;
        var stack = [];
        var tag;
        
        if (!isBackward) {
            var iterator = new TokenIterator(session, row, firstTag.start.column);
            var start = {
                row: row,
                column: firstTag.start.column + firstTag.tagName.length + 2
            };
            if (firstTag.start.row == firstTag.end.row)
                start.column = firstTag.end.column;
            while (tag = this._readTagForward(iterator)) {
                if (tag.selfClosing) {
                    if (!stack.length) {
                        tag.start.column += tag.tagName.length + 2;
                        tag.end.column -= 2;
                        return Range.fromPoints(tag.start, tag.end);
                    } else
                        continue;
                }
                
                if (tag.closing) {
                    this._pop(stack, tag);
                    if (stack.length == 0)
                        return Range.fromPoints(start, tag.start);
                }
                else {
                    stack.push(tag);
                }
            }
        }
        else {
            var iterator = new TokenIterator(session, row, firstTag.end.column);
            var end = {
                row: row,
                column: firstTag.start.column
            };
            
            while (tag = this._readTagBackward(iterator)) {
                if (tag.selfClosing) {
                    if (!stack.length) {
                        tag.start.column += tag.tagName.length + 2;
                        tag.end.column -= 2;
                        return Range.fromPoints(tag.start, tag.end);
                    } else
                        continue;
                }
                
                if (!tag.closing) {
                    this._pop(stack, tag);
                    if (stack.length == 0) {
                        tag.start.column += tag.tagName.length + 2;
                        if (tag.start.row == tag.end.row && tag.start.column < tag.end.column)
                            tag.start.column = tag.end.column;
                        return Range.fromPoints(tag.start, end);
                    }
                }
                else {
                    stack.push(tag);
                }
            }
        }
        
    };

}).call(FoldMode.prototype);

});

ace.define("ace/mode/xml",["require","exports","module","ace/lib/oop","ace/lib/lang","ace/mode/text","ace/mode/xml_highlight_rules","ace/mode/behaviour/xml","ace/mode/folding/xml","ace/worker/worker_client"], function(acequire, exports, module) {
"use strict";

var oop = acequire("../lib/oop");
var lang = acequire("../lib/lang");
var TextMode = acequire("./text").Mode;
var XmlHighlightRules = acequire("./xml_highlight_rules").XmlHighlightRules;
var XmlBehaviour = acequire("./behaviour/xml").XmlBehaviour;
var XmlFoldMode = acequire("./folding/xml").FoldMode;
var WorkerClient = acequire("../worker/worker_client").WorkerClient;

var Mode = function() {
   this.HighlightRules = XmlHighlightRules;
   this.$behaviour = new XmlBehaviour();
   this.foldingRules = new XmlFoldMode();
};

oop.inherits(Mode, TextMode);

(function() {

    this.voidElements = lang.arrayToMap([]);

    this.blockComment = {start: "<!--", end: "-->"};

    this.createWorker = function(session) {
        var worker = new WorkerClient(["ace"], __webpack_require__(3850), "Worker");
        worker.attachToDocument(session.getDocument());

        worker.on("error", function(e) {
            session.setAnnotations(e.data);
        });

        worker.on("terminate", function() {
            session.clearAnnotations();
        });

        return worker;
    };
    
    this.$id = "ace/mode/xml";
}).call(Mode.prototype);

exports.Mode = Mode;
});


/***/ }),

/***/ 3850:
/***/ (function(module, exports) {

module.exports.id = 'ace/mode/xml_worker';
module.exports.src = "\"no use strict\";(function(window){function resolveModuleId(id,paths){for(var testPath=id,tail=\"\";testPath;){var alias=paths[testPath];if(\"string\"==typeof alias)return alias+tail;if(alias)return alias.location.replace(/\\/*$/,\"/\")+(tail||alias.main||alias.name);if(alias===!1)return\"\";var i=testPath.lastIndexOf(\"/\");if(-1===i)break;tail=testPath.substr(i)+tail,testPath=testPath.slice(0,i)}return id}if(!(void 0!==window.window&&window.document||window.acequire&&window.define)){window.console||(window.console=function(){var msgs=Array.prototype.slice.call(arguments,0);postMessage({type:\"log\",data:msgs})},window.console.error=window.console.warn=window.console.log=window.console.trace=window.console),window.window=window,window.ace=window,window.onerror=function(message,file,line,col,err){postMessage({type:\"error\",data:{message:message,data:err.data,file:file,line:line,col:col,stack:err.stack}})},window.normalizeModule=function(parentId,moduleName){if(-1!==moduleName.indexOf(\"!\")){var chunks=moduleName.split(\"!\");return window.normalizeModule(parentId,chunks[0])+\"!\"+window.normalizeModule(parentId,chunks[1])}if(\".\"==moduleName.charAt(0)){var base=parentId.split(\"/\").slice(0,-1).join(\"/\");for(moduleName=(base?base+\"/\":\"\")+moduleName;-1!==moduleName.indexOf(\".\")&&previous!=moduleName;){var previous=moduleName;moduleName=moduleName.replace(/^\\.\\//,\"\").replace(/\\/\\.\\//,\"/\").replace(/[^\\/]+\\/\\.\\.\\//,\"\")}}return moduleName},window.acequire=function acequire(parentId,id){if(id||(id=parentId,parentId=null),!id.charAt)throw Error(\"worker.js acequire() accepts only (parentId, id) as arguments\");id=window.normalizeModule(parentId,id);var module=window.acequire.modules[id];if(module)return module.initialized||(module.initialized=!0,module.exports=module.factory().exports),module.exports;if(!window.acequire.tlns)return console.log(\"unable to load \"+id);var path=resolveModuleId(id,window.acequire.tlns);return\".js\"!=path.slice(-3)&&(path+=\".js\"),window.acequire.id=id,window.acequire.modules[id]={},importScripts(path),window.acequire(parentId,id)},window.acequire.modules={},window.acequire.tlns={},window.define=function(id,deps,factory){if(2==arguments.length?(factory=deps,\"string\"!=typeof id&&(deps=id,id=window.acequire.id)):1==arguments.length&&(factory=id,deps=[],id=window.acequire.id),\"function\"!=typeof factory)return window.acequire.modules[id]={exports:factory,initialized:!0},void 0;deps.length||(deps=[\"require\",\"exports\",\"module\"]);var req=function(childId){return window.acequire(id,childId)};window.acequire.modules[id]={exports:{},factory:function(){var module=this,returnExports=factory.apply(this,deps.map(function(dep){switch(dep){case\"require\":return req;case\"exports\":return module.exports;case\"module\":return module;default:return req(dep)}}));return returnExports&&(module.exports=returnExports),module}}},window.define.amd={},acequire.tlns={},window.initBaseUrls=function(topLevelNamespaces){for(var i in topLevelNamespaces)acequire.tlns[i]=topLevelNamespaces[i]},window.initSender=function(){var EventEmitter=window.acequire(\"ace/lib/event_emitter\").EventEmitter,oop=window.acequire(\"ace/lib/oop\"),Sender=function(){};return function(){oop.implement(this,EventEmitter),this.callback=function(data,callbackId){postMessage({type:\"call\",id:callbackId,data:data})},this.emit=function(name,data){postMessage({type:\"event\",name:name,data:data})}}.call(Sender.prototype),new Sender};var main=window.main=null,sender=window.sender=null;window.onmessage=function(e){var msg=e.data;if(msg.event&&sender)sender._signal(msg.event,msg.data);else if(msg.command)if(main[msg.command])main[msg.command].apply(main,msg.args);else{if(!window[msg.command])throw Error(\"Unknown command:\"+msg.command);window[msg.command].apply(window,msg.args)}else if(msg.init){window.initBaseUrls(msg.tlns),acequire(\"ace/lib/es5-shim\"),sender=window.sender=window.initSender();var clazz=acequire(msg.module)[msg.classname];main=window.main=new clazz(sender)}}}})(this),ace.define(\"ace/lib/oop\",[\"require\",\"exports\",\"module\"],function(acequire,exports){\"use strict\";exports.inherits=function(ctor,superCtor){ctor.super_=superCtor,ctor.prototype=Object.create(superCtor.prototype,{constructor:{value:ctor,enumerable:!1,writable:!0,configurable:!0}})},exports.mixin=function(obj,mixin){for(var key in mixin)obj[key]=mixin[key];return obj},exports.implement=function(proto,mixin){exports.mixin(proto,mixin)}}),ace.define(\"ace/lib/lang\",[\"require\",\"exports\",\"module\"],function(acequire,exports){\"use strict\";exports.last=function(a){return a[a.length-1]},exports.stringReverse=function(string){return string.split(\"\").reverse().join(\"\")},exports.stringRepeat=function(string,count){for(var result=\"\";count>0;)1&count&&(result+=string),(count>>=1)&&(string+=string);return result};var trimBeginRegexp=/^\\s\\s*/,trimEndRegexp=/\\s\\s*$/;exports.stringTrimLeft=function(string){return string.replace(trimBeginRegexp,\"\")},exports.stringTrimRight=function(string){return string.replace(trimEndRegexp,\"\")},exports.copyObject=function(obj){var copy={};for(var key in obj)copy[key]=obj[key];return copy},exports.copyArray=function(array){for(var copy=[],i=0,l=array.length;l>i;i++)copy[i]=array[i]&&\"object\"==typeof array[i]?this.copyObject(array[i]):array[i];return copy},exports.deepCopy=function deepCopy(obj){if(\"object\"!=typeof obj||!obj)return obj;var copy;if(Array.isArray(obj)){copy=[];for(var key=0;obj.length>key;key++)copy[key]=deepCopy(obj[key]);return copy}if(\"[object Object]\"!==Object.prototype.toString.call(obj))return obj;copy={};for(var key in obj)copy[key]=deepCopy(obj[key]);return copy},exports.arrayToMap=function(arr){for(var map={},i=0;arr.length>i;i++)map[arr[i]]=1;return map},exports.createMap=function(props){var map=Object.create(null);for(var i in props)map[i]=props[i];return map},exports.arrayRemove=function(array,value){for(var i=0;array.length>=i;i++)value===array[i]&&array.splice(i,1)},exports.escapeRegExp=function(str){return str.replace(/([.*+?^${}()|[\\]\\/\\\\])/g,\"\\\\$1\")},exports.escapeHTML=function(str){return str.replace(/&/g,\"&#38;\").replace(/\"/g,\"&#34;\").replace(/'/g,\"&#39;\").replace(/</g,\"&#60;\")},exports.getMatchOffsets=function(string,regExp){var matches=[];return string.replace(regExp,function(str){matches.push({offset:arguments[arguments.length-2],length:str.length})}),matches},exports.deferredCall=function(fcn){var timer=null,callback=function(){timer=null,fcn()},deferred=function(timeout){return deferred.cancel(),timer=setTimeout(callback,timeout||0),deferred};return deferred.schedule=deferred,deferred.call=function(){return this.cancel(),fcn(),deferred},deferred.cancel=function(){return clearTimeout(timer),timer=null,deferred},deferred.isPending=function(){return timer},deferred},exports.delayedCall=function(fcn,defaultTimeout){var timer=null,callback=function(){timer=null,fcn()},_self=function(timeout){null==timer&&(timer=setTimeout(callback,timeout||defaultTimeout))};return _self.delay=function(timeout){timer&&clearTimeout(timer),timer=setTimeout(callback,timeout||defaultTimeout)},_self.schedule=_self,_self.call=function(){this.cancel(),fcn()},_self.cancel=function(){timer&&clearTimeout(timer),timer=null},_self.isPending=function(){return timer},_self}}),ace.define(\"ace/range\",[\"require\",\"exports\",\"module\"],function(acequire,exports){\"use strict\";var comparePoints=function(p1,p2){return p1.row-p2.row||p1.column-p2.column},Range=function(startRow,startColumn,endRow,endColumn){this.start={row:startRow,column:startColumn},this.end={row:endRow,column:endColumn}};(function(){this.isEqual=function(range){return this.start.row===range.start.row&&this.end.row===range.end.row&&this.start.column===range.start.column&&this.end.column===range.end.column},this.toString=function(){return\"Range: [\"+this.start.row+\"/\"+this.start.column+\"] -> [\"+this.end.row+\"/\"+this.end.column+\"]\"},this.contains=function(row,column){return 0==this.compare(row,column)},this.compareRange=function(range){var cmp,end=range.end,start=range.start;return cmp=this.compare(end.row,end.column),1==cmp?(cmp=this.compare(start.row,start.column),1==cmp?2:0==cmp?1:0):-1==cmp?-2:(cmp=this.compare(start.row,start.column),-1==cmp?-1:1==cmp?42:0)},this.comparePoint=function(p){return this.compare(p.row,p.column)},this.containsRange=function(range){return 0==this.comparePoint(range.start)&&0==this.comparePoint(range.end)},this.intersects=function(range){var cmp=this.compareRange(range);return-1==cmp||0==cmp||1==cmp},this.isEnd=function(row,column){return this.end.row==row&&this.end.column==column},this.isStart=function(row,column){return this.start.row==row&&this.start.column==column},this.setStart=function(row,column){\"object\"==typeof row?(this.start.column=row.column,this.start.row=row.row):(this.start.row=row,this.start.column=column)},this.setEnd=function(row,column){\"object\"==typeof row?(this.end.column=row.column,this.end.row=row.row):(this.end.row=row,this.end.column=column)},this.inside=function(row,column){return 0==this.compare(row,column)?this.isEnd(row,column)||this.isStart(row,column)?!1:!0:!1},this.insideStart=function(row,column){return 0==this.compare(row,column)?this.isEnd(row,column)?!1:!0:!1},this.insideEnd=function(row,column){return 0==this.compare(row,column)?this.isStart(row,column)?!1:!0:!1},this.compare=function(row,column){return this.isMultiLine()||row!==this.start.row?this.start.row>row?-1:row>this.end.row?1:this.start.row===row?column>=this.start.column?0:-1:this.end.row===row?this.end.column>=column?0:1:0:this.start.column>column?-1:column>this.end.column?1:0},this.compareStart=function(row,column){return this.start.row==row&&this.start.column==column?-1:this.compare(row,column)},this.compareEnd=function(row,column){return this.end.row==row&&this.end.column==column?1:this.compare(row,column)},this.compareInside=function(row,column){return this.end.row==row&&this.end.column==column?1:this.start.row==row&&this.start.column==column?-1:this.compare(row,column)},this.clipRows=function(firstRow,lastRow){if(this.end.row>lastRow)var end={row:lastRow+1,column:0};else if(firstRow>this.end.row)var end={row:firstRow,column:0};if(this.start.row>lastRow)var start={row:lastRow+1,column:0};else if(firstRow>this.start.row)var start={row:firstRow,column:0};return Range.fromPoints(start||this.start,end||this.end)},this.extend=function(row,column){var cmp=this.compare(row,column);if(0==cmp)return this;if(-1==cmp)var start={row:row,column:column};else var end={row:row,column:column};return Range.fromPoints(start||this.start,end||this.end)},this.isEmpty=function(){return this.start.row===this.end.row&&this.start.column===this.end.column},this.isMultiLine=function(){return this.start.row!==this.end.row},this.clone=function(){return Range.fromPoints(this.start,this.end)},this.collapseRows=function(){return 0==this.end.column?new Range(this.start.row,0,Math.max(this.start.row,this.end.row-1),0):new Range(this.start.row,0,this.end.row,0)},this.toScreenRange=function(session){var screenPosStart=session.documentToScreenPosition(this.start),screenPosEnd=session.documentToScreenPosition(this.end);return new Range(screenPosStart.row,screenPosStart.column,screenPosEnd.row,screenPosEnd.column)},this.moveBy=function(row,column){this.start.row+=row,this.start.column+=column,this.end.row+=row,this.end.column+=column}}).call(Range.prototype),Range.fromPoints=function(start,end){return new Range(start.row,start.column,end.row,end.column)},Range.comparePoints=comparePoints,Range.comparePoints=function(p1,p2){return p1.row-p2.row||p1.column-p2.column},exports.Range=Range}),ace.define(\"ace/apply_delta\",[\"require\",\"exports\",\"module\"],function(acequire,exports){\"use strict\";exports.applyDelta=function(docLines,delta){var row=delta.start.row,startColumn=delta.start.column,line=docLines[row]||\"\";switch(delta.action){case\"insert\":var lines=delta.lines;if(1===lines.length)docLines[row]=line.substring(0,startColumn)+delta.lines[0]+line.substring(startColumn);else{var args=[row,1].concat(delta.lines);docLines.splice.apply(docLines,args),docLines[row]=line.substring(0,startColumn)+docLines[row],docLines[row+delta.lines.length-1]+=line.substring(startColumn)}break;case\"remove\":var endColumn=delta.end.column,endRow=delta.end.row;row===endRow?docLines[row]=line.substring(0,startColumn)+line.substring(endColumn):docLines.splice(row,endRow-row+1,line.substring(0,startColumn)+docLines[endRow].substring(endColumn))}}}),ace.define(\"ace/lib/event_emitter\",[\"require\",\"exports\",\"module\"],function(acequire,exports){\"use strict\";var EventEmitter={},stopPropagation=function(){this.propagationStopped=!0},preventDefault=function(){this.defaultPrevented=!0};EventEmitter._emit=EventEmitter._dispatchEvent=function(eventName,e){this._eventRegistry||(this._eventRegistry={}),this._defaultHandlers||(this._defaultHandlers={});var listeners=this._eventRegistry[eventName]||[],defaultHandler=this._defaultHandlers[eventName];if(listeners.length||defaultHandler){\"object\"==typeof e&&e||(e={}),e.type||(e.type=eventName),e.stopPropagation||(e.stopPropagation=stopPropagation),e.preventDefault||(e.preventDefault=preventDefault),listeners=listeners.slice();for(var i=0;listeners.length>i&&(listeners[i](e,this),!e.propagationStopped);i++);return defaultHandler&&!e.defaultPrevented?defaultHandler(e,this):void 0}},EventEmitter._signal=function(eventName,e){var listeners=(this._eventRegistry||{})[eventName];if(listeners){listeners=listeners.slice();for(var i=0;listeners.length>i;i++)listeners[i](e,this)}},EventEmitter.once=function(eventName,callback){var _self=this;callback&&this.addEventListener(eventName,function newCallback(){_self.removeEventListener(eventName,newCallback),callback.apply(null,arguments)})},EventEmitter.setDefaultHandler=function(eventName,callback){var handlers=this._defaultHandlers;if(handlers||(handlers=this._defaultHandlers={_disabled_:{}}),handlers[eventName]){var old=handlers[eventName],disabled=handlers._disabled_[eventName];disabled||(handlers._disabled_[eventName]=disabled=[]),disabled.push(old);var i=disabled.indexOf(callback);-1!=i&&disabled.splice(i,1)}handlers[eventName]=callback},EventEmitter.removeDefaultHandler=function(eventName,callback){var handlers=this._defaultHandlers;if(handlers){var disabled=handlers._disabled_[eventName];if(handlers[eventName]==callback)handlers[eventName],disabled&&this.setDefaultHandler(eventName,disabled.pop());else if(disabled){var i=disabled.indexOf(callback);-1!=i&&disabled.splice(i,1)}}},EventEmitter.on=EventEmitter.addEventListener=function(eventName,callback,capturing){this._eventRegistry=this._eventRegistry||{};var listeners=this._eventRegistry[eventName];return listeners||(listeners=this._eventRegistry[eventName]=[]),-1==listeners.indexOf(callback)&&listeners[capturing?\"unshift\":\"push\"](callback),callback},EventEmitter.off=EventEmitter.removeListener=EventEmitter.removeEventListener=function(eventName,callback){this._eventRegistry=this._eventRegistry||{};var listeners=this._eventRegistry[eventName];if(listeners){var index=listeners.indexOf(callback);-1!==index&&listeners.splice(index,1)}},EventEmitter.removeAllListeners=function(eventName){this._eventRegistry&&(this._eventRegistry[eventName]=[])},exports.EventEmitter=EventEmitter}),ace.define(\"ace/anchor\",[\"require\",\"exports\",\"module\",\"ace/lib/oop\",\"ace/lib/event_emitter\"],function(acequire,exports){\"use strict\";var oop=acequire(\"./lib/oop\"),EventEmitter=acequire(\"./lib/event_emitter\").EventEmitter,Anchor=exports.Anchor=function(doc,row,column){this.$onChange=this.onChange.bind(this),this.attach(doc),column===void 0?this.setPosition(row.row,row.column):this.setPosition(row,column)};(function(){function $pointsInOrder(point1,point2,equalPointsInOrder){var bColIsAfter=equalPointsInOrder?point1.column<=point2.column:point1.column<point2.column;return point1.row<point2.row||point1.row==point2.row&&bColIsAfter}function $getTransformedPoint(delta,point,moveIfEqual){var deltaIsInsert=\"insert\"==delta.action,deltaRowShift=(deltaIsInsert?1:-1)*(delta.end.row-delta.start.row),deltaColShift=(deltaIsInsert?1:-1)*(delta.end.column-delta.start.column),deltaStart=delta.start,deltaEnd=deltaIsInsert?deltaStart:delta.end;return $pointsInOrder(point,deltaStart,moveIfEqual)?{row:point.row,column:point.column}:$pointsInOrder(deltaEnd,point,!moveIfEqual)?{row:point.row+deltaRowShift,column:point.column+(point.row==deltaEnd.row?deltaColShift:0)}:{row:deltaStart.row,column:deltaStart.column}}oop.implement(this,EventEmitter),this.getPosition=function(){return this.$clipPositionToDocument(this.row,this.column)},this.getDocument=function(){return this.document},this.$insertRight=!1,this.onChange=function(delta){if(!(delta.start.row==delta.end.row&&delta.start.row!=this.row||delta.start.row>this.row)){var point=$getTransformedPoint(delta,{row:this.row,column:this.column},this.$insertRight);this.setPosition(point.row,point.column,!0)}},this.setPosition=function(row,column,noClip){var pos;if(pos=noClip?{row:row,column:column}:this.$clipPositionToDocument(row,column),this.row!=pos.row||this.column!=pos.column){var old={row:this.row,column:this.column};this.row=pos.row,this.column=pos.column,this._signal(\"change\",{old:old,value:pos})}},this.detach=function(){this.document.removeEventListener(\"change\",this.$onChange)},this.attach=function(doc){this.document=doc||this.document,this.document.on(\"change\",this.$onChange)},this.$clipPositionToDocument=function(row,column){var pos={};return row>=this.document.getLength()?(pos.row=Math.max(0,this.document.getLength()-1),pos.column=this.document.getLine(pos.row).length):0>row?(pos.row=0,pos.column=0):(pos.row=row,pos.column=Math.min(this.document.getLine(pos.row).length,Math.max(0,column))),0>column&&(pos.column=0),pos}}).call(Anchor.prototype)}),ace.define(\"ace/document\",[\"require\",\"exports\",\"module\",\"ace/lib/oop\",\"ace/apply_delta\",\"ace/lib/event_emitter\",\"ace/range\",\"ace/anchor\"],function(acequire,exports){\"use strict\";var oop=acequire(\"./lib/oop\"),applyDelta=acequire(\"./apply_delta\").applyDelta,EventEmitter=acequire(\"./lib/event_emitter\").EventEmitter,Range=acequire(\"./range\").Range,Anchor=acequire(\"./anchor\").Anchor,Document=function(textOrLines){this.$lines=[\"\"],0===textOrLines.length?this.$lines=[\"\"]:Array.isArray(textOrLines)?this.insertMergedLines({row:0,column:0},textOrLines):this.insert({row:0,column:0},textOrLines)};(function(){oop.implement(this,EventEmitter),this.setValue=function(text){var len=this.getLength()-1;this.remove(new Range(0,0,len,this.getLine(len).length)),this.insert({row:0,column:0},text)},this.getValue=function(){return this.getAllLines().join(this.getNewLineCharacter())},this.createAnchor=function(row,column){return new Anchor(this,row,column)},this.$split=0===\"aaa\".split(/a/).length?function(text){return text.replace(/\\r\\n|\\r/g,\"\\n\").split(\"\\n\")}:function(text){return text.split(/\\r\\n|\\r|\\n/)},this.$detectNewLine=function(text){var match=text.match(/^.*?(\\r\\n|\\r|\\n)/m);this.$autoNewLine=match?match[1]:\"\\n\",this._signal(\"changeNewLineMode\")},this.getNewLineCharacter=function(){switch(this.$newLineMode){case\"windows\":return\"\\r\\n\";case\"unix\":return\"\\n\";default:return this.$autoNewLine||\"\\n\"}},this.$autoNewLine=\"\",this.$newLineMode=\"auto\",this.setNewLineMode=function(newLineMode){this.$newLineMode!==newLineMode&&(this.$newLineMode=newLineMode,this._signal(\"changeNewLineMode\"))},this.getNewLineMode=function(){return this.$newLineMode},this.isNewLine=function(text){return\"\\r\\n\"==text||\"\\r\"==text||\"\\n\"==text},this.getLine=function(row){return this.$lines[row]||\"\"},this.getLines=function(firstRow,lastRow){return this.$lines.slice(firstRow,lastRow+1)},this.getAllLines=function(){return this.getLines(0,this.getLength())},this.getLength=function(){return this.$lines.length},this.getTextRange=function(range){return this.getLinesForRange(range).join(this.getNewLineCharacter())},this.getLinesForRange=function(range){var lines;if(range.start.row===range.end.row)lines=[this.getLine(range.start.row).substring(range.start.column,range.end.column)];else{lines=this.getLines(range.start.row,range.end.row),lines[0]=(lines[0]||\"\").substring(range.start.column);var l=lines.length-1;range.end.row-range.start.row==l&&(lines[l]=lines[l].substring(0,range.end.column))}return lines},this.insertLines=function(row,lines){return console.warn(\"Use of document.insertLines is deprecated. Use the insertFullLines method instead.\"),this.insertFullLines(row,lines)},this.removeLines=function(firstRow,lastRow){return console.warn(\"Use of document.removeLines is deprecated. Use the removeFullLines method instead.\"),this.removeFullLines(firstRow,lastRow)},this.insertNewLine=function(position){return console.warn(\"Use of document.insertNewLine is deprecated. Use insertMergedLines(position, ['', '']) instead.\"),this.insertMergedLines(position,[\"\",\"\"])},this.insert=function(position,text){return 1>=this.getLength()&&this.$detectNewLine(text),this.insertMergedLines(position,this.$split(text))},this.insertInLine=function(position,text){var start=this.clippedPos(position.row,position.column),end=this.pos(position.row,position.column+text.length);return this.applyDelta({start:start,end:end,action:\"insert\",lines:[text]},!0),this.clonePos(end)},this.clippedPos=function(row,column){var length=this.getLength();void 0===row?row=length:0>row?row=0:row>=length&&(row=length-1,column=void 0);var line=this.getLine(row);return void 0==column&&(column=line.length),column=Math.min(Math.max(column,0),line.length),{row:row,column:column}},this.clonePos=function(pos){return{row:pos.row,column:pos.column}},this.pos=function(row,column){return{row:row,column:column}},this.$clipPosition=function(position){var length=this.getLength();return position.row>=length?(position.row=Math.max(0,length-1),position.column=this.getLine(length-1).length):(position.row=Math.max(0,position.row),position.column=Math.min(Math.max(position.column,0),this.getLine(position.row).length)),position},this.insertFullLines=function(row,lines){row=Math.min(Math.max(row,0),this.getLength());var column=0;this.getLength()>row?(lines=lines.concat([\"\"]),column=0):(lines=[\"\"].concat(lines),row--,column=this.$lines[row].length),this.insertMergedLines({row:row,column:column},lines)},this.insertMergedLines=function(position,lines){var start=this.clippedPos(position.row,position.column),end={row:start.row+lines.length-1,column:(1==lines.length?start.column:0)+lines[lines.length-1].length};return this.applyDelta({start:start,end:end,action:\"insert\",lines:lines}),this.clonePos(end)},this.remove=function(range){var start=this.clippedPos(range.start.row,range.start.column),end=this.clippedPos(range.end.row,range.end.column);return this.applyDelta({start:start,end:end,action:\"remove\",lines:this.getLinesForRange({start:start,end:end})}),this.clonePos(start)},this.removeInLine=function(row,startColumn,endColumn){var start=this.clippedPos(row,startColumn),end=this.clippedPos(row,endColumn);return this.applyDelta({start:start,end:end,action:\"remove\",lines:this.getLinesForRange({start:start,end:end})},!0),this.clonePos(start)},this.removeFullLines=function(firstRow,lastRow){firstRow=Math.min(Math.max(0,firstRow),this.getLength()-1),lastRow=Math.min(Math.max(0,lastRow),this.getLength()-1);var deleteFirstNewLine=lastRow==this.getLength()-1&&firstRow>0,deleteLastNewLine=this.getLength()-1>lastRow,startRow=deleteFirstNewLine?firstRow-1:firstRow,startCol=deleteFirstNewLine?this.getLine(startRow).length:0,endRow=deleteLastNewLine?lastRow+1:lastRow,endCol=deleteLastNewLine?0:this.getLine(endRow).length,range=new Range(startRow,startCol,endRow,endCol),deletedLines=this.$lines.slice(firstRow,lastRow+1);return this.applyDelta({start:range.start,end:range.end,action:\"remove\",lines:this.getLinesForRange(range)}),deletedLines},this.removeNewLine=function(row){this.getLength()-1>row&&row>=0&&this.applyDelta({start:this.pos(row,this.getLine(row).length),end:this.pos(row+1,0),action:\"remove\",lines:[\"\",\"\"]})},this.replace=function(range,text){if(range instanceof Range||(range=Range.fromPoints(range.start,range.end)),0===text.length&&range.isEmpty())return range.start;if(text==this.getTextRange(range))return range.end;this.remove(range);var end;return end=text?this.insert(range.start,text):range.start},this.applyDeltas=function(deltas){for(var i=0;deltas.length>i;i++)this.applyDelta(deltas[i])},this.revertDeltas=function(deltas){for(var i=deltas.length-1;i>=0;i--)this.revertDelta(deltas[i])},this.applyDelta=function(delta,doNotValidate){var isInsert=\"insert\"==delta.action;(isInsert?1>=delta.lines.length&&!delta.lines[0]:!Range.comparePoints(delta.start,delta.end))||(isInsert&&delta.lines.length>2e4&&this.$splitAndapplyLargeDelta(delta,2e4),applyDelta(this.$lines,delta,doNotValidate),this._signal(\"change\",delta))},this.$splitAndapplyLargeDelta=function(delta,MAX){for(var lines=delta.lines,l=lines.length,row=delta.start.row,column=delta.start.column,from=0,to=0;;){from=to,to+=MAX-1;var chunk=lines.slice(from,to);if(to>l){delta.lines=chunk,delta.start.row=row+from,delta.start.column=column;break}chunk.push(\"\"),this.applyDelta({start:this.pos(row+from,column),end:this.pos(row+to,column=0),action:delta.action,lines:chunk},!0)}},this.revertDelta=function(delta){this.applyDelta({start:this.clonePos(delta.start),end:this.clonePos(delta.end),action:\"insert\"==delta.action?\"remove\":\"insert\",lines:delta.lines.slice()})},this.indexToPosition=function(index,startRow){for(var lines=this.$lines||this.getAllLines(),newlineLength=this.getNewLineCharacter().length,i=startRow||0,l=lines.length;l>i;i++)if(index-=lines[i].length+newlineLength,0>index)return{row:i,column:index+lines[i].length+newlineLength};return{row:l-1,column:lines[l-1].length}},this.positionToIndex=function(pos,startRow){for(var lines=this.$lines||this.getAllLines(),newlineLength=this.getNewLineCharacter().length,index=0,row=Math.min(pos.row,lines.length),i=startRow||0;row>i;++i)index+=lines[i].length+newlineLength;return index+pos.column}}).call(Document.prototype),exports.Document=Document}),ace.define(\"ace/worker/mirror\",[\"require\",\"exports\",\"module\",\"ace/range\",\"ace/document\",\"ace/lib/lang\"],function(acequire,exports){\"use strict\";acequire(\"../range\").Range;var Document=acequire(\"../document\").Document,lang=acequire(\"../lib/lang\"),Mirror=exports.Mirror=function(sender){this.sender=sender;var doc=this.doc=new Document(\"\"),deferredUpdate=this.deferredUpdate=lang.delayedCall(this.onUpdate.bind(this)),_self=this;sender.on(\"change\",function(e){var data=e.data;if(data[0].start)doc.applyDeltas(data);else for(var i=0;data.length>i;i+=2){if(Array.isArray(data[i+1]))var d={action:\"insert\",start:data[i],lines:data[i+1]};else var d={action:\"remove\",start:data[i],end:data[i+1]};doc.applyDelta(d,!0)}return _self.$timeout?deferredUpdate.schedule(_self.$timeout):(_self.onUpdate(),void 0)})};(function(){this.$timeout=500,this.setTimeout=function(timeout){this.$timeout=timeout},this.setValue=function(value){this.doc.setValue(value),this.deferredUpdate.schedule(this.$timeout)},this.getValue=function(callbackId){this.sender.callback(this.doc.getValue(),callbackId)},this.onUpdate=function(){},this.isPending=function(){return this.deferredUpdate.isPending()}}).call(Mirror.prototype)}),ace.define(\"ace/mode/xml/sax\",[\"require\",\"exports\",\"module\"],function(){function XMLReader(){}function parse(source,defaultNSMapCopy,entityMap,domBuilder,errorHandler){function fixedFromCharCode(code){if(code>65535){code-=65536;var surrogate1=55296+(code>>10),surrogate2=56320+(1023&code);return String.fromCharCode(surrogate1,surrogate2)}return String.fromCharCode(code)}function entityReplacer(a){var k=a.slice(1,-1);return k in entityMap?entityMap[k]:\"#\"===k.charAt(0)?fixedFromCharCode(parseInt(k.substr(1).replace(\"x\",\"0x\"))):(errorHandler.error(\"entity not found:\"+a),a)}function appendText(end){var xt=source.substring(start,end).replace(/&#?\\w+;/g,entityReplacer);locator&&position(start),domBuilder.characters(xt,0,end-start),start=end}function position(start,m){for(;start>=endPos&&(m=linePattern.exec(source));)startPos=m.index,endPos=startPos+m[0].length,locator.lineNumber++;locator.columnNumber=start-startPos+1}for(var startPos=0,endPos=0,linePattern=/.+(?:\\r\\n?|\\n)|.*$/g,locator=domBuilder.locator,parseStack=[{currentNSMap:defaultNSMapCopy}],closeMap={},start=0;;){var i=source.indexOf(\"<\",start);if(0>i){if(!source.substr(start).match(/^\\s*$/)){var doc=domBuilder.document,text=doc.createTextNode(source.substr(start));doc.appendChild(text),domBuilder.currentElement=text}return}switch(i>start&&appendText(i),source.charAt(i+1)){case\"/\":var config,end=source.indexOf(\">\",i+3),tagName=source.substring(i+2,end);if(!(parseStack.length>1)){errorHandler.fatalError(\"end tag name not found for: \"+tagName);break}config=parseStack.pop();var localNSMap=config.localNSMap;if(config.tagName!=tagName&&errorHandler.fatalError(\"end tag name: \"+tagName+\" does not match the current start tagName: \"+config.tagName),domBuilder.endElement(config.uri,config.localName,tagName),localNSMap)for(var prefix in localNSMap)domBuilder.endPrefixMapping(prefix);end++;break;case\"?\":locator&&position(i),end=parseInstruction(source,i,domBuilder);break;case\"!\":locator&&position(i),end=parseDCC(source,i,domBuilder,errorHandler);break;default:try{locator&&position(i);var el=new ElementAttributes,end=parseElementStartPart(source,i,el,entityReplacer,errorHandler),len=el.length;if(len&&locator){for(var backup=copyLocator(locator,{}),i=0;len>i;i++){var a=el[i];position(a.offset),a.offset=copyLocator(locator,{})}copyLocator(backup,locator)}!el.closed&&fixSelfClosed(source,end,el.tagName,closeMap)&&(el.closed=!0,entityMap.nbsp||errorHandler.warning(\"unclosed xml attribute\")),appendElement(el,domBuilder,parseStack),\"http://www.w3.org/1999/xhtml\"!==el.uri||el.closed?end++:end=parseHtmlSpecialContent(source,end,el.tagName,entityReplacer,domBuilder)}catch(e){errorHandler.error(\"element parse error: \"+e),end=-1}}0>end?appendText(i+1):start=end}}function copyLocator(f,t){return t.lineNumber=f.lineNumber,t.columnNumber=f.columnNumber,t}function parseElementStartPart(source,start,el,entityReplacer,errorHandler){for(var attrName,value,p=++start,s=S_TAG;;){var c=source.charAt(p);switch(c){case\"=\":if(s===S_ATTR)attrName=source.slice(start,p),s=S_EQ;else{if(s!==S_ATTR_S)throw Error(\"attribute equal must after attrName\");s=S_EQ}break;case\"'\":case'\"':if(s===S_EQ){if(start=p+1,p=source.indexOf(c,start),!(p>0))throw Error(\"attribute value no end '\"+c+\"' match\");value=source.slice(start,p).replace(/&#?\\w+;/g,entityReplacer),el.add(attrName,value,start-1),s=S_E}else{if(s!=S_V)throw Error('attribute value must after \"=\"');value=source.slice(start,p).replace(/&#?\\w+;/g,entityReplacer),el.add(attrName,value,start),errorHandler.warning('attribute \"'+attrName+'\" missed start quot('+c+\")!!\"),start=p+1,s=S_E}break;case\"/\":switch(s){case S_TAG:el.setTagName(source.slice(start,p));case S_E:case S_S:case S_C:s=S_C,el.closed=!0;case S_V:case S_ATTR:case S_ATTR_S:break;default:throw Error(\"attribute invalid close char('/')\")}break;case\"\":errorHandler.error(\"unexpected end of input\");case\">\":switch(s){case S_TAG:el.setTagName(source.slice(start,p));case S_E:case S_S:case S_C:break;case S_V:case S_ATTR:value=source.slice(start,p),\"/\"===value.slice(-1)&&(el.closed=!0,value=value.slice(0,-1));case S_ATTR_S:s===S_ATTR_S&&(value=attrName),s==S_V?(errorHandler.warning('attribute \"'+value+'\" missed quot(\")!!'),el.add(attrName,value.replace(/&#?\\w+;/g,entityReplacer),start)):(errorHandler.warning('attribute \"'+value+'\" missed value!! \"'+value+'\" instead!!'),el.add(value,value,start));break;case S_EQ:throw Error(\"attribute value missed!!\")}return p;case\"\":c=\" \";default:if(\" \">=c)switch(s){case S_TAG:el.setTagName(source.slice(start,p)),s=S_S;break;case S_ATTR:attrName=source.slice(start,p),s=S_ATTR_S;break;case S_V:var value=source.slice(start,p).replace(/&#?\\w+;/g,entityReplacer);errorHandler.warning('attribute \"'+value+'\" missed quot(\")!!'),el.add(attrName,value,start);case S_E:s=S_S}else switch(s){case S_ATTR_S:errorHandler.warning('attribute \"'+attrName+'\" missed value!! \"'+attrName+'\" instead!!'),el.add(attrName,attrName,start),start=p,s=S_ATTR;\nbreak;case S_E:errorHandler.warning('attribute space is acequired\"'+attrName+'\"!!');case S_S:s=S_ATTR,start=p;break;case S_EQ:s=S_V,start=p;break;case S_C:throw Error(\"elements closed character '/' and '>' must be connected to\")}}p++}}function appendElement(el,domBuilder,parseStack){for(var tagName=el.tagName,localNSMap=null,currentNSMap=parseStack[parseStack.length-1].currentNSMap,i=el.length;i--;){var a=el[i],qName=a.qName,value=a.value,nsp=qName.indexOf(\":\");if(nsp>0)var prefix=a.prefix=qName.slice(0,nsp),localName=qName.slice(nsp+1),nsPrefix=\"xmlns\"===prefix&&localName;else localName=qName,prefix=null,nsPrefix=\"xmlns\"===qName&&\"\";a.localName=localName,nsPrefix!==!1&&(null==localNSMap&&(localNSMap={},_copy(currentNSMap,currentNSMap={})),currentNSMap[nsPrefix]=localNSMap[nsPrefix]=value,a.uri=\"http://www.w3.org/2000/xmlns/\",domBuilder.startPrefixMapping(nsPrefix,value))}for(var i=el.length;i--;){a=el[i];var prefix=a.prefix;prefix&&(\"xml\"===prefix&&(a.uri=\"http://www.w3.org/XML/1998/namespace\"),\"xmlns\"!==prefix&&(a.uri=currentNSMap[prefix]))}var nsp=tagName.indexOf(\":\");nsp>0?(prefix=el.prefix=tagName.slice(0,nsp),localName=el.localName=tagName.slice(nsp+1)):(prefix=null,localName=el.localName=tagName);var ns=el.uri=currentNSMap[prefix||\"\"];if(domBuilder.startElement(ns,localName,tagName,el),el.closed){if(domBuilder.endElement(ns,localName,tagName),localNSMap)for(prefix in localNSMap)domBuilder.endPrefixMapping(prefix)}else el.currentNSMap=currentNSMap,el.localNSMap=localNSMap,parseStack.push(el)}function parseHtmlSpecialContent(source,elStartEnd,tagName,entityReplacer,domBuilder){if(/^(?:script|textarea)$/i.test(tagName)){var elEndStart=source.indexOf(\"</\"+tagName+\">\",elStartEnd),text=source.substring(elStartEnd+1,elEndStart);if(/[&<]/.test(text))return/^script$/i.test(tagName)?(domBuilder.characters(text,0,text.length),elEndStart):(text=text.replace(/&#?\\w+;/g,entityReplacer),domBuilder.characters(text,0,text.length),elEndStart)}return elStartEnd+1}function fixSelfClosed(source,elStartEnd,tagName,closeMap){var pos=closeMap[tagName];return null==pos&&(pos=closeMap[tagName]=source.lastIndexOf(\"</\"+tagName+\">\")),elStartEnd>pos}function _copy(source,target){for(var n in source)target[n]=source[n]}function parseDCC(source,start,domBuilder,errorHandler){var next=source.charAt(start+2);switch(next){case\"-\":if(\"-\"===source.charAt(start+3)){var end=source.indexOf(\"-->\",start+4);return end>start?(domBuilder.comment(source,start+4,end-start-4),end+3):(errorHandler.error(\"Unclosed comment\"),-1)}return-1;default:if(\"CDATA[\"==source.substr(start+3,6)){var end=source.indexOf(\"]]>\",start+9);return domBuilder.startCDATA(),domBuilder.characters(source,start+9,end-start-9),domBuilder.endCDATA(),end+3}var matchs=split(source,start),len=matchs.length;if(len>1&&/!doctype/i.test(matchs[0][0])){var name=matchs[1][0],pubid=len>3&&/^public$/i.test(matchs[2][0])&&matchs[3][0],sysid=len>4&&matchs[4][0],lastMatch=matchs[len-1];return domBuilder.startDTD(name,pubid&&pubid.replace(/^(['\"])(.*?)\\1$/,\"$2\"),sysid&&sysid.replace(/^(['\"])(.*?)\\1$/,\"$2\")),domBuilder.endDTD(),lastMatch.index+lastMatch[0].length}}return-1}function parseInstruction(source,start,domBuilder){var end=source.indexOf(\"?>\",start);if(end){var match=source.substring(start,end).match(/^<\\?(\\S*)\\s*([\\s\\S]*?)\\s*$/);return match?(match[0].length,domBuilder.processingInstruction(match[1],match[2]),end+2):-1}return-1}function ElementAttributes(){}function _set_proto_(thiz,parent){return thiz.__proto__=parent,thiz}function split(source,start){var match,buf=[],reg=/'[^']+'|\"[^\"]+\"|[^\\s<>\\/=]+=?|(\\/?\\s*>|<)/g;for(reg.lastIndex=start,reg.exec(source);match=reg.exec(source);)if(buf.push(match),match[1])return buf}var nameStartChar=/[A-Z_a-z\\xC0-\\xD6\\xD8-\\xF6\\u00F8-\\u02FF\\u0370-\\u037D\\u037F-\\u1FFF\\u200C-\\u200D\\u2070-\\u218F\\u2C00-\\u2FEF\\u3001-\\uD7FF\\uF900-\\uFDCF\\uFDF0-\\uFFFD]/,nameChar=RegExp(\"[\\\\-\\\\.0-9\"+nameStartChar.source.slice(1,-1)+\"·̀-ͯ\\\\ux203F-⁀]\"),tagNamePattern=RegExp(\"^\"+nameStartChar.source+nameChar.source+\"*(?::\"+nameStartChar.source+nameChar.source+\"*)?$\"),S_TAG=0,S_ATTR=1,S_ATTR_S=2,S_EQ=3,S_V=4,S_E=5,S_S=6,S_C=7;return XMLReader.prototype={parse:function(source,defaultNSMap,entityMap){var domBuilder=this.domBuilder;domBuilder.startDocument(),_copy(defaultNSMap,defaultNSMap={}),parse(source,defaultNSMap,entityMap,domBuilder,this.errorHandler),domBuilder.endDocument()}},ElementAttributes.prototype={setTagName:function(tagName){if(!tagNamePattern.test(tagName))throw Error(\"invalid tagName:\"+tagName);this.tagName=tagName},add:function(qName,value,offset){if(!tagNamePattern.test(qName))throw Error(\"invalid attribute:\"+qName);this[this.length++]={qName:qName,value:value,offset:offset}},length:0,getLocalName:function(i){return this[i].localName},getOffset:function(i){return this[i].offset},getQName:function(i){return this[i].qName},getURI:function(i){return this[i].uri},getValue:function(i){return this[i].value}},_set_proto_({},_set_proto_.prototype)instanceof _set_proto_||(_set_proto_=function(thiz,parent){function p(){}p.prototype=parent,p=new p;for(parent in thiz)p[parent]=thiz[parent];return p}),XMLReader}),ace.define(\"ace/mode/xml/dom\",[\"require\",\"exports\",\"module\"],function(){function copy(src,dest){for(var p in src)dest[p]=src[p]}function _extends(Class,Super){function t(){}var pt=Class.prototype;if(Object.create){var ppt=Object.create(Super.prototype);pt.__proto__=ppt}pt instanceof Super||(t.prototype=Super.prototype,t=new t,copy(pt,t),Class.prototype=pt=t),pt.constructor!=Class&&(\"function\"!=typeof Class&&console.error(\"unknow Class:\"+Class),pt.constructor=Class)}function DOMException(code,message){if(message instanceof Error)var error=message;else error=this,Error.call(this,ExceptionMessage[code]),this.message=ExceptionMessage[code],Error.captureStackTrace&&Error.captureStackTrace(this,DOMException);return error.code=code,message&&(this.message=this.message+\": \"+message),error}function NodeList(){}function LiveNodeList(node,refresh){this._node=node,this._refresh=refresh,_updateLiveList(this)}function _updateLiveList(list){var inc=list._node._inc||list._node.ownerDocument._inc;if(list._inc!=inc){var ls=list._refresh(list._node);__set__(list,\"length\",ls.length),copy(ls,list),list._inc=inc}}function NamedNodeMap(){}function _findNodeIndex(list,node){for(var i=list.length;i--;)if(list[i]===node)return i}function _addNamedNode(el,list,newAttr,oldAttr){if(oldAttr?list[_findNodeIndex(list,oldAttr)]=newAttr:list[list.length++]=newAttr,el){newAttr.ownerElement=el;var doc=el.ownerDocument;doc&&(oldAttr&&_onRemoveAttribute(doc,el,oldAttr),_onAddAttribute(doc,el,newAttr))}}function _removeNamedNode(el,list,attr){var i=_findNodeIndex(list,attr);if(!(i>=0))throw DOMException(NOT_FOUND_ERR,Error());for(var lastIndex=list.length-1;lastIndex>i;)list[i]=list[++i];if(list.length=lastIndex,el){var doc=el.ownerDocument;doc&&(_onRemoveAttribute(doc,el,attr),attr.ownerElement=null)}}function DOMImplementation(features){if(this._features={},features)for(var feature in features)this._features=features[feature]}function Node(){}function _xmlEncoder(c){return\"<\"==c&&\"&lt;\"||\">\"==c&&\"&gt;\"||\"&\"==c&&\"&amp;\"||'\"'==c&&\"&quot;\"||\"&#\"+c.charCodeAt()+\";\"}function _visitNode(node,callback){if(callback(node))return!0;if(node=node.firstChild)do if(_visitNode(node,callback))return!0;while(node=node.nextSibling)}function Document(){}function _onAddAttribute(doc,el,newAttr){doc&&doc._inc++;var ns=newAttr.namespaceURI;\"http://www.w3.org/2000/xmlns/\"==ns&&(el._nsMap[newAttr.prefix?newAttr.localName:\"\"]=newAttr.value)}function _onRemoveAttribute(doc,el,newAttr){doc&&doc._inc++;var ns=newAttr.namespaceURI;\"http://www.w3.org/2000/xmlns/\"==ns&&delete el._nsMap[newAttr.prefix?newAttr.localName:\"\"]}function _onUpdateChild(doc,el,newChild){if(doc&&doc._inc){doc._inc++;var cs=el.childNodes;if(newChild)cs[cs.length++]=newChild;else{for(var child=el.firstChild,i=0;child;)cs[i++]=child,child=child.nextSibling;cs.length=i}}}function _removeChild(parentNode,child){var previous=child.previousSibling,next=child.nextSibling;return previous?previous.nextSibling=next:parentNode.firstChild=next,next?next.previousSibling=previous:parentNode.lastChild=previous,_onUpdateChild(parentNode.ownerDocument,parentNode),child}function _insertBefore(parentNode,newChild,nextChild){var cp=newChild.parentNode;if(cp&&cp.removeChild(newChild),newChild.nodeType===DOCUMENT_FRAGMENT_NODE){var newFirst=newChild.firstChild;if(null==newFirst)return newChild;var newLast=newChild.lastChild}else newFirst=newLast=newChild;var pre=nextChild?nextChild.previousSibling:parentNode.lastChild;newFirst.previousSibling=pre,newLast.nextSibling=nextChild,pre?pre.nextSibling=newFirst:parentNode.firstChild=newFirst,null==nextChild?parentNode.lastChild=newLast:nextChild.previousSibling=newLast;do newFirst.parentNode=parentNode;while(newFirst!==newLast&&(newFirst=newFirst.nextSibling));return _onUpdateChild(parentNode.ownerDocument||parentNode,parentNode),newChild.nodeType==DOCUMENT_FRAGMENT_NODE&&(newChild.firstChild=newChild.lastChild=null),newChild}function _appendSingleChild(parentNode,newChild){var cp=newChild.parentNode;if(cp){var pre=parentNode.lastChild;cp.removeChild(newChild);var pre=parentNode.lastChild}var pre=parentNode.lastChild;return newChild.parentNode=parentNode,newChild.previousSibling=pre,newChild.nextSibling=null,pre?pre.nextSibling=newChild:parentNode.firstChild=newChild,parentNode.lastChild=newChild,_onUpdateChild(parentNode.ownerDocument,parentNode,newChild),newChild}function Element(){this._nsMap={}}function Attr(){}function CharacterData(){}function Text(){}function Comment(){}function CDATASection(){}function DocumentType(){}function Notation(){}function Entity(){}function EntityReference(){}function DocumentFragment(){}function ProcessingInstruction(){}function XMLSerializer(){}function serializeToString(node,buf){switch(node.nodeType){case ELEMENT_NODE:var attrs=node.attributes,len=attrs.length,child=node.firstChild,nodeName=node.tagName,isHTML=htmlns===node.namespaceURI;buf.push(\"<\",nodeName);for(var i=0;len>i;i++)serializeToString(attrs.item(i),buf,isHTML);if(child||isHTML&&!/^(?:meta|link|img|br|hr|input|button)$/i.test(nodeName)){if(buf.push(\">\"),isHTML&&/^script$/i.test(nodeName))child&&buf.push(child.data);else for(;child;)serializeToString(child,buf),child=child.nextSibling;buf.push(\"</\",nodeName,\">\")}else buf.push(\"/>\");return;case DOCUMENT_NODE:case DOCUMENT_FRAGMENT_NODE:for(var child=node.firstChild;child;)serializeToString(child,buf),child=child.nextSibling;return;case ATTRIBUTE_NODE:return buf.push(\" \",node.name,'=\"',node.value.replace(/[<&\"]/g,_xmlEncoder),'\"');case TEXT_NODE:return buf.push(node.data.replace(/[<&]/g,_xmlEncoder));case CDATA_SECTION_NODE:return buf.push(\"<![CDATA[\",node.data,\"]]>\");case COMMENT_NODE:return buf.push(\"<!--\",node.data,\"-->\");case DOCUMENT_TYPE_NODE:var pubid=node.publicId,sysid=node.systemId;if(buf.push(\"<!DOCTYPE \",node.name),pubid)buf.push(' PUBLIC \"',pubid),sysid&&\".\"!=sysid&&buf.push('\" \"',sysid),buf.push('\">');else if(sysid&&\".\"!=sysid)buf.push(' SYSTEM \"',sysid,'\">');else{var sub=node.internalSubset;sub&&buf.push(\" [\",sub,\"]\"),buf.push(\">\")}return;case PROCESSING_INSTRUCTION_NODE:return buf.push(\"<?\",node.target,\" \",node.data,\"?>\");case ENTITY_REFERENCE_NODE:return buf.push(\"&\",node.nodeName,\";\");default:buf.push(\"??\",node.nodeName)}}function importNode(doc,node,deep){var node2;switch(node.nodeType){case ELEMENT_NODE:node2=node.cloneNode(!1),node2.ownerDocument=doc;case DOCUMENT_FRAGMENT_NODE:break;case ATTRIBUTE_NODE:deep=!0}if(node2||(node2=node.cloneNode(!1)),node2.ownerDocument=doc,node2.parentNode=null,deep)for(var child=node.firstChild;child;)node2.appendChild(importNode(doc,child,deep)),child=child.nextSibling;return node2}function cloneNode(doc,node,deep){var node2=new node.constructor;for(var n in node){var v=node[n];\"object\"!=typeof v&&v!=node2[n]&&(node2[n]=v)}switch(node.childNodes&&(node2.childNodes=new NodeList),node2.ownerDocument=doc,node2.nodeType){case ELEMENT_NODE:var attrs=node.attributes,attrs2=node2.attributes=new NamedNodeMap,len=attrs.length;attrs2._ownerElement=node2;for(var i=0;len>i;i++)node2.setAttributeNode(cloneNode(doc,attrs.item(i),!0));break;case ATTRIBUTE_NODE:deep=!0}if(deep)for(var child=node.firstChild;child;)node2.appendChild(cloneNode(doc,child,deep)),child=child.nextSibling;return node2}function __set__(object,key,value){object[key]=value}function getTextContent(node){switch(node.nodeType){case 1:case 11:var buf=[];for(node=node.firstChild;node;)7!==node.nodeType&&8!==node.nodeType&&buf.push(getTextContent(node)),node=node.nextSibling;return buf.join(\"\");default:return node.nodeValue}}var htmlns=\"http://www.w3.org/1999/xhtml\",NodeType={},ELEMENT_NODE=NodeType.ELEMENT_NODE=1,ATTRIBUTE_NODE=NodeType.ATTRIBUTE_NODE=2,TEXT_NODE=NodeType.TEXT_NODE=3,CDATA_SECTION_NODE=NodeType.CDATA_SECTION_NODE=4,ENTITY_REFERENCE_NODE=NodeType.ENTITY_REFERENCE_NODE=5,ENTITY_NODE=NodeType.ENTITY_NODE=6,PROCESSING_INSTRUCTION_NODE=NodeType.PROCESSING_INSTRUCTION_NODE=7,COMMENT_NODE=NodeType.COMMENT_NODE=8,DOCUMENT_NODE=NodeType.DOCUMENT_NODE=9,DOCUMENT_TYPE_NODE=NodeType.DOCUMENT_TYPE_NODE=10,DOCUMENT_FRAGMENT_NODE=NodeType.DOCUMENT_FRAGMENT_NODE=11,NOTATION_NODE=NodeType.NOTATION_NODE=12,ExceptionCode={},ExceptionMessage={};ExceptionCode.INDEX_SIZE_ERR=(ExceptionMessage[1]=\"Index size error\",1),ExceptionCode.DOMSTRING_SIZE_ERR=(ExceptionMessage[2]=\"DOMString size error\",2),ExceptionCode.HIERARCHY_REQUEST_ERR=(ExceptionMessage[3]=\"Hierarchy request error\",3),ExceptionCode.WRONG_DOCUMENT_ERR=(ExceptionMessage[4]=\"Wrong document\",4),ExceptionCode.INVALID_CHARACTER_ERR=(ExceptionMessage[5]=\"Invalid character\",5),ExceptionCode.NO_DATA_ALLOWED_ERR=(ExceptionMessage[6]=\"No data allowed\",6),ExceptionCode.NO_MODIFICATION_ALLOWED_ERR=(ExceptionMessage[7]=\"No modification allowed\",7);var NOT_FOUND_ERR=ExceptionCode.NOT_FOUND_ERR=(ExceptionMessage[8]=\"Not found\",8);ExceptionCode.NOT_SUPPORTED_ERR=(ExceptionMessage[9]=\"Not supported\",9);var INUSE_ATTRIBUTE_ERR=ExceptionCode.INUSE_ATTRIBUTE_ERR=(ExceptionMessage[10]=\"Attribute in use\",10);ExceptionCode.INVALID_STATE_ERR=(ExceptionMessage[11]=\"Invalid state\",11),ExceptionCode.SYNTAX_ERR=(ExceptionMessage[12]=\"Syntax error\",12),ExceptionCode.INVALID_MODIFICATION_ERR=(ExceptionMessage[13]=\"Invalid modification\",13),ExceptionCode.NAMESPACE_ERR=(ExceptionMessage[14]=\"Invalid namespace\",14),ExceptionCode.INVALID_ACCESS_ERR=(ExceptionMessage[15]=\"Invalid access\",15),DOMException.prototype=Error.prototype,copy(ExceptionCode,DOMException),NodeList.prototype={length:0,item:function(index){return this[index]||null}},LiveNodeList.prototype.item=function(i){return _updateLiveList(this),this[i]},_extends(LiveNodeList,NodeList),NamedNodeMap.prototype={length:0,item:NodeList.prototype.item,getNamedItem:function(key){for(var i=this.length;i--;){var attr=this[i];if(attr.nodeName==key)return attr}},setNamedItem:function(attr){var el=attr.ownerElement;if(el&&el!=this._ownerElement)throw new DOMException(INUSE_ATTRIBUTE_ERR);var oldAttr=this.getNamedItem(attr.nodeName);return _addNamedNode(this._ownerElement,this,attr,oldAttr),oldAttr},setNamedItemNS:function(attr){var oldAttr,el=attr.ownerElement;if(el&&el!=this._ownerElement)throw new DOMException(INUSE_ATTRIBUTE_ERR);return oldAttr=this.getNamedItemNS(attr.namespaceURI,attr.localName),_addNamedNode(this._ownerElement,this,attr,oldAttr),oldAttr},removeNamedItem:function(key){var attr=this.getNamedItem(key);return _removeNamedNode(this._ownerElement,this,attr),attr},removeNamedItemNS:function(namespaceURI,localName){var attr=this.getNamedItemNS(namespaceURI,localName);return _removeNamedNode(this._ownerElement,this,attr),attr},getNamedItemNS:function(namespaceURI,localName){for(var i=this.length;i--;){var node=this[i];if(node.localName==localName&&node.namespaceURI==namespaceURI)return node}return null}},DOMImplementation.prototype={hasFeature:function(feature,version){var versions=this._features[feature.toLowerCase()];return versions&&(!version||version in versions)?!0:!1},createDocument:function(namespaceURI,qualifiedName,doctype){var doc=new Document;if(doc.implementation=this,doc.childNodes=new NodeList,doc.doctype=doctype,doctype&&doc.appendChild(doctype),qualifiedName){var root=doc.createElementNS(namespaceURI,qualifiedName);doc.appendChild(root)}return doc},createDocumentType:function(qualifiedName,publicId,systemId){var node=new DocumentType;return node.name=qualifiedName,node.nodeName=qualifiedName,node.publicId=publicId,node.systemId=systemId,node}},Node.prototype={firstChild:null,lastChild:null,previousSibling:null,nextSibling:null,attributes:null,parentNode:null,childNodes:null,ownerDocument:null,nodeValue:null,namespaceURI:null,prefix:null,localName:null,insertBefore:function(newChild,refChild){return _insertBefore(this,newChild,refChild)},replaceChild:function(newChild,oldChild){this.insertBefore(newChild,oldChild),oldChild&&this.removeChild(oldChild)},removeChild:function(oldChild){return _removeChild(this,oldChild)},appendChild:function(newChild){return this.insertBefore(newChild,null)},hasChildNodes:function(){return null!=this.firstChild},cloneNode:function(deep){return cloneNode(this.ownerDocument||this,this,deep)},normalize:function(){for(var child=this.firstChild;child;){var next=child.nextSibling;next&&next.nodeType==TEXT_NODE&&child.nodeType==TEXT_NODE?(this.removeChild(next),child.appendData(next.data)):(child.normalize(),child=next)}},isSupported:function(feature,version){return this.ownerDocument.implementation.hasFeature(feature,version)},hasAttributes:function(){return this.attributes.length>0},lookupPrefix:function(namespaceURI){for(var el=this;el;){var map=el._nsMap;if(map)for(var n in map)if(map[n]==namespaceURI)return n;el=2==el.nodeType?el.ownerDocument:el.parentNode}return null},lookupNamespaceURI:function(prefix){for(var el=this;el;){var map=el._nsMap;if(map&&prefix in map)return map[prefix];el=2==el.nodeType?el.ownerDocument:el.parentNode}return null},isDefaultNamespace:function(namespaceURI){var prefix=this.lookupPrefix(namespaceURI);return null==prefix}},copy(NodeType,Node),copy(NodeType,Node.prototype),Document.prototype={nodeName:\"#document\",nodeType:DOCUMENT_NODE,doctype:null,documentElement:null,_inc:1,insertBefore:function(newChild,refChild){if(newChild.nodeType==DOCUMENT_FRAGMENT_NODE){for(var child=newChild.firstChild;child;){var next=child.nextSibling;this.insertBefore(child,refChild),child=next}return newChild}return null==this.documentElement&&1==newChild.nodeType&&(this.documentElement=newChild),_insertBefore(this,newChild,refChild),newChild.ownerDocument=this,newChild},removeChild:function(oldChild){return this.documentElement==oldChild&&(this.documentElement=null),_removeChild(this,oldChild)},importNode:function(importedNode,deep){return importNode(this,importedNode,deep)},getElementById:function(id){var rtv=null;return _visitNode(this.documentElement,function(node){return 1==node.nodeType&&node.getAttribute(\"id\")==id?(rtv=node,!0):void 0}),rtv},createElement:function(tagName){var node=new Element;node.ownerDocument=this,node.nodeName=tagName,node.tagName=tagName,node.childNodes=new NodeList;var attrs=node.attributes=new NamedNodeMap;return attrs._ownerElement=node,node},createDocumentFragment:function(){var node=new DocumentFragment;return node.ownerDocument=this,node.childNodes=new NodeList,node},createTextNode:function(data){var node=new Text;return node.ownerDocument=this,node.appendData(data),node},createComment:function(data){var node=new Comment;return node.ownerDocument=this,node.appendData(data),node},createCDATASection:function(data){var node=new CDATASection;return node.ownerDocument=this,node.appendData(data),node},createProcessingInstruction:function(target,data){var node=new ProcessingInstruction;return node.ownerDocument=this,node.tagName=node.target=target,node.nodeValue=node.data=data,node},createAttribute:function(name){var node=new Attr;return node.ownerDocument=this,node.name=name,node.nodeName=name,node.localName=name,node.specified=!0,node},createEntityReference:function(name){var node=new EntityReference;return node.ownerDocument=this,node.nodeName=name,node},createElementNS:function(namespaceURI,qualifiedName){var node=new Element,pl=qualifiedName.split(\":\"),attrs=node.attributes=new NamedNodeMap;return node.childNodes=new NodeList,node.ownerDocument=this,node.nodeName=qualifiedName,node.tagName=qualifiedName,node.namespaceURI=namespaceURI,2==pl.length?(node.prefix=pl[0],node.localName=pl[1]):node.localName=qualifiedName,attrs._ownerElement=node,node},createAttributeNS:function(namespaceURI,qualifiedName){var node=new Attr,pl=qualifiedName.split(\":\");return node.ownerDocument=this,node.nodeName=qualifiedName,node.name=qualifiedName,node.namespaceURI=namespaceURI,node.specified=!0,2==pl.length?(node.prefix=pl[0],node.localName=pl[1]):node.localName=qualifiedName,node}},_extends(Document,Node),Element.prototype={nodeType:ELEMENT_NODE,hasAttribute:function(name){return null!=this.getAttributeNode(name)},getAttribute:function(name){var attr=this.getAttributeNode(name);return attr&&attr.value||\"\"},getAttributeNode:function(name){return this.attributes.getNamedItem(name)},setAttribute:function(name,value){var attr=this.ownerDocument.createAttribute(name);attr.value=attr.nodeValue=\"\"+value,this.setAttributeNode(attr)},removeAttribute:function(name){var attr=this.getAttributeNode(name);attr&&this.removeAttributeNode(attr)},appendChild:function(newChild){return newChild.nodeType===DOCUMENT_FRAGMENT_NODE?this.insertBefore(newChild,null):_appendSingleChild(this,newChild)},setAttributeNode:function(newAttr){return this.attributes.setNamedItem(newAttr)},setAttributeNodeNS:function(newAttr){return this.attributes.setNamedItemNS(newAttr)},removeAttributeNode:function(oldAttr){return this.attributes.removeNamedItem(oldAttr.nodeName)},removeAttributeNS:function(namespaceURI,localName){var old=this.getAttributeNodeNS(namespaceURI,localName);old&&this.removeAttributeNode(old)},hasAttributeNS:function(namespaceURI,localName){return null!=this.getAttributeNodeNS(namespaceURI,localName)},getAttributeNS:function(namespaceURI,localName){var attr=this.getAttributeNodeNS(namespaceURI,localName);return attr&&attr.value||\"\"},setAttributeNS:function(namespaceURI,qualifiedName,value){var attr=this.ownerDocument.createAttributeNS(namespaceURI,qualifiedName);attr.value=attr.nodeValue=\"\"+value,this.setAttributeNode(attr)},getAttributeNodeNS:function(namespaceURI,localName){return this.attributes.getNamedItemNS(namespaceURI,localName)},getElementsByTagName:function(tagName){return new LiveNodeList(this,function(base){var ls=[];return _visitNode(base,function(node){node===base||node.nodeType!=ELEMENT_NODE||\"*\"!==tagName&&node.tagName!=tagName||ls.push(node)}),ls})},getElementsByTagNameNS:function(namespaceURI,localName){return new LiveNodeList(this,function(base){var ls=[];return _visitNode(base,function(node){node===base||node.nodeType!==ELEMENT_NODE||\"*\"!==namespaceURI&&node.namespaceURI!==namespaceURI||\"*\"!==localName&&node.localName!=localName||ls.push(node)}),ls})}},Document.prototype.getElementsByTagName=Element.prototype.getElementsByTagName,Document.prototype.getElementsByTagNameNS=Element.prototype.getElementsByTagNameNS,_extends(Element,Node),Attr.prototype.nodeType=ATTRIBUTE_NODE,_extends(Attr,Node),CharacterData.prototype={data:\"\",substringData:function(offset,count){return this.data.substring(offset,offset+count)},appendData:function(text){text=this.data+text,this.nodeValue=this.data=text,this.length=text.length},insertData:function(offset,text){this.replaceData(offset,0,text)},appendChild:function(){throw Error(ExceptionMessage[3])},deleteData:function(offset,count){this.replaceData(offset,count,\"\")},replaceData:function(offset,count,text){var start=this.data.substring(0,offset),end=this.data.substring(offset+count);text=start+text+end,this.nodeValue=this.data=text,this.length=text.length}},_extends(CharacterData,Node),Text.prototype={nodeName:\"#text\",nodeType:TEXT_NODE,splitText:function(offset){var text=this.data,newText=text.substring(offset);text=text.substring(0,offset),this.data=this.nodeValue=text,this.length=text.length;var newNode=this.ownerDocument.createTextNode(newText);return this.parentNode&&this.parentNode.insertBefore(newNode,this.nextSibling),newNode}},_extends(Text,CharacterData),Comment.prototype={nodeName:\"#comment\",nodeType:COMMENT_NODE},_extends(Comment,CharacterData),CDATASection.prototype={nodeName:\"#cdata-section\",nodeType:CDATA_SECTION_NODE},_extends(CDATASection,CharacterData),DocumentType.prototype.nodeType=DOCUMENT_TYPE_NODE,_extends(DocumentType,Node),Notation.prototype.nodeType=NOTATION_NODE,_extends(Notation,Node),Entity.prototype.nodeType=ENTITY_NODE,_extends(Entity,Node),EntityReference.prototype.nodeType=ENTITY_REFERENCE_NODE,_extends(EntityReference,Node),DocumentFragment.prototype.nodeName=\"#document-fragment\",DocumentFragment.prototype.nodeType=DOCUMENT_FRAGMENT_NODE,_extends(DocumentFragment,Node),ProcessingInstruction.prototype.nodeType=PROCESSING_INSTRUCTION_NODE,_extends(ProcessingInstruction,Node),XMLSerializer.prototype.serializeToString=function(node){var buf=[];return serializeToString(node,buf),buf.join(\"\")},Node.prototype.toString=function(){return XMLSerializer.prototype.serializeToString(this)};try{Object.defineProperty&&(Object.defineProperty(LiveNodeList.prototype,\"length\",{get:function(){return _updateLiveList(this),this.$$length}}),Object.defineProperty(Node.prototype,\"textContent\",{get:function(){return getTextContent(this)},set:function(data){switch(this.nodeType){case 1:case 11:for(;this.firstChild;)this.removeChild(this.firstChild);(data||data+\"\")&&this.appendChild(this.ownerDocument.createTextNode(data));break;default:this.data=data,this.value=value,this.nodeValue=data}}}),__set__=function(object,key,value){object[\"$$\"+key]=value})}catch(e){}return DOMImplementation}),ace.define(\"ace/mode/xml/dom-parser\",[\"require\",\"exports\",\"module\",\"ace/mode/xml/sax\",\"ace/mode/xml/dom\"],function(acequire){\"use strict\";function DOMParser(options){this.options=options||{locator:{}}}function buildErrorHandler(errorImpl,domBuilder,locator){function build(key){var fn=errorImpl[key];if(!fn)if(isCallback)fn=2==errorImpl.length?function(msg){errorImpl(key,msg)}:errorImpl;else for(var i=arguments.length;--i&&!(fn=errorImpl[arguments[i]]););errorHandler[key]=fn&&function(msg){fn(msg+_locator(locator),msg,locator)}||function(){}}if(!errorImpl){if(domBuilder instanceof DOMHandler)return domBuilder;errorImpl=domBuilder}var errorHandler={},isCallback=errorImpl instanceof Function;return locator=locator||{},build(\"warning\",\"warn\"),build(\"error\",\"warn\",\"warning\"),build(\"fatalError\",\"warn\",\"warning\",\"error\"),errorHandler}function DOMHandler(){this.cdata=!1}function position(locator,node){node.lineNumber=locator.lineNumber,node.columnNumber=locator.columnNumber}function _locator(l){return l?\"\\n@\"+(l.systemId||\"\")+\"#[line:\"+l.lineNumber+\",col:\"+l.columnNumber+\"]\":void 0}function _toString(chars,start,length){return\"string\"==typeof chars?chars.substr(start,length):chars.length>=start+length||start?new java.lang.String(chars,start,length)+\"\":chars}function appendElement(hander,node){hander.currentElement?hander.currentElement.appendChild(node):hander.document.appendChild(node)}var XMLReader=acequire(\"./sax\"),DOMImplementation=acequire(\"./dom\");return DOMParser.prototype.parseFromString=function(source,mimeType){var options=this.options,sax=new XMLReader,domBuilder=options.domBuilder||new DOMHandler,errorHandler=options.errorHandler,locator=options.locator,defaultNSMap=options.xmlns||{},entityMap={lt:\"<\",gt:\">\",amp:\"&\",quot:'\"',apos:\"'\"};return locator&&domBuilder.setDocumentLocator(locator),sax.errorHandler=buildErrorHandler(errorHandler,domBuilder,locator),sax.domBuilder=options.domBuilder||domBuilder,/\\/x?html?$/.test(mimeType)&&(entityMap.nbsp=\" \",entityMap.copy=\"©\",defaultNSMap[\"\"]=\"http://www.w3.org/1999/xhtml\"),source?sax.parse(source,defaultNSMap,entityMap):sax.errorHandler.error(\"invalid document source\"),domBuilder.document},DOMHandler.prototype={startDocument:function(){this.document=(new DOMImplementation).createDocument(null,null,null),this.locator&&(this.document.documentURI=this.locator.systemId)},startElement:function(namespaceURI,localName,qName,attrs){var doc=this.document,el=doc.createElementNS(namespaceURI,qName||localName),len=attrs.length;appendElement(this,el),this.currentElement=el,this.locator&&position(this.locator,el);for(var i=0;len>i;i++){var namespaceURI=attrs.getURI(i),value=attrs.getValue(i),qName=attrs.getQName(i),attr=doc.createAttributeNS(namespaceURI,qName);attr.getOffset&&position(attr.getOffset(1),attr),attr.value=attr.nodeValue=value,el.setAttributeNode(attr)}},endElement:function(){var current=this.currentElement;current.tagName,this.currentElement=current.parentNode},startPrefixMapping:function(){},endPrefixMapping:function(){},processingInstruction:function(target,data){var ins=this.document.createProcessingInstruction(target,data);this.locator&&position(this.locator,ins),appendElement(this,ins)},ignorableWhitespace:function(){},characters:function(chars){if(chars=_toString.apply(this,arguments),this.currentElement&&chars){if(this.cdata){var charNode=this.document.createCDATASection(chars);this.currentElement.appendChild(charNode)}else{var charNode=this.document.createTextNode(chars);this.currentElement.appendChild(charNode)}this.locator&&position(this.locator,charNode)}},skippedEntity:function(){},endDocument:function(){this.document.normalize()},setDocumentLocator:function(locator){(this.locator=locator)&&(locator.lineNumber=0)},comment:function(chars){chars=_toString.apply(this,arguments);var comm=this.document.createComment(chars);this.locator&&position(this.locator,comm),appendElement(this,comm)},startCDATA:function(){this.cdata=!0},endCDATA:function(){this.cdata=!1},startDTD:function(name,publicId,systemId){var impl=this.document.implementation;if(impl&&impl.createDocumentType){var dt=impl.createDocumentType(name,publicId,systemId);this.locator&&position(this.locator,dt),appendElement(this,dt)}},warning:function(error){console.warn(error,_locator(this.locator))},error:function(error){console.error(error,_locator(this.locator))},fatalError:function(error){throw console.error(error,_locator(this.locator)),error}},\"endDTD,startEntity,endEntity,attributeDecl,elementDecl,externalEntityDecl,internalEntityDecl,resolveEntity,getExternalSubset,notationDecl,unparsedEntityDecl\".replace(/\\w+/g,function(key){DOMHandler.prototype[key]=function(){return null}}),{DOMParser:DOMParser}}),ace.define(\"ace/mode/xml_worker\",[\"require\",\"exports\",\"module\",\"ace/lib/oop\",\"ace/lib/lang\",\"ace/worker/mirror\",\"ace/mode/xml/dom-parser\"],function(acequire,exports){\"use strict\";var oop=acequire(\"../lib/oop\");acequire(\"../lib/lang\");var Mirror=acequire(\"../worker/mirror\").Mirror,DOMParser=acequire(\"./xml/dom-parser\").DOMParser,Worker=exports.Worker=function(sender){Mirror.call(this,sender),this.setTimeout(400),this.context=null};oop.inherits(Worker,Mirror),function(){this.setOptions=function(options){this.context=options.context},this.onUpdate=function(){var value=this.doc.getValue();if(value){var parser=new DOMParser,errors=[];parser.options.errorHandler={fatalError:function(fullMsg,errorMsg,locator){errors.push({row:locator.lineNumber,column:locator.columnNumber,text:errorMsg,type:\"error\"})},error:function(fullMsg,errorMsg,locator){errors.push({row:locator.lineNumber,column:locator.columnNumber,text:errorMsg,type:\"error\"})},warning:function(fullMsg,errorMsg,locator){errors.push({row:locator.lineNumber,column:locator.columnNumber,text:errorMsg,type:\"warning\"})}},parser.parseFromString(value),this.sender.emit(\"error\",errors)}}}.call(Worker.prototype)}),ace.define(\"ace/lib/es5-shim\",[\"require\",\"exports\",\"module\"],function(){function Empty(){}function doesDefinePropertyWork(object){try{return Object.defineProperty(object,\"sentinel\",{}),\"sentinel\"in object\n}catch(exception){}}function toInteger(n){return n=+n,n!==n?n=0:0!==n&&n!==1/0&&n!==-(1/0)&&(n=(n>0||-1)*Math.floor(Math.abs(n))),n}Function.prototype.bind||(Function.prototype.bind=function(that){var target=this;if(\"function\"!=typeof target)throw new TypeError(\"Function.prototype.bind called on incompatible \"+target);var args=slice.call(arguments,1),bound=function(){if(this instanceof bound){var result=target.apply(this,args.concat(slice.call(arguments)));return Object(result)===result?result:this}return target.apply(that,args.concat(slice.call(arguments)))};return target.prototype&&(Empty.prototype=target.prototype,bound.prototype=new Empty,Empty.prototype=null),bound});var defineGetter,defineSetter,lookupGetter,lookupSetter,supportsAccessors,call=Function.prototype.call,prototypeOfArray=Array.prototype,prototypeOfObject=Object.prototype,slice=prototypeOfArray.slice,_toString=call.bind(prototypeOfObject.toString),owns=call.bind(prototypeOfObject.hasOwnProperty);if((supportsAccessors=owns(prototypeOfObject,\"__defineGetter__\"))&&(defineGetter=call.bind(prototypeOfObject.__defineGetter__),defineSetter=call.bind(prototypeOfObject.__defineSetter__),lookupGetter=call.bind(prototypeOfObject.__lookupGetter__),lookupSetter=call.bind(prototypeOfObject.__lookupSetter__)),2!=[1,2].splice(0).length)if(function(){function makeArray(l){var a=Array(l+2);return a[0]=a[1]=0,a}var lengthBefore,array=[];return array.splice.apply(array,makeArray(20)),array.splice.apply(array,makeArray(26)),lengthBefore=array.length,array.splice(5,0,\"XXX\"),lengthBefore+1==array.length,lengthBefore+1==array.length?!0:void 0}()){var array_splice=Array.prototype.splice;Array.prototype.splice=function(start,deleteCount){return arguments.length?array_splice.apply(this,[void 0===start?0:start,void 0===deleteCount?this.length-start:deleteCount].concat(slice.call(arguments,2))):[]}}else Array.prototype.splice=function(pos,removeCount){var length=this.length;pos>0?pos>length&&(pos=length):void 0==pos?pos=0:0>pos&&(pos=Math.max(length+pos,0)),length>pos+removeCount||(removeCount=length-pos);var removed=this.slice(pos,pos+removeCount),insert=slice.call(arguments,2),add=insert.length;if(pos===length)add&&this.push.apply(this,insert);else{var remove=Math.min(removeCount,length-pos),tailOldPos=pos+remove,tailNewPos=tailOldPos+add-remove,tailCount=length-tailOldPos,lengthAfterRemove=length-remove;if(tailOldPos>tailNewPos)for(var i=0;tailCount>i;++i)this[tailNewPos+i]=this[tailOldPos+i];else if(tailNewPos>tailOldPos)for(i=tailCount;i--;)this[tailNewPos+i]=this[tailOldPos+i];if(add&&pos===lengthAfterRemove)this.length=lengthAfterRemove,this.push.apply(this,insert);else for(this.length=lengthAfterRemove+add,i=0;add>i;++i)this[pos+i]=insert[i]}return removed};Array.isArray||(Array.isArray=function(obj){return\"[object Array]\"==_toString(obj)});var boxedString=Object(\"a\"),splitString=\"a\"!=boxedString[0]||!(0 in boxedString);if(Array.prototype.forEach||(Array.prototype.forEach=function(fun){var object=toObject(this),self=splitString&&\"[object String]\"==_toString(this)?this.split(\"\"):object,thisp=arguments[1],i=-1,length=self.length>>>0;if(\"[object Function]\"!=_toString(fun))throw new TypeError;for(;length>++i;)i in self&&fun.call(thisp,self[i],i,object)}),Array.prototype.map||(Array.prototype.map=function(fun){var object=toObject(this),self=splitString&&\"[object String]\"==_toString(this)?this.split(\"\"):object,length=self.length>>>0,result=Array(length),thisp=arguments[1];if(\"[object Function]\"!=_toString(fun))throw new TypeError(fun+\" is not a function\");for(var i=0;length>i;i++)i in self&&(result[i]=fun.call(thisp,self[i],i,object));return result}),Array.prototype.filter||(Array.prototype.filter=function(fun){var value,object=toObject(this),self=splitString&&\"[object String]\"==_toString(this)?this.split(\"\"):object,length=self.length>>>0,result=[],thisp=arguments[1];if(\"[object Function]\"!=_toString(fun))throw new TypeError(fun+\" is not a function\");for(var i=0;length>i;i++)i in self&&(value=self[i],fun.call(thisp,value,i,object)&&result.push(value));return result}),Array.prototype.every||(Array.prototype.every=function(fun){var object=toObject(this),self=splitString&&\"[object String]\"==_toString(this)?this.split(\"\"):object,length=self.length>>>0,thisp=arguments[1];if(\"[object Function]\"!=_toString(fun))throw new TypeError(fun+\" is not a function\");for(var i=0;length>i;i++)if(i in self&&!fun.call(thisp,self[i],i,object))return!1;return!0}),Array.prototype.some||(Array.prototype.some=function(fun){var object=toObject(this),self=splitString&&\"[object String]\"==_toString(this)?this.split(\"\"):object,length=self.length>>>0,thisp=arguments[1];if(\"[object Function]\"!=_toString(fun))throw new TypeError(fun+\" is not a function\");for(var i=0;length>i;i++)if(i in self&&fun.call(thisp,self[i],i,object))return!0;return!1}),Array.prototype.reduce||(Array.prototype.reduce=function(fun){var object=toObject(this),self=splitString&&\"[object String]\"==_toString(this)?this.split(\"\"):object,length=self.length>>>0;if(\"[object Function]\"!=_toString(fun))throw new TypeError(fun+\" is not a function\");if(!length&&1==arguments.length)throw new TypeError(\"reduce of empty array with no initial value\");var result,i=0;if(arguments.length>=2)result=arguments[1];else for(;;){if(i in self){result=self[i++];break}if(++i>=length)throw new TypeError(\"reduce of empty array with no initial value\")}for(;length>i;i++)i in self&&(result=fun.call(void 0,result,self[i],i,object));return result}),Array.prototype.reduceRight||(Array.prototype.reduceRight=function(fun){var object=toObject(this),self=splitString&&\"[object String]\"==_toString(this)?this.split(\"\"):object,length=self.length>>>0;if(\"[object Function]\"!=_toString(fun))throw new TypeError(fun+\" is not a function\");if(!length&&1==arguments.length)throw new TypeError(\"reduceRight of empty array with no initial value\");var result,i=length-1;if(arguments.length>=2)result=arguments[1];else for(;;){if(i in self){result=self[i--];break}if(0>--i)throw new TypeError(\"reduceRight of empty array with no initial value\")}do i in this&&(result=fun.call(void 0,result,self[i],i,object));while(i--);return result}),Array.prototype.indexOf&&-1==[0,1].indexOf(1,2)||(Array.prototype.indexOf=function(sought){var self=splitString&&\"[object String]\"==_toString(this)?this.split(\"\"):toObject(this),length=self.length>>>0;if(!length)return-1;var i=0;for(arguments.length>1&&(i=toInteger(arguments[1])),i=i>=0?i:Math.max(0,length+i);length>i;i++)if(i in self&&self[i]===sought)return i;return-1}),Array.prototype.lastIndexOf&&-1==[0,1].lastIndexOf(0,-3)||(Array.prototype.lastIndexOf=function(sought){var self=splitString&&\"[object String]\"==_toString(this)?this.split(\"\"):toObject(this),length=self.length>>>0;if(!length)return-1;var i=length-1;for(arguments.length>1&&(i=Math.min(i,toInteger(arguments[1]))),i=i>=0?i:length-Math.abs(i);i>=0;i--)if(i in self&&sought===self[i])return i;return-1}),Object.getPrototypeOf||(Object.getPrototypeOf=function(object){return object.__proto__||(object.constructor?object.constructor.prototype:prototypeOfObject)}),!Object.getOwnPropertyDescriptor){var ERR_NON_OBJECT=\"Object.getOwnPropertyDescriptor called on a non-object: \";Object.getOwnPropertyDescriptor=function(object,property){if(\"object\"!=typeof object&&\"function\"!=typeof object||null===object)throw new TypeError(ERR_NON_OBJECT+object);if(owns(object,property)){var descriptor,getter,setter;if(descriptor={enumerable:!0,configurable:!0},supportsAccessors){var prototype=object.__proto__;object.__proto__=prototypeOfObject;var getter=lookupGetter(object,property),setter=lookupSetter(object,property);if(object.__proto__=prototype,getter||setter)return getter&&(descriptor.get=getter),setter&&(descriptor.set=setter),descriptor}return descriptor.value=object[property],descriptor}}}if(Object.getOwnPropertyNames||(Object.getOwnPropertyNames=function(object){return Object.keys(object)}),!Object.create){var createEmpty;createEmpty=null===Object.prototype.__proto__?function(){return{__proto__:null}}:function(){var empty={};for(var i in empty)empty[i]=null;return empty.constructor=empty.hasOwnProperty=empty.propertyIsEnumerable=empty.isPrototypeOf=empty.toLocaleString=empty.toString=empty.valueOf=empty.__proto__=null,empty},Object.create=function(prototype,properties){var object;if(null===prototype)object=createEmpty();else{if(\"object\"!=typeof prototype)throw new TypeError(\"typeof prototype[\"+typeof prototype+\"] != 'object'\");var Type=function(){};Type.prototype=prototype,object=new Type,object.__proto__=prototype}return void 0!==properties&&Object.defineProperties(object,properties),object}}if(Object.defineProperty){var definePropertyWorksOnObject=doesDefinePropertyWork({}),definePropertyWorksOnDom=\"undefined\"==typeof document||doesDefinePropertyWork(document.createElement(\"div\"));if(!definePropertyWorksOnObject||!definePropertyWorksOnDom)var definePropertyFallback=Object.defineProperty}if(!Object.defineProperty||definePropertyFallback){var ERR_NON_OBJECT_DESCRIPTOR=\"Property description must be an object: \",ERR_NON_OBJECT_TARGET=\"Object.defineProperty called on non-object: \",ERR_ACCESSORS_NOT_SUPPORTED=\"getters & setters can not be defined on this javascript engine\";Object.defineProperty=function(object,property,descriptor){if(\"object\"!=typeof object&&\"function\"!=typeof object||null===object)throw new TypeError(ERR_NON_OBJECT_TARGET+object);if(\"object\"!=typeof descriptor&&\"function\"!=typeof descriptor||null===descriptor)throw new TypeError(ERR_NON_OBJECT_DESCRIPTOR+descriptor);if(definePropertyFallback)try{return definePropertyFallback.call(Object,object,property,descriptor)}catch(exception){}if(owns(descriptor,\"value\"))if(supportsAccessors&&(lookupGetter(object,property)||lookupSetter(object,property))){var prototype=object.__proto__;object.__proto__=prototypeOfObject,delete object[property],object[property]=descriptor.value,object.__proto__=prototype}else object[property]=descriptor.value;else{if(!supportsAccessors)throw new TypeError(ERR_ACCESSORS_NOT_SUPPORTED);owns(descriptor,\"get\")&&defineGetter(object,property,descriptor.get),owns(descriptor,\"set\")&&defineSetter(object,property,descriptor.set)}return object}}Object.defineProperties||(Object.defineProperties=function(object,properties){for(var property in properties)owns(properties,property)&&Object.defineProperty(object,property,properties[property]);return object}),Object.seal||(Object.seal=function(object){return object}),Object.freeze||(Object.freeze=function(object){return object});try{Object.freeze(function(){})}catch(exception){Object.freeze=function(freezeObject){return function(object){return\"function\"==typeof object?object:freezeObject(object)}}(Object.freeze)}if(Object.preventExtensions||(Object.preventExtensions=function(object){return object}),Object.isSealed||(Object.isSealed=function(){return!1}),Object.isFrozen||(Object.isFrozen=function(){return!1}),Object.isExtensible||(Object.isExtensible=function(object){if(Object(object)===object)throw new TypeError;for(var name=\"\";owns(object,name);)name+=\"?\";object[name]=!0;var returnValue=owns(object,name);return delete object[name],returnValue}),!Object.keys){var hasDontEnumBug=!0,dontEnums=[\"toString\",\"toLocaleString\",\"valueOf\",\"hasOwnProperty\",\"isPrototypeOf\",\"propertyIsEnumerable\",\"constructor\"],dontEnumsLength=dontEnums.length;for(var key in{toString:null})hasDontEnumBug=!1;Object.keys=function(object){if(\"object\"!=typeof object&&\"function\"!=typeof object||null===object)throw new TypeError(\"Object.keys called on a non-object\");var keys=[];for(var name in object)owns(object,name)&&keys.push(name);if(hasDontEnumBug)for(var i=0,ii=dontEnumsLength;ii>i;i++){var dontEnum=dontEnums[i];owns(object,dontEnum)&&keys.push(dontEnum)}return keys}}Date.now||(Date.now=function(){return(new Date).getTime()});var ws=\"\t\\n\u000b\\f\\r   ᠎             　\\u2028\\u2029﻿\";if(!String.prototype.trim||ws.trim()){ws=\"[\"+ws+\"]\";var trimBeginRegexp=RegExp(\"^\"+ws+ws+\"*\"),trimEndRegexp=RegExp(ws+ws+\"*$\");String.prototype.trim=function(){return(this+\"\").replace(trimBeginRegexp,\"\").replace(trimEndRegexp,\"\")}}var toObject=function(o){if(null==o)throw new TypeError(\"can't convert \"+o+\" to object\");return Object(o)}});";

/***/ })

});