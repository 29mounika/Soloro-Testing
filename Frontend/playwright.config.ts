
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    video: 'on', // Change to 'on' to always record
  },
  reporter: [['html', { outputFolder: 'playwright-report', open: 'never' }]],
  testDir: './Frontend', // Optional: where you put tests
});
