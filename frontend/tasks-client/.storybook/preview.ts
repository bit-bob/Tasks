import type { Preview } from "@storybook/react";

const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: "^on[A-Z].*" },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/,
      },
    },
  },
};

export default preview;

import { withThemeFromJSXProvider } from "@storybook/addon-styling";
import { GlobalStyles } from "../GlobalStyles";

export const decorators = [
  withThemeFromJSXProvider({
    GlobalStyles,
  }),
];
