# TMWB Embedded Toolkit (Drupal module)

Embeds the Embedded Systems Toolkit into any Drupal 10 or 11 page. The module is branded TMWB (TheMakersWorkbench.com) but is not tied to any particular site or theme.

## What does it do?

- Adds a text filter, **TMWB Embedded Toolkit Embed**. It replaces a placeholder in your content with the tool.
- Loads the tool's CSS and JavaScript through a normal Drupal library, only on pages that use it.
- Adds a short server-rendered description under the tool (optional) and Schema.org `WebApplication` structured data (optional).
- Sizes everything in pixels and resets a theme's global form styles inside the tool.

## Install

1. Copy this folder to `web/modules/custom/tmwb_embedded_toolkit`.
2. Enable it: `drush en tmwb_embedded_toolkit`.
3. Edit your text format (for example Full HTML) and enable **TMWB Embedded Toolkit Embed**.
4. Clear caches: `drush cr`.

## Use

In the source view of content using that format, add:

```html
<div class="tmwb-embedded-toolkit"></div>
```

Optional: `data-heading="h3"` sets the heading level of the tool's title (default `h2`). Only the first placeholder on a page is used.

## Keeping the bundled copy current

After changing the tool in the repository root, run `python scripts/sync_drupal_module.py` from the repository.

## License

Apache License 2.0. See `assets/LICENSE` and `assets/NOTICE`. Keep the attribution intact.
