# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in Zvision-OS, please **do not** open a public GitHub issue.

Instead, report it privately:

**Email:** zvisionforb2b@gmail.com  
**Subject:** `[SECURITY] Brief description`

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (optional)

We will respond within **48 hours** and keep you updated as we address the issue.

## Scope

| In Scope | Out of Scope |
|----------|-------------|
| Agent prompt injection vulnerabilities | Third-party MCP servers |
| Hook system bypass | Obsidian plugin security |
| Credential handling in templates/examples | Evolution API (third-party) |
| Sensitive data exposure in committed files | OpenRouter/LLM providers |

## Security Best Practices for Users

### Credentials
- **Never commit** `.mcp.json` — it contains your API keys (already in `.gitignore`)
- **Never commit** `.env` — same reason
- Use `.mcp.json.example` as a template with placeholder values only
- Rotate API keys periodically and immediately after any suspected exposure

### Token Guardian Hook
Zvision-OS includes a pre-commit hook (`.claude/hooks/token-guardian.js`) that automatically blocks commits containing hardcoded secrets matching known patterns (GitHub tokens, API keys, etc.).

### Gitignored Sensitive Files
The following files are gitignored by default and must **never** be force-added:
```
.env
.mcp.json
.mcp.json.local
.paperclip/
```

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest (main) | Yes |
| Older releases | No — please update to main |

## Acknowledgments

We thank security researchers who responsibly disclose vulnerabilities to help keep Zvision-OS safe for everyone.
