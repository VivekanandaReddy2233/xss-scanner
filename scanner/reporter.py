from jinja2 import Template
import datetime

HTML_TMPL = """
<html>
<head>
  <meta charset="utf-8">
  <title>XSS Scan Report</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
    pre { white-space: pre-wrap; word-break: break-word; }
    .meta { margin-bottom: 16px; }
  </style>
</head>
<body>
  <h1>XSS Scan Report</h1>
  <div class="meta">
    <p>Generated: {{ generated }}</p>
    <p>Target: {{ target }}</p>
    <p>Total reflections: {{ findings|length }}</p>
  </div>
  {% if findings %}
  <table>
    <thead>
      <tr><th>Parameter</th><th>Detected Context</th><th>Payload</th><th>Status</th><th>URL</th><th>Snippet</th></tr>
    </thead>
    <tbody>
    {% for f in findings %}
      <tr>
        <td>{{ f.param }}</td>
        <td>{{ f.context }}</td>
        <td><pre>{{ f.payload }}</pre></td>
        <td>{{ f.status_code }}</td>
        <td><a href="{{ f.url }}">link</a></td>
        <td><pre>{{ f.snippet }}</pre></td>
      </tr>
    {% endfor %}
    </tbody>
  </table>
  {% else %}
    <p>No reflections detected.</p>
  {% endif %}
</body>
</html>
"""

class Reporter:
    def __init__(self, findings, target=None):
        self.findings = findings or []
        self.target = target

    def to_html(self, out_path='report.html'):
        tmpl = Template(HTML_TMPL)
        rendered = tmpl.render(
            generated=datetime.datetime.utcnow().isoformat() + 'Z',
            findings=self.findings,
            target=self.target
        )
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(rendered)
        return out_path
