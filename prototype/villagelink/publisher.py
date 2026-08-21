from __future__ import annotations

from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from villagelink.db import all_links, initialise


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path not in ("/", "/links"):
            self.send_error(404)
            return

        rows = all_links()
        body_rows = "\n".join(
            f"""
            <tr>
              <td>{row['id']}</td>
              <td><a href="{escape(row['link'])}">{escape(row['link'])}</a></td>
              <td><a href="{escape(row['left_uri'])}">{escape(row['left_uri'])}</a></td>
              <td><a href="{escape(row['right_uri'])}">{escape(row['right_uri'])}</a></td>
              <td><a href="{escape(row['evidence_source'])}">{escape(row['evidence_source'])}</a></td>
              <td>{escape(row['sampled_at'])}</td>
            </tr>
            """
            for row in rows
        )

        page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Village Links</title>
  <style>
    body {{ font: 16px system-ui, sans-serif; margin: 2rem; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border-bottom: 1px solid #ddd; padding: .6rem; text-align: left; vertical-align: top; }}
    a {{ overflow-wrap: anywhere; }}
  </style>
</head>
<body>
  <h1>Village Links</h1>
  <p>Prototype publication of the links currently held in SQLite.</p>
  <table>
    <thead>
      <tr><th>ID</th><th>Village Link</th><th>Left</th><th>Right</th><th>Evidence</th><th>Sampled</th></tr>
    </thead>
    <tbody>{body_rows}</tbody>
  </table>
</body>
</html>"""

        data = page.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main() -> None:
    initialise()
    server = ThreadingHTTPServer(("0.0.0.0", 8080), Handler)
    print("Publishing Village Links on http://0.0.0.0:8080")
    server.serve_forever()


if __name__ == "__main__":
    main()
