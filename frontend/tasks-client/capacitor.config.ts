import { CapacitorConfig } from "@capacitor/cli";

const config: CapacitorConfig = {
  appId: "dev.lukeharris.tasks",
  appName: "Tasks",
  webDir: "out",
  server: {
    androidScheme: "http",
  },
  android: {
    allowMixedContent: true,
  },
};

export default config;
