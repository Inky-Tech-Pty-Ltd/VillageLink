"""Domain-aware launcher for the prototype browser.

This keeps the current prototype home page intact while applying the small
composer change in one place: Domain is an editable first field, defaulting
to ``village.link``, for both Village Links and star credentials.
"""

from . import browser


def _domain_aware_home(html: str) -> str:
    html = html.replace(
        '<input id="endpoint-a" class="endpoint" type="text" inputmode="url" placeholder="A — first URL">',
        '<input id="domain" class="endpoint" type="text" inputmode="url" value="village.link" aria-label="Domain"><input id="endpoint-a" class="endpoint" type="text" inputmode="url" placeholder="A — first URL">',
    )
    html = html.replace(
        'const marker="https://wab.village.link/";',
        "function markerForDomain(domain){return 'https://wab.'+domain+'/'}",
    )
    html = html.replace(
        "function composeVillageLink(){const a=document.getElementById('endpoint-a').value.trim(),b=document.getElementById('endpoint-b').value.trim(),message=document.getElementById('message'),result=document.getElementById('result');message.textContent='';if(!a||!b){message.textContent='Enter both URLs.';return}const composed=marker+encodeEndpoint(a)+'!'+encodeEndpoint(b);",
        "function composeVillageLink(){const domain=document.getElementById('domain').value.trim().toLowerCase().replace(/\\.$/,'');const a=document.getElementById('endpoint-a').value.trim(),b=document.getElementById('endpoint-b').value.trim(),message=document.getElementById('message'),result=document.getElementById('result');message.textContent='';if(!domain||domain.includes('/')||domain.includes(':')||domain.includes(' ')){message.textContent='Enter a bare domain such as village.link.';return}if(!a||!b){message.textContent='Enter both URLs.';return}const composed=markerForDomain(domain)+encodeEndpoint(a)+'!'+encodeEndpoint(b);",
    )
    html = html.replace(
        "function composeStarCredential(){const a=document.getElementById('endpoint-a').value.trim(),entered=",
        "function composeStarCredential(){const domain=document.getElementById('domain').value.trim().toLowerCase().replace(/\\.$/,'');const a=document.getElementById('endpoint-a').value.trim(),entered=",
    )
    html = html.replace(
        "message.textContent='';if(!a){message.textContent='Enter the centre URI A.';return}",
        "message.textContent='';if(!domain||domain.includes('/')||domain.includes(':')||domain.includes(' ')){message.textContent='Enter a bare domain such as village.link.';return}if(!a){message.textContent='Enter the centre URI A.';return}",
    )
    html = html.replace(
        "credential={type:'StarCredential',A:a,B:members}",
        "credential={type:'StarCredential',domain:domain,A:a,B:members}",
    )
    return html


browser.HOME_HTML = _domain_aware_home(browser.HOME_HTML)


def main() -> int:
    return browser.main()


if __name__ == "__main__":
    raise SystemExit(main())
