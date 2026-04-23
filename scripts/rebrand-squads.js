#!/usr/bin/env node
/**
 * rebrand-squads.js — Remove SINAPSE/external branding de node_modules/sinapse-ai
 * Executado automaticamente via postinstall hook
 * Muda slashPrefix de SINAPSE para prefixes específicos por squad
 */

const fs = require('fs');
const path = require('path');

const SQUAD_PREFIX_MAP = {
  'squad-animations': 'ca',
  'squad-brand': 'brand',
  'squad-claude': 'claude',
  'squad-cloning': 'cloning',
  'squad-commercial': 'commercial',
  'squad-content': 'content',
  'squad-copy': 'copywriting',
  'squad-council': 'council',
  'squad-courses': 'courses',
  'squad-cybersecurity': 'cyber',
  'squad-design': 'digital-experience',
  'squad-finance': 'finance',
  'squad-growth': 'growth',
  'squad-paidmedia': 'paidmedia',
  'squad-product': 'product',
  'squad-research': 'research',
  'squad-storytelling': 'narrative',
  'claude-code-mastery': 'mastery',
  'squad-artdir': 'arte',
};

const AUTHOR_REPLACEMENTS = [
  ['Caio Imori', 'Zvision'],
  ['author: Sinapse', 'author: "Zvision"'],
  ['author: "Sinapse"', 'author: "Zvision"'],
  ['created_by: "Caio Imori"', 'created_by: "Zvision"'],
];

const sinapseSquadsPath = path.join(__dirname, '..', 'node_modules', 'sinapse-ai', 'squads');

if (!fs.existsSync(sinapseSquadsPath)) {
  console.log('sinapse-ai squads not found — skipping rebrand');
  process.exit(0);
}

const squads = fs.readdirSync(sinapseSquadsPath);
let patched = 0;

for (const squad of squads) {
  const squadYaml = path.join(sinapseSquadsPath, squad, 'squad.yaml');
  if (!fs.existsSync(squadYaml)) continue;

  let content = fs.readFileSync(squadYaml, 'utf8');
  let changed = false;

  // Fix slashPrefix
  const newPrefix = SQUAD_PREFIX_MAP[squad];
  if (newPrefix && content.includes('slashPrefix: SINAPSE')) {
    content = content.replace('slashPrefix: SINAPSE', `slashPrefix: ${newPrefix}`);
    changed = true;
  } else if (content.includes('slashPrefix: SINAPSE')) {
    // Unknown squad — use squad name as prefix
    const fallback = squad.replace('squad-', '').replace(/-/g, '');
    content = content.replace('slashPrefix: SINAPSE', `slashPrefix: ${fallback}`);
    changed = true;
  }

  // Fix author references
  for (const [from, to] of AUTHOR_REPLACEMENTS) {
    if (content.includes(from)) {
      content = content.split(from).join(to);
      changed = true;
    }
  }

  if (changed) {
    fs.writeFileSync(squadYaml, content, 'utf8');
    patched++;
    console.log(`✓ Rebranded: ${squad} → prefix: ${newPrefix || 'fallback'}`);
  }
}

console.log(`\nZvision rebrand complete: ${patched}/${squads.length} squads patched`);
