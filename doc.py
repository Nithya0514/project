<!DOCTYPE html>
<html>
<head>
<title>Person List</title>
</head>
<body>
<h1>Person List</h1>
<ul>
{% for person in people %}
<li>{{ person.first_name }} {{ person.last_name }}</li>
{% empty %}
<li>No people found.</li>
{% endfor %}
</ul>
</body>
</html>

INSTALLED_APPS = [
...
'people',
]
