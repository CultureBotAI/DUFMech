/* Static pages remain complete and navigable if this enhancement cannot load. */
(() => {
  'use strict';
  const byId = id => document.getElementById(id);
  const human = value => String(value || '').replaceAll('_', ' ');
  const count = value => value === null || value === undefined ? 'Not available' : Number(value).toLocaleString('en-US');
  const allowed = (select, value, fallback) => select && [...select.options].some(option => option.value === value) ? value : fallback;

  const PALETTE = [
    '#12623c', '#1d6f8a', '#9c4a1a', '#6a3d9a',
    '#b02a37', '#2b59c3', '#7a6f14', '#0f766e',
  ];

  function syncSearchBars(value) {
    const hero = byId('hero-search-input');
    if (hero && hero.value !== value) hero.value = value;
    document.querySelectorAll('.header-search input[name="q"]').forEach(input => {
      if (input.value !== value) input.value = value;
    });
  }

  function initCatalogue() {
    const catalogue = document.querySelector('[data-catalogue]');
    if (!catalogue) return;
    const root = catalogue.dataset.root;
    const category = catalogue.dataset.category;
    const initialPage = Number(catalogue.dataset.page);
    const query = byId('family-query');
    const seed = byId('seed-filter');
    const characterization = byId('characterization-filter');
    const curation = byId('curation-filter');
    const sort = byId('family-sort');
    const tbody = byId('family-table').querySelector('tbody');
    const size = 50;
    let page = initialPage;
    let rows;

    const textCell = (tr, value, className = '') => {
      const td = document.createElement('td');
      td.textContent = value;
      td.className = className;
      tr.append(td);
      return td;
    };

    function familyRow(row) {
      const tr = document.createElement('tr');
      tr.id = row.pfam_id;
      const a = document.createElement('a');
      a.href = root + 'families/' + row.pfam_id + '.html';
      a.textContent = row.pfam_id;
      textCell(tr, '').append(a);
      const label = document.createElement('strong');
      label.textContent = row.name || row.short_name || row.pfam_id;
      textCell(tr, '').append(label, document.createElement('br'), row.short_name);
      textCell(tr, human(row.unknown_status));
      textCell(tr, human(row.characterization_status || 'UNSCORED'));
      textCell(tr, row.characterization_status ?
        'Known: ' + count(row.known_evidence_count) + '; partial: ' + count(row.partial_evidence_count) +
        '; context: ' + count(row.context_evidence_count) : 'Not scored');
      ['proteins', 'structures', 'alphafold_models'].forEach(key => textCell(tr, count(row[key]), 'num'));
      const others = Object.entries(row.cross_mech.records_by_mech).map(([name, n]) => name + ': ' + n);
      if (row.cross_mech.protein_traits_record) others.push('ProteinTraitsMech trait record');
      if (row.cross_mech.scanned === false) others.push('not covered by the cross-Mech scan');
      textCell(tr, others.join('; '));
      textCell(tr, human(row.curation_status));
      return tr;
    }

    function restore() {
      const params = new URLSearchParams(location.search);
      query.value = params.get('q') || '';
      syncSearchBars(query.value);
      seed.value = allowed(seed, params.has('seed') ? params.get('seed') : category, '');
      characterization.value = allowed(characterization, params.get('characterization') || '', '');
      if (curation) curation.value = allowed(curation, params.get('curation') || '', '');
      sort.value = allowed(sort, params.get('sort') || 'proteins-desc', 'proteins-desc');
      const requested = Number(params.get('page') || initialPage);
      page = Number.isSafeInteger(requested) && requested > 0 ? requested : 1;
      render();
    }

    function writeState() {
      const url = new URL(location.href);
      const state = {
        q: query.value,
        seed: seed.value,
        characterization: characterization.value,
        curation: curation ? curation.value : '',
        sort: sort.value,
        page: String(page),
      };
      for (const [key, value] of Object.entries(state)) {
        if (value || key === 'seed') url.searchParams.set(key, value);
        else url.searchParams.delete(key);
      }
      url.hash = 'families';
      if (url.href !== location.href) history.pushState(null, '', url);
    }

    function render() {
      const term = query.value.trim().toLowerCase();
      const matches = rows.filter(row => (!seed.value || row.unknown_status === seed.value) &&
        (!characterization.value || (row.characterization_status || 'UNSCORED') === characterization.value) &&
        (!curation || !curation.value || row.curation_status === curation.value) &&
        [row.pfam_id, row.short_name, row.name, row.interpro_id].join(' ').toLowerCase().includes(term));
      const [key, order] = sort.value.split('-');
      const direction = order === 'desc' ? -1 : 1;
      matches.sort((a, b) => {
        if (a[key] === null && b[key] !== null) return 1;
        if (b[key] === null && a[key] !== null) return -1;
        const av = typeof a[key] === 'string' ? a[key].toLowerCase() : a[key];
        const bv = typeof b[key] === 'string' ? b[key].toLowerCase() : b[key];
        const difference = av < bv ? -1 : av > bv ? 1 : 0;
        return difference * direction || a.pfam_id.localeCompare(b.pfam_id, 'en');
      });
      const pages = Math.max(1, Math.ceil(matches.length / size));
      page = Math.min(Math.max(1, page), pages);
      tbody.replaceChildren(...matches.slice((page - 1) * size, page * size).map(familyRow));
      tbody.closest('.table-wrap').scrollTop = 0;
      byId('family-count').textContent = matches.length.toLocaleString('en-US') + ' of ' +
        rows.length.toLocaleString('en-US') + ' families match.';
      byId('family-empty').hidden = matches.length !== 0;
      byId('family-page').textContent = 'Page ' + page + ' of ' + pages;
      byId('previous-families').disabled = page === 1;
      byId('next-families').disabled = page === pages;
    }

    async function start() {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), 15000);
      try {
        const response = await fetch(root + 'catalogue.json', {signal: controller.signal});
        if (!response.ok) throw new Error('HTTP ' + response.status);
        const payload = await response.json();
        if (payload.version !== 1 || !Array.isArray(payload.fields) || !Array.isArray(payload.rows)) {
          throw new Error('Invalid catalogue');
        }
        rows = payload.rows.map(values => {
          if (!Array.isArray(values) || values.length !== payload.fields.length) throw new Error('Invalid row');
          const row = Object.fromEntries(payload.fields.map((key, i) => [key, values[i]]));
          if (!/^PF[0-9]{5}$/.test(row.pfam_id) || typeof row.name !== 'string' ||
              typeof row.short_name !== 'string' || typeof row.interpro_id !== 'string' ||
              !row.cross_mech || typeof row.cross_mech.records_by_mech !== 'object') throw new Error('Invalid family');
          for (const key of ['proteins', 'structures', 'alphafold_models', 'known_evidence_count',
            'partial_evidence_count', 'context_evidence_count']) {
            if (row[key] !== null && (!Number.isSafeInteger(row[key]) || row[key] < 0)) throw new Error('Invalid count');
          }
          return row;
        });
        if (new Set(rows.map(row => row.pfam_id)).size !== rows.length) throw new Error('Duplicate family');
        const legacyId = location.hash.slice(1).toUpperCase();
        if (rows.some(row => row.pfam_id === legacyId)) {
          location.replace(root + 'families/' + legacyId + '.html');
          return;
        }
        restore();
        byId('family-controls').hidden = false;
        byId('family-pagination').hidden = false;
        byId('static-pagination').hidden = true;
        byId('family-controls').addEventListener('submit', event => event.preventDefault());
        query.addEventListener('input', () => {
          syncSearchBars(query.value);
          page = 1; render(); writeState();
        });
        const heroForm = byId('hero-search-form');
        const heroInput = byId('hero-search-input');
        if (heroInput) {
          heroInput.addEventListener('input', () => {
            query.value = heroInput.value;
            syncSearchBars(query.value);
            page = 1; render(); writeState();
          });
        }
        if (heroForm && heroInput) {
          heroForm.addEventListener('submit', event => {
            event.preventDefault();
            query.value = heroInput.value;
            syncSearchBars(query.value);
            page = 1; render(); writeState();
            catalogue.scrollIntoView({behavior: 'smooth'});
          });
        }
        document.querySelectorAll('.header-search').forEach(form => {
          const input = form.querySelector('input[name="q"]');
          if (!input) return;
          form.addEventListener('submit', event => {
            event.preventDefault();
            query.value = input.value;
            syncSearchBars(query.value);
            page = 1; render(); writeState();
            catalogue.scrollIntoView({behavior: 'smooth'});
          });
        });
        [seed, characterization, curation, sort].filter(Boolean).forEach(control => control.addEventListener('change', () => {
          page = 1; render(); writeState();
        }));
        byId('reset-families').addEventListener('click', () => {
          query.value = ''; syncSearchBars('');
          seed.value = category; characterization.value = '';
          if (curation) curation.value = '';
          sort.value = 'proteins-desc'; page = 1; render(); writeState(); query.focus();
        });
        byId('previous-families').addEventListener('click', () => { page--; render(); writeState(); });
        byId('next-families').addEventListener('click', () => { page++; render(); writeState(); });
        window.addEventListener('popstate', restore);
      } catch (_) {
        const errEl = byId('catalogue-error');
        errEl.replaceChildren(
          'Search is unavailable because the catalogue could not be loaded. ' +
          'The table below is the static catalogue page; search parameters have not been applied. ' +
          'Use the numbered pages or complete JSON download. '
        );
        const retryBtn = document.createElement('button');
        retryBtn.type = 'button';
        retryBtn.textContent = 'Retry';
        retryBtn.addEventListener('click', () => {
          errEl.hidden = true;
          start();
        });
        errEl.append(retryBtn);
        errEl.hidden = false;
      } finally {
        clearTimeout(timer);
      }
    }
    start();
  }

  function attachCanvasInteractions(canvas, state, onSelect, draw) {
    let dragging = false;
    let startX = 0, startY = 0, moved = false;

    function toCanvasCoords(event) {
      const rect = canvas.getBoundingClientRect();
      return {
        cx: (event.clientX - rect.left) * (canvas.width / Math.max(1, rect.width)),
        cy: (event.clientY - rect.top) * (canvas.height / Math.max(1, rect.height)),
      };
    }

    function nearestPoint(cx, cy) {
      let best = null;
      let bestDist2 = 144;
      for (const item of state.projected) {
        if (!item.visible) continue;
        const dx = item.px - cx;
        const dy = item.py - cy;
        const d2 = dx * dx + dy * dy;
        if (d2 <= bestDist2) {
          bestDist2 = d2;
          best = item.point;
        }
      }
      return best;
    }

    canvas.addEventListener('mousedown', event => {
      dragging = true;
      moved = false;
      startX = event.clientX;
      startY = event.clientY;
    });
    window.addEventListener('mousemove', event => {
      if (!dragging) return;
      const dx = event.clientX - startX;
      const dy = event.clientY - startY;
      if (Math.abs(dx) > 3 || Math.abs(dy) > 3) moved = true;
      startX = event.clientX;
      startY = event.clientY;
      const rect = canvas.getBoundingClientRect();
      state.panX += dx * (canvas.width / Math.max(1, rect.width));
      state.panY += dy * (canvas.height / Math.max(1, rect.height));
      draw();
    });
    window.addEventListener('mouseup', () => { dragging = false; });

    canvas.addEventListener('mousemove', event => {
      if (dragging) return;
      const {cx, cy} = toCanvasCoords(event);
      const hit = nearestPoint(cx, cy);
      if (hit !== state.hovered) {
        state.hovered = hit;
        canvas.style.cursor = hit ? 'pointer' : 'grab';
        draw();
        if (!state.selected && hit) onSelect(hit, false);
      }
    });

    canvas.addEventListener('click', event => {
      if (moved) return;
      const {cx, cy} = toCanvasCoords(event);
      const hit = nearestPoint(cx, cy);
      state.selected = hit;
      draw();
      if (hit) onSelect(hit, true);
    });

    canvas.addEventListener('wheel', event => {
      event.preventDefault();
      const factor = event.deltaY < 0 ? 1.15 : 1 / 1.15;
      state.zoom = Math.max(0.6, Math.min(18, state.zoom * factor));
      draw();
    }, {passive: false});
  }

  function renderLegend(container, groups, activeValue, onToggle) {
    container.replaceChildren();
    const heading = document.createElement('h3');
    heading.textContent = 'Legend';
    container.append(heading);
    const list = document.createElement('div');
    list.className = 'legend-items';
    groups.forEach((group, idx) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'legend-pill' + (activeValue === group.key ? ' is-active' : '');
      const swatch = document.createElement('span');
      swatch.className = 'swatch';
      swatch.style.backgroundColor = PALETTE[idx % PALETTE.length];
      const label = document.createElement('span');
      label.textContent = group.label + ' (' + group.count.toLocaleString('en-US') + ')';
      btn.append(swatch, label);
      btn.addEventListener('click', () => onToggle(group.key));
      list.append(btn);
    });
    container.append(list);
  }

  function initTextMap() {
    const container = document.querySelector('[data-text-map]');
    if (!container) return;
    const canvas = byId('corpus-map');
    const ctx = canvas.getContext('2d');
    const search = byId('map-search');
    const colorBy = byId('map-color');
    const seedSelect = byId('map-seed');
    const curSelect = byId('map-curation');
    const cmSelect = byId('map-cross-mech');
    const resetBtn = byId('map-reset');
    const statusEl = byId('map-status');
    const selectionEl = byId('map-selection');
    const legendEl = byId('map-legend');
    const state = {zoom: 1, panX: 0, panY: 0, hovered: null, selected: null, projected: []};
    let payload = null;
    let records = [];

    function showRecord(rec, pinned) {
      selectionEl.replaceChildren();
      const title = document.createElement('p');
      const link = document.createElement('a');
      link.href = 'families/' + rec.pfam_id + '.html';
      link.textContent = rec.pfam_id + ': ' + rec.short_name;
      const strong = document.createElement('strong');
      strong.append(link);
      title.append(strong, ' — ' + rec.name + (pinned ? ' (pinned)' : ''));
      const meta = document.createElement('p');
      meta.textContent = 'Seed status: ' + human(rec.seed) +
        ' · Curation: ' + human(rec.curation) +
        ' · Linkage: ' + rec.cross_mech +
        ' · Proteins: ' + count(rec.proteins) +
        ' · Structures: ' + count(rec.structures);
      selectionEl.append(title, meta);
    }

    function draw() {
      if (!records.length) return;
      const q = search.value.trim().toLowerCase();
      const seedVal = seedSelect.value;
      const curVal = curSelect.value;
      const cmVal = cmSelect.value;
      const mode = colorBy.value;
      const categories = mode === 'curation' ? payload.curation_statuses :
        mode === 'cross_mech' ? payload.cross_mech_bins : payload.seed_statuses;
      const counts = new Map(categories.map(k => [k, 0]));

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const pad = 36;
      const w = canvas.width - pad * 2;
      const h = canvas.height - pad * 2;
      const cx = canvas.width / 2 + state.panX;
      const cy = canvas.height / 2 + state.panY;

      let matched = 0;
      state.projected = records.map(rec => {
        const visible = (!seedVal || rec.seed === seedVal) &&
          (!curVal || rec.curation === curVal) &&
          (!cmVal || rec.cross_mech === cmVal) &&
          (!q || rec.searchText.includes(q));
        const groupKey = mode === 'curation' ? rec.curation :
          mode === 'cross_mech' ? rec.cross_mech : rec.seed;
        if (visible) {
          matched++;
          counts.set(groupKey, (counts.get(groupKey) || 0) + 1);
        }
        const px = cx + rec.nx * (w * 0.46) * state.zoom;
        const py = cy - rec.ny * (h * 0.46) * state.zoom;
        const colorIdx = Math.max(0, categories.indexOf(groupKey));
        return {point: rec, px, py, visible, color: PALETTE[colorIdx % PALETTE.length]};
      });

      for (const item of state.projected) {
        if (item.visible) continue;
        ctx.fillStyle = 'rgba(130, 145, 155, 0.14)';
        ctx.beginPath();
        ctx.arc(item.px, item.py, 2, 0, Math.PI * 2);
        ctx.fill();
      }
      for (const item of state.projected) {
        if (!item.visible) continue;
        ctx.fillStyle = item.color;
        ctx.beginPath();
        ctx.arc(item.px, item.py, q ? 3.5 : 2.4, 0, Math.PI * 2);
        ctx.fill();
      }
      for (const special of [state.hovered, state.selected]) {
        if (!special) continue;
        const found = state.projected.find(item => item.point === special);
        if (!found) continue;
        ctx.strokeStyle = '#d97706';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(found.px, found.py, 6.5, 0, Math.PI * 2);
        ctx.stroke();
      }

      statusEl.textContent = 'Showing ' + matched.toLocaleString('en-US') + ' of ' +
        records.length.toLocaleString('en-US') + ' DUF/Pfam families.';

      const activeSelect = mode === 'curation' ? curSelect :
        mode === 'cross_mech' ? cmSelect : seedSelect;
      renderLegend(
        legendEl,
        categories.map(k => ({key: k, label: human(k), count: counts.get(k) || 0})),
        activeSelect.value,
        key => {
          activeSelect.value = activeSelect.value === key ? '' : key;
          draw();
          writeMapState();
        }
      );
    }

    function restoreMapState() {
      const params = new URLSearchParams(location.search);
      search.value = params.get('q') || '';
      syncSearchBars(search.value);
      colorBy.value = allowed(colorBy, params.get('color') || 'seed', 'seed');
      seedSelect.value = allowed(seedSelect, params.get('seed') || '', '');
      curSelect.value = allowed(curSelect, params.get('curation') || '', '');
      cmSelect.value = allowed(cmSelect, params.get('cross_mech') || '', '');
      draw();
    }

    function writeMapState() {
      const url = new URL(location.href);
      const mapParams = {
        q: search.value.trim(),
        color: colorBy.value !== 'seed' ? colorBy.value : '',
        seed: seedSelect.value,
        curation: curSelect.value,
        cross_mech: cmSelect.value,
      };
      for (const [k, v] of Object.entries(mapParams)) {
        if (v) url.searchParams.set(k, v);
        else url.searchParams.delete(k);
      }
      if (url.href !== location.href) history.replaceState(null, '', url);
    }

    async function load() {
      try {
        statusEl.removeAttribute('role');
        const res = await fetch(container.dataset.src);
        if (!res.ok) throw new Error('HTTP ' + res.status);
        payload = await res.json();
        const pts = payload.points || [];
        let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
        for (const p of pts) {
          if (p[0] < minX) minX = p[0];
          if (p[0] > maxX) maxX = p[0];
          if (p[1] < minY) minY = p[1];
          if (p[1] > maxY) maxY = p[1];
        }
        const spanX = Math.max(1e-6, maxX - minX);
        const spanY = Math.max(1e-6, maxY - minY);
        records = pts.map(p => {
          const seed = payload.seed_statuses[p[5]] || 'UNKNOWN_CANDIDATE';
          const curation = payload.curation_statuses[p[6]] || 'SNAPSHOT_ONLY';
          const cross_mech = payload.cross_mech_bins[p[7]] || 'DUFMech only';
          return {
            x: p[0], y: p[1],
            nx: ((p[0] - minX) / spanX) * 2 - 1,
            ny: ((p[1] - minY) / spanY) * 2 - 1,
            pfam_id: p[2], short_name: p[3], name: p[4],
            seed, curation, cross_mech,
            proteins: p[8], structures: p[9],
            searchText: (p[2] + ' ' + p[3] + ' ' + p[4]).toLowerCase(),
          };
        });
        restoreMapState();
        byId('map-controls').addEventListener('submit', e => e.preventDefault());
        search.addEventListener('input', () => { syncSearchBars(search.value); draw(); writeMapState(); });
        [colorBy, seedSelect, curSelect, cmSelect].forEach(el => el.addEventListener('change', () => { draw(); writeMapState(); }));
        resetBtn.addEventListener('click', () => {
          search.value = ''; syncSearchBars('');
          colorBy.value = 'seed';
          seedSelect.value = ''; curSelect.value = ''; cmSelect.value = '';
          state.zoom = 1; state.panX = 0; state.panY = 0;
          state.hovered = null; state.selected = null;
          draw();
          writeMapState();
        });
        window.addEventListener('popstate', restoreMapState);
        attachCanvasInteractions(canvas, state, showRecord, draw);
      } catch (_) {
        statusEl.setAttribute('role', 'alert');
        statusEl.replaceChildren('Text embedding map could not be loaded. ');
        const retryBtn = document.createElement('button');
        retryBtn.type = 'button';
        retryBtn.textContent = 'Retry';
        retryBtn.addEventListener('click', load);
        statusEl.append(retryBtn);
      }
    }
    load();
  }

  function initSequenceMap() {
    const container = document.querySelector('[data-sequence-map]');
    if (!container) return;
    const canvas = byId('seq-canvas');
    const ctx = canvas.getContext('2d');
    const search = byId('seq-search');
    const colorBy = byId('seq-color');
    const seedSelect = byId('seq-seed');
    const curSelect = byId('seq-curation');
    const chanSelect = byId('seq-channel');
    const lenSelect = byId('seq-length');
    const resetBtn = byId('seq-reset');
    const statusEl = byId('seq-status');
    const selectionEl = byId('seq-selection');
    const legendEl = byId('seq-legend');
    const state = {zoom: 1, panX: 0, panY: 0, hovered: null, selected: null, projected: []};
    let payload = null;
    let proteins = [];

    function showProtein(prot, pinned) {
      selectionEl.replaceChildren();
      const title = document.createElement('p');
      const uLink = document.createElement('a');
      uLink.href = 'https://www.uniprot.org/uniprotkb/' + prot.uniprot_accession + '/entry';
      uLink.textContent = prot.uniprot_accession;
      const strong = document.createElement('strong');
      strong.append(uLink);
      title.append(
        strong,
        ' — ' + prot.label + (prot.organism ? ' (' + prot.organism + ')' : '') +
        ' · ' + prot.length.toLocaleString('en-US') + ' aa' + (pinned ? ' [pinned]' : '')
      );
      const famP = document.createElement('p');
      famP.append('DUF/Pfam families (' + prot.records.length + '): ');
      prot.records.forEach((rec, idx) => {
        if (idx > 0) famP.append(', ');
        const a = document.createElement('a');
        a.href = rec.page;
        a.textContent = rec.id + ' (' + rec.short_name + ')';
        famP.append(a);
      });
      selectionEl.append(title, famP);
    }

    function draw() {
      if (!proteins.length) return;
      const q = search.value.trim().toLowerCase();
      const seedVal = seedSelect.value;
      const curVal = curSelect.value;
      const chanVal = chanSelect.value;
      const lenVal = lenSelect.value;
      const mode = colorBy.value;
      const categories = mode === 'curation' ? payload.curation_statuses :
        mode === 'channel' ? payload.channels :
        mode === 'length_bin' ? payload.length_bins : payload.seed_statuses;
      const counts = new Map(categories.map(k => [k, 0]));

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const pad = 36;
      const w = canvas.width - pad * 2;
      const h = canvas.height - pad * 2;
      const cx = canvas.width / 2 + state.panX;
      const cy = canvas.height / 2 + state.panY;

      let matched = 0;
      const matchedFamilies = new Set();
      state.projected = proteins.map(prot => {
        const visible = (!seedVal || prot.seed_statuses.includes(seedVal)) &&
          (!curVal || prot.curation_statuses.includes(curVal)) &&
          (!chanVal || prot.sequence_origin === chanVal) &&
          (!lenVal || prot.length_bin === lenVal) &&
          (!q || prot.searchText.includes(q));
        const groupKey = mode === 'curation' ? prot.primary_curation_status :
          mode === 'channel' ? prot.sequence_origin :
          mode === 'length_bin' ? prot.length_bin : prot.primary_seed_status;
        if (visible) {
          matched++;
          counts.set(groupKey, (counts.get(groupKey) || 0) + 1);
          prot.records.forEach(r => matchedFamilies.add(r.id));
        }
        const px = cx + prot.nx * (w * 0.46) * state.zoom;
        const py = cy - prot.ny * (h * 0.46) * state.zoom;
        const colorIdx = Math.max(0, categories.indexOf(groupKey));
        return {point: prot, px, py, visible, color: PALETTE[colorIdx % PALETTE.length]};
      });

      for (const item of state.projected) {
        if (item.visible) continue;
        ctx.fillStyle = 'rgba(130, 145, 155, 0.18)';
        ctx.beginPath();
        ctx.arc(item.px, item.py, 2.8, 0, Math.PI * 2);
        ctx.fill();
      }
      for (const item of state.projected) {
        if (!item.visible) continue;
        ctx.fillStyle = item.color;
        ctx.beginPath();
        ctx.arc(item.px, item.py, 4.0, 0, Math.PI * 2);
        ctx.fill();
      }
      for (const special of [state.hovered, state.selected]) {
        if (!special) continue;
        const found = state.projected.find(item => item.point === special);
        if (!found) continue;
        ctx.strokeStyle = '#d97706';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(found.px, found.py, 7.5, 0, Math.PI * 2);
        ctx.stroke();
      }

      statusEl.textContent = 'Showing ' + matched.toLocaleString('en-US') + ' of ' +
        proteins.length.toLocaleString('en-US') + ' proteins across ' +
        matchedFamilies.size.toLocaleString('en-US') + ' DUF/Pfam families.';

      const activeSelect = mode === 'curation' ? curSelect :
        mode === 'channel' ? chanSelect :
        mode === 'length_bin' ? lenSelect : seedSelect;
      renderLegend(
        legendEl,
        categories.map(k => ({key: k, label: human(k), count: counts.get(k) || 0})),
        activeSelect.value,
        key => {
          activeSelect.value = activeSelect.value === key ? '' : key;
          draw();
          writeSeqState();
        }
      );
    }

    function restoreSeqState() {
      const params = new URLSearchParams(location.search);
      search.value = params.get('q') || '';
      syncSearchBars(search.value);
      colorBy.value = allowed(colorBy, params.get('color') || 'seed', 'seed');
      seedSelect.value = allowed(seedSelect, params.get('seed') || '', '');
      curSelect.value = allowed(curSelect, params.get('curation') || '', '');
      chanSelect.value = allowed(chanSelect, params.get('channel') || '', '');
      lenSelect.value = allowed(lenSelect, params.get('length') || '', '');
      draw();
    }

    function writeSeqState() {
      const url = new URL(location.href);
      const seqParams = {
        q: search.value.trim(),
        color: colorBy.value !== 'seed' ? colorBy.value : '',
        seed: seedSelect.value,
        curation: curSelect.value,
        channel: chanSelect.value,
        length: lenSelect.value,
      };
      for (const [k, v] of Object.entries(seqParams)) {
        if (v) url.searchParams.set(k, v);
        else url.searchParams.delete(k);
      }
      if (url.href !== location.href) history.replaceState(null, '', url);
    }

    async function load() {
      try {
        statusEl.removeAttribute('role');
        const res = await fetch(container.dataset.src);
        if (!res.ok) throw new Error('HTTP ' + res.status);
        payload = await res.json();
        const raw = payload.proteins || [];
        let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
        for (const p of raw) {
          if (p.x < minX) minX = p.x;
          if (p.x > maxX) maxX = p.x;
          if (p.y < minY) minY = p.y;
          if (p.y > maxY) maxY = p.y;
        }
        const spanX = Math.max(1e-6, maxX - minX);
        const spanY = Math.max(1e-6, maxY - minY);
        proteins = raw.map(p => ({
          ...p,
          nx: ((p.x - minX) / spanX) * 2 - 1,
          ny: ((p.y - minY) / spanY) * 2 - 1,
          searchText: [
            p.uniprot_accession, p.label, p.organism,
            ...(p.records || []).map(r => r.id + ' ' + r.short_name + ' ' + r.label),
          ].join(' ').toLowerCase(),
        }));
        restoreSeqState();
        byId('seq-controls').addEventListener('submit', e => e.preventDefault());
        search.addEventListener('input', () => { syncSearchBars(search.value); draw(); writeSeqState(); });
        [colorBy, seedSelect, curSelect, chanSelect, lenSelect].forEach(el => el.addEventListener('change', () => { draw(); writeSeqState(); }));
        resetBtn.addEventListener('click', () => {
          search.value = ''; syncSearchBars('');
          colorBy.value = 'seed';
          seedSelect.value = ''; curSelect.value = ''; chanSelect.value = ''; lenSelect.value = '';
          state.zoom = 1; state.panX = 0; state.panY = 0;
          state.hovered = null; state.selected = null;
          draw();
          writeSeqState();
        });
        window.addEventListener('popstate', restoreSeqState);
        attachCanvasInteractions(canvas, state, showProtein, draw);
      } catch (_) {
        statusEl.setAttribute('role', 'alert');
        statusEl.replaceChildren('Sequence embedding map could not be loaded. ');
        const retryBtn = document.createElement('button');
        retryBtn.type = 'button';
        retryBtn.textContent = 'Retry';
        retryBtn.addEventListener('click', load);
        statusEl.append(retryBtn);
      }
    }
    load();
  }

  // Built here rather than rendered so the static family pages carry no extra bytes;
  // without JavaScript the header's Repository link remains the reporting route.
  function initFeedback() {
    const match = location.pathname.match(/\/families\/(PF[0-9]{5})(?:\.html)?$/);
    const download = match && document.querySelector('a[download][href="' + match[1] + '.json"]');
    if (!download) return;
    const issue = new URL('https://github.com/CultureBotAI/DUFMech/issues/new');
    issue.searchParams.set('title', match[1]);
    issue.searchParams.set('body', location.origin + location.pathname);
    const link = document.createElement('a');
    link.href = issue.href;
    link.textContent = 'Report a problem on GitHub';
    download.after(' | ', link);
  }

  initCatalogue();
  initTextMap();
  initSequenceMap();
  initFeedback();
})();
