Allow filtering by the first letter of the mineral name.
Add links for each letter of the alphabet. This should be added to the layout template so that it appears on every page. When a letter is clicked, a list of minerals that start with that letter should be displayed in the list view. The letter of the alphabet currently being displayed should be bolded. In the details view, no letter should be bolded. On the homepage, select ‘A’ by default.
Allow text search.
Add a search box and button. The search box and button should be implemented as a form. When the search button is clicked, the site will search for minerals whose name contains the search text. The names of the minerals that match the search will be displayed in the list view. Add the search form to the layout template so that searching can be performed from any page in the site.
Allow filtering by group.
Add the ability to filter the list of minerals by adding links to these groups on the left side of the layout template. Clicking a group name, displays a list of all of the minerals in the database that are in that group. The group name being displayed should be bolded. In the details view, no group name should be bolded.
Silicates
Oxides
Sulfates
Sulfides
Carbonates
Halides
Sulfosalts
Phosphates
Borates
Organic Minerals
Arsenates
Native Elements
Other
Optimize database queries
Use the django-debug-toolbar to check that queries to the database take no longer than 10ms to complete.
Unit test the app.
Write unit tests to test that each view is displaying the correct information. Write unit tests to test that the models, classes, and other functions behave as expected.
Make the templates match the style used in the example files.
Look at the example HTML files and global.css to determine the styles used in the pages.
Coding Style
Make sure your coding style complies with PEP 8.

Hopefully the data downloaded with the database.  If not, run the migrations and then run load_data from the manage.py command line and it will load. (python manage.py load_data)  After that, everything will be up and running.

