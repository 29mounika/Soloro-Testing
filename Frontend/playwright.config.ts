import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    video: 'on', // Always record video
  },
  reporter: [['html', { outputFolder: 'playwright-report', open: 'never' }]],
  testDir: '.', // Root of Frontend folder
});

