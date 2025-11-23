import argparse

def build_argparser():
    p = argparse.ArgumentParser(description='Reflected XSS Scanner')
    p.add_argument('--url', required=True, help='Target URL (e.g. http://127.0.0.1:5000/search)')
    p.add_argument('--params', required=True, help='Comma separated param names to test (e.g. q,id)')
    p.add_argument('--method', default='GET', choices=['GET', 'POST'], help='HTTP method')
    p.add_argument('--out', default='report.html', help='Output report path')
    p.add_argument('--contexts', default=None, help='Comma-separated contexts to try (overrides defaults)')
    p.add_argument('--context', default='auto', choices=['auto', 'text', 'attr-value', 'attr-name', 'js'],
                   help=('Injection context for PayloadGenerator. auto = let scanner decide. '
                         'text = inside HTML text node. attr-value = inside attribute value. '
                         'attr-name = break attribute names. js = inside <script> or event handlers.'))
    return p
