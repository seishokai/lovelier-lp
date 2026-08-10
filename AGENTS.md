# LOVELIER project requirements

- Every user-facing copy change must be implemented in all six languages: Japanese, English, Simplified Chinese, Vietnamese, Korean, and Filipino. Update the `js/i18n-supplement-*.js` dictionaries in the same change; never ship a Japanese-only interim state.
- Every layout or component change must include mobile treatment in the same change. Check at 320, 375, 390, and 430 CSS pixels as well as desktop widths. Avoid horizontal overflow, clipped headings, cropped faces, and controls hidden behind the fixed booking bar.
- Preserve the black, white, and restrained gold luxury art direction. Authority claims must retain their qualification note and must not invent unsupported figures.
- Before publishing, run JavaScript syntax checks, CSS brace checks, local-reference checks, multilingual coverage checks, and verify the GitHub Pages build completed for the pushed commit.
