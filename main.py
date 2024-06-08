import click
from parserplan import generate_plan
from analyzer import analyze_plan
from report import generate_report

@click.command()
@click .option('--directory' , default='.', help='Terraform project directory.')
@click .option('--output' , default='report.html', help='Output report file.')
def main(directory, output):
    print("puneet")
    plan= generate_plan(directory)
    print("puneet1")
    summary = analyze_plan(plan)
    generate_report(summary, output)
    click.echo('Report generated: {output}')

main()