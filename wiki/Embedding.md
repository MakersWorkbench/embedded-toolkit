# Embedding

## Any web page

Copy `emb.css`, `js/embedded-logic.js`, and `js/embedded-app.js` from the repository, then add:

```html
<link rel="stylesheet" href="emb.css">
<div class="tmwb-emb" id="tmwb-emb" data-heading="h2"></div>
<script src="js/embedded-logic.js"></script>
<script src="js/embedded-app.js"></script>
```

`data-heading` sets the heading level of the tool's title (`h1` to `h6`, default `h1`). Everything is scoped under `.tmwb-emb` and sized in pixels. Only one copy can be on a page.

## Drupal

The repository includes `drupal/tmwb_embedded_toolkit`, a Drupal 10/11 module.

1. Copy the folder to `web/modules/custom/`.
2. Enable **TMWB Embedded Toolkit** (`drush en tmwb_embedded_toolkit`).
3. Edit your text format (Configuration, Text formats and editors) and turn on **TMWB Embedded Toolkit Embed**. The format must allow `div` elements with a `class` attribute.
4. In the body, switch to source mode and add:

```html
<div class="tmwb-embedded-toolkit" data-heading="h2"></div>
```

The filter swaps the placeholder for the tool, loads its CSS and JavaScript, adds a server-rendered description for search engines, and optionally adds Schema.org `WebApplication` structured data.
