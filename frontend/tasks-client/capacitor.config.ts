import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.example.app',
  appName: 'Tasks',
  webDir: 'out',
  server: {
    androidScheme: 'http'
  },
  android: {
    allowMixedContent: true
  },
};

export default config;
