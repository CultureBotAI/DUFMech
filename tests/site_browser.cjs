'use strict';

const {test, before, after} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const http = require('node:http');
const {execFileSync} = require('node:child_process');
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');

const root = path.resolve(__dirname, '..');
const fixture = fs.mkdtempSync(path.join(os.tmpdir(), 'dufmech-browser-'));
const screenshots = process.env.DUFMECH_SCREENSHOT_DIR || path.join(os.tmpdir(), 'dufmech-browser-screenshots');
const realSite = path.resolve(process.env.DUFMECH_SITE_DIR || path.join(root, 'pages'));
let server, browser, origin;

before(async () => {
  assert.ok(fs.existsSync(path.join(realSite, 'catalogue.json')),
    `Build the current site before browser testing: ${realSite} (or set DUFMECH_SITE_DIR)`);
  execFileSync(process.env.DUFMECH_PYTHON || path.join(root, '.venv/bin/python'),
    ['tests/site_browser_fixture.py', fixture], {cwd: root, env: {...process.env, PYTHONPATH: 'src:.'}});
  fs.mkdirSync(screenshots, {recursive: true});
  server = http.createServer((req, res) => {
    const pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    const actual = realSite && pathname.startsWith('/real/');
    const directory = actual ? path.resolve(realSite) : fixture;
    const relative = actual ? pathname.slice(6) : pathname.slice(1);
    let file = path.resolve(directory, relative || 'index.html');
    if (!file.startsWith(directory + path.sep)) { res.writeHead(403).end(); return; }
    try {
      if (fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
      const types = {'.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json'};
      res.setHeader('Content-Type', (types[path.extname(file)] || 'text/plain') + '; charset=utf-8');
      res.end(fs.readFileSync(file));
    } catch (_) { res.writeHead(404).end(); }
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  origin = `http://127.0.0.1:${server.address().port}`;
  browser = await chromium.launch({headless: true,
    ...(process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE ? {executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE} : {})});
});

after(async () => {
  if (browser) await browser.close();
  if (server) await new Promise(resolve => server.close(resolve));
  fs.rmSync(fixture, {recursive: true, force: true});
});

async function ready(page, relative = '/index.html') {
  await page.goto(origin + relative);
  await page.locator('#family-controls:not([hidden])').waitFor();
}

async function noOverflow(page) {
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, page.url());
}

async function firstId(page) {
  return page.locator('#family-table tbody tr').first().getAttribute('id');
}

test('sorting, full-corpus search, filters, counts, URL state, reload and back', async () => {
  const context = await browser.newContext({viewport: {width: 1440, height: 900}});
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
  await ready(page);
  assert.equal(await firstId(page), 'PF00123');
  assert.equal(await page.locator('#family-table tbody tr').count(), 50);
  await page.selectOption('#family-sort', 'proteins-asc');
  assert.equal(await firstId(page), 'PF00002');
  await page.selectOption('#family-sort', 'pfam_id-asc');
  assert.equal(await firstId(page), 'PF00001');
  const tableViewport = page.locator('#family-table').locator('..');
  await tableViewport.evaluate(element => { element.scrollTop = element.scrollHeight; });
  assert.ok(await tableViewport.evaluate(element => element.scrollTop > 0));
  await page.click('#next-families');
  assert.equal(await firstId(page), 'PF00051');
  assert.equal(await tableViewport.evaluate(element => element.scrollTop), 0);
  assert.equal(await page.locator('#family-table tbody tr').first().evaluate(element => {
    const row = element.getBoundingClientRect();
    const viewport = element.closest('.table-wrap').getBoundingClientRect();
    return row.top >= viewport.top && row.bottom <= viewport.bottom;
  }), true);
  assert.equal(new URL(page.url()).searchParams.get('page'), '2');
  await page.reload();
  await page.locator('#family-controls:not([hidden])').waitFor();
  assert.equal(await firstId(page), 'PF00051');
  await page.fill('#family-query', 'IPR000120');
  assert.match(await page.locator('#family-count').innerText(), /^1 of 123/);
  assert.equal(await firstId(page), 'PF00120');
  await page.fill('#family-query', 'Fixture family 005');
  assert.equal(await firstId(page), 'PF00005');
  await page.goBack();
  assert.equal(await page.inputValue('#family-query'), 'IPR000120');
  assert.equal(await firstId(page), 'PF00120');
  await page.selectOption('#seed-filter', 'UNKNOWN_CANDIDATE');
  assert.match(await page.locator('#family-count').innerText(), /^0 of 123/);
  assert.equal(await page.locator('#family-empty').isVisible(), true);
  await page.click('#reset-families');
  assert.match(await page.locator('#family-count').innerText(), /^123 of 123/);
  await page.selectOption('#characterization-filter', 'UNSCORED');
  await page.selectOption('#seed-filter', 'KNOWN_HISTORICAL_DUF');
  assert.match(await page.locator('#family-count').innerText(), /^23 of 123/);
  await page.reload();
  await page.locator('#family-controls:not([hidden])').waitFor();
  assert.equal(await page.inputValue('#seed-filter'), 'KNOWN_HISTORICAL_DUF');
  assert.equal(await page.inputValue('#characterization-filter'), 'UNSCORED');
  await noOverflow(page);
  assert.deepEqual(errors, []);
  await context.close();
});

test('actual generated corpus controls restore state and show the first row after pagination', async () => {
  const payload = JSON.parse(fs.readFileSync(path.join(realSite, 'index.json'), 'utf8'));
  const sorted = [...payload.families].sort((a, b) => a.pfam_id.localeCompare(b.pfam_id));
  for (const width of [1440, 390]) {
    const context = await browser.newContext({viewport: {width, height: 900}});
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
    await ready(page, '/real/index.html');
    await page.selectOption('#family-sort', 'pfam_id-asc');
    assert.equal(await firstId(page), sorted[0].pfam_id);
    if (sorted.length > 50) {
      const viewport = page.locator('#family-table').locator('..');
      await viewport.evaluate(element => { element.scrollTop = element.scrollHeight; });
      assert.ok(await viewport.evaluate(element => element.scrollTop > 0));
      await page.click('#next-families');
      assert.equal(await viewport.evaluate(element => element.scrollTop), 0);
      assert.equal(await firstId(page), sorted[50].pfam_id);
      await page.reload();
      await page.locator('#family-controls:not([hidden])').waitFor();
      assert.equal(await firstId(page), sorted[50].pfam_id);
    }
    const target = sorted.find(row => row.pfam_id === 'PF04149') || sorted[0];
    await page.selectOption('#seed-filter', target.unknown_status);
    await page.selectOption('#characterization-filter', target.characterization_status || 'UNSCORED');
    await page.fill('#family-query', target.pfam_id);
    assert.equal(await firstId(page), target.pfam_id);
    assert.equal(await page.locator('#family-table tbody tr').count(), 1);
    await page.locator('#family-table tbody tr a').first().click();
    await page.waitForURL(`**/families/${target.pfam_id}.html`);
    await page.goBack();
    await page.locator('#family-controls:not([hidden])').waitFor();
    assert.equal(await page.inputValue('#family-query'), target.pfam_id);
    assert.equal(await page.inputValue('#seed-filter'), target.unknown_status);
    await page.reload();
    await page.locator('#family-controls:not([hidden])').waitFor();
    assert.equal(await firstId(page), target.pfam_id);
    await noOverflow(page);
    assert.deepEqual(errors, []);
    await context.close();
  }
});

test('stable category pages, legacy record hashes and no-JS catalogue pagination', async () => {
  const context = await browser.newContext();
  const page = await context.newPage();
  await ready(page, '/category/unknown_candidate.html');
  assert.match(await page.locator('#family-count').innerText(), /^100 of 123/);
  await page.fill('#family-query', 'unmatchable');
  await page.click('#reset-families');
  assert.equal(await page.inputValue('#seed-filter'), 'UNKNOWN_CANDIDATE');
  await page.goto(origin + '/index.html#PF00001');
  await page.waitForURL('**/families/PF00001.html');
  assert.match(await page.locator('h1').innerText(), /PF00001/);
  await context.close();
  const plain = await browser.newContext({javaScriptEnabled: false, viewport: {width: 390, height: 844}});
  const staticPage = await plain.newPage();
  await staticPage.goto(origin + '/index.html');
  assert.equal(await staticPage.locator('#family-table tbody tr').count(), 50);
  await staticPage.locator('#static-pagination a').nth(2).click();
  assert.equal(await staticPage.locator('#family-table tbody tr').count(), 23);
  await noOverflow(staticPage);
  await plain.close();
});

test('failed or malformed catalogue fetch retains static navigation and explains unapplied search', async () => {
  for (const failure of ['http', 'malformed']) {
    const context = await browser.newContext();
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.route('**/catalogue.json', route => route.fulfill(failure === 'http' ?
      {status: 503, body: 'Unavailable'} : {status: 200, contentType: 'application/json', body: '{"broken":true}'}));
    await page.goto(origin + '/index.html?q=PF00001');
    await page.locator('#catalogue-error:not([hidden])').waitFor();
    assert.match(await page.locator('#catalogue-error').innerText(), /parameters have not been applied/);
    assert.equal(await page.locator('#family-table tbody tr').count(), 50);
    assert.equal(await page.locator('#static-pagination').isVisible(), true);
    assert.deepEqual(errors, []);
    await context.close();
  }
});

async function contrastAudit(page) {
  const failures = await page.evaluate(() => {
    const rgba = value => value.match(/[\d.]+/g).map(Number);
    function luminance(rgb) {
      return rgb.slice(0, 3).map(v => v / 255).map(v => v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4)
        .reduce((sum, value, i) => sum + value * [.2126, .7152, .0722][i], 0);
    }
    const bad = [];
    for (const element of document.querySelectorAll('a, p, h1, h2, th, td, label, button, select, input, dt, dd, figcaption, .metric span')) {
      if (!element.checkVisibility() || element.getBoundingClientRect().width === 0) continue;
      const foreground = rgba(getComputedStyle(element).color);
      let ancestor = element, background;
      while (ancestor) {
        const candidate = rgba(getComputedStyle(ancestor).backgroundColor);
        if (candidate.length === 3 || candidate[3] === 1) { background = candidate; break; }
        ancestor = ancestor.parentElement;
      }
      if (!background) continue;
      const values = [luminance(foreground), luminance(background)].sort((a, b) => a - b);
      const ratio = (values[1] + .05) / (values[0] + .05);
      if (ratio < 4.5) bad.push({tag: element.tagName, text: element.textContent.slice(0, 60), ratio});
    }
    return bad;
  });
  assert.deepEqual(failures, [], page.url());
}

async function checkDomainMatches(page, payload, width, theme) {
  const dataset = payload.provenance?.members;
  if (!dataset) return;
  const rows = JSON.parse(fs.readFileSync(path.join(realSite, dataset.local_source), 'utf8'));
  const plotted = rows.filter(row => row.length && row.match_ranges?.length);
  for (const pfam of [...new Set(plotted.map(row => row.pfam_id))]) {
    await page.goto(origin + `/real/families/${pfam}.html#domain-matches`);
    const expected = plotted.filter(row => row.pfam_id === pfam)
      .sort((a, b) => a.uniprot_accession.localeCompare(b.uniprot_accession));
    assert.equal(await page.locator('.domain-track').count(), expected.length);
    for (let i = 0; i < expected.length; i++) {
      const row = expected[i];
      const ranges = row.match_ranges.map(range => range.split('-').map(Number))
        .sort((a, b) => a[0] - b[0] || a[1] - b[1]);
      const track = page.locator('.domain-track').nth(i);
      assert.equal(await track.getAttribute('aria-label'),
        `${row.uniprot_accession}: matches at residues ${ranges.map(range => range.join('-')).join(', ')} of ${row.length}`);
      const bars = await track.locator('.domain-match').evaluateAll(elements => elements.map(element => ({
        left: parseFloat(element.style.left), width: parseFloat(element.style.width),
        renderedWidth: element.getBoundingClientRect().width,
      })));
      assert.equal(bars.length, ranges.length);
      ranges.forEach(([start, end], j) => {
        assert.ok(Math.abs(bars[j].left - (start - 1) / row.length * 100) < .0001);
        assert.ok(Math.abs(bars[j].width - (end - start + 1) / row.length * 100) < .0001);
        assert.ok(bars[j].renderedWidth > 0);
      });
      assert.equal(await page.locator('.domain-figure').nth(i).getByRole('link', {name: 'Match source'})
        .getAttribute('href'), row.member_source_url);
    }
    await noOverflow(page);
    await contrastAudit(page);
    await page.locator('#domain-matches').screenshot({
      path: path.join(screenshots, `domain-${pfam}-${width}-${theme}.png`),
    });
    await page.getByRole('link', {name: 'Frozen member dataset and attribution'}).click();
    assert.equal(new URL(page.url()).hash, '#member-dataset');
    assert.match(await page.locator('#member-dataset').innerText(), /UniProt Consortium/);
    for (const key of ['local_source', 'local_manifest', 'local_tsv']) {
      if (!dataset[key]) continue;
      const response = await page.request.get(origin + '/real/' + dataset[key]);
      assert.equal(response.status(), 200);
      assert.deepEqual(await response.body(), fs.readFileSync(path.join(realSite, dataset[key])));
    }
  }
}

test('desktop and 390px pages, persisted light/dark/system, contrast, keyboard and screenshots', async () => {
  for (const width of [1440, 390]) {
    const context = await browser.newContext({viewport: {width, height: width === 390 ? 844 : 900}, colorScheme: 'light'});
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
    const prefix = '/real/';
    const payload = JSON.parse(fs.readFileSync(path.join(realSite, 'index.json'), 'utf8'));
    const longest = [...payload.families].sort((a, b) => b.name.length - a.name.length)[0].pfam_id;
    const described = [...payload.families].sort((a, b) => b.description.length - a.description.length)[0].pfam_id;
    for (const theme of ['light', 'dark']) {
      await ready(page, prefix + 'index.html');
      await page.selectOption('#theme-control', theme);
      await page.reload();
      await page.locator('#family-controls:not([hidden])').waitFor();
      assert.equal(await page.inputValue('#theme-control'), theme);
      await noOverflow(page);
      await contrastAudit(page);
      await page.screenshot({path: path.join(screenshots, `catalogue-${width}-${theme}.png`), fullPage: true});
      const pages = ['categories.html', 'sources.html', 'cross-mech.html',
        'category/unknown_candidate.html', `families/${longest}.html`, `families/${described}.html`];
      const retained = Object.keys(payload.metadata || {}).find(id => payload.metadata[id].reviews?.length);
      if (retained) pages.push(`families/${retained}.html`);
      if (fs.existsSync(path.join(realSite, 'schema.html'))) pages.push('schema.html');
      for (const relative of pages) {
        await page.goto(origin + prefix + relative);
        if (relative.startsWith('category/')) await page.locator('#family-controls:not([hidden])').waitFor();
        assert.equal(await page.inputValue('#theme-control'), theme);
        await noOverflow(page);
        await contrastAudit(page);
      }
      await page.goto(origin + prefix + `families/${retained || described}.html`);
      await page.screenshot({path: path.join(screenshots, `record-${width}-${theme}.png`), fullPage: true});
      await checkDomainMatches(page, payload, width, theme);
    }
    await page.selectOption('#theme-control', 'system');
    await page.emulateMedia({colorScheme: 'dark'});
    assert.equal(await page.evaluate(() => getComputedStyle(document.documentElement).colorScheme), 'dark');
    await page.emulateMedia({colorScheme: 'light'});
    assert.equal(await page.evaluate(() => getComputedStyle(document.documentElement).colorScheme), 'light');
    await page.goto(origin + prefix + 'index.html');
    await page.keyboard.press('Tab');
    assert.equal(await page.evaluate(() => document.activeElement.textContent), 'Skip to content');
    assert.deepEqual(errors, []);
    await context.close();
  }
});

test('denied local storage does not break themes or search', async () => {
  const context = await browser.newContext();
  await context.addInitScript(() => {
    Storage.prototype.getItem = () => { throw new Error('storage denied'); };
    Storage.prototype.setItem = () => { throw new Error('storage denied'); };
  });
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await ready(page);
  await page.selectOption('#theme-control', 'dark');
  await page.fill('#family-query', 'PF00001');
  assert.equal(await firstId(page), 'PF00001');
  assert.deepEqual(errors, []);
  await context.close();
});
