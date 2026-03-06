const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  const filePath = path.resolve(__dirname, 'itinerary.html');
  await page.goto(`file://${filePath}`, { waitUntil: 'networkidle0', timeout: 30000 });
  
  // Wait for fonts to load
  await new Promise(r => setTimeout(r, 3000));
  
  await page.pdf({
    path: path.resolve(__dirname, 'THE-GAP-Itinerary.pdf'),
    format: 'Letter',
    printBackground: true,
    margin: { top: '0', right: '0', bottom: '0', left: '0' },
    displayHeaderFooter: false,
  });
  
  await browser.close();
  console.log('PDF generated: THE-GAP-Itinerary.pdf');
})();
