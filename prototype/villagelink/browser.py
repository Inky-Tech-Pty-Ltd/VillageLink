from __future__ import annotations

import sys
from dataclasses import dataclass
from urllib.parse import quote, urlparse

from PySide6.QtCore import QTimer, QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QSplitter, QVBoxLayout, QWidget

from .codec import parse as parse_village_link

HOME_URL = "https://home.village.link/"
STAR_CREDENTIAL_URL = "https://home.village.link/star-credential"
MARKER = "https://wab.village.link/"

HOME_HTML = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Village Link</title>
<style>
:root{color-scheme:light}*{box-sizing:border-box}body{margin:0;min-height:100vh;background:#fff;color:#202124;font-family:Arial,Helvetica,sans-serif}.favorites-bar{position:fixed;top:0;left:0;right:0;height:52px;display:flex;align-items:center;justify-content:flex-start;gap:8px;padding:8px 14px;background:#f8f9fa;border-bottom:1px solid #e3e6ea;z-index:10}.favorite{display:inline-flex;align-items:center;height:34px;padding:0 14px;border:1px solid #d9dde3;border-radius:6px;background:#fff;color:#3c4043;text-decoration:none;font-size:14px;white-space:nowrap}.favorite:hover{background:#f1f3f4}.favorite:active{background:#e8eaed}main{width:min(760px,calc(100vw - 64px));margin:104px auto 0;text-align:center}.mark{font-size:64px;line-height:1;margin-bottom:10px;color:#d81b86}h1{margin:0 0 30px;font-size:48px;font-weight:400;letter-spacing:-1px}.trust{width:100%;height:54px;border:1px solid #dfe1e5;border-radius:27px;box-shadow:0 1px 6px rgba(32,33,36,.18);display:flex;align-items:center;padding:0 20px;color:#9aa0a6;font-size:17px;text-align:left}.trust::before{content:"⌕";margin-right:14px;font-size:25px;color:#5f6368}.composer{margin-top:30px;text-align:left}.composer-head{display:flex;align-items:center;justify-content:space-between;gap:16px;margin:0 4px 14px}.mode-select{border:0;background:transparent;color:#3c4043;font:600 15px Arial,Helvetica,sans-serif;padding:0 22px 0 0;cursor:pointer;outline:none}.compose-button{padding:10px 18px;border:1px solid #dadce0;border-radius:18px;background:#f8f9fa;color:#3c4043;font-size:14px;cursor:pointer}.compose-button:hover,.more-button:hover{background:#f1f3f4}.endpoint{width:100%;height:44px;margin:0 0 14px;padding:0 15px;border:1px solid #dadce0;border-radius:22px;outline:none;font-size:14px;color:#202124}.endpoint:focus{border-color:#9aa0a6;box-shadow:0 1px 4px rgba(32,33,36,.12)}.more-button{display:none;padding:10px 14px;border:1px solid #dadce0;border-radius:18px;background:#f8f9fa;color:#3c4043;font-size:14px;cursor:pointer;margin:0 0 14px}.message{min-height:20px;margin:2px 4px 0;color:#b3261e;font-size:14px}.result{display:none;margin-top:14px}.result a{display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:#1a73e8;text-decoration:none;padding:9px 12px;border:1px solid #dadce0;border-radius:18px}.result pre{margin:0;padding:16px;border:1px solid #dadce0;border-radius:14px;background:#f8f9fa;white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.5 Consolas,"Courier New",monospace}
</style></head><body><nav class="favorites-bar" aria-label="Favourites"><a class="favorite" href="https://village.link/wiki/index.php/Asha_Bhosle">Asha Bhosle</a><a class="favorite" href="https://village.link/wiki/index.php/Puck-GPT">Puck-GPT</a><a class="favorite" href="https://village.link/wiki/index.php/Joe_Rasmussen">Joe Rasmussen</a></nav><main><div class="mark">✱</div><h1>Village Link</h1><div class="trust">Trust engine</div><section class="composer"><div class="composer-head"><select id="mode" class="mode-select" onchange="setComposerMode(this.value)"><option value="link">Compose a village link:</option><option value="star">Compose a star credential:</option></select><button class="compose-button" type="button" onclick="composeCurrent()">Compose</button></div><input id="endpoint-a" class="endpoint" type="text" inputmode="url" placeholder="A — first URL"><div id="b-fields"></div><button id="more-b" class="more-button" type="button" onclick="addB()">+ more links if required ...</button><div id="message" class="message" role="alert" aria-live="polite"></div><div id="result" class="result"></div></section></main>
<script>
const marker="https://wab.village.link/";
function encodeEndpoint(v){return encodeURIComponent(v).replace(/[!'()*]/g,c=>'%' + c.charCodeAt(0).toString(16).toUpperCase())}
function isUri(value){return /^[A-Za-z][A-Za-z0-9+.-]*:/.test(value)}
function makeInput(id,placeholder,value=''){const input=document.createElement('input');input.id=id;input.className='endpoint b-endpoint';input.type='text';input.inputMode='url';input.placeholder=placeholder;input.autocomplete='off';input.value=value;return input}
function renderLinkFields(){const fields=document.getElementById('b-fields');fields.replaceChildren(makeInput('endpoint-b','B — second URL'));document.getElementById('endpoint-a').placeholder='A — first URL';document.getElementById('more-b').style.display='none'}
function renderStarFields(){const fields=document.getElementById('b-fields');fields.replaceChildren(makeInput('b1','B1 — the first link'),makeInput('b2','B2 — the second link'),makeInput('b3','B3 — the third link'));document.getElementById('endpoint-a').placeholder='A — a URL for the centre of the star';document.getElementById('more-b').style.display='inline-block'}
function addB(){const fields=document.getElementById('b-fields'),n=fields.querySelectorAll('.b-endpoint').length+1;fields.appendChild(makeInput('b'+n,'B'+n+' — another link'))}
function setComposerMode(mode){document.getElementById('message').textContent='';document.getElementById('result').style.display='none';document.getElementById('result').replaceChildren();if(mode==='star')renderStarFields();else renderLinkFields()}
function composeCurrent(){if(document.getElementById('mode').value==='star')composeStarCredential();else composeVillageLink()}
function composeVillageLink(){const a=document.getElementById('endpoint-a').value.trim(),b=document.getElementById('endpoint-b').value.trim(),message=document.getElementById('message'),result=document.getElementById('result');message.textContent='';if(!a||!b){message.textContent='Enter both URLs.';return}const composed=marker+encodeEndpoint(a)+'!'+encodeEndpoint(b);const link=document.createElement('a');link.href=composed;link.textContent=composed;link.title=composed;result.replaceChildren(link);result.style.display='block'}
function composeStarCredential(){const a=document.getElementById('endpoint-a').value.trim(),entered=[...document.querySelectorAll('.b-endpoint')].map(input=>input.value.trim()).filter(Boolean),message=document.getElementById('message'),result=document.getElementById('result');message.textContent='';if(!a){message.textContent='Enter the centre URI A.';return}if(!isUri(a)){message.textContent='A must be a URI with a scheme, such as https:, mailto: or urn:.';return}const invalid=entered.find(value=>!isUri(value));if(invalid){message.textContent='Every B must be a URI with a scheme.';return}const members=[...new Set(entered)].sort(),credential={type:'StarCredential',A:a,B:members},pre=document.createElement('pre');pre.textContent=JSON.stringify(credential,null,2);result.replaceChildren(pre);result.style.display='block'}
const initialMode=location.pathname.includes('star-credential')?'star':'link';document.getElementById('mode').value=initialMode;setComposerMode(initialMode);
</script></body></html>"""


def village_targets(raw_url: str) -> tuple[str, str] | None:
    try: return parse_village_link(raw_url)
    except ValueError: return None


def compose_village_link(left: str, right: str) -> str:
    return MARKER + quote(left, safe="-._~") + "!" + quote(right, safe="-._~")


@dataclass(frozen=True)
class BrowserState:
    kind: str
    left: str = ""
    right: str | None = None
    village_link: str | None = None


class VillagePage(QWebEnginePage):
    def __init__(self, browser: "Browser", parent: QWebEngineView, side: str) -> None:
        super().__init__(parent); self.browser=browser; self.side=side
    def acceptNavigationRequest(self, url: QUrl, nav_type, is_main_frame: bool) -> bool:  # noqa: N802
        if is_main_frame:
            if self.side=="left" and url.scheme()=="data":
                return super().acceptNavigationRequest(url,nav_type,is_main_frame)
            if self.side=="left" and url.toString().rstrip("/")==STAR_CREDENTIAL_URL.rstrip("/"):
                QTimer.singleShot(0,lambda:self.browser.show_star_credential_composer(remember=True));return False
            if self.side=="left" and url.toString().rstrip("/")==HOME_URL.rstrip("/") and self.browser._composer_visible:
                QTimer.singleShot(0,lambda:self.browser.show_home(remember=True));return False
            targets=village_targets(url.toString())
            if targets:
                QTimer.singleShot(0,lambda:self.browser.open_village_link(*targets,village_link=url.toString(),remember=True));return False
            if self.side=="left" and self.browser.consume_internal_left_navigation(url): return super().acceptNavigationRequest(url,nav_type,is_main_frame)
            if self.side=="left" and (self.browser._home_visible or self.browser._composer_visible):
                target=url.toString();QTimer.singleShot(0,lambda target=target:self.browser.open_single(target,remember=True));return False
        return super().acceptNavigationRequest(url,nav_type,is_main_frame)


class Browser(QMainWindow):
    def __init__(self) -> None:
        super().__init__();self.setWindowTitle("Village Link Browser — prototype");self.resize(1400,900)
        self._internal_left_url=None;self._state_history=[];self._current_village_link=None;self._home_visible=False;self._composer_visible=False

        self.home=QPushButton("⌂");self.home.setToolTip("Home");self.home.setFixedWidth(38);self.home.clicked.connect(lambda:self.show_home(remember=True))
        self.global_back=QPushButton("←");self.global_back.setToolTip("Back");self.global_back.setFixedWidth(38);self.global_back.clicked.connect(self.go_global_back)
        self.global_address=QLineEdit();self.global_address.setPlaceholderText("URL or Village Link");self.global_address.returnPressed.connect(self.navigate_global)
        self.copy_link=QPushButton("⧉");self.copy_link.setToolTip("Copy Village Link");self.copy_link.setFixedWidth(38);self.copy_link.clicked.connect(self.copy_village_link);self.copy_link.hide()
        self.dismiss_w=QPushButton("×");self.dismiss_w.setToolTip("Dismiss and return Home");self.dismiss_w.setFixedWidth(38);self.dismiss_w.clicked.connect(lambda:self.show_home(remember=True));self.dismiss_w.hide()
        global_bar=QHBoxLayout();global_bar.setContentsMargins(0,0,0,0);global_bar.addWidget(self.home);global_bar.addWidget(self.global_back);global_bar.addWidget(self.global_address);global_bar.addWidget(self.copy_link);global_bar.addWidget(self.dismiss_w)

        self.left=QWebEngineView();self.right=QWebEngineView();self.left.setPage(VillagePage(self,self.left,"left"));self.right.setPage(VillagePage(self,self.right,"right"))
        self.left_box=self._make_pane("left",self.left);self.right_box=self._make_pane("right",self.right)
        self.left.urlChanged.connect(self.on_left_url_changed);self.right.urlChanged.connect(lambda u:self.right_address.setText(u.toString()))
        self.splitter=QSplitter();self.splitter.setChildrenCollapsible(False);self.splitter.setHandleWidth(1);self.splitter.setStyleSheet("QSplitter::handle { background: #d0d0d0; }");self.splitter.addWidget(self.left_box);self.splitter.addWidget(self.right_box);self.splitter.setSizes([700,700])

        root=QWidget();layout=QVBoxLayout(root);layout.setContentsMargins(8,8,8,8);layout.setSpacing(6);layout.addLayout(global_bar);layout.addWidget(self.splitter);self.setCentralWidget(root);self.show_home(remember=False)

    def _make_pane(self, side: str, view: QWebEngineView) -> QWidget:
        back=QPushButton("←");back.setToolTip("Back");back.setFixedWidth(38);back.clicked.connect(view.back)
        address=QLineEdit();address.returnPressed.connect(lambda s=side:self.navigate_pane(s))
        promote=QPushButton("□");promote.setToolTip("Promote");promote.setFixedWidth(38);promote.clicked.connect(lambda _=False,s=side:self.promote_pane(s))
        close=QPushButton("×");close.setToolTip("Close");close.setFixedWidth(38);close.clicked.connect(lambda _=False,s=side:self.close_pane(s))
        bar=QHBoxLayout();bar.setSpacing(4)
        if side=="left":bar.setContentsMargins(0,0,2,0)
        else:bar.setContentsMargins(2,0,0,0)
        bar.addWidget(back);bar.addWidget(address);bar.addWidget(promote);bar.addWidget(close)
        view_box=QWidget();view_layout=QVBoxLayout(view_box);view_layout.setSpacing(0)
        if side=="left":view_layout.setContentsMargins(0,0,4,0)
        else:view_layout.setContentsMargins(4,0,0,0)
        view_layout.addWidget(view)
        box=QWidget();box_layout=QVBoxLayout(box);box_layout.setContentsMargins(0,0,0,0);box_layout.setSpacing(4);box_layout.addLayout(bar);box_layout.addWidget(view_box)
        if side=="left":self.left_back=back;self.left_address=address;self.left_promote=promote;self.left_close=close
        else:self.right_back=back;self.right_address=address;self.right_promote=promote;self.right_close=close
        return box

    def on_left_url_changed(self,url:QUrl)->None:
        value=url.toString();self.left_address.setText(value)
        if self._home_visible:self.set_global_address(HOME_URL);return
        if self._composer_visible:self.set_global_address(STAR_CREDENTIAL_URL);return
        if not self.right_box.isVisible():self.set_global_address(value)

    def current_state(self) -> BrowserState:
        if self._composer_visible:return BrowserState("composer")
        if self._home_visible:return BrowserState("home")
        if self.right_box.isVisible():return BrowserState("split",self.left.url().toString(),self.right.url().toString(),self._current_village_link)
        return BrowserState("single",self.left.url().toString())

    def remember_current_state(self) -> None:self._state_history.append(self.current_state())
    def consume_internal_left_navigation(self, url: QUrl) -> bool:
        if self._internal_left_url and url==self._internal_left_url:self._internal_left_url=None;return True
        return False
    def load_left(self,url:QUrl)->None:self._internal_left_url=url;self.left.setUrl(url)
    def set_global_address(self,value:str)->None:self.global_address.setText(value)
    def _prepare_standard(self)->None:self._home_visible=False;self._composer_visible=False;self.left.setZoomFactor(1.0);self.right.setZoomFactor(1.0);self.copy_link.hide();self.dismiss_w.hide()

    def _set_left_pane_chrome(self,visible:bool)->None:
        for widget in (self.left_back,self.left_address,self.left_promote,self.left_close):widget.setVisible(visible)

    def show_home(self,remember:bool)->None:
        if remember:self.remember_current_state()
        self._home_visible=True;self._composer_visible=False;self._current_village_link=None;self.copy_link.hide();self.dismiss_w.hide();self.right_box.hide();self._set_left_pane_chrome(False);self.left.setZoomFactor(1.0);self.left.setHtml(HOME_HTML,QUrl(HOME_URL));self.set_global_address(HOME_URL)

    def show_star_credential_composer(self,remember:bool)->None:
        if remember:self.remember_current_state()
        self._home_visible=False;self._composer_visible=True;self._current_village_link=None;self.copy_link.hide();self.dismiss_w.hide();self.right_box.hide();self._set_left_pane_chrome(False);self.left.setZoomFactor(1.0);self.left.setHtml(HOME_HTML,QUrl(STAR_CREDENTIAL_URL));self.set_global_address(STAR_CREDENTIAL_URL)

    def navigate_global(self)->None:
        raw=self.global_address.text().strip()
        if not raw:return
        if raw.rstrip("/")==HOME_URL.rstrip("/"):self.show_home(remember=True);return
        if raw.rstrip("/")==STAR_CREDENTIAL_URL.rstrip("/"):self.show_star_credential_composer(remember=True);return
        targets=village_targets(raw)
        if targets:self.open_village_link(*targets,village_link=raw,remember=True);return
        self.open_single(raw,remember=True)
    def navigate_pane(self,side:str)->None:
        address=self.left_address if side=="left" else self.right_address;view=self.left if side=="left" else self.right;raw=address.text().strip()
        if not raw:return
        targets=village_targets(raw)
        if targets:self.open_village_link(*targets,village_link=raw,remember=True);return
        view.setUrl(QUrl.fromUserInput(raw))
    def open_single(self,url:str,remember:bool)->None:
        if remember:self.remember_current_state()
        self._prepare_standard();self.right_box.hide();self._set_left_pane_chrome(False);q=QUrl.fromUserInput(url);self.load_left(q);self.set_global_address(q.toString())
    def open_village_link(self,left:str,right:str,village_link:str|None=None,remember:bool=True)->None:
        if remember:self.remember_current_state()
        self._prepare_standard();self._current_village_link=village_link or compose_village_link(left,right);self.right_box.show();self._set_left_pane_chrome(True);self.left.setZoomFactor(0.85);self.right.setZoomFactor(0.85);self.load_left(QUrl(left));self.right.setUrl(QUrl(right));self.splitter.setSizes([700,700]);self.copy_link.show();self.dismiss_w.show();self.set_global_address(self._current_village_link)
    def promote_pane(self,side:str)->None:
        if not self.right_box.isVisible():return
        view=self.left if side=="left" else self.right;self.open_single(view.url().toString(),remember=True)
    def close_pane(self,side:str)->None:
        if not self.right_box.isVisible():return
        survivor=self.right if side=="left" else self.left;self.open_single(survivor.url().toString(),remember=True)
    def copy_village_link(self)->None:
        if self._current_village_link:QGuiApplication.clipboard().setText(self._current_village_link)
    def restore_state(self,state:BrowserState)->None:
        if state.kind=="home":self.show_home(remember=False)
        elif state.kind=="composer":self.show_star_credential_composer(remember=False)
        elif state.kind=="split" and state.right:self.open_village_link(state.left,state.right,village_link=state.village_link,remember=False)
        else:self.open_single(state.left,remember=False)
    def go_global_back(self)->None:
        if self._state_history:self.restore_state(self._state_history.pop())

    def place_on_screen(self)->None:
        screen=QGuiApplication.primaryScreen()
        if screen is None:return
        available=screen.availableGeometry();w=min(self.width(),available.width());h=min(self.height(),available.height());self.resize(w,h);self.move(available.x()+(available.width()-w)//2,available.y()+(available.height()-h)//2)


def main()->int:
    app=QApplication(sys.argv);browser=Browser();browser.place_on_screen();browser.show();return app.exec()


if __name__=="__main__":raise SystemExit(main())