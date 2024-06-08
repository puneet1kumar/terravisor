from jinja2 import Template

REPORT_TEMPLATE ="""<h1> Terraform Plan Summary</h1>
{% for action, resources in summary.items() %}
<h2>{{action.capitalize() }}</h2>
<ul>
{% for resource in resources %}
<li>{{resource['type']}}.{{resource['name']}}({{resource['address']}})</1i>
{% endfor %}
</ul>
{% endfor %}
"""

def generate_report(summary: dict, output_file: str):
    template = Template(REPORT_TEMPLATE)
    report_html = template.render(summary=summary)
    
    with open(output_file, "w") as f:
        f.write(report_html)