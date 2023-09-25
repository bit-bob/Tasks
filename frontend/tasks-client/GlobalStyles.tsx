import { createGlobalStyle } from "styled-components";
import reset from "styled-reset";

import "@fontsource/azeret-mono";
import "@fontsource/comfortaa";

import { slate50 } from "./constants";

export const GlobalStyles = createGlobalStyle`
${reset}
html {
    background-color: ${slate50};
}
`;
