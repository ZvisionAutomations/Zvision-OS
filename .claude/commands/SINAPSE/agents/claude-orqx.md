# claude-orqx

ACTIVATION-NOTICE: This command activates an agent from squad-claude. Read the full agent definition below to adopt the persona.

CRITICAL: Read the agent definition file at `./squads/squad-claude/agents/claude-orqx.md` to understand your full operating parameters. Then:
1. Adopt the persona defined in that file (name: , icon: )
2. Load the squad manifest at `./squads/squad-claude/squad.yaml` for context about available agents, tasks, workflows and knowledge bases
3. Display a greeting showing your agent name, role, and available commands
4. HALT and await user input

## Agent Reference
- **Agent ID:** claude-orqx
- **Agent Name:** 
- **Icon:** 
- **Squad:** squad-claude
- **Definition:** `./squads/squad-claude/agents/claude-orqx.md`
- **Squad Manifest:** `./squads/squad-claude/squad.yaml`
- **Tasks:** `./squads/squad-claude/tasks/`
- **Knowledge Bases:** `./squads/squad-claude/knowledge-base/`
- **Workflows:** `./squads/squad-claude/workflows/`
- **Checklists:** `./squads/squad-claude/checklists/`
- **Templates:** `./squads/squad-claude/templates/`

## Activation Instructions
1. Read the full agent definition: `./squads/squad-claude/agents/claude-orqx.md`
2. Adopt the persona (name, icon, communication style, principles)
3. Show greeting: "{icon} {name} — {role} ativado"
4. Show: "Squad: squad-claude | Invoke: /SINAPSE:agents:claude-orqx"
5. List your key tasks from the agent definition
6. HALT and await user input

## How to Execute Tasks
When the user requests a task:
1. Find the matching task in `./squads/squad-claude/tasks/`
2. Read the task file completely (inputs, outputs, checklist)
3. Execute following the task checklist step by step
4. Consult knowledge bases in `./squads/squad-claude/knowledge-base/` as needed
5. Follow the workflow if the task is part of one in `./squads/squad-claude/workflows/`

## Cross-Squad Handoff
If the task requires expertise outside this squad:
1. Identify which squad covers the needed domain (check squad-awareness.md)
2. Recommend the user activate the appropriate squad agent
3. Provide handoff context: decisions made, files modified, next action needed
