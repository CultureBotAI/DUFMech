/* Apply before paint; storage denial must never prevent a page from loading. */
(() => {
  'use strict';
  let preference = 'system';
  try { preference = localStorage.getItem('mech-theme') || 'system'; } catch (_) { /* Optional storage. */ }
  if (!['system', 'light', 'dark'].includes(preference)) preference = 'system';
  const apply = () => {
    if (preference === 'system') delete document.documentElement.dataset.theme;
    else document.documentElement.dataset.theme = preference;
  };
  apply();
  document.addEventListener('DOMContentLoaded', () => {
    const control = document.getElementById('theme-control');
    if (!control) return;
    control.value = preference;
    control.addEventListener('change', () => {
      preference = control.value;
      try { localStorage.setItem('mech-theme', preference); } catch (_) { /* Optional storage. */ }
      apply();
    });
    window.addEventListener('storage', event => {
      if (event.key !== 'mech-theme') return;
      preference = ['light', 'dark'].includes(event.newValue) ? event.newValue : 'system';
      control.value = preference;
      apply();
    });
  });
})();
