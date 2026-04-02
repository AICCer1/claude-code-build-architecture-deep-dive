# 关键文件与符号索引

## query runtime
- `src/query.ts`
  - `query()`
  - `queryLoop()`
  - `yieldMissingToolResultBlocks()`
- `src/QueryEngine.ts`
  - `class QueryEngine`
  - `submitMessage()`
- `src/query/config.ts`
  - `buildQueryConfig()`
- `src/query/stopHooks.ts`
  - `handleStopHooks()`

## tool plane
- `src/Tool.ts`
  - `buildTool()`
  - `findToolByName()`
  - `ToolUseContext`
- `src/tools.ts`
  - `getTools()`
- `src/services/tools/toolOrchestration.ts`
  - `runTools()`
  - `partitionToolCalls()`
- `src/services/tools/toolExecution.ts`
  - `runToolUse()`

## memory
- `src/memdir/memdir.ts`
  - `buildMemoryLines()`
  - `ensureMemoryDirExists()`
- `src/memdir/paths.ts`
  - `isAutoMemoryEnabled()`
  - `getAutoMemBase()`
- `src/memdir/memoryScan.ts`
  - `scanMemoryFiles()`
  - `formatMemoryManifest()`
- `src/memdir/findRelevantMemories.ts`
  - `findRelevantMemories()`
- `src/services/SessionMemory/sessionMemory.ts`
- `src/services/SessionMemory/sessionMemoryUtils.ts`
- `src/services/extractMemories/extractMemories.ts`

## extensions
- `src/services/mcp/client.ts`
- `src/services/lsp/LSPServerManager.ts`
  - `createLSPServerManager()`
- `src/skills/loadSkillsDir.ts`
- `src/utils/plugins/*`

## collaboration
- `src/tools/AgentTool/AgentTool.ts`
- `src/tasks/Task.ts`
- `src/coordinator/*`
- `src/tools/SendMessageTool/*`
- `src/tools/TeamCreateTool/*`

## state & persistence
- `src/state/AppStateStore.ts`
- `src/utils/sessionStorage.ts`
- `src/utils/fileHistory.ts`
