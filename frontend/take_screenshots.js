const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    try {
        console.log('Launching browser...');
        const browser = await puppeteer.launch({ headless: 'new' });
        const page = await browser.newPage();
        await page.setViewport({ width: 1440, height: 900 });

        const baseUrl = 'http://localhost:3000';
        const getPath = (name) => path.join(__dirname, '..', 'docs', name);

        // 1. Landing Page
        console.log('Taking screenshot of landing page...');
        await page.goto(baseUrl, { waitUntil: 'networkidle0' });
        await page.screenshot({ path: getPath('landing.png') });

        // 2. Login Page
        console.log('Taking screenshot of login page...');
        await page.goto(`${baseUrl}/login`, { waitUntil: 'networkidle0' });
        await page.screenshot({ path: getPath('login.png') });

        // Login Programmatically
        console.log('Logging in...');
        const inputs = await page.$$('input');
        if (inputs.length >= 2) {
            await inputs[0].type('abc');
            await inputs[1].type('abc');

            const buttons = await page.$$('button');
            for (let btn of buttons) {
                const text = await page.evaluate(el => el.textContent, btn);
                if (text && text.includes('Sign In')) {
                    await btn.click();
                    break;
                }
            }
            // wait for navigation to dashboard (Next.js client-side routing)
            await new Promise(r => setTimeout(r, 2000));
        } else {
            console.error('Cannot find login inputs');
        }

        // 3. Dashboard
        console.log('Taking screenshot of dashboard...');
        await page.screenshot({ path: getPath('dashboard.png') });

        // 4. Python Track
        console.log('Taking screenshot of Python track...');
        await page.goto(`${baseUrl}/dashboard/python`, { waitUntil: 'networkidle0' });
        await page.screenshot({ path: getPath('python_track.png') });

        // 5. AI Mentor UI
        console.log('Taking screenshot of AI Mentor UI...');
        await page.goto(`${baseUrl}/dashboard/python/1`, { waitUntil: 'networkidle0' });

        // click AI tab
        const aiTabs = await page.$$('button');
        for (let btn of aiTabs) {
            const text = await page.evaluate(el => el.textContent, btn);
            if (text && text.includes('ai') || text && text.includes('Ai')) {
                await btn.click();
                break;
            }
        }

        // Wait a moment for rendering
        await new Promise(r => setTimeout(r, 1000));

        await page.screenshot({ path: getPath('ai_mentor.png') });

        console.log('Screenshots complete!');
        await browser.close();
    } catch (e) {
        console.error('Error:', e);
        process.exit(1);
    }
})();
