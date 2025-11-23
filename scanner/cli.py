from .scanner import Scanner
from .reporter import Reporter
from .utils import build_argparser

def main():
    ap = build_argparser()
    args = ap.parse_args()

    params = [p.strip() for p in args.params.split(',') if p.strip()]

    contexts = None
    if args.contexts:
        contexts = [c.strip() for c in args.contexts.split(',') if c.strip()]

    # map single context arg values to internal context names
    if args.context and args.context != 'auto':
        mapping = {
            'attr-name': 'attr_name',
            'attr-value': 'attr_value',
            'text': 'text',
            'js': 'js'
        }
        contexts = [mapping.get(args.context, args.context)]

    scanner = Scanner(base_url=args.url, params=params, method=args.method, contexts=contexts)
    findings = scanner.run()

    reporter = Reporter(findings, target=args.url)
    out = reporter.to_html(args.out)

    print(f"[+] Scan completed. Found {len(findings)} reflections.")
    print(f"[+] Report saved to: {out}")

if __name__ == '__main__':
    main()
