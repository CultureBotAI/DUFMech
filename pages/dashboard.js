/* Static pages remain complete and navigable if this enhancement cannot load. */
(() => {
  'use strict';
  const catalogue = document.querySelector('[data-catalogue]');
  if (!catalogue) return;
  const root = catalogue.dataset.root;
  const category = catalogue.dataset.category;
  const initialPage = Number(catalogue.dataset.page);
  const byId = id => document.getElementById(id);
  const query = byId('family-query');
  const seed = byId('seed-filter');
  const characterization = byId('characterization-filter');
  const sort = byId('family-sort');
  const tbody = byId('family-table').querySelector('tbody');
  const size = 50;
  let page = initialPage;
  let rows;
  const human = value => String(value || '').replaceAll('_', ' ');
  const count = value => value === null ? 'Not available' : value.toLocaleString('en-US');
  const allowed = (select, value, fallback) => [...select.options].some(option => option.value === value) ? value : fallback;
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
    seed.value = allowed(seed, params.has('seed') ? params.get('seed') : category, '');
    characterization.value = allowed(characterization, params.get('characterization') || '', '');
    sort.value = allowed(sort, params.get('sort') || 'proteins-desc', 'proteins-desc');
    const requested = Number(params.get('page') || initialPage);
    page = Number.isSafeInteger(requested) && requested > 0 ? requested : 1;
    render();
  }
  function writeState() {
    const url = new URL(location.href);
    const state = {q: query.value, seed: seed.value, characterization: characterization.value,
      sort: sort.value, page: String(page)};
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
      query.addEventListener('input', () => { page = 1; render(); writeState(); });
      [seed, characterization, sort].forEach(control => control.addEventListener('change', () => {
        page = 1; render(); writeState();
      }));
      byId('reset-families').addEventListener('click', () => {
        query.value = ''; seed.value = category; characterization.value = '';
        sort.value = 'proteins-desc'; page = 1; render(); writeState(); query.focus();
      });
      byId('previous-families').addEventListener('click', () => { page--; render(); writeState(); });
      byId('next-families').addEventListener('click', () => { page++; render(); writeState(); });
      window.addEventListener('popstate', restore);
    } catch (_) {
      byId('catalogue-error').textContent = 'Search is unavailable because the catalogue could not be loaded. ' +
        'The table below is the static catalogue page; search parameters have not been applied. ' +
        'Use the numbered pages or complete JSON download.';
      byId('catalogue-error').hidden = false;
    } finally {
      clearTimeout(timer);
    }
  }
  start();
})();
