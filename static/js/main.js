// ─── Skills (skillData is injected by Django template inline script above) ───

function renderSkills() {
  const grid = document.getElementById('skillsGrid');
  if (!grid) return;
  grid.innerHTML = '';
  skillData.forEach((cat, ci) => {
    const card = document.createElement('div'); card.className = 'sk-cat';
    const title = document.createElement('div'); title.className = 'sk-cat-title'; title.textContent = cat.category;
    card.appendChild(title);
    const wrap = document.createElement('div'); wrap.className = 'tags-wrap';
    cat.tags.forEach((tag, ti) => wrap.appendChild(makeTag(tag, ci, ti)));
    card.appendChild(wrap);
    const row = document.createElement('div'); row.className = 'add-row';
    const inp = document.createElement('input'); inp.className = 'add-in'; inp.placeholder = 'Add skill…'; inp.type = 'text';
    const btn = document.createElement('button'); btn.className = 'add-btn'; btn.textContent = '+ Add';
    const add = () => {
      const v = inp.value.trim(); if (!v) return;
      skillData[ci].tags.push(v); inp.value = ''; renderSkills();
      setTimeout(() => { const ins = document.querySelectorAll('.add-in'); if (ins[ci]) ins[ci].focus(); }, 40);
    };
    btn.onclick = add; inp.addEventListener('keydown', e => { if (e.key === 'Enter') add(); });
    row.appendChild(inp); row.appendChild(btn); card.appendChild(row); grid.appendChild(card);
  });
}

function makeTag(text, ci, ti) {
  const t = document.createElement('div'); t.className = 'tag';
  const l = document.createElement('span'); l.textContent = text;
  const r = document.createElement('button'); r.className = 'rm'; r.textContent = '✕'; r.title = 'Remove';
  r.onclick = () => { skillData[ci].tags.splice(ti, 1); renderSkills(); };
  t.appendChild(l); t.appendChild(r); return t;
}

// ─── Experience role tabs ─────────────────────────────────────────────────────

function switchRole(idx) {
  document.querySelectorAll('.rtab').forEach((t, i) => t.classList.toggle('active', i === idx));
  document.querySelectorAll('.role-panel').forEach((p, i) => p.classList.toggle('active', i === idx));
}

// ─── On DOM ready ─────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', function () {

  // Render skills grid from DB-seeded skillData
  renderSkills();

  // Scroll-in animation for cards
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.edu-card, .ach-card, .proj-card').forEach(el => io.observe(el));

  // Scroll progress bar
  window.addEventListener('scroll', () => {
    const p = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
    const bar = document.getElementById('scrollBar');
    if (bar) bar.style.width = p + '%';
  });

});
