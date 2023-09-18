/** @type { import('@storybook/react').Preview } */
const preview = {
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
import { GlobalStyles } from "../client/GlobalStyles";

export const decorators = [
  withThemeFromJSXProvider({
    GlobalStyles,
  }),
];
