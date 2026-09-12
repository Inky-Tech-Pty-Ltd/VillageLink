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
MARKER = "https://wab.village.link/"

HOME_HTML = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Village Link</title>
<style>
:root{color-scheme:light}*{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;background:#fff;color:#202124;font-family:Arial,Helvetica,sans-serif}main{width:min(760px,calc(100vw - 64px));text-align:center;transform:translateY(-3vh)}.mark{font-size:64px;line-height:1;margin-bottom:10px;color:#d81b86}h1{margin:0 0 30px;font-size:48px;font-weight:400;letter-spacing:-1px}.trust{width:100%;height:54px;border:1px solid #dfe1e5;border-radius:27px;box-shadow:0 1px 6px rgba(32,33,36,.18);display:flex;align-items:center;padding:0 20px;color:#9aa0a6;font-size:17px;text-align:left}.trust::before{content:"⌕";margin-right:14px;font-size:25px;color:#5f6368}.composer{margin-top:30px;text-align:left}.composer-title{margin:0 0 12px 4px;font-size:15px;font-weight:600;color:#5f6368}.endpoint{width:100%;height:44px;margin:7px 0;padding:0 15px;border:1px solid #dadce0;border-radius:22px;outline:none;font-size:14px;color:#202124}.endpoint:focus{border-color:#9aa0a6;box-shadow:0 1px 4px rgba(32,33,36,.12)}.compose-row{display:flex;align-items:center;gap:12px;margin-top:10px}button{padding:10px 18px;border:1px solid #dadce0;border-radius:18px;background:#f8f9fa;color:#3c4043;font-size:14px;cursor:pointer}button:hover{background:#f1f3f4}#result{flex:1;min-width:0;display:none;align-items:center;gap:6px}#result a{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:#1a73e8;text-decoration:none;padding:9px 12px;border:1px solid #dadce0;border-radius:18px}#result a:hover{background:#f8f9fa;text-decoration:underline}#copy{flex:0 0 auto;width:38px;padding:9px 0}.bookmarks{display:flex;justify-content:center;gap:12px;margin-top:24px;flex-wrap:wrap}.bookmark{display:inline-block;padding:10px 15px;border:1px solid #dadce0;border-radius:18px;color:#3c4043;text-decoration:none;background:#f8f9fa;font-size:14px}.bookmark:hover{background:#f1f3f4}
</style></head><body><main><div class="mark">✱</div><h1>Village Link</h1><div class="trust">Trust engine</div><section class="composer"><div class="composer-title">Compose a Village Link</div><input id="endpoint-a" class="endpoint" type="url" placeholder="A — first URL"><input id="endpoint-b" class="endpoint" type="url" placeholder="B — second URL"><div class="compose-row"><button type="button" onclick="composeVillageLink()">Compose</button><div id="result"><a id="result-link"></a><button id="copy" type="button" onclick="copyVillageLink()" title="Copy Village Link">⧉</button></div></div></section><div class="bookmarks"><a class="bookmark" href="https://village.link/wiki/index.php/Asha_Bhosle">Asha Bhosle</a><a class="bookmark" href="https://village.link/wiki/index.php/Puck-GPT">Puck-GPT</a><a class="bookmark" href="https://village.link/wiki/index.php/StarJoeRasmussen">Joe Rasmussen</a></div></main>
<script>const marker="https://wab.village.link/";let composed="";function encodeEndpoint(v){return encodeURIComponent(v).replace(/[!'()*]/g,c=>'%' + c.charCodeAt(0).toString(16).toUpperCase())}function composeVillageLink(){const a=document.getElementById('endpoint-a').value.trim(),b=document.getElementById('endpoint-b').value.trim(),r=document.getElementById('result'),l=document.getElementById('result-link');if(!a||!b){r.style.display='flex';l.removeAttribute('href');l.textContent='Enter both URLs.';return}composed=marker+encodeEndpoint(a)+'!'+encodeEndpoint(b);l.href=composed;l.textContent=composed;l.title=composed;r.style.display='flex'}function copyVillageLink(){if(!composed)return;navigator.clipboard.writeText(composed).then(()=>{const b=document.getElementById('copy');b.textContent='✓';setTimeout(()=>b.textContent='⧉',1200)})}</script></body></html>"""


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
            targets=village_targets(url.toString())
            if targets:
                QTimer.singleShot(0,lambda:self.browser.open_village_link(*targets,village_link=url.toString(),remember=True));return False
            if self.side=="left" and self.browser.consume_internal_left_navigation(url): return super().acceptNavigationRequest(url,nav_type,is_main_frame)
        return super().acceptNavigationRequest(url,nav_type,is_main_frame)


class Browser(QMainWindow):
    def __init__(self) -> None:
        super().__init__();self.setWindowTitle("Village Link Browser — prototype");self.resize(1400,900)
        self._internal_left_url=None;self._state_history=[];self._current_village_link=None;self._home_visible=False

        self.home=QPushButton("⌂");self.home.setToolTip("Home");self.home.setFixedWidth(38);self.home.clicked.connect(lambda:self.show_home(remember=True))
        self.global_back=QPushButton("←");self.global_back.setToolTip("Back");self.global_back.setFixedWidth(38);self.global_back.clicked.connect(self.go_global_back)
        self.global_address=QLineEdit();self.global_address.setPlaceholderText("URL or Village Link");self.global_address.returnPressed.connect(self.navigate_global)
        self.copy_link=QPushButton("⧉");self.copy_link.setToolTip("Copy Village Link");self.copy_link.setFixedWidth(38);self.copy_link.clicked.connect(self.copy_village_link);self.copy_link.hide()
        self.dismiss_w=QPushButton("×");self.dismiss_w.setToolTip("Dismiss and return Home");self.dismiss_w.setFixedWidth(38);self.dismiss_w.clicked.connect(lambda:self.show_home(remember=True));self.dismiss_w.hide()
        global_bar=QHBoxLayout();global_bar.setContentsMargins(0,0,0,0);global_bar.addWidget(self.home);global_bar.addWidget(self.global_back);global_bar.addWidget(self.global_address);global_bar.addWidget(self.copy_link);global_bar.addWidget(self.dismiss_w)

        self.left=QWebEngineView();self.right=QWebEngineView();self.left.setPage(VillagePage(self,self.left,"left"));self.right.setPage(VillagePage(self,self.right,"right"))
        self.left_box=self._make_pane("left",self.left);self.right_box=self._make_pane("right",self.right)
        self.left.urlChanged.connect(lambda u:self.left_address.setText(u.toString()));self.right.urlChanged.connect(lambda u:self.right_address.setText(u.toString()))
        self.splitter=QSplitter();self.splitter.setChildrenCollapsible(False);self.splitter.addWidget(self.left_box);self.splitter.addWidget(self.right_box)
        layout=QVBoxLayout();layout.addLayout(global_bar);layout.addWidget(self.splitter);container=QWidget();container.setLayout(layout);self.setCentralWidget(container);self.show_home()

    def _make_pane(self,side,view):
        back=QPushButton("←");back.setToolTip("Back");back.setFixedWidth(34);back.clicked.connect(view.back)
        address=QLineEdit();address.returnPressed.connect(lambda:self.navigate_pane(side))
        promote=QPushButton("□");promote.setToolTip("Promote");promote.setFixedWidth(34);promote.clicked.connect(lambda:self.promote_pane(side))
        close=QPushButton("×");close.setToolTip("Close");close.setFixedWidth(34);close.clicked.connect(lambda:self.close_pane(side))
        bar=QHBoxLayout();bar.setContentsMargins(0,0,0,0);bar.setSpacing(4);bar.addWidget(back);bar.addWidget(address);bar.addWidget(promote);bar.addWidget(close)
        box=QWidget();lay=QVBoxLayout(box);lay.setContentsMargins(0,0,0,0);lay.setSpacing(4);lay.addLayout(bar);lay.addWidget(view)
        setattr(self,f"{side}_back",back);setattr(self,f"{side}_address",address);setattr(self,f"{side}_promote",promote);setattr(self,f"{side}_close",close);return box

    def is_split(self): return not self.right_box.isHidden()
    def current_state(self):
        if self._home_visible:return BrowserState("home")
        if self.is_split():return BrowserState("split",self.left.url().toString(),self.right.url().toString(),self._current_village_link)
        return BrowserState("single",self.left.url().toString())
    def remember_state(self):
        s=self.current_state()
        if not self._state_history or self._state_history[-1]!=s:self._state_history.append(s)
    def consume_internal_left_navigation(self,url):
        if self._internal_left_url is None or url.toString()!=self._internal_left_url:return False
        self._internal_left_url=None;return True
    def _show_split_chrome(self,visible):
        self.copy_link.setVisible(visible);self.dismiss_w.setVisible(visible);self.right_box.setVisible(visible)
        self.left_box.findChildren(QPushButton)[0].setVisible(visible);self.left_address.setVisible(visible);self.left_promote.setVisible(visible);self.left_close.setVisible(visible)
    def show_home(self,*,remember=False):
        if remember and not self._home_visible:self.remember_state()
        self._home_visible=True;self._current_village_link=None;self._internal_left_url=None;self.right_box.hide();self.copy_link.hide();self.dismiss_w.hide();self.global_address.setText(HOME_URL)
        for w in (self.left_back,self.left_address,self.left_promote,self.left_close):w.hide()
        self.left.setHtml(HOME_HTML,QUrl(HOME_URL))
    def open_single(self,url,*,remember=False):
        if remember:self.remember_state()
        self._home_visible=False;self._current_village_link=None;self._internal_left_url=QUrl(url).toString();self.right_box.hide();self.copy_link.hide();self.dismiss_w.hide();self.global_address.setText(url)
        for w in (self.left_back,self.left_address,self.left_promote,self.left_close):w.hide()
        self.left.setUrl(QUrl(url))
    def open_village_link(self,left,right,*,village_link=None,remember=False):
        if remember:self.remember_state()
        self._home_visible=False;self._current_village_link=village_link or compose_village_link(left,right);self.global_address.setText(self._current_village_link);self._internal_left_url=QUrl(left).toString();self.left.setUrl(QUrl(left));self.right.setUrl(QUrl(right));self._show_split_chrome(True);self.splitter.setSizes([1,1])
    def restore_state(self,s):
        if s.kind=="home":self.show_home()
        elif s.kind=="split" and s.right is not None:self.open_village_link(s.left,s.right,village_link=s.village_link)
        else:self.open_single(s.left)
    def go_global_back(self):
        if self._state_history:self.restore_state(self._state_history.pop())
    def navigate_global(self):
        raw=self.global_address.text().strip()
        if not raw or raw==HOME_URL:self.show_home(remember=True);return
        if not urlparse(raw).scheme:raw="https://"+raw;self.global_address.setText(raw)
        targets=village_targets(raw)
        if targets:self.open_village_link(*targets,village_link=raw,remember=True)
        else:self.open_single(raw,remember=True)
    def navigate_pane(self,side):
        edit=self.left_address if side=="left" else self.right_address;view=self.left if side=="left" else self.right;raw=edit.text().strip()
        if raw and not urlparse(raw).scheme:raw="https://"+raw;edit.setText(raw)
        if raw:view.setUrl(QUrl(raw))
    def promote_pane(self,side):
        if not self.is_split():return
        self.remember_state();view=self.left if side=="left" else self.right;self.open_single(view.url().toString())
    def close_pane(self,side):
        if not self.is_split():return
        self.remember_state();survivor=self.right if side=="left" else self.left;self.open_single(survivor.url().toString())
    def copy_village_link(self):
        if self._current_village_link:
            QApplication.clipboard().setText(self._current_village_link);self.copy_link.setText("✓");QTimer.singleShot(1200,lambda:self.copy_link.setText("⧉"))
    def place_on_screen(self):
        screen=QGuiApplication.primaryScreen()
        if screen is None:return
        a=screen.availableGeometry();w=min(self.width(),a.width());h=min(self.height(),a.height());self.resize(w,h);self.move(a.x()+(a.width()-w)//2,a.y()+(a.height()-h)//2)


def main():
    app=QApplication(sys.argv);browser=Browser();browser.place_on_screen();browser.show();raise SystemExit(app.exec())

if __name__=="__main__":main()
