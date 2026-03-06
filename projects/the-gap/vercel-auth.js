const puppeteer = require('puppeteer');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto('https://vercel.com/oauth/device?user_code=LCZG-QCLK', { waitUntil: 'networkidle0' });
  
  // Type email and continue
  await page.type('input[type="email"]', 'thegapbuild2026@gmail.com');
  await sleep(500);
  
  // Find the continue button
  const buttons = await page.$$('button');
  for (const btn of buttons) {
    const text = await page.evaluate(el => el.innerText, btn);
    if (text.toLowerCase().includes('continue') || text.toLowerCase().includes('next')) {
      await btn.click();
      console.log('Clicked:', text);
      break;
    }
  }
  
  await sleep(3000);
  console.log('URL after email:', page.url());
  await page.screenshot({ path: '/tmp/vercel-step2.png' });
  
  // Check for password field or verification
  const content = await page.content();
  console.log('Has password field:', content.includes('password') || content.includes('Password'));
  console.log('Has code field:', content.includes('verification') || content.includes('code'));
  
  // Try entering password if field exists
  try {
    const pwInput = await page.$('input[type="password"]');
    if (pwInput) {
      await pwInput.type('BridgeTheGap2026!');
      await sleep(300);
      const submitBtns = await page.$$('button[type="submit"], button');
      for (const btn of submitBtns) {
        const text = await page.evaluate(el => el.innerText, btn);
        if (text.toLowerCase().includes('continue') || text.toLowerCase().includes('sign') || text.toLowerCase().includes('log')) {
          await btn.click();
          console.log('Clicked submit:', text);
          break;
        }
      }
      await sleep(3000);
      console.log('URL after login attempt:', page.url());
      await page.screenshot({ path: '/tmp/vercel-step3.png' });
    }
  } catch(e) {
    console.log('Password error:', e.message.slice(0,100));
  }
  
  await browser.close();
})();
