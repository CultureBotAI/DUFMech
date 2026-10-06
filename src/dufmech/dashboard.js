/* Progressive enhancement: without JavaScript the bounded table keeps every row. */
(() => {
  'use strict';
  const rows = Array.from(document.querySelectorAll('tbody tr'));
  const query = document.getElementById('family-query');
  const status = document.getElementById('seed-filter');
  const previous = document.getElementById('previous-families');
  const next = document.getElementById('next-families');
  const count = document.getElementById('family-count');
  const pageLabel = document.getElementById('family-page');
  const size = 50;
  let page = 0;
  [...new Set(rows.map(row => row.dataset.status))].sort().forEach(value => {
    const option = document.createElement('option');
    option.value = value;
    option.textContent = value.replaceAll('_', ' ');
    status.append(option);
  });
  function render() {
    const term = query.value.trim().toLocaleLowerCase();
    const matches = rows.filter(row => (!status.value || row.dataset.status === status.value) &&
      row.dataset.search.toLocaleLowerCase().includes(term));
    const pages = Math.max(1, Math.ceil(matches.length / size));
    page = Math.max(0, Math.min(page, pages - 1));
    rows.forEach(row => { row.hidden = true; });
    matches.slice(page * size, (page + 1) * size).forEach(row => { row.hidden = false; });
    count.textContent = matches.length.toLocaleString() + ' of ' + rows.length.toLocaleString() +
      ' families match.' + (matches.length ? '' : ' No matching families. Clear the search or filters to try again.');
    pageLabel.textContent = 'Page ' + (page + 1) + ' of ' + pages;
    previous.disabled = page === 0;
    next.disabled = page + 1 >= pages;
  }
  function revealHash() {
    const id = location.hash.slice(1).toUpperCase();
    const index = rows.findIndex(row => row.id === id);
    if (index < 0) return false;
    query.value = ''; status.value = ''; page = Math.floor(index / size);
    render();
    rows[index].scrollIntoView({block: 'nearest'});
    return true;
  }
  query.addEventListener('input', () => { page = 0; render(); });
  status.addEventListener('change', () => { page = 0; render(); });
  document.getElementById('reset-families').addEventListener('click', () => {
    query.value = ''; status.value = ''; page = 0; render(); query.focus();
  });
  previous.addEventListener('click', () => { page--; render(); });
  next.addEventListener('click', () => { page++; render(); });
  window.addEventListener('hashchange', revealHash);
  window.addEventListener('pageshow', () => { if (!revealHash()) render(); });
  document.getElementById('family-controls').hidden = false;
  document.getElementById('family-pagination').hidden = false;
  if (!revealHash()) render();
})();
