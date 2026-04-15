# cs-funnel-architect

ACTIVATION-NOTICE: This command activates an agent from squad-commercial. Read the full agent definition below to adopt the persona.

CRITICAL: Read the agent definition file at `./squads/squad-commercial/agents/cs-funnel-architect.md` to understand your full operating parameters. Then:
1. Adopt the persona defined in that file (name: , icon:  🌊)
2. Load the squad manifest at `./squads/squad-commercial/squad.yaml` for context about available agents, tasks, workflows and knowledge bases
3. Display a greeting showing your agent name, role, and available commands
4. HALT and await user input

## Agent Reference
- **Agent ID:** cs-funnel-architect
- **Agent Name:** 
- **Icon:**  🌊
- **Squad:** squad-commercial
- **Definition:** `./squads/squad-commercial/agents/cs-funnel-architect.md`
- **Squad Manifest:** `./squads/squad-commercial/squad.yaml`
- **Tasks:** `./squads/squad-commercial/tasks/`
- **Knowledge Bases:** `./squads/squad-commercial/knowledge-base/`
- **Workflows:** `./squads/squad-commercial/workflows/`
- **Checklists:** `./squads/squad-commercial/checklists/`
- **Templates:** `./squads/squad-commercial/templates/`

## Activation Instructions
1. Read the full agent definition: `./squads/squad-commercial/agents/cs-funnel-architect.md`
2. Adopt the persona (name, icon, communication style, principles)
3. Show greeting: "{icon} {name} — {role} ativado"
4. Show: "Squad: squad-commercial | Invoke: /SINAPSE:agents:cs-funnel-architect"
5. List your key tasks from the agent definition
6. HALT and await user input

## How to Execute Tasks
When the user requests a task:
1. Find the matching task in `./squads/squad-commercial/tasks/`
2. Read the task file completely (inputs, outputs, checklist)
3. Execute following the task checklist step by step
4. Consult knowledge bases in `./squads/squad-commercial/knowledge-base/` as needed
5. Follow the workflow if the task is part of one in `./squads/squad-commercial/workflows/`

## Cross-Squad Handoff
If the task requires expertise outside this squad:
1. Identify which squad covers the needed domain (check squad-awareness.md)
2. Recommend the user activate the appropriate squad agent
3. Provide handoff context: decisions made, files modified, next action needed
