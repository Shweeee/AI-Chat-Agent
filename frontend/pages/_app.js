import "@/styles/globals.css";  // Or "../styles/globals.css" if not using absolute path

export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />;
}
