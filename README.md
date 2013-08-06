Visual Style Test App
=====================

The visual style test app lets you preview the site wide styling
for a collection of common widgets and components. Out of the box,
only bootstrap is included, but other apps can also register their
own widgets to be displayed.


Installation
------------

1. Add `visual_style` to `INSTALLED_APPS`
2. In your application or site-wide templates directory, add a template
   named `visual_style/base.html`. This template must contain the stylesheets
   and javascript that are common to all pages on the site, and sufficient to
   display the registered components. In most cases, you can get away with just
   extending your site base template and making defining a "content" block
   inside of the body.
3. Include `visual_style.urls` in your urlconf.
4. If you would like to regenerate example bootstrap widgets, add a
   `BOOTSTRAP_DOC_DIRECTORY` setting which contains the location of your
   bootstrap docs relative to a static directory (ex. if you installed the docs
   in project_root/foo_app/static/bower/bootstrap/docs, then the setting would
   be `BOOTSTRAP_DOC_DIRECTORY = 'bower/boostrap/docs`.)


Registering Components
----------------------

If you have any components that are in use site-wide, you can create a template
named `visual_style/snippets/<component>.html` in the app defining
the component. This template should inherit from
`visual_style/snippet_details.html', and override the `content`, `scripts`, and
`styles` blocks as necessary. The template will automatically be added to the
nav bar in the visual style test page.
