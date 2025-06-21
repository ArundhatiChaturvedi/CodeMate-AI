def scan_security_issues(code):
    issues = []
    if not code or len(code) > 10000:
        return ["Invalid code input"]
    
    if "eval(" in code or "exec(" in code:
        issues.append("Use of eval/exec can lead to code injection")
    
    if "input(" in code and "int(" not in code:
        issues.append("Validate all user inputs properly")
    
    if "open(" in code and ("'w'" in code or '"w"' in code):
        issues.append("Ensure file writes are secure")
    
    if "pickle.load(" in code:
        issues.append("Unpickling data can execute arbitrary code")
    
    return issues if issues else ["✅ No major security issues detected"]
