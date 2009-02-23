from . import Tag

HTML_TAG_NAMES = ["a", "abbr", "acronym", "address", "applet", "area", "b",
                  "base", "basefont", "bdo", "big", "blockquote", "body", "br",
                  "button", "caption", "center", "cite", "code", "col",
                  "colgroup", "dd", "del_", "dfn", "dir", "div", "dl", "dt",
                  "em", "fieldset", "font", "form", "frame", "frameset", "h1",
                  "h2", "h3", "h4", "h5", "h6", "head", "hr", "html", "i",
                  "iframe", "img", "input", "ins", "isindex", "kbd", "label",
                  "legend", "li", "link", "map", "menu", "meta", "noframes",
                  "noscript", "object", "ol", "optgroup", "option", "param",
                  "p", "pre", "q", "s", "samp", "script", "select", "small",
                  "span", "strike", "strong", "style", "sub", "sup", "table",
                  "tbody", "td", "textarea", "tfoot", "th", "thead", "title",
                  "tr", "tt", "u", "ul", "var", "xmp"]

for _html_tag in HTML_TAG_NAMES:
    globals()[_html_tag] = Tag(_html_tag)
