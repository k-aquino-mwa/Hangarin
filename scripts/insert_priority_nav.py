from pathlib import Path

path = Path(__file__).resolve().parents[1] / "templates" / "base.html"
text = path.read_text(encoding='utf-8')

needle = '<a href="{% url \'category-list\' %}">'
idx = text.find(needle)
if idx == -1:
    raise SystemExit('category link not found')

# Find closing </li> for that item by scanning forward
start = text.find('</li>', idx)
if start == -1:
    raise SystemExit('category list item closing tag not found')
end = start + len('</li>')

insert = (
    '\n\t\t\t\t\t<li class="nav-item">\n'
    "\t\t\t\t\t\t<a href=\"{% url 'priority-list' %}\">\n"
    '\t\t\t\t\t\t\t<i class="la la-list-alt"></i>\n'
    '\t\t\t\t\t\t\t<p>Priorities</p>\n'
    '\t\t\t\t\t\t</a>\n'
    '\t\t\t\t\t</li>\n'
)

new_text = text[:end] + insert + text[end:]
path.write_text(new_text, encoding='utf-8')
print('Inserted priorities nav item.')
