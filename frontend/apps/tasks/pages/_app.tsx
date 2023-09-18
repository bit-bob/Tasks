import { OpenAPI } from "api-types";
import { GlobalStyles } from "components/GlobalStyles";

// TODO: Configure with environment variables
OpenAPI.BASE = "http://localhost:8080";

export default function App({ Component, pageProps }) {
  return (
    <>
      <GlobalStyles />
      <Component {...pageProps} />
    </>
  );
}
