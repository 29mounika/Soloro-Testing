import { test, expect } from '@playwright/test';

test('Homepage should load with correct title', async ({ page }) => {
  await page.goto('http://dev.mysoloro.com');
  await expect(page).toHaveTitle(/Soloro/);
});
test('Log in button should be visible', async ({ page }) => {
  await page.goto('http://dev.mysoloro.com');
  const loginBtn = page.locator('text=Log in');
  await expect(loginBtn).toBeVisible();
});
test('Explore Our Locations button should be clickable', async ({ page }) => {
  await page.goto('http://dev.mysoloro.com');
  const exploreBtn = page.locator('text=Explore Our Locations');
  await expect(exploreBtn).toBeVisible();
  await exploreBtn.click();
  // Optionally validate navigation or URL change
});
