from pathlib import Path
import re, json
root = Path('/root/.openclaw/workspace/claude-code-build/src')
out = Path('/root/.openclaw/workspace/claude-code-build-analysis/docs/generated')
out.mkdir(parents=True, exist_ok=True)

# directory counts
lines = ['# 目录文件计数（自动生成）','', '| 目录 | 文件数 |', '|---|---:|']
for p in sorted([x for x in root.iterdir() if x.is_dir()]):
    count = sum(1 for f in p.rglob('*') if f.is_file())
    lines.append(f'| `{p.name}` | {count} |')
(out/'directory-counts.md').write_text('\n'.join(lines), encoding='utf-8')

# root files
lines = ['# 根层关键文件（自动生成）','', '| 文件 | 角色 |', '|---|---|']
roles = {
    'main.tsx':'启动与装配入口',
    'query.ts':'交互路径主循环',
    'QueryEngine.ts':'Headless/SDK 会话引擎',
    'Tool.ts':'工具抽象协议',
    'tools.ts':'工具池装配器',
    'commands.ts':'命令总表聚合器',
    'Task.ts':'任务抽象',
    'tasks.ts':'任务导出与注册入口',
    'replLauncher.tsx':'REPL 启动器',
    'interactiveHelpers.tsx':'交互路径辅助',
}
for f in sorted(root.glob('*')):
    if f.is_file():
        lines.append(f'| `{f.name}` | {roles.get(f.name, "-")} |')
(out/'root-files.md').write_text('\n'.join(lines), encoding='utf-8')

# selected symbol index
selected = [
    'main.tsx','query.ts','QueryEngine.ts','Tool.ts','tools.ts','commands.ts',
    'state/AppStateStore.ts','utils/hooks.ts','query/stopHooks.ts',
    'services/mcp/client.ts','services/lsp/LSPServerManager.ts',
    'skills/loadSkillsDir.ts','memdir/memdir.ts','tools/AgentTool/AgentTool.tsx'
]
pat = re.compile(r'^(export\s+)?(async\s+)?(function|class)\s+([A-Za-z0-9_]+)|^(export\s+)?const\s+([A-Za-z0-9_]+)\s*=')
lines = ['# 关键文件符号索引（自动生成）','']
for rel in selected:
    f = root / rel
    if not f.exists():
        continue
    lines.append(f'## `{rel}`')
    lines.append('')
    lines.append('| 行号 | 符号 |')
    lines.append('|---:|---|')
    found = 0
    for i, line in enumerate(f.read_text(encoding='utf-8', errors='ignore').splitlines(),1):
        m = pat.match(line.strip())
        if m:
            name = m.group(4) or m.group(6)
            lines.append(f'| {i} | `{name}` |')
            found += 1
    if found == 0:
        lines.append('| - | *(无简单匹配结果)* |')
    lines.append('')
(out/'key-file-symbols.md').write_text('\n'.join(lines), encoding='utf-8')
