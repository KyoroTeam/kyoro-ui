import App from './App.svelte';
import 'carbon-components-svelte/css/all.css';

var app = new App({
  target: document.body,
});

export default app;

// Hot Module Replacement (HMR) - Remove this snippet to remove HMR.
// Learn more: https://www.snowpack.dev/concepts/hot-module-replacement
const anyMeta = import.meta as any;
if (anyMeta.hot) {
  anyMeta.hot.accept();
  anyMeta.hot.dispose(() => {
    app.$destroy();
  });
}
